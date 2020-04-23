# app/routes.py

from flask import request
from app import api, app, utils

from twilio.twiml.messaging_response import MessagingResponse

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/newMessage', methods=['POST'])
def new_message():
    msg = request.values.get('Body', '')

    if msg == '/stats':
        return _send_stats_update()


    return _send_message('Please type `/stats` to get the current Covid-19 statistics in Indonesia')


def _send_message(message):
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(message)
    return str(resp)


def _send_stats_update():
    data = api.get_stats("Indonesia")
    sby_data =  api.get_surabaya_stats()

    msg = "% s\n\n--------------------------------------------------------\n% s"% (
        utils.parse_data_to_stats(data),
        utils.parse_sby_data_to_stats(sby_data)
    )
    return _send_message(msg)
