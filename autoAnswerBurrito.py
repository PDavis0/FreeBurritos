import twilio # phone number 


# Chipotle tweets -> grab "@chipotleTweets"s' tweet -> find code -> twilio text 888222

#find code

#for each line, find words, if word.length==8 && substring(0,3) =="FREE" , set = burritoCode

#import file and get code
String code = " "
tweet = open("chipotleTweet",r)
tweetString = tweet.read()
code = findCode(tweetString)





def findCode(text):
    test = text.split()
    counter = 0
    code = 'Could not find code'
    while counter < len(test) :
        tempWord = test[counter]
        if tempWord[0:4] == 'FREE':
            code = tempWord
        counter = counter + 1
    return code