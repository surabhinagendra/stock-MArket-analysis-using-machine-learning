from newsapi import NewsApiClient
from textblob import TextBlob
import pandas as pd
from datetime import datetime
import numpy as np

def get_news(cname):
	api_key = '9d450ce252524cdbaefed3691053ab78'
	newsapi = NewsApiClient(api_key)
	all_articles = newsapi.get_everything(q=cname or 'stock' or 'market' or'sensex' or 'nifty' or 'nasdaq'  or 'prices',sources=['the-times-of-india','google-news-in','the-hindu','cnbc'], from_parameter='2013-04-02',to='2018-04',language='en',sort_by='relevancy')
	articles1=all_articles['articles']
	date=[]
	pol=[]
	i=0
	for key ,value in  all_articles.items():
		if type(value) is list :
			for x in value:
				if type(x) is dict:
					for k,v in x.items():
						if k == 'description':
							analysis=TextBlob(v)
							pola=analysis.sentiment.polarity
							pol.append(pola)
						if k == "publishedAt"	:
							date1=v.encode('utf-8')
							date.append(date1)
	df=pd.DataFrame(np.column_stack([date, pol]),columns=['Date','PolN'])
	date=[]
	for row in df['Date']:
		dates=row.decode("utf-8") 
		dates=dates.split('T')
		date1=datetime.strptime(dates[0],'%Y-%m-%d')
		date1=datetime.strftime(date1,'%d-%m-%Y')
		date.append(date1)
	fdf=pd.DataFrame(np.column_stack([pol]),index=date,columns=['PolN'])				
	return fdf



