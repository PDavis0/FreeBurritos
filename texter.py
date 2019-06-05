from twilio.rest import Client
import keys

def textCode(number, code):
<<<<<<< HEAD
    account_sid = x"
    auth_token  = "x"

    client = Client(account_sid, auth_token)
=======
    client = Client(keys.account_sid, keys.auth_token)
>>>>>>> b9941b014f78c355a0d97382125e107e29a4f477

    message = client.messages.create(
        to=number, 
        from_="+x",
        body=code
    )
