import constants
from runners.fetch_tweets import FetchTweets
from runners.process_tweets import ProceessTweets
from runners.tweet_processor import TweetProcessor
from constants import tweetCount
from IPython.display import display
#obj = FetchTweets()
#print(obj.fetchtweets())


processor = TweetProcessor()
data=processor.fetchtweets()


#
# preprocessed_tweet = processor.pre_process()
#
# analyzer = SentimentAnalyzer()
#
# analysis = analyzer.analyze(preprocessed_tweet)
# db = Database()
# db.store(analysis, preprocessed_tweet)
