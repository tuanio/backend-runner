from app import app, db
from flask import make_response, jsonify

@app.route('/update-highscore/<int:score>')
def update_highscore(score: int):
  print('User score is:', score)
  return make_response(jsonify({'ok': 'ok'}))