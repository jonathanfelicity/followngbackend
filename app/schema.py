from .models import User, Campaign, Wallet
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from . import ma

# Define the User schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Define the Wallet schema
class WalletSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wallet

# Define the Campaign schema
class CampaignSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Campaign

# Initialize the User schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Initialize the Wallet schema
wallet_schema = WalletSchema()
wallets_schema = WalletSchema(many=True)

# Initialize the Campaign schema
campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)