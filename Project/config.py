import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SITE_URL = os.environ.get('SITE_URL') or '0.0.0.0'
