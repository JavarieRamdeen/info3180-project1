import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = 'postgres://qqryhwxjpyxrrn:1f24c797e7429f4e2f4843f97869b60d6d48b9be5d72d88053dcca846f59dceb@ec2-54-158-26-89.compute-1.amazonaws.com:5432/djlg70kot3d98'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed