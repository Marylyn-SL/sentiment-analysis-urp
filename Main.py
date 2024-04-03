import tweepy
from tweepy import OAuthHandler
import configparser
from Repositories import Repositories 
from TweetParser import TweetParser 
from SentimentAnalyser import SentimentAnalyser 
import snscrape.modules.twitter as sntwitter
import json

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from X
        config = configparser.RawConfigParser()
        config.read('configuration.ini')

        consumer_key = config['Keys']['consumer_key']
        consumer_key_secret = config['Keys']['consumer_key_secret']
        access_token = config['Keys']['access_token']
        access_token_secret = config['Keys']['access_token_secret']
        bearer_token = config['Keys']['bearer_token']
        self.connectionString = config['Keys']['connectionString']
        
        # authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_key_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
            self.client = tweepy.Client(bearer_token)
        except:
            print("Error: Authentication Failed")
 
    def get_tweets_attributes(self, query, lang, count=1):
        '''
        Function to fetch certain attributes for tweets
        '''
        repos = Repositories(self.connectionString)
        tweetParser = TweetParser()
        analyser = SentimentAnalyser()

        for response in tweepy.Paginator(
            self.client.search_recent_tweets,
            query=query,
            expansions=["author_id","geo.place_id"],
            user_fields =['id','name','username','url','public_metrics'],
            tweet_fields=["id","lang","public_metrics","geo","source"],
            place_fields=["contained_within","country","country_code","full_name","geo","id","name","place_type"],
            limit=count
            ):
            tweets = response.data

            usersdict = {x.id:x.username for x in response.includes['users']}
            print(tweets)
            try:
                print('json' + json.dumps(response.data))
            except Exception as ex:
                print('cant parse' + str(ex))

            try:
                for tweet in tweets:
                    print(tweet)
                    tweetText = tweet.text
                    tweet_id = int(tweet.id)

                    sentimentPolarity, cleanTweet = analyser.get_tweet_sentiment(tweetText, lang)
                    
                    parsed_tweet = {}
                    parsed_tweet['tweet_id'] = tweet_id
                    parsed_tweet['text'] = tweetText
                    parsed_tweet['text_in_english'] = cleanTweet
                    parsed_tweet['created_at'] = tweet.created_at
                    parsed_tweet['source'] = tweet.source
                    parsed_tweet['favorite_count'] = tweet.public_metrics["like_count"]
                    parsed_tweet['retweet_count'] = int(tweet.public_metrics["retweet_count"])
                    parsed_tweet['lang'] = tweet.lang
                    parsed_tweet['SentimentPolarity'] = round(sentimentPolarity,2)
                    parsed_tweet['Longitude'] = None
                    parsed_tweet['Latitude'] = None
                    parsed_tweet['place_id'] = None

                    if tweet.geo is not None:
                        print(tweet.geo)
                        parsed_tweet['place_id'] = tweet.geo['place_id']

                    parsed_tweet['user_id'] = int(tweet.author_id)
                    parsed_tweet['screen_name'] = usersdict[tweet.author_id]

                    userId = repos.update_users(tweetParser.get_users_from_tweets(parsed_tweet))
                    repos.update_tweets(tweetParser.get_tweets_from_tweets(parsed_tweet,query), userId)
    
            except tweepy.TweepyException as e:
                print("Error : " + str(e))

def get_tweets(query, lang, count=1):
    scraper = sntwitter.TwitterSearchScraper(query)
    tweets = []
    for i, tweet in enumerate(scraper.get_items()):
        data = [
        tweet.date,tweet.id,
        tweet.content,
        tweet.user.username,
        tweet.likeCount,
        tweet.retweetCount,
        ]
        tweets.append(data)
        if i > count:
            break


def main():
    api = TwitterClient()
    query = "Sephora lang:en"
    langs = ['en'] 
    for lang in langs:
        api.get_tweets_attributes(query, lang, count=55)

if __name__ == "__main__":
    main()
