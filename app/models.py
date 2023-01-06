from . import db
from datetime import datetime
from sqlalchemy.sql import func




# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    is_banned = db.Column(db.Boolean, default=False, nullable=False)
    insta_id = db.Column(db.String(255), nullable=False, unique=True)
    created_At = db.Column(db.DateTime, server_default=db.func.now())

# Define the Wallet model
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = db.relationship('User', backref=db.backref('wallet', uselist=False))

# Define the Campaign model
class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type =  db.Column(db.db.String(255), nullable=False)
    goal = db.Column(db.Integer, nullable=False)
    # link = db.column(db.String,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    user = db.relationship('User', backref=db.backref('campaigns', lazy=True))
    campaign_created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
