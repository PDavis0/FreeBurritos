from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


forwardTexts = Flask(__name__)


@forwardTexts.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print(message_body)
    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == '__main__':
    forwardTexts.run(
        host="0.0.0.0",
        port=int("5000")
    )
