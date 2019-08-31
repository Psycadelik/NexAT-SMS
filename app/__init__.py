from flask import Flask, request, jsonify

from app.nexmo import nexmo_sms
from app.africastalking import africastalking_sms
from app.uncharted import uncharted_sms
from app.africastalking import subscription_sms
from app.africastalking import cheza_sms

from app.config import configs
from app import tasks

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# from app import models


def nexmoclient(sms, recipient):
    return nexmo_sms(sms, recipient)


def atclient(sms, recipient):
    return africastalking_sms(sms, recipient)


def chezaAT(recipient):
    return cheza_sms(recipient)


def anonymous(sms, recipient):
    return uncharted_sms(sms, recipient)


# app = Flask(__name__)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.route('/sendsms', methods=['POST'])
    def send_sms():

        provider = request.get_json().get('provider')

        sms = request.get_json().get('sms')

        recipient = request.get_json().get('recipient')

        if provider == 'nexmo':

            return nexmoclient(sms, recipient)

        elif provider == 'africastalking':

            return atclient(sms, recipient)

        elif provider == 'chezaAT':

            return chezaAT(recipient)

        else:
            return anonymous(sms, recipient)

    @app.route('/inbox/sms', methods=['POST'])
    def inbox_sms_incoming():
        phoneNumber = request.get_json().get("phoneNumber")
        shortCode = request.get_json().get("shortCode")
        keyword = request.get_json().get("keyword")
        updateType = request.get_json().get("updateType")

        return jsonify(phoneNumber, shortCode, keyword, updateType)

    return app
