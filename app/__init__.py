from flask import Flask, request

from app.nexmo import nexmo_sms
from app.africastalking import africastalking_sms
from app.uncharted import uncharted_sms

from app.config import configs
from app import tasks


def nexmoclient(sms, recipient):
    return nexmo_sms(sms, recipient)


def atclient(sms,recipient):
    return africastalking_sms(sms, recipient)


def anonymous(sms, recipient):
    return uncharted_sms(sms, recipient)


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])

    @app.route('/sendsms', methods=['POST'])
    def send_sms():

        provider = request.get_json().get('provider')

        sms = request.get_json().get('sms')

        recipient = request.get_json().get('recipient')

        if provider == 'nexmo':

            return nexmoclient(sms, recipient)

        elif provider == 'africastalking':

            return atclient(sms, recipient)

        else:
            return anonymous(sms, recipient)

    return app
