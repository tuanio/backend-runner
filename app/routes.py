from app import app, db
import string
from app.models import User, Score, AllScore
from app.utils import make_response
from datetime import timedelta
from flask import request, jsonify
from flask_cors import cross_origin
import json
import random

from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)

## asdf = secret key

def gen_secret_key(size: int=16):
    return ''.join([random.choice(string.ascii_letters) for i in range(size)])

# Homepage
@app.route('/', methods=['GET'])
def index():
    return make_response(dict(
        msg='Welcome to Coronavirus Runner!',
        code=1,
        data=dict()
    ))


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
            disabled=False,
            gender=gender,
            course=course,
            is_super=is_super,
            secret_key=gen_secret_key()
        )

        db.session.add(new_user)
        db.session.commit()

        new_score_record = Score(
            user_id=new_user.id,
            max_score=0,
            tried=0
        )

        db.session.add(new_score_record)
        db.session.commit()

        return make_response(
            dict(
                msg='Tạo tài khoản thành công!',
                code=1,
                data=dict(asdf=new_user.secret_key)
            )
        )

    return make_response(
        dict(
            msg='Tài khoản đã tồn tại!',
            code=0,
            data=dict()
        )
    )


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
        return make_response(dict(
            msg="Sai tài khoản hoặc mật khẩu!",
            code=0,
            data=dict()
        ))

    # tao secret key moi
    user.secret_key = gen_secret_key()
    db.session.commit()

    # Generate access token then return to client-side
    access_token = create_access_token(
        identity=dict(
            user_id=user.id,
            username=username
        ),
        expires_delta=timedelta(hours=app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    )
    return make_response(
        dict(
            msg='Đăng nhập thành công!',
            code=1,
            data=dict(
                access_token=access_token,
                user_name=username,
                is_super=user.is_super,
                asdf=user.secret_key
            )
        ))


# Test access token route
@app.route('/auth', methods=['GET'])
@jwt_required()
def auth():
    '''
    kkk
    '''
    user_id = get_jwt_identity().get('user_id', None)
    secret_key = request.args.get('kkk', None)
    user = User.query.filter_by(id=user_id).one_or_none()

    if not user or not user.check_secret_key(secret_key):
        return make_response(dict(
            msg="Không tồn tại tài khoản",
            code=0,
            data=dict()
        ))
    # tao secret key moi
    user.secret_key = gen_secret_key()
    db.session.commit()

    return make_response(
        dict(
            msg="Tài khoản hiện tại",
            code=1,
            data=dict(
                user_id=user_id,
                user_disabled=user.disabled,
                asdf=user.secret_key
            )
        )
    )


# Update hightscore
@app.route('/uh/<int:user_score>', methods=['GET'])
@jwt_required()
def update_highscore(user_score: int):
    '''
    update-highscore
    okdiei
    '''
    user_id = get_jwt_identity().get('user_id', None)
    secret_key = request.args.get('okdiei', None)
    score = Score.query.filter_by(user_id=user_id).one_or_none()
    user = User.query.filter_by(id=user_id).one_or_none()
    if not score or not user.check_secret_key(secret_key):
        return make_response(
            dict(
                msg="Không tồn tại user",
                code=0,
                data=dict()
            )
        )

    if not user.disabled:
        score.max_score = max(score.max_score, user_score)
        score.tried += 1

        new_allscore = AllScore(
            user_id=user_id,
            score=user_score,
            tried_in=score.tried
        )
        db.session.add(new_allscore)
        db.session.commit()

    user.secret_key = gen_secret_key()
    db.session.commit()

    return make_response(
        dict(
            msg='ok',
            code=1,
            data=dict(
                user_score=user_score,
                asdf=user.secret_key
            )
        )
    )


@app.route('/get-highscore', methods=['GET'])
@jwt_required()
def get_highscore():
    '''
    ktjdk
    '''
    user_id = get_jwt_identity().get('user_id', None)
    secret_key = request.args.get('ktjdk', None)
    score = Score.query.filter_by(user_id=user_id).one_or_none()
    user = User.query.filter_by(id=user_id).one_or_none()
    if not score or not user.check_secret_key(secret_key):
        return make_response(
            dict(
                msg="Không tồn tại user",
                code=0,
                data=dict()
            )
        )
    user.secret_key = gen_secret_key()
    db.session.commit()
    return make_response(
        dict(
            code=1,
            msg="Trả về điểm của user thành công",
            data=dict(
                score=score.max_score,
                asdf=user.secret_key
            )
        )
    )


@app.route('/uwu', methods=['GET'])
@jwt_required()
def reset_user_score():
    '''
    reset user score
    reset toàn bộ điểm và lần thử của user
    uwu
    '''
    user_id = get_jwt_identity().get('user_id', None)
    secret_key = request.args.get('uwu', None)
    user = User.query.filter_by(id=user_id).one_or_none()
    if not user or not user.check_secret_key(secret_key):
        return make_response(
            dict(
                msg="Không tồn tại user",
                code=0
            )
        )
    user.secret_key = gen_secret_key()
    db.session.commit()
    if not user.is_super:
        return make_response(
            dict(
                msg="User không có quyền làm điều này",
                code=2,
                data=dict(asdf=user.secret_key)
            )
        )

    list_scores = Score.query.all()
    for record in list_scores:
        record.max_score = 0
        record.tried = 0
    user.secret_key = gen_secret_key()
    db.session.commit()

    return make_response(
        dict(
            msg="Reset hoàn tất",
            code=1,
            data=dict(asdf=user.secret_key)
        )
    )


@app.route('/owo')
@jwt_required()
def disable_all_user():
    '''
    disable-all-user
    owo
    '''
    user_id = get_jwt_identity().get('user_id', None)
    secret_key = request.args.get('owo', None)
    user = User.query.filter_by(id=user_id).one_or_none()
    if not user or not user.check_secret_key(secret_key):
        return make_response(
            dict(
                msg="Không tồn tại user",
                code=0
            )
        )
    user.secret_key = gen_secret_key()
    db.session.commit()
    if not user.is_super:
        return make_response(
            dict(
                msg="User không có quyền làm điều này",
                code=2,
                data=dict(asdf=user.secret_key)
            )
        )

    list_scores = User.query.all()
    for record in list_scores:
        record.disabled = True
    user.secret_key = gen_secret_key()
    db.session.commit()
    return make_response(
        dict(
            msg="Disable hoàn tất",
            code=1,
            data=dict(asdf=user.secret_key)
        )
    )


@app.route('/eau')
@jwt_required()
def enable_all_user():
    '''
    enable all user
    eau
    '''
    user_id = get_jwt_identity().get('user_id', None)
    secret_key = request.args.get('eau', None)
    user = User.query.filter_by(id=user_id).one_or_none()
    if not user:
        return make_response(
            dict(
                msg="Không tồn tại user",
                code=0
            )
        )
    user.secret_key = gen_secret_key()
    db.session.commit()
    if not user.is_super:
        return make_response(
            dict(
                msg="User không có quyền làm điều này",
                code=2,
                data=dict(asdf=user.secret_key)
            )
        )

    list_scores = User.query.all()
    for record in list_scores:
        record.disabled = False
    user.secret_key = gen_secret_key()
    db.session.commit()
    return make_response(
        dict(
            msg="Enable hoàn tất",
            code=1,
            data=dict(asdf=user.secret_key)
        )
    )


@app.route('/get-leaderboard')
def get_leaderboard():
    leaderboard = db.session.query(
        User, Score
    ).filter(User.id == Score.user_id).order_by(
        Score.max_score.desc()
    ).with_entities(
        User.username,
        User.gender,
        Score.max_score,
    ).all()

    data = {f'{idx}': dict(username=datum[0], gender=datum[1], score=datum[2])
            for idx, datum in enumerate(leaderboard)}
    return jsonify(
        dict(
            code=1,
            msg="Trả về leaderboard thành công",
            data=dict(data=data)
        )
    )
