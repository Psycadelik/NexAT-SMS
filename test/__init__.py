import unittest
import json

from sibsco import create_app


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(environment="testing")

    def setUp(self):
        with self.app.app_context():
            self.app.testing = True
            self.app = self.app.test_client()

            self.data = {
                "provider": "nexmo",
                "sms": "test message",
                "recipient": 254727440297
            }

            self.dat = {
                "provider": "nexmo"

            }

            self.afData = {
                "provider": "africastalking",
                "sms": "test sms",
                "recipient": 254727440297
            }

            self.afDat = {
                "provider": "africastalking",
                "sms": "",
                "recipient": 254727440297
            }

            self.uData = {
                "provider": "vendit",
                "sms": "test sms",
                "recipient": 254727440297
            }

            self.sms = {
                "phoneNumber": 254727440297,
                "shortCode": 4598,
                "keyword": "cheza",
                "updateType": "init"
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
        self.assertTrue(response.status_code, 200)

    def test_successful_africastalking_sms(self):
        res = "sent"

        response = self.app.post('/sendsms', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_failed_africastalking_sms(self):
        res = "Invalid username and/or api_key"

        response = self.app.post('/sendsms', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_anonymous_sms(self):
        res = "Message queued"

        response = self.app.post('/sendsms', data=json.dumps(self.uData), content_type='application/json')
        self.assertTrue(response, res)

    def test_inbox_sms(self):

        response = self.app.post('/inbox/sms', data=json.dumps(self.sms), content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
