from . import api, db
from flask import jsonify, request
from .contants import BASE_URL
from .models import User, Wallet, Campaign



from .schema import (
    wallet_schema, 
    wallets_schema,  
    user_schema, 
    users_schema, 
    campaign_schema, 
    campaigns_schema
)

# INDEX ENDPOINT
@api.route(f'{BASE_URL}', methods=['GET', 'POST'])
def index():
    if request.method != 'GET':
        return jsonify({
            "status": "Method Not Allowed",
        }), 405
    return jsonify({
        "status": "successfull",
        "message": "Welcome to maxapi"
    })



# CREATE NEW USER
@api.route(f'{BASE_URL}/user/create', methods=['POST'])
def create_user():
 # Get the request data as a json object
    data = request.get_json()
    # Create a new User object with the request data
    user = User(
        username=data['username'],
        insta_id=data['insta_id']
    )
    # Add the user to the database
    db.session.add(user)
    db.session.commit()
    # Serialize the user and return a response
    return jsonify({'user': user.username}), 201

# GET ALL USERS
@api.route(f'{BASE_URL}/users')
def get_users():
    # Get all users from the database
    users = User.query.all()
    # Serialize the users and return a response
    return users_schema.jsonify(users)


# GET USER BY ID
@api.route(f'{BASE_URL}/users/<int:user_id>')
def get_user(user_id):
    # Get the user with the given ID
    user = User.query.get(user_id)
    if user is None:
        # Return a 404 error if the user does not exist
        return jsonify({'error': 'User not found'}), 404
    # Serialize the user and return a response
    return user_schema.jsonify(user)





# GET USER WALLET
@api.route(f'{BASE_URL}/users/<int:user_id>/wallet')
def get_user_wallet(user_id):
    # Get the user's wallet
    wallet = Wallet.query.filter_by(user_id=user_id).first()
    if wallet is None:
        # Return a 404 error if the wallet does not exist
        return jsonify({'error': 'Wallet not found'}), 404
    # Serialize the wallet and return a response
    return wallet_schema.jsonify(wallet)


# FUND WALLET
@api.route(f'{BASE_URL}/wallet/fund', methods=['POST', 'GET'])
def create_wallet():
    # Get the request data as a json object
    data = request.get_json()
    # Create a new Wallet object with the request data
    wallet = Wallet(
        balance=data['balance'],
        user_id=data['user_id']
    )
    # Add the wallet to the database
    db.session.add(wallet)
    db.session.commit()
    # Serialize the wallet and return a response
    return jsonify({'wallet': wallet.id}), 201


# FUND WALLET
@api.route('/wallets/<int:wallet_id>', methods=['PUT'])
def update_wallet(wallet_id):
    # Get the wallet to update
    wallet = Wallet.query.get(wallet_id)
    if wallet is None:
        # Return a 404 error if the wallet does not exist
        return jsonify({'error': 'Wallet not found'}), 404
    # Get the request data as a json object
    data = request.get_json()
    # Update the wallet with the request data
    wallet.balance = data['balance']
    # Save the changes to the database
    db.session.commit()
    # Serialize the wallet and return a response
    return jsonify(wallet)


# CREATE CAMPAIGN
@api.route(f'{BASE_URL}/campaigns', methods=['POST', 'GET'])
def create_campaign():
    # Get the request data as a json object
    data = request.get_json()
    # Create a new Campaign object with the request data
    campaign = Campaign(
        type=data['type'],
        goal=data['goal'],
        user_id=data['user_id']
    )
    # Add the campaign to the database
    db.session.add(campaign)
    db.session.commit()
    # Serialize the campaign and return a response
    return jsonify({'campaign': campaign.type}), 201





# ERROR PAGE 404
@api.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "status": "404 NOT FOUND",
        "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }), 404
# ERROR PAGE 500
@api.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        "status": "500 SERVER SIDE ERROR",
        "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }), 500

# ERROR PAGE 403
@api.errorhandler(403)
def page_forbidden(e):
    return jsonify({
        "status": "403 CLIENT SIDE ERROR",
        "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }), 403