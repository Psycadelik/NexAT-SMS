from flask import Flask, request

from app.nexmo import nexmo_sms
from app.africastalking import africastalking_sms

from app.config import configs


def nexmoclient(sms):
    nexmo_sms(sms)


def atclient(sms):
    africastalking_sms(sms)


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])

    @app.route('/sendsms', methods=['POST'])
    def send_sms():
        # sms and provider are picked from the request
        provider = request.get_json().get('provider')
        # print(provider)
        sms = request.get_json().get('sms')

        if provider == 'nexmo':
            return nexmoclient(sms)
        elif provider == 'africastalking':
            return atclient(sms)
        else:
            return "invalid provider"

    return app
