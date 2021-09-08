#!/bin/bash
set -e

export LC_ALL=pt_BR.UTF-8
export LANG=pt_BR.UTF-8

if [ "$1" = "manage" ]; then
    shift 1
    exec python manage.py "$@"
else
    python manage.py migrate                  # Apply database migrations
    python manage.py collectstatic --noinput  # Collect static files
    python manage.py clear_cache              # Clear cache

    # Prepare log files and start outputting logs to stdout
    touch /usr/src/logs/gunicorn.log
    touch /usr/src/logs/access.log
    tail -n 0 -f /usr/src/logs/*.log &

    # Start Gunicorn processes
    echo Starting Gunicorn.
    exec gunicorn settings.wsgi \
        --name e-commerce-django \
        --bind 0.0.0.0:8000 \
        --workers 5 \
        --timeout 60 \
        --worker-class gevent \
        --keep-alive 5 \
        --log-level=info \
        --log-file=/usr/src/logs/gunicorn.log \
        --access-logfile=/usr/src/logs/access.log \
        --access-logformat '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' \
        "$@"
fi