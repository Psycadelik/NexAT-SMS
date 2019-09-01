import os
from flask import Flask, request, jsonify

from app.nexmo import nexmo_sms
from app.africastalking import africastalking_sms
from app.uncharted import uncharted_sms
from app.africastalking import subscription_sms
from app.africastalking import cheza_sms

from app.config import configs
from app import tasks

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

from app.db import get_db


# from app.models import SMS

# from app import models


def nexmoclient(sms, recipient):
    return nexmo_sms(sms, recipient)


def atclient(sms, recipient):
    return africastalking_sms(sms, recipient)


def chezaAT(recipient):
    return cheza_sms(recipient)


def subscribe_user(recipient):
    return subscription_sms(recipient)


def anonymous(sms, recipient):
    return uncharted_sms(sms, recipient)


# app = Flask(__name__)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


def create_app(environment='development', test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configs[environment])
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'cheza.sqlite')
    )
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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

    @app.route('/create/subscription', methods=['POST'])
    def create_sms_subscription():

        recipient = request.get_json().get('recipient')

        try:
            subscribe_user(recipient)

            return jsonify("Subscription created successfully")
        except Exception as e:
            return jsonify("an error occurred while saving to database")

    @app.shell_context_processor
    @app.route('/inbox/sms', methods=['POST'])
    def inbox_sms_incoming():
        phoneNumber = request.get_json().get("phoneNumber")
        shortCode = request.get_json().get("shortCode")
        keyword = request.get_json().get("keyword")
        updateType = request.get_json().get("updateType")

        db = get_db()
        db.execute(
            'INSERT INTO sms (phoneNumber, shortCode, keyword, updateType) VALUES (?,?,?,?)',
            (phoneNumber, shortCode, keyword, updateType)
        )
        db.commit()

        # m = SMS()
        # m.phoneNumber = phoneNumber
        # m.shortCode = shortCode
        # m.keyword = keyword
        # m.updateType = updateType
        # db.session.add(m)

        message = ["Response saved successfully from +{}".format(phoneNumber)]

        try:
            return jsonify(message)
        except Exception as e:
            return jsonify("an error occurred while saving to database")

    @app.route('/cheza/winner', methods=['GET'])
    def pick_random_winner():
        db = get_db()
        sms_responses = db.execute(
            'SELECT phoneNumber from sms where updateType = ?',
            ('sms')
        )

    from . import db
    db.init_app(app)
    return app
