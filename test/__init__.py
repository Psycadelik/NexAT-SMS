import unittest


class TestUtils(BaseException):
    def test_nexmo_sms(self):
        sms = "test sms"
        provider = "nexmo"

    def test_africastalking_sms(self):
        sms = "test sms"
        provider = "africastalking"

    def test_anonymous_sms(self):
        sms = "test sms"
        provider = "unknown"


if __name__ == "__main__":
    unittest.main()
