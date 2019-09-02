import africastalking
import os
from flask import jsonify


def africastalking_sms(sms, recipient):
    username = os.getenv("AT_USERNAME")
    api_key = os.getenv("AT_API_KEY")

    africastalking.initialize(username, api_key)

    atsms = africastalking.SMS

    recipients = ["+{}".format(recipient)]

    message = sms

    sender = os.getenv("AT_SHORTCODE")

    try:
        response = atsms.send(message, recipients, sender)
        return jsonify(response)
    except Exception as e:
        return jsonify('Encountered an error while sending: %s' % str(e))


def cheza_sms(recipient):
    username = os.getenv("AT_USERNAME")
    api_key = os.getenv("AT_API_KEY")

    africastalking.initialize(username, api_key)

    atsms = africastalking.SMS

    recipients = ["+{}".format(recipient)]

    message1 = "Who is the president of Kenya? " \
               "A.  Raila Odinga" \
               "B.  Uhuru Kenyatta"

    message2 = "which is the largest county in Kenya?" \
               "A. Tana River" \
               "B. Makueni"

    sender = os.getenv("AT_SHORTCODE")

    try:
        response = atsms.send(message1, recipients, sender)
        return jsonify(response)
    except Exception as e:
        return jsonify('Encountered an error while sending: %s' % str(e))


def subscription_sms(recipient):
    username = os.getenv("AT_USERNAME")
    api_key = os.getenv("AT_API_KEY")

    africastalking.initialize(username, api_key)

    sms = africastalking.SMS
    token = africastalking.Token

    shortCode = os.getenv("AT_SUB_SHORTCODE")
    keyword = os.getenv("AT_KEYWORD")

    recipients = ["+{}".format(recipient)]

    try:
        checkoutToken = token.create_checkout_token(recipients)['token']

        response = sms.create_subscription(shortCode, keyword, recipients, checkoutToken)

        return jsonify("Status: %s \n Description: %s" % (response['status'], response['description']))
    except Exception as e:
        return jsonify("Error creating subscription:%s" % str(e))
