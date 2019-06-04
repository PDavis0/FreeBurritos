import tweepy

#im an idiot - Parker
#we need to create an code class w/ a code parameter. That eliminates this global variable stuff

#override tweepy.StreamListener, adding logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        store_tweet_filename = "chipotleTweetsTweet.txt"
        with open(store_tweet_filename,'w') as tf:
                tf.write(status.text)



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
myStream.filter(follow=['141341662'])




