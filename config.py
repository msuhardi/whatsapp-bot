# config.py

import os

class Config(object):
    RAPID_API_KEY = os.environ.get('RAPID_API_KEY')
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')