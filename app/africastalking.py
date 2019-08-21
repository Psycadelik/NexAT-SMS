import africastalking
import os
from flask import jsonify


def africastalking_sms(sms):
    username = os.getenv("AT_USERNAME")
    api_key = os.getenv("AT_API_KEY")

    africastalking.initialize(username, api_key)

    atsms = africastalking.SMS

    recipients = ["+254727440297", "+254726063033"]

    message = sms

    sender = os.getenv("AT_SHORTCODE")

    try:
        response = atsms.send(message, recipients, sender)
        return jsonify(response)
    except Exception as e:
        return jsonify('Encountered an error while sending: %s' % str(e))
