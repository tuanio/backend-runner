from flask.helpers import send_file
from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    # False là giới tính Nam, True là giới tính Nữ
    gender = db.Column(db.Boolean, default=False, server_default="false")
    # Đây là option [other, k13, k14, k15, k16, k17]
    disabled = db.Column(db.Boolean, default=False)
    course = db.Column(db.String(10), default="other")
    is_super = db.Column(db.Boolean, default=False, server_default="false")
    secret_key = db.Column(db.String(16), default=None)

    def __init__(
        self,
        username,
        password,
        disabled,
        gender=False,
        course="other",
        is_super=False,
        secret_key=None
    ):
        self.username = username
        self.password = password
        self.disabled = disabled
        self.gender = gender
        self.course = course
        self.is_super = is_super
        self.secret_key = secret_key

    def check_password(self, password):
        return self.password == password

    def check_secret_key(self, secret_key):
        return self.secret_key == secret_key

    def __repr__(self):
        return '<User({}, {}, {}, {}, {}, {})>'.format(
            self.username,
            self.password,
            self.disabled,
            self.gender,
            self.course,
            self.is_super
        )


class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    max_score = db.Column(db.Integer, default=0)
    tried = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(
        self,
        user_id,
        max_score=0,
        tried=0
    ):
        self.user_id = user_id
        self.max_score = max_score
        self.tried = tried

    def __repr__(self):
        return '<Score({}, {}, {})>'.format(
            self.user_id,
            self.max_score,
            self.tried
        )


class AllScore(db.Model):
    __tablename__ = 'allscore'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, default=0)
    tried_in = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(
        self,
        user_id,
        score=0,
        tried_in=0
    ):
        self.user_id = user_id
        self.score = score
        self.tried_in = tried_in

    def __repr__(self):
        return '<Score({}, {}, {})>'.format(
            self.user_id,
            self.score,
            self.tried_in
        )
