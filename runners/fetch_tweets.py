import tweepy

from constants import consumer_key, consumer_secret, access_token, access_secret


class FetchTweets:

    def __init__(self):
        # authentication
        authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_secret)
        self.api = tweepy.API(authentication, wait_on_rate_limit=True)

    def fetchtweets(self):
        # fetching tweets
        new_tweets = self.api.search_tweets(q="FIFA", count=50, result_type="recent", tweet_mode="extended")
        return new_tweets
