# twitter API credentials
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Access the environment variables
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')
conn_string='postgresql://aditya:aditya@localhost:5432/FIFA2022'
hashtag = "USC"
maxId = -1
tweetCount=0
tweetsPerQry = 20
maxTweets = 60
tweets = pd.DataFrame(
            columns=["username", "created_at", "tweet_text", "retweet_count", "fav_count", "media_source"])