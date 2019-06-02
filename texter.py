from twilio.rest import Client

def textCode(number, code):
    account_sid = x"
    auth_token  = "x"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=number, 
        from_="+x",
        body=code
    )
