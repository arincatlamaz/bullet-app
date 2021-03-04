### Jak wlączyć program?

1. Stworzyć database(na przyklad postgres)
2.  Napisać w pliku /bullet/local_settings.py :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bullet1',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
3. Stwórz virtual environment
3. Napisz pip install -r requirements.txt.
4. Napisz python manage.py migrate
5. Napisz python manage.py createsuperuser
6. Napisz python manage.py runserver



