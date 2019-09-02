from flask import jsonify


def uncharted_sms(sms, recipient):
    response = "message queued"

    return jsonify(response)
