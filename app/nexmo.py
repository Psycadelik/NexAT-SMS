import nexmo
import os


def nexmo_sms(sms):
    NEXMO_API_KEY = os.getenv("NEXMO_API_KEY")
    NEXMO_API_SECRET = os.getenv("NEXMO_API_SECRET")

    client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)

    responseData = client.send_message(
        {
            "from": "Acme Inc",
            "to": 254727440297,
            "text": sms,
            # "text": "A text message sent using the Nexmo SMS API",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

    return sms