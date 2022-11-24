# twitter API credentials
import pandas as pd

consumer_key = 'HhPnaHmHjgYtnQ5kgtROO751y'
consumer_secret = 'Gf4PNwrtCQrCtmgKM046WB5wzgAwi5g6wFvOWXvy427GQcnHd6'
access_token = '964409866902122496-58zNwrlXJ2ZMxE7ufCJto1tnueoxiRj'
access_secret = 'Ytcl2GJg6p7ZV4GGMMI5gVFSwuQY8zZp7JeKB8OYNdoPd'
conn_string='postgresql://aditya:aditya@localhost:5432/FIFA2022'
hashtag = "USC"
maxId = -1
tweetCount=0
tweetsPerQry = 20
maxTweets = 60
tweets = pd.DataFrame(
            columns=["username", "created_at", "tweet_text", "retweet_count", "fav_count", "media_source"])