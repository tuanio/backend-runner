from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SECRET_KEY'] = 'thisisthebiggestprojectever'

db = SQLAlchemy(app)

from app.routes import *
from app.models import *