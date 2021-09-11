from flask.typing import StatusCode
from app import app
from datetime import timedelta
from flask import make_response, jsonify, request

from flask_jwt_extended import (
  create_access_token,
  get_jwt_identity,
  jwt_required
)


# Homepage
@app.route('/', methods=['GET'])
def index():
  return jsonify(msg='Welcome to Coronavirus Runner!'), 200


# Login
@app.route('/login', methods=['POST'])
def login():
  username = request.json.get('username', None)
  password = request.json.get('password', None)

  # Need to check username and passowrd before
  if username != 'test' or password != 'test':
    return jsonify(msg='Wrong username or password!'), 401
  
  # Generate access token then return to client-side
  access_token = create_access_token(
    identity=username,
    expires_delta=timedelta(minutes=app.config['TIME_TO_DIE'])
  )
  return jsonify(access_token=access_token), 200


# Test access token route
@app.route('/auth', methods=['GET'])
@jwt_required()
def auth():
  current_user = get_jwt_identity()
  return jsonify(logged_in_as=current_user), 200


# Update hightscore
@app.route('/update-highscore/<int:score>')
def update_highscore(score: int):
  user_id = ...

  return jsonify(ok='ok')