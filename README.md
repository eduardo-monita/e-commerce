# tcc
virtualenv venv -p python3
source venv/bin/activate
pip install --upgrade pip
python manage.py migrate
python manage.py collectstatic

python manage.py loaddata admin_interface_theme_django.json
python manage.py loaddata admin_interface_theme_bootstrap.json
python manage.py loaddata admin_interface_theme_foundation.json
python manage.py loaddata admin_interface_theme_uswds.json