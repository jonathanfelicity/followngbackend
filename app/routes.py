
from . import api, db
from .models import User, Wallet
from flask import jsonify, request as req

BASE_URL = '/api/v1/'
APP_NAME = 'FOLLOWNG'

@api.route('/', methods=['POST'])
def index():
    return {"followng": f"Welcome to {APP_NAME}"}




@api.route(f'{BASE_URL}/users', methods=['GET', 'POST'])
def users():
    if req.method == 'POST':
        username, *_ = req.get_json()
        user = User(username='jfmurum')
        db.session.add(user)
        db.session.commit()
        return jsonify(username)
    return f'{User.query.all()}'



from flask import render_template

@api.errorhandler(404)
def page_not_found(e): # e must be in there
    # note that we set the 404 status, this is what it catches
    return {"Resour"}, 404