from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from texter import textCode


forwardTexts = Flask(__name__)


@forwardTexts.route('/sms', methods=['POST'])
def sms():
    #number = request.form['From']
    message_body = request.form['Body']
    #resp = MessagingResponse()
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    textCode("+1XXXX",message_body)
    return 'OK'

if __name__ == '__main__':
    forwardTexts.run(
        host="0.0.0.0",
        port=int("5000")
    )
