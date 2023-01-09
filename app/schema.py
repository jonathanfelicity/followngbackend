from .models import User, Campaign, Wallet
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from . import ma

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ['created_At']
        load_instance = True

class WalletSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Wallet
        exclude = ['user']
        load_instance = True

class CampaignSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Campaign
        exclude = ['user', 'campaign_created_at']
        load_instance = True
        

# Initialize the User schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Initialize the Wallet schema
wallet_schema = WalletSchema()
wallets_schema = WalletSchema(many=True)

# Initialize the Campaign schema
campaign_schema = CampaignSchema()
campaigns_schema = CampaignSchema(many=True)