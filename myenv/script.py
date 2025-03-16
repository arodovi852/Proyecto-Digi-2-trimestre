import tweepy
import keys

client = tweepy.Client(keys.BEARER_TOKEN, keys.API_KEY, keys.API_KEY_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

def tweet(text: str):
    client.create_tweet(text=text)