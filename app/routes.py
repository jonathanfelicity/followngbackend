
from . import api, db
from .models import User, Wallet
from flask import jsonify, request as req

BASE_URL = '/api/v1/'


@api.route(f'{BASE_URL}')
def index():
    return {'msg': 'Welcome to FollowNG api'}




@api.route(f'{BASE_URL}/users', methods=['GET', 'POST'])
def users():
    if req.method == 'POST':
        username, *_ = req.get_json()
        user = User(username='jfmurum')
        db.session.add(user)
        db.session.commit()
        return jsonify(username)
    return f"{User.query.all()}"

