from app import db, User

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