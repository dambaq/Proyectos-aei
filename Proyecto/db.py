import os

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'usac',
        'USER': 'postgres',
        'PASSWORD': '9844',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}