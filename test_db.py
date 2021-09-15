from app import db, User, Score

username = 'trungio'
password = 'trung2001'
gender = False
course = 'K15'
is_super = True
disabled = False

new_user1 = User(
    username=username,
    password=password,
    gender=gender,
    disabled=disabled,
    course=course,
    is_super=is_super
)

new_user2 = User(
    username="tuanio",
    password="Tuan1211",
    gender=False,
    disabled=False,
    course=course,
    is_super=is_super
)

db.session.add(new_user1)
db.session.add(new_user2)
db.session.commit()

new_score_record1 = Score(
    user_id=new_user1.id,
    max_score=0,
    tried=0
)

new_score_record2 = Score(
    user_id=new_user2.id,
    max_score=0,
    tried=0
)

db.session.add(new_score_record1)
db.session.add(new_score_record2)
db.session.commit()