Create database (for example postgres)
Add database settings to the /bullet/local_settings.py file. Example file:
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'bullet',
         'USER': 'postgres',
         'PASSWORD': 'postgres',
         'HOST': '127.0.0.1',
         'PORT': '5432',
     }
}
pip -r requirements.txt. Before executing this command, create a virtual environment if necessary
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
