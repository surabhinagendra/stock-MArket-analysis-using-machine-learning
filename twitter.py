import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import time
import random

def generate_randomdate():
	datel="02-04-2013"
	dateh="02-04-2018"
	prop=random.random()
	stime = time.mktime(time.strptime(datel, '%d-%m-%Y'))
	etime = time.mktime(time.strptime(dateh, '%d-%m-%Y'))
	ptime = stime + prop * (etime - stime)
	date= time.strftime('%d-%m-%y', time.localtime(ptime))
	
	return date



def get_tweets(cname):
	consumer_key = ''
	consumer_secret = ''

	access_token = ''
	access_token_secret = ''

	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	api = tweepy.API(auth)
	pol=[]
	date=[]
	public_tweets=api.search('stock' or 'market' or 'price' or 'nasdaq' or 'sensex' or 'nifty' or cname)
	for tweet in public_tweets:
		analysis=TextBlob(tweet.text)
		pola=analysis.sentiment.polarity
		pol.append(pola)
		daten=generate_randomdate()
		date.append(daten)
	fdf=pd.DataFrame(np.column_stack([pol]),index=date,columns=['PolT'])		
	return fdf	

	
	


