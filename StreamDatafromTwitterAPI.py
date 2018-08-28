#Twitter API requires twitter account
import tweepy,json
#Tweepy package has an OAuth handler, all you need to do is pass the API keys
access_token="393101461-cfZOpvqicEAhsdQhYbzRukG8ldzj9GxNF7WCyr1j"
access_token_secret="RlNjJswkmLZPXrFLjUGUeUkTi078bnqkSOINmlLSshkwS"
consumer_key="WJQsr0BHKWRSgcP0QPXq3kt5C"
consumer_secret="B63IqvZMPVZjJJT36PVrhk3tYyEIGowcnDzl6eZRUaKwdMzI9c"
#pass the API key and secret to the handler, then pass to access credentials using ser_access_token method.
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# define twitter stream listener class
#define twitter listener that create a file called 'tweets .txt', collects streeming tweers and writes

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets = 0
        self.file= open("tweets.txt","w")
        self.tweet_list =[]
    def on_status(self, status):
        tweet=status._json
    #write the stream tweets to "tweets.txt"
        self.file.write(json.dumps(tweet)+ '/n')
        self.tweet_list.append(status)
        self.num_tweets +=1
    #once the 10 tweets been stream, listener close the file
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

#create streaming object and authenticate

l=MyStreamListener()
stream=tweepy.Stream(auth,l)

#Stream tweets that contain key words by applying the filter method

stream.filter(track=['trump','clinton','sander','cruz'])

#Load and explore Twitter data
tweets_data_path = 'tweets.txt'
# Initialize empty list to store tweets: tweets_dat
tweets_data=[]
#Open connection to file
tweets_file = open(tweets_data_path,'r')
#Read in tweets and store in list:tweets_data
for line in tweets_file:
        tweets_data.append(json.loads(line))
tweets_file.closed()
print(tweets_data.keys())