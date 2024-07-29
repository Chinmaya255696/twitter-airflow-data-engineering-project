from ntscraper import Nitter
import pandas as pd
from datetime import datetime
import s3fs 


def run_twitter_etl():
    # Initialize the scraper
    scraper = Nitter(log_level=1, skip_instance_check=False)

    # Fetch tweets
    tweets = scraper.get_tweets("elonmusk", mode="user", number=60)

    # Print the fetched tweets (for debugging purposes)
    print(tweets)

    # Create an empty list to store refined tweets
    tweet_list = []

    for tweet in tweets['tweets']:
            # Access tweet attributes directly
            refined_tweet = {
                "user": tweet['user']['username'],
                "text": tweet['text'],
                "favorite_count": tweet['stats']['likes'],
                "retweet_count": tweet['stats']['retweets'],
                'created_at': tweet['date']
            }
            tweet_list.append(refined_tweet)

    # Convert list of refined tweets to a DataFrame
    df = pd.DataFrame(tweet_list)

    # Save DataFrame to CSV
    df.to_csv("s3://chinmya-airflow-bucket/elonmusk_tweet_data.csv", index=False)
