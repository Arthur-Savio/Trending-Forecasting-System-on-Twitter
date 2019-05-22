import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweets.api_twitter.src.read_tweets import MyListener
from tweets.api_twitter.src.to_process_tweets import ProcessTweets
from tweets.api_twitter.src.read_trending_topics import ReadTrendingTopics
from tweets.api_twitter.src.mining_location import MiningLocation

class InitializeTwitterApi:
    #Authentication class and API start

    def __init__(self):
        #Key and tokens attributes are obtained with twitter signup

        self.consumer_key = "YOUR CONSUMER KEY"
        self.consumer_secret = "YOUR SECRET KEY"
        self.access_token = "YOUR ACCESS TOKEN"
        self.access_token_secret = "YOUR TOKEN SECRET"
        self.auth = None
        self.api = None
        self.result = None
        self.geo_location = None
        self.ppt = ProcessTweets()
        self.set_access_api_keys()

    def set_access_api_keys(self):
        #Key and tokens validation 
        
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    def init_read_trending_topics(self):
        return ReadTrendingTopics(self.api).read()
        
    def init_read_api(self, term, limit):
        receive_my_listener = MyListener(term, limit)
        twitter_stream = Stream(self.auth, receive_my_listener)
        twitter_stream.filter(track=[term], languages=["en"])
        twitter_stream.disconnect()
        self.ppt.initialize_process()
        self.ppt.read_datas_to_generate_tokens()
        self.result = self.ppt.selected_tweets
        self.geo_location = self.ppt.geo_location

