import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

# Load all the environmental variables into constants
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

input("Do you really want to authenticate?")

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=CLIENT_ID,
    redirect_uri="https://127.0.0.1",
    scope=[
        "tweet.read",
        "tweet.write",
        "users.read",
        "follows.read",
        "follows.write",
        # Stay connected to the account
        # until access is revoked
        "offline.access",
    ],
    # Client Secret is only necessary if using a confidential client
    client_secret=CLIENT_SECRET
)

auth_url = oauth2_user_handler.get_authorization_url()

print(f"Auth url:\n{auth_url}")

input("""You'll be redirected to a page.
There, you'll get redirected to a URL.
Press enter when you have that URL.""")

auth_response_url = input("URL: ")

access_token = oauth2_user_handler.fetch_token(auth_response_url)

print(f"Access token: {access_token}")

