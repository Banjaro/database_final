import sqlalchemy
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from sqlalchemy.exc import ProgrammingError

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)


from app import models
try:
    engine = sqlalchemy.create_engine(
        'mysql+pymysql://{}:{}@localhost'.format(
            Config.db_username, Config.db_password))
    engine.execute('CREATE DATABASE {}'.format(Config.db_name))
    engine.execute('use {}'.format(Config.db_name))
    db.create_all()
except ProgrammingError:
    db.create_all()

from app import routes
