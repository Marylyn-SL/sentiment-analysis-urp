class TweetParser:
    def get_users_from_tweets(self, tweet):
        user = {}
        user['user_id'] = tweet['user_id']
        user['screen_name'] = tweet['screen_name']

        return user

    def get_place_from_tweets(self, tweet):
        place = {}
        if tweet['place'] is not None:
            place['ExternalId'] = tweet['place']['ExternalId']
            place['Name'] = tweet['place']['Name']
            place['FullName'] = tweet['place']['FullName']
            place['PlaceType'] = tweet['place']['PlaceType']
            place['Country'] = tweet['place']['Country']
            place['CountryCode'] = tweet['place']['CountryCode']
            place['URL'] = tweet['place']['URL']

        return place

    def get_tweets_from_tweets(self, raw_tweet, query):
        tweet = {}
        tweet['tweet_id'] = raw_tweet['tweet_id']
        tweet['text'] = raw_tweet['text']
        tweet['text_in_english'] = raw_tweet['text_in_english']
        tweet['created_at'] = raw_tweet['created_at']
        tweet['source'] = raw_tweet['source']
        tweet['favorite_count'] = raw_tweet['favorite_count']
        tweet['retweet_count'] = raw_tweet['retweet_count']
        tweet['lang'] = raw_tweet['lang']
        tweet['Latitude'] = raw_tweet['Latitude']
        tweet['Longitude'] = raw_tweet['Longitude']
        tweet['place_id'] = raw_tweet['place_id']
        tweet['SentimentPolarity'] = raw_tweet['SentimentPolarity']
        tweet['fk_user_id'] = raw_tweet['user_id']
        tweet['query'] = query

        return tweet