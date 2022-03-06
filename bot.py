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

# client = tweepy.Client(BEARER_TOKEN)
# client = tweepy.Client(access_token=USER_ACCESS_TOKEN, wait_on_rate_limit=True)
client = tweepy.Client(
    access_token=USER_ACCESS_TOKEN,
    access_token_secret=USER_ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)
client.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"

kaubu = client.get_user(username="kaubu")
print(f"kaubu = {kaubu}:")
pprint(kaubu)
print(f"kaubu.data = {kaubu.data}:")
pprint(kaubu.data)
print(f"kaubu.data type = {type(kaubu.data)}")
print(f"kaubu.data.id = {kaubu.data.id}")
client.follow_user(kaubu.data.id)