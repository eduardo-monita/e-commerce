# tcc
virtualenv venv -p python3
source venv/bin/activate
pip install --upgrade pip
python manage.py migrate
python manage.py collectstatic