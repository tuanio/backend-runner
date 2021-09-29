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
username = 'postgres'
password = 'Tuan1211'
db_name = 'backend_runner'
host = 'localhost'
port = '5432'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ntwufnwkupmnjz:b3301f3ff3db213384ab9f48b3012934c4a23ec3ffca09d7874140f05bbc6db6@ec2-44-193-150-214.compute-1.amazonaws.com:5432/ddihuntcjekmfb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from app.routes import *
from app.models import *