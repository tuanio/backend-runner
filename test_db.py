from app import db, User, Score

username = 'trungio'
password = 'trung2001'
gender = False
course = 'k15'
is_super = True

new_user = User(
    username=username,
    password=password,
    gender=gender,
    course=course,
    is_super=is_super
)
db.session.add(new_user)
db.session.commit()

score = Score(
    user_id=new_user.id,
    max_score=0,
    tried=0
)
db.session.add(score)
db.session.commit()