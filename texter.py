from twilio.rest import Client




def textCode(code):
    account_sid = "xxxxxxxxxxxxxxxxx"
    auth_token  = "xxxxxxxxxxxxxxx"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+1xxxxxxxx", 
        from_="+1xxxxxxxx",
        body=code
    )
