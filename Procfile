release: python manage.py migrate
web: gunicorn --workers=5 core.wsgi --log-file -