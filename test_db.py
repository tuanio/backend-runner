from app import db, User

username = 'trungio'
password = 'trung2001'
gender = False
course = 'k15'
is_super = True

user = User(username, password, gender, course, is_super)

db.session.add(user)
db.session.commit()