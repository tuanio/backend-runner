from app import app, db
from app.models import User
from app.utils import make_response
from datetime import timedelta
from flask import request, jsonify
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
        method='POST',
        msg='Welcome to Coronavirus Runner!',
        code=1,
        data=dict()
    ), 200


# Register
@app.route('/register', methods=['POST'])
def register():
    request_data = json.loads(request.data)
    username = request_data.get('username', None)
    password = request_data.get('password', None)
    gender = request_data.get('gender', None)
    course = request_data.get('course', None)

    # Mặc định là tài khoản thường
    is_super = False

    # Nếu user là None có nghĩa là chưa có trong db, cho phép tạo mới
    user = User.query.filter_by(username=username).one_or_none()

    if not user:
        new_user = User(
            username=username,
            password=password,
            gender=gender,
            course=course,
            is_super=is_super
        )

        db.session.add(new_user)
        db.session.commit()

        return make_response(
            method='POST',
            msg='Tạo tài khoản thành công!',
            code=1,
            data=dict()
        ), 201

    return make_response(
        method='POST',
        msg='Tài khoản đã tồn tại!',
        code=0,
        data=dict()
    ), 409


# Login
@app.route('/login', methods=['POST'])
def login():
    request_data = json.loads(request.data)
    username = request_data.get('username', None)
    password = request_data.get('password', None)

    # Nếu user là None có nghĩa là chưa có trong db, cho phép tạo mới
    user = User.query.filter_by(username=username).one_or_none()
    # Need to check username and passowrd before
    if not user or not user.check_password(password):
        return make_response(
            dict(
                msg="Sai tài khoản hoặc mật khẩu!",
                code=0,
                data=dict()
            ))

    # Generate access token then return to client-side
    access_token = create_access_token(
        identity=dict(
            user_id=user.id
        ),
        expires_delta=timedelta(hours=app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    )
    print(username, password)
    return make_response(
        dict(
            msg='Đăng nhập thành công!',
            code=1,
            data=dict(access_token=access_token)
        ))


# Test access token route
@app.route('/auth', methods=['GET'])
@jwt_required()
def auth():
    current_user = get_jwt_identity()
    return make_response(
        method='POST',
        msg="Tài khoản hiện tại",
        code=1,
        data=dict(current_user=current_user)
    ), 200


# Update hightscore
@app.route('/update-highscore/<int:score>', methods=['GET'])
@jwt_required()
def update_highscore(score: int):
    print('Your score: ', score)
    return make_response(dict(mgs='ok', code=1, score=score))
