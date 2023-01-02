from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String, DateTime, Float)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from . import Base


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




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, default=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    balance = Column(Float, default=200.0, nullable=False)
    is_banned = Column(Boolean, default=False, nullable=False)

    campaigns = relationship("Campaign", back_populates="owner")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    engagement = Column(Integer, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="campaigns")
