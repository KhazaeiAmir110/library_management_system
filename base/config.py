import os

from base import secret


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = secret.CSRF_SESSION_KEY
    SECRET_KEY = secret.SECRET_KEY


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/book_store'


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = '...'
