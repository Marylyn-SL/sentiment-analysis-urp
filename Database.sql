-- docker run -d --name booking-postgres -e POSTGRES_DB=fypdb -e POSTGRES_USER=fypuser -e POSTGRES_PASSWORD=fyppass -v fyp_pgdata:/var/lib/postgresql/data -p 5432:5432 postgres


CREATE TABLE IF NOT EXISTS Users (
    ID SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL UNIQUE,
    name VARCHAR(100),
    screen_name VARCHAR(100),
    location VARCHAR(300),
    description TEXT,
    URL VARCHAR(400),
    followers_count INT,
    friends_count INT,
    user_created_at TIMESTAMP,
    verified BOOLEAN,
    statuses_count INT,
    profile_image_url VARCHAR(400),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Place (
    ID SERIAL PRIMARY KEY,
    external_id VARCHAR(100) NOT NULL,
    name VARCHAR(100),
    full_name VARCHAR(400),
    place_type VARCHAR(300),
    URL VARCHAR(400),
    country VARCHAR(100),
    country_code VARCHAR(10),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Posts (
    ID SERIAL PRIMARY KEY,
    tweet_id BIGINT NOT NULL UNIQUE,
    text TEXT,
    text_in_english TEXT,
    created_at TIMESTAMP,
    source VARCHAR(300),
    favorite_count INT,
    retweet_count INT,
    lang VARCHAR(5),
    sentiment_polarity FLOAT,
    place VARCHAR(300),
    place_id VARCHAR(300),
    query VARCHAR(100),
    fk_user_id INT REFERENCES Users(ID),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    longitude FLOAT,
    latitude FLOAT,
    relevance FLOAT
);
