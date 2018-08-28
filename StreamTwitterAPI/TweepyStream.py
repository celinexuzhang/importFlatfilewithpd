import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token="393101461-cfZOpvqicEAhsdQhYbzRukG8ldzj9GxNF7WCyr1j"
access_token_secret="RlNjJswkmLZPXrFLjUGUeUkTi078bnqkSOINmlLSshkwS"
consumer_key="WJQsr0BHKWRSgcP0QPXq3kt5C"
consumer_secret="B63IqvZMPVZjJJT36PVrhk3tYyEIGowcnDzl6eZRUaKwdMzI9c"

#Twitter auth

class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

#twitter client

class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth= TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client=API(self.auth)

        self.twitter_user=twitter_user
    def get_user_timeline_tweets(self,num_tweets):
        tweets= []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self,num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends,id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets=[]
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

#create a class call StdOutListener, which will inherent from StreemListener class
class TwitterListener(StreamListener):
    def __init__(self,fetched_tweet_filename):
        self.fetched_tweet_filename = fetched_tweet_filename
#StreamListener class provide direct method we overwrite
    def on_data(self,data):
        try:
            with open(self.fetched_tweet_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("error on data:%s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code==420:
            #returning false on data methon in ase rate limit occurs
            return False
        print(status_code)

#from this StdoutListener class we will create an object

class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator=TwitterAuthenticator()
    def stream_tweets(self,fetched_tweet_filename, hash_tag_list):
#this handle twitter authentication and the connection to the Twitter Streaming API
        listener = TwitterListener(fetched_tweet_filename)  # object we create for the StdOutListener which will inherent from StreamListener Class
        auth=self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)

if __name__== "__main__":
    hash_tag_list = ['trump','clinton','sander','cruz']
    fetched_tweet_filename = "tweet_1.json"

    twitter_client=TwitterClient('realDonaldTrump')
    print(twitter_client.get_user_timeline_tweets(10))

    #twitterstreamer= TwitterStreamer()
    #twitterstreamer.stream_tweets(fetched_tweet_filename,hash_tag_list)