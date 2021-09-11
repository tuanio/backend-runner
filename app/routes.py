from app import app
from app.models import User
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


# Register




# Login
@app.route('/login', methods=['POST'])
def login():
  username = request.json.get('username', None)
  password = request.json.get('password', None)

  user = User.query.filter_by(username=username).one_or_none()

  # Need to check username and passowrd before
  if not user or not user.check_password(password):
    return jsonify(
      msg="Sai tài khoản hoặc mật khẩu!",
      code=0,
      data=dict()
      ), 401

  # Generate access token then return to client-side
  access_token = create_access_token(
    identity=dict(
      user_id=user.id
    ),
    expires_delta=timedelta(hours=app.config['JWT_ACCESS_TOKEN_EXPIRES'])
  )
  return jsonify(
    msg='Đăng nhập thành công!',
    code=1,
    data=dict(access_token=access_token)
  ), 200


# Test access token route
@app.route('/auth', methods=['GET'])
@jwt_required()
def auth():
  current_user = get_jwt_identity()
  print(current_user)
  return jsonify(
    msg="Tài khoản hiện tại",
    logged_in_as=current_user,
    code=1,
    ), 200


# Update hightscore
@app.route('/update-highscore/<int:score>')
def update_highscore(score: int):
  user_id = ...

  return jsonify(ok='ok')