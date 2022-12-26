
from . import api, db
from .models import User, Campaign
from flask import jsonify, request as req
from .schema import single_user, all_users

import sys


BASE_URL = '/api/v1/'

@api.route(f'{BASE_URL}/users', methods=['GET', 'POST'])
def users():
    if req.method == 'POST':
        username = req.json.get('username')
        if not username:
            return jsonify({'error': 'missing required field: username'}), 400
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': f'user with username {username} already exists'}), 400        
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return single_user.jsonify(user)
    else:
        return all_users.jsonify(User.query.all())



@api.route(f'{BASE_URL}/users/<int:user_id>/campaigns', methods=['POST'])
def create_campaign(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'user not found'}), 404

    data = req.json
    type = data.get('type')
    engagement = data.get('engagement')

    if not type or not engagement:
        return jsonify({'error': 'missing required fields'}), 400
    
    campaign = Campaign(type=type, engagement=engagement, owner=user)
    db.session.add(campaign)
    db.session.commit()

    return jsonify(campaign)





@api.route(f'{BASE_URL}/campaign')
def campaign():
    campaigns = Campaign.query.join(User).all()
    return jsonify(campaigns)


    

@api.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404