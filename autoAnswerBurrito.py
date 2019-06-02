import twilio # phone number 
from texter import textCode
import IngestChipotleTweets
import app

# Chipotle tweets -> grab "@chipotleTweets"s' tweet -> find code -> twilio text 888222

#
# Before running this file, 
# run ./ngrok http 5000 in terminal
# run app.py in another terminal
# update Twilio "when a message comes in" field to be 
# the ngrok port forwarding address it gives you, with "/sms" appended
#

def findCode(text) :
    test = text.split()
    counter = 0
    code = 'Could not find code'
    while counter < len(test) :
        tempWord = test[counter]
        if tempWord[0:4] == 'FREE':
            code = tempWord
        counter = counter + 1
    return code

#seperate file grabbing tweet -> text file "sampleChipotleTweet"

#find code
tweetString = IngestChipotleTweets.getCode()
#tweet = open('sampleChipotleTweet.txt','r')     ...not stored in a text file.
#tweetString = tweet.read()
code = findCode(tweetString)
print(code)

#text code to 888222
textCode("+1888222",code)
#reponse forwarding is done by app.py
