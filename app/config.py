import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    DATABASE_URL='postgres://okwtglrfkgtgba:b4253e0096dd33e04cb4fff38b4b80174beb0e52e95878f176d68ebd89ea1f5d@ec2-52-202-152-4.compute-1.amazonaws.com:5432/d4lho342c7n69a'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed