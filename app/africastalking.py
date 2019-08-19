import africastalking
import os


def africastalking_sms(sms):
    username = ""
    api_key = ""

    africastalking.initialize(username, api_key)

    atsms = africastalking.SMS

    # Set the numbers you want to send to in international format
    recipients = ["+254727440297", "+254733YYYZZZ"]

    # Set your message
    # message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
    message = sms

    # Set your shortCode or senderId
    sender = "shortCode or senderId"

    try:
        # Thats it, hit send and we'll take care of the rest.
        response = atsms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print('Encountered an error while sending: %s' % str(e))

    return sms
