import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:T3stP@ssword1@localhost/testing'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
