

class ProceessTweets() :

    def processtweets(tweets):
        for tweet in tweets:
            username = tweet.user.name
            created_at = tweet.created_at
            tweet_text = tweet.text
            #tweet_text_sent = tweet.text
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
            print(data_dict)



