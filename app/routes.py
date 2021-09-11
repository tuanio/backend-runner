from app import app
from app.models import User
from datetime import timedelta
import flask
from flask import jsonify, request
from app.utils import make_response
import json

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)


# Homepage
@app.route('/', methods=['GET'])
def index():
    return make_response(
        method='GET', 
        msg='Welcome to Coronavirus Runner!'
    ), 200


# Register


# Login
@app.route('/login', methods=['POST'])
def login():

    request_data = json.loads(request.get_data())
    username = request_data.get('username', None)
    password = request_data.get('password', None)

    user = User.query.filter_by(username=username).one_or_none()

    # Need to check username and passowrd before
    if not user or not user.check_password(password):
        return make_response(
            msg="Sai tài khoản hoặc mật khẩu!",
            code=0,
            data=dict()
        )), 401

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
    return make_response(
        method='GET',
        msg="Tài khoản hiện tại",
        logged_in_as=current_user,
        code=1,
    ), 200


# Update hightscore
@app.route('/update-highscore', methods=['PUT'])
@jwt_required()
def update_highscore(score: int):
    user_id = get_jwt_identity()
    high_score = request.json.get('high-score', 0)

    return make_response(
        method='PUT', 
        msg='Cập nhật điểm cao thành công',
        code=1,
        data=dict()
    ), 200
