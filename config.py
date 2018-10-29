import os
basedir = os.path.abspath(os.path.dirname(__file__))

_SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
_SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SITE_URL = os.environ.get('SITE_URL') or '0.0.0.0'
    #SESSION_TYPE = 'redis'
    SQLALCHEMY_DATABASE_URI = _SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_MIGRATE_REPO = _SQLALCHEMY_MIGRATE_REPO
    SQLALCHEMY_TRACK_MODIFICATIONS = False