import africastalking
import os
from flask import jsonify


#
# class SmsService:
#     def __init__(self):
#
#         self.username = os.getenv("AT_USERNAME")
#
#         self.api_key = os.getenv("AT_API_KEY")
#
#         africastalking.initialize(self.username, self.api_key)
#
#         self.sms = africastalking.SMS

def africastalking_sms(sms):
    username = os.getenv("AT_USERNAME")
    api_key = os.getenv("AT_API_KEY")

    africastalking.initialize(username, api_key)

    atsms = africastalking.SMS

    # Set the numbers you want to send to in international format
    recipients = ["+254727440297", "+254726063033"]

    # Set your message
    # message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
    message = sms

    # Set your shortCode or senderId
    sender = os.getenv("AT_SHORTCODE")

    try:
        # Thats it, hit send and we'll take care of the rest.
        response = atsms.send(message, recipients, sender)
        return jsonify(response)
    except Exception as e:
        return jsonify('Encountered an error while sending: %s' % str(e))
