from . import api, db
from flask import jsonify, request, Response
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
@api.route(f'{BASE_URL}/users/create', methods=['POST'])
def create_user():
    # Get the user data from the request
    data = request.get_json()
    # Check if the username or instagram ID already exists
    existing_user = User.query.filter((User.username == data['username']) | (User.insta_id == data['insta_id'])).first()
    if existing_user is not None:
        # Return an error if the username or instagram ID already exists
        return jsonify({'error': 'Username or Instagram ID already exists'}), 400
    # Create a new user object
    new_user = User(**data)
    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()
    # Serialize the user and return a response
    data = user_schema.dumps(new_user)
    response = Response(data, status=201, mimetype='application/json')
    return response

# GET ALL USERS
@api.route(f'{BASE_URL}/users')
def get_users():
    # Get all users from the database
    users = User.query.all()
    # Serialize the users and return a response
    data = user_schema.dump(users, many=True)
    response = jsonify({'items': data})
    return response


# GET USER BALLANCE
@api.route(f'{BASE_URL}/users/<username>/balance')
def get_user_balance(username):
    # Get the user by username
    user = User.query.filter_by(username=username).first()
    # Return a 404 error if the user does not exist
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    # Get the user's wallet
    wallet = user.wallet
    # Create a wallet for the user if one does not exist
    if wallet is None:
        wallet = Wallet(user_id=user.id)
        db.session.add(wallet)
        db.session.commit()
    # Get the user's balance and the date the wallet was last updated
    balance = wallet.balance
    updated_at = wallet.updated_at
    # Return the balance and the date the wallet was last updated as a response
    return jsonify({'balance': balance, 'updated_at': updated_at})


# FUND WALLET
@api.route(f'{BASE_URL}/wallet/<username>/fund', methods=['POST'])
def fund_wallet(username):
    # Get the user by username
    user = User.query.filter_by(username=username).first()
    # Return a 404 error if the user does not exist
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    # Get the user's wallet
    wallet = user.wallet
    # Create a wallet for the user if one does not exist
    if wallet is None:
        wallet = Wallet(user_id=user.id)
        db.session.add(wallet)
    # Get the amount to fund from the request data
    data = request.get_json()
    amount = data['amount']
    # Add the amount to the wallet balance
    wallet.balance += amount
    # Commit the changes to the database
    db.session.commit()
    # Serialize the wallet and return a response
    data = wallet_schema.dump(wallet)
    response = jsonify({'items': data})
    return response




@api.route(f'{BASE_URL}/wallet/<username>/expend', methods=['POST'])
def expend_funds(username):
    # Get the user by username
    user = User.query.filter_by(username=username).first()
    # Return a 404 error if the user does not exist
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    # Get the user's wallet
    wallet = user.wallet
    # Return an error if the wallet does not exist
    if wallet is None:
        return jsonify({'error': 'Wallet not found'}), 404
    # Get the expenditure from the request data
    data = request.get_json()
    expenditure = data['expenditure']
    # Check if the expenditure is greater than the balance
    if expenditure > wallet.balance:
        return jsonify({'error': 'Insufficient balance'}), 400
    # Subtract the expenditure from the balance
    wallet.balance -= expenditure
    # Check if the balance has reached 0
    # if wallet.balance == 0:
    #     return jsonify({'message': 'Low balance'}), 200
    # Commit the changes to the database
    db.session.commit()
    # Serialize the wallet and return a response
    data = wallet_schema.dump(wallet)
    response = jsonify({'items': data})
    return response


# CREATING CAMPAIGN
@api.route('/campaigns/create', methods=['POST'])
def create_campaign():
    # Get the user by username from the request data
    data = request.get_json()
    username = data['username']
    user = User.query.filter_by(username=username).first()
    # Return a 404 error if the user does not exist
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    # Create a new campaign using the request data
    campaign = Campaign(**data)
    # Set the user_id of the campaign to the id of the user
    campaign.user_id = user.id
    # Add the campaign to the database
    db.session.add(campaign)
    # Commit the changes to the database
    db.session.commit()
    # Serialize the campaign and return a response
    data = campaign_schema.dump(campaign)
    response = jsonify({'items': data})
    return response


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