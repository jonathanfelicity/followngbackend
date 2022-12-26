from datetime import datetime
from . import db
import sys

import random



def generate_device():
    device_names = [
        'samsung_galaxy_s7',
        'huawei_mate_9_pro',
        'one_plus_3t',
        'lg_g5',
        'zte_axon_7',
        'samsung_galaxy_s7_edge',
    ]
    
    name = random.choice(device_names)
    
    instagram_version = f"{random.randint(10, 30)}.{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(10, 99)}.{random.randint(10, 99)}"
    android_version = random.randint(16, 29)
    android_release = f"{random.randint(5, 11)}.{random.randint(0, 9)}"
    dpi = f"{random.randint(200, 700)}dpi"
    resolution_x = random.randint(600, 2000)
    resolution_y = random.randint(600, 2000)
    resolution = f"{resolution_x}x{resolution_y}"
    manufacturer = f"manufacturer_{random.randint(1, 1000)}"
    device = f"device_{random.randint(1, 1000)}"
    model = f"model_{random.randint(1, 1000)}"
    cpu = f"cpu_{random.randint(1, 1000)}"

    return {
        'name': name,
        'instagram_version': instagram_version,
        'android_version': android_version,
        'android_release': android_release,
        'dpi': dpi,
        'resolution': resolution,
        'manufacturer': manufacturer,
        'device': device,
        'model': model,
        'cpu': cpu,
        }



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    is_banned = db.Column(db.Boolean, default=False, nullable=False)
    balance = db.Column(db.Float, default=200.0, nullable=False)



    campaigns = db.relationship('Campaign', backref='user', lazy=True)


    def __init__(self, username) -> None:
        self.username = username
        self.device = generate_device()

    def __repr__(self):
        return f"User('{self.username}', '{self.created_at}')"


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    engagement = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_complete = db.Column(db.Boolean, default=False, nullable=False)