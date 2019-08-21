from flask import Flask, request

from app.nexmo import nexmo_sms
from app.africastalking import africastalking_sms
from app.uncharted import uncharted_sms

from app.config import configs
from app import tasks


def nexmoclient(sms):
    return nexmo_sms(sms)


def atclient(sms):
    return africastalking_sms(sms)


def anonymous(sms):
    return uncharted_sms(sms)


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])

    @app.route('/sendsms', methods=['POST'])
    def send_sms():

        provider = request.get_json().get('provider')

        sms = request.get_json().get('sms')

        if provider == 'nexmo':

            return nexmoclient(sms)

        elif provider == 'africastalking':

            return atclient(sms)

        else:
            return anonymous(sms)

    return app
