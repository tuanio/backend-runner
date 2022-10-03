from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "https://corona-runner.vercel.app"}}) # change from '*' to this route 
app.config['CORS_HEADERS'] = 'Content-Type'

# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)

# Secret key for jwt, need to be kept confidential
app.config['SECRET_KEY'] = 'b61bbf5093e943859dcc1bbd17f1d5f0'

# Number of hours for access token exp
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 24

# local postgresql config database
# username = 'postgres'
# password = 'Long2002'
# db_name = 'backend_runner'
# host = 'localhost'
# port = '5432'

PGDATABASE='railway'
PGHOST='containers-us-west-73.railway.app'
PGPASSWORD='pGSDhgzeUknrx1PFpy4x'
PGPORT=5443
PGUSER='postgres'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:NeyG6PZLTSq2Q1MIs1Qo@containers-us-west-35.railway.app:6914/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
engine_container = db.get_engine(app)

status_code = dict(SUCCESS=1, FAILURE=0)

from app.routes import *
from app.models import *