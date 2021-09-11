from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

# Secret key for jwt, need to be kept confidential
app.config['SECRET_KEY'] = 'b61bbf5093e943859dcc1bbd17f1d5f0'

# Number of minutes for access token exp
app.config['TIME_TO_DIE'] = 30

# local postgresql config database
username = 'postgres'
password = 'trung@2001'
db_name = 'backend_runner'
host = 'localhost'
port = '5432'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# sqlite config database
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"


db = SQLAlchemy(app)

from app.routes import *
from app.models import *