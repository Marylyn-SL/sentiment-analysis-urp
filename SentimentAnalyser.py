from textblob import TextBlob
import re

class SentimentAnalyser:
    """
    Class for sentiment analysis.
    """

    def clean_tweet(self, tweet):
        """
        Utility function to clean tweet text by removing links, special characters, and usernames.
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet, lang):
        """
        Function to get sentiment polarity of a tweet.
        """
        cleanTweet = self.clean_tweet(tweet)
        analysis = TextBlob(cleanTweet)

        if lang == "en": 
            return analysis.sentiment.polarity, cleanTweet
        else:
            return None, cleanTweet