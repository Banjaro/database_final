import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123'
    # Here is where you set your mysql username and password
    db_username = 'root'
    db_password = 'T3stP@ssword1'
    db_name = 'bigboidb'
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://{}:{}@localhost/{}'.format(
            db_username, db_password, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
