from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SECRET_KEY']= 'f0fc14b08995b4cbd607ed82031ed0839214f47d6750c73ebd4d0b0422093a8ef3f724'
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///followng.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(api)



from . import routes