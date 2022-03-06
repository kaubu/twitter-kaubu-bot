import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("ENV_TEST")) # Check if the .env file is loaded