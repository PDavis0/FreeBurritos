import tweepy
import keys

#im an idiot - Parker
#we need to create an code class w/ a code parameter. That eliminates this global variable stuff

#override tweepy.StreamListener, adding logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        store_tweet_filename = "chipotleTweetsTweet.txt"
        with open(store_tweet_filename,'w') as tf:
                tf.write(status.text)



#tweepy SETUP... (my twitter keys & tokens)
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=['141341662'])




