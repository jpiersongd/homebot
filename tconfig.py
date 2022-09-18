import datetime
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'xxxxx' # replace with your Account SID
TWILIO_AUTH_TOKEN = 'xxxxx' # replace with your Auth Token
TWILIO_PHONE_SENDER = "+xxxxx" # replace with the phone number you registered in twilio
TWILIO_PHONE_RECIPIENT = "xxxxx" # replace with your phone number

def send_text_alert(alert_str):
    """Sends an SMS text alert."""
    shorttimestamp = (' {:%H:%M}'.format(datetime.datetime.now()))
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=TWILIO_PHONE_RECIPIENT,
        from_=TWILIO_PHONE_SENDER,
        body=(alert_str + shorttimestamp))
    print("sms sent")
