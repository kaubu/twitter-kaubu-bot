import os

import tweepy
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")

oauth1_user_handler = tweepy.OAuth1UserHandler(
    API_KEY, # Consumer Key
    API_KEY_SECRET, # Consumer Secret
    callback="https://127.0.0.1",
)

input("Press [Enter] to begin auth process")

print("""You'll get a link, visit it, authenticate with twitter.
After that, you'll get redirected to a bogus URL.
In that URL it should be displayed like:
https://127.0.0.1/?oauth_token=<TOKEN>&oauth_verifier=<VERIFIER>
Take note of that Verifier.
Visit this link below:
""")

print(oauth1_user_handler.get_authorization_url(signin_with_twitter=True))

print()

oauth_verifier = input("Enter your verifier: ")

access_token, access_token_secret = oauth1_user_handler.get_access_token(
    oauth_verifier
)

print(f"Access Token:\n{access_token}\n")
print(f"Access Token Secret:\n{access_token_secret}\n")

