import tweepy
import pandas as pd
import constants
from constants import consumer_key, consumer_secret, access_token, access_secret, hashtag, tweetsPerQry, maxTweets


class TweetProcessor:

    # init
    def __init__(self):
        # TODO: Shift this to process_tweet
        # authentication
        authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_secret)
        self.api = tweepy.API(authentication, wait_on_rate_limit=True)

    # fetch tweets
    def fetchtweets(self):

        while constants.tweetCount < maxTweets:
            if constants.maxId <= 0:
                new_tweets = self.api.search_tweets(q=hashtag, count=tweetsPerQry, result_type="recent",
                                                    tweet_mode="extended", lang="en")

            else:
                new_tweets = self.api.search_tweets(q=hashtag, count=tweetsPerQry, max_id=str(constants.maxId - 1),
                                                    result_type="recent", tweet_mode="extended", lang="en")

            if not new_tweets:
                print("Done")
                break
            # pre-process tweets

            for tweet in new_tweets:
                username = tweet.user.name
                created_at = tweet.created_at
                tweet_text = tweet.full_text
                tweet_text_sent = tweet.full_text
                retweet_count = tweet.retweet_count
                fav_count = tweet.favorite_count
                media_source = tweet.source
                data_dict = {
                    "username": username,
                    "created_at": created_at,
                    "tweet_text": tweet_text,
                    "retweet_count": retweet_count,
                    "fav_count": fav_count,
                    "media_source": media_source,
                }
                constants.tweets = constants.tweets.append([data_dict], ignore_index=True, sort=False)
                # print(data_dict)
            constants.tweetCount += len(new_tweets)
            constants.maxId = new_tweets[-1].id
        return constants.tweets
