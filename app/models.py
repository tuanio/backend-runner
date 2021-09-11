from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    # đây là option [other, k13, k14, k15, k16, k17]
    course = db.String(db.String(10), default="other")
    is_super = db.Column(db.Boolean, default=False)

    def __init__(
        self,
        username,
        password,
        course="other",
        is_super=False
    ):
        self.username=username,
        self.password=password,
        self.course=course,
        self.is_super=is_super


    def __repr__(self):
        return '<User({}, {}, {}, {})>'.format(
            self.username,
            self.password,
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
        tried=0,
    ):
        self.max_score=max_score,
        self.tried=tried,
        self.user_id=user_id


    def __repr__(self):
        return '<User({}, {}, {}, {})>'.format(
            self.user_id,
            self.max_score,
            self.tried
        )