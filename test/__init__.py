import unittest
import json
from app.nexmo import nexmo_sms
from app.africastalking import africastalking_sms
from app import create_app
from flask import jsonify


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(environment="testing")

    def setUp(self):
        with self.app.app_context():
            # app = create_app(environment="testing")
            self.app.testing = True
            self.app = self.app.test_client()

            self.data = {
                "provider": "nexmo",
                "sms": "test message"
            }

            self.dat = {
                "provider": "nexmo"

            }

            self.da = {
                "provider": "africastalking",
                "sms": "test sms"
            }

            self.af = {
                "provider": "africastalking",
                "sms": ""
            }

            self.response = {
                "message sent successfully"
            }

            self.re = {
                "error processing message"
            }

            self.res = {
                "message has been added to queue"
            }

            self.jsonStr = {
                "SMSMessageData": {
                    "Message": "Sent to 2/2 Total Cost: KES 1.6000",
                    "Recipients": [
                        {
                            "cost": "KES 0.8000",
                            "messageId": "ATXid_db3892dd2b049fd664ddab10cf3a3744",
                            "number": "+254726063033",
                            "status": "Success",
                            "statusCode": 101
                        },
                        {
                            "cost": "KES 0.8000",
                            "messageId": "ATXid_c914d64cac5ededc8ae3434a2ae982d0",
                            "number": "+254727440297",
                            "status": "Success",
                            "statusCode": 101
                        }
                    ]
                }
            }

    def test_endpoint(self):
        response = self.app.post('/sendsms', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_successful_nexmo_sms(self):
        res = "Message sent successfully"

        response = self.app.post('/sendsms', data=json.dumps(self.data), content_type='application/json')
        self.assertTrue(response, res)

    def test_failed_nexmo_sms(self):
        res = "There was an error processing your request in the Platform."

        response = self.app.post('/sendsms', data=json.dumps(self.dat), content_type='application/json')
        self.assertTrue(response, res)

    def test_successful_africastalking_sms(self):
        res = "sent"

        response = self.app.post('/sendsms', data=json.dumps(self.da), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_failed_africastalking_sms(self):
        res = "Invalid username and/or api_key"

        response = self.app.post('/sendsms', data=json.dumps(self.af), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_anonymous_sms(self):
        sms = "test sms"
        provider = "unknown"


if __name__ == "__main__":
    unittest.main()
