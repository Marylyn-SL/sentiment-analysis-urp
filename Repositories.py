import psycopg2

class Repositories:
    """Handles database operations."""

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def update_tweets(self, tweet, user_id):
        """Update or insert tweet data."""
        try:
            update_tweet_sql = """
                INSERT INTO posts (tweet_id, text, text_in_english, created_at, source, 
                                   favorite_count, retweet_count, lang, sentiment_polarity, 
                                   query, longitude, latitude, fk_user_id, place_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (tweet_id) DO UPDATE 
                SET favorite_count = EXCLUDED.favorite_count,
                    retweet_count = EXCLUDED.retweet_count;
            """
            connection = psycopg2.connect(self.connection_string)
            cursor = connection.cursor()
            values = (tweet['tweet_id'], tweet['text'], tweet['text_in_english'], tweet['created_at'], 
                      tweet['source'], tweet['favorite_count'], tweet['retweet_count'], tweet['lang'], 
                      tweet['SentimentPolarity'], tweet['query'], tweet['Longitude'], 
                      tweet['Latitude'], user_id, tweet['place_id'])
            cursor.execute(update_tweet_sql, values)

            connection.commit()
            connection.close()

        except psycopg2.Error as e:
            print("psycopg2 Error:", e)
            print(values)

    def update_place(self, place):
        """Update or insert place details."""
        try:
            update_place_sql = """
                INSERT INTO place (external_id, name, full_name, place_type, url, country, country_code)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (external_id) DO NOTHING
                RETURNING id;
            """
            connection = psycopg2.connect(self.connection_string)
            cursor = connection.cursor()
            values = (place['ExternalId'], place['Name'], place['FullName'], place['PlaceType'], 
                      place['URL'], place['Country'], place['CountryCode'])
            cursor.execute(update_place_sql, values)

            place_id = cursor.fetchone()[0]  
            connection.commit()
            connection.close()
            return place_id
        
        except psycopg2.Error as e:
            print("psycopg2 Error:", e)

    def update_users(self, user):
        """Update or insert user data."""
        try:
            update_user_sql = """
                INSERT INTO users (user_id, screen_name)
                VALUES (%s, %s)
                ON CONFLICT (user_id) DO UPDATE 
                SET screen_name = EXCLUDED.screen_name
                RETURNING id;
            """
            connection = psycopg2.connect(self.connection_string)
            cursor = connection.cursor()
            values = (user['user_id'], user['screen_name'])

            cursor.execute(update_user_sql, values)

            user_id = cursor.fetchone()[0] 
            connection.commit()
            connection.close()
            return user_id
        
        except psycopg2.Error as e:
            print("psycopg2 Error:", e)