from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    # đây là option [khác, k13, k14, k15, k16, k17]
    course = db.String(db.String(10))
    is_super = db.Column(db.Boolean, default=False)


class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    max_score = db.Column(db.Integer, default=0)
    tried = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
