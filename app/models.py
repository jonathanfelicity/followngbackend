from datetime import datetime
from . import db




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    created_At = db.Column(db.DateTime, server_default=db.func.now())
    is_Banned = db.Column(db.Boolean, default=False, nullable=False)


    wallet = db.relationship("Wallet", backref="user", uselist=False)


    def __repr__(self):
        return f"User('{self.username}', '{self.created_At}'"



class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=200.0, nullable=False)
    updated_At = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                       onupdate=db.func.current_timestamp())
    
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"User('{self.owner}', '{self.balance}', '{self.balance}'"