
from . import api, db
from models import User, Wallet
from flask import jsonify, request as req
from .schema import single_user


BASE_URL = '/api/v1/'

@api.route(f'{BASE_URL}/users', methods=['GET', 'POST'])
def users():
    if req.method == 'POST':
        username = req.json['username']
        if User.query.filter_by(username=username).first():
            return jsonify({'username': username})
        try:
            user = User(username)
            db.session.add(user)
            db.session.commit()
            return single_user.jsonify(user)
        except:
            return jsonify({'error': 'an error occured while trying login'})
    return f'{User.query.all()}'




@api.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404