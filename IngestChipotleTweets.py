import tweepy

globalCodeVariable = " "

def setCode(code):
    globalCode=code

def getCode():
    return globalCodeVariable

#override tweepy.StreamListener, adding logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        #kinda set the code 2 ways... no time to check.. gotta golf
        globalCodeVariable = status.text
        setCode(status.text)

        print(status.text)



#tweepy SETUP... (my twitter keys & tokens)
# Consumer keys and access tokens, used for OAuth
consumer_key = 'P2UChBzWXkg3pQFSFTa5zP8nv'
consumer_secret = 'BUHOHsKVbC7ndbINKNUiJDN0vgKEyBlJq88VK9Y117nLu6iRM8'
access_token = '171536160-CSObVDa39klgVsGfj2H9CJL3gHjvlLZUOaDv453t'
access_token_secret = 'qS5Tsk7O0mhmGG8lXUNbUxDrYxbep5emvqmm7hRTOldJz'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=['171536160'])



