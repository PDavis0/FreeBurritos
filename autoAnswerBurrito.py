import twilio # phone number 
from texter import textCode
import IngestChipotleTweets


# Chipotle tweets -> grab "@chipotleTweets"s' tweet -> find code -> twilio text 888222

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
code = IngestChipotleTweets.getCode()
tweet = open('sampleChipotleTweet.txt','r')
tweetString = tweet.read()
code = findCode(tweetString)
print(code)

#text code to 888222
textCode(code)
#seperate file interpretting chipotle texts (forward to our phone number)
