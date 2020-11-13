import os

DATABASE = {
    'HOST': os.environ['DB_HOST'],
    'PORT': os.environ['DB_PORT'],
    'NAME': os.environ['DB_NAME'],
    'USER': os.environ['DB_USER'],
    'PASSWORD': os.environ['DB_PASSWORD'],
}