import os
import logging
from pprint import pprint

import tweepy
from dotenv import load_dotenv

# Start logging
logger = logging.getLogger("Tweepy")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="tweepy.log")
logger.addHandler(handler)

# Load values from the .env file
load_dotenv()

print(os.getenv("ENV_TEST")) # Check if the .env file is loaded

# Load all the environmental variables into constants
# API_KEY is the same as CONSUMER KEY
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

USER_ACCESS_TOKEN = os.getenv("USER_ACCESS_TOKEN")
USER_ACCESS_TOKEN_SECRET = os.getenv("USER_ACCESS_TOKEN_SECRET")

# To make sure I don't start the program erroneously
input("Press ENTER to start program...")

client = tweepy.Client(
    bearer_token = BEARER_TOKEN, # REQUIRED
    consumer_key = API_KEY,
    consumer_secret = API_KEY_SECRET,
    access_token = USER_ACCESS_TOKEN,
    access_token_secret = USER_ACCESS_TOKEN_SECRET,
)

