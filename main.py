import numpy as np
import pandas as pd
import matplotlib
import textblob
import os
import csv
import textblob
import tweepy


dates = []
prices = []





def get_data(filename):
	with open(filename,'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			try:
				prices.append(float(row[1]))
		 	except ValueError:
		 		next(csvFileReader)


return



get_data("C:/Users/Surabhi N/Downloads/input data set/wipro.csv")





