#!/usr/bin/env python
# encoding: utf-8

# Original code from:
# https://gist.github.com/brenorb/1ec2afb8d66af850acc294309b9e49ea
# Modified to use APIv2

import os

import tweepy #https://github.com/tweepy/tweepy
import csv

from dotenv import load_dotenv
load_dotenv()

#Twitter API credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")

# Access Token for the developer's app
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# # Access Token for another user
# access_key = os.getenv("USER_ACCESS_TOKEN")
# access_secret = os.getenv("USER_ACCESS_TOKEN_SECRET")

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	client = tweepy.Client(
		bearer_token = BEARER_TOKEN, # REQUIRED
		consumer_key = API_KEY,
		consumer_secret = API_KEY_SECRET,
		access_token = ACCESS_TOKEN,
		access_token_secret = ACCESS_TOKEN_SECRET,
	)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = client.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before {}".format(oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...{} tweets downloaded so far".format(len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('{}_tweets.csv'.format(screen_name), 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
		print('{}_tweets.csv was successfully created.'.format(screen_name))
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("xkaubu")
