import os

import tweepy
from dotenv import load_dotenv

# Load values from the .env file
load_dotenv()

print(os.getenv("ENV_TEST")) # Check if the .env file is loaded

# Load all the environmental variables into constants
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
# Bearer token is not needed
# BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

authenticator = tweepy.OAuthHandler