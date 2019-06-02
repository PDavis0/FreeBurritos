from twilio.rest import Client

def textCode(number, code):
    account_sid = "AC136c27d243f697f5b31270917024f879"
    auth_token  = "7b9530de53f35a007881f7128c20de5f"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=number, 
        from_="+16149074552",
        body=code
    )
