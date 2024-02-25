import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    DEBUG = os.environ.get('FLASK_DEBUG') or True