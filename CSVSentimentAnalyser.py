import pandas as pd
import requests

# Load CSV file
csv_file_path = 'clean_tweets.csv'
output_csv_file_path = 'meaning_cloud_sentiment_analysis.csv'

# MeaningCloud API
api_key = '634d07b312413741f2248f7808b2605a'
url = "https://api.meaningcloud.com/sentiment-2.1"

def analyze_sentiment(text):
    """Function to analyze sentiment of a given text using MeaningCloud."""
    payload = {
        'key': api_key,
        'txt': text,
        'lang': 'en',
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        sentiment_result = response.json()
        # Extracting the score_tag
        return sentiment_result.get('score_tag', '')
    else:
        print(f"Error: {response.text}")
        return "Error"

df = pd.read_csv(csv_file_path)
df['MeaningCloud_Sentiment'] = df['Tweet'].apply(analyze_sentiment)
df.to_csv(output_csv_file_path, index=False)

print("Sentiment analysis complete. Results saved to:", output_csv_file_path)