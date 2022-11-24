from nltk.corpus import stopwords
from textblob import TextBlob

# SentimentAnalyzer

#  analyze_tweet

def clean_text(text):
  ex_list = ['rt', 'http', 'RT']
  exc = '|'.join(ex_list)
  text = re.sub(exc, ' ' , text)
  text = text.lower()
  words = text.split()
  stopword_list = stopwords.words('english')
  words = [word for word in words if not word in stopword_list]
  clean_text = ' '.join(words)
  return clean_text

def sentiment_score(text):
  analysis = TextBlob(text)
  if analysis.sentiment.polarity > 0:
    return 1
  elif analysis.sentiment.polarity == 0:
    return 0
  else:
    return -1