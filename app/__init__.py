import sqlalchemy
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

try:
    db.create_all()
except:
    engine = sqlalchemy.create_engine(
        'mysql+pymysql://{}:{}@localhost'.format(
            Config.db_user, Config.db_password
        ))
    engine.execute('CREATE DATABASE {}'.format(Config.db_name))
    engine.execute('use {}'.format(Config.db_name))



from app import routes, models
