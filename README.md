# Это проект Вероиники Нефедовой. 
Она делала его сама, в отличие от ее друзей-лоботрясов.
### Для старта проекта

1. Создать базу данных (например postgres)
2. Прописать в файл /bullet/local_settings.py настройки БД. Пример файла:
```
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
```
3. pip -r requirements.txt. Перед выполнением этой команды создать если необходимо virtual environment
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver



