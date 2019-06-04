from twilio.rest import Client
import keys

def textCode(number, code):
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
        to=number, 
        from_="+16149074552",
        body=code
    )
