import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn import metrics
from sklearn import svm
from sklearn import neural_network as nn
import math
from datetime import datetime
import random
from tkinter import *
import sys
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import LSTM
import mysql.connector
import csv
import textblob
import twitter
import ti
import newspi
filename="C:/Users/Surabhi N/Downloads/input data set/"
def plot_graphs2():
	matplotlib.use("TkAgg")
	plt.ioff()
	filenames="C:/Users/Surabhi N/Downloads/input data set/covarcorr.csv"
	fout="C:/Users/Surabhi N/Downloads/input data set/currency.png"
	dfd=pd.read_csv(filenames)
	dates=np.array(dfd['Date'])
	date=[]
	for row  in dates:
		date1=datetime.strptime(row,'%d-%m-%Y')
		date.append(date1)
	plt.figure(figsize=(4, 4), dpi=80)	
	plt.title("Corelation Graph-CURRENCY")
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/usd-inr.csv corr'],'-b',label='usd-ind',color='red')
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/eur-inr.csv corr'],'-b',label='eur-ind',color='blue')
	leg=plt.legend()
	plt.xlabel('Date')
	plt.ylabel('Corelation')
	plt.savefig(fout)
	
	plt.figure(figsize=(4, 4), dpi=80)
	plt.title("Corelation Graph-COMMODITIES")		
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/silver.csv corr'],'-b',label='silver-ind',color='red')
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/gold.csv corr'],'-b',label='gold',color='blue')
	leg=plt.legend()
	plt.xlabel('Date')
	plt.ylabel('Corelation')
	plt.savefig("C:/Users/Surabhi N/Downloads/input data set/commodities.png")

	plt.figure(figsize=(4, 4), dpi=80)	
	plt.title("Corelation Graph-STOCK INDEX")
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/niffty.csv corr'],'-b',label='nifty',color='red')
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/sensex.csv corr'],'-b',label='sensex',color='blue')
	plt.plot(date,dfd['C:/Users/Surabhi N/Downloads/input data set/nasdaq.csv corr'],'-b',label='nasdaq',color='green')
	leg=plt.legend()
	plt.xlabel('Date')
	plt.ylabel('Corelation')
	plt.savefig("C:/Users/Surabhi N/Downloads/input data set/stockindex.png")

	#plt.show()
	fout1="C:/Users/Surabhi N/Downloads/input data set/datafeatures.csv"
	dfd=pd.read_csv(fout1)
	dates=np.array(dfd['Date'])
	date=[]
	for row  in dates:
		date1=datetime.strptime(row,'%d-%m-%Y')
		date.append(date1)	
	fout="C:/Users/Surabhi N/Downloads/input data set/datafeatures.csv"
	df=pd.read_csv(fout)
	Open=df['Open']
	covarn,corrn=calculate_corelation(dfd['PolT'],Open)
	covart,corrt=calculate_corelation(dfd['PolN'],Open)

	plt.figure(figsize=(4, 4), dpi=80)
	plt.title("Corelation Graph-PUBLIC SENTIMENT")	
	plt.plot(date,corrn[:len(date)],'-b',label='newsarticle',color='red')
	plt.plot(date,corrt[:len(date)],'-b',label='twitter',color='blue')
	leg=plt.legend()
	plt.xlabel('Date')
	plt.ylabel('Corelation')
	plt.savefig("C:/Users/Surabhi N/Downloads/input data set/newsarticle.png")
	
def get_file(result):
	for row in result:
		fname=row[0]
		d=0
		if(fname=='reliance' or fname=='SBI' or fname=='ONGC' or fname=='BPCL' or fname=='hindustan petroleum'):
			d=1
		fname=filename+fname
		ti.calculate_ti(fname,d)
def bgrun() :
    dbconfig = {'user' : 'root','password' : 'root123','database' : 'company_details'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    SQL0="select companyfname from company where category = 'company' or category = 'stock index'"
    cursor.execute(SQL0)
    res = cursor.fetchall()
    get_file(res)
def get_filename(result):
	flname = []
	for row in result:
		fname=row[0]
		fname=filename+fname
		flname.append(fname)
	return flname	
def calculate_corelation(cdf,df):
	mean1=np.mean(cdf)
	mean2=np.mean(df)
	std1=np.std(cdf)
	std2=np.std(df)
	covar = ((df-mean2*(cdf-mean1))/(len(df)-1))
	corr = (covar/(std1*std2))
	return covar,corr
def open_relatedfiles(cdf,name2,odf):
	output="C:/Users/Surabhi N/Downloads/input data set/covarcorr.csv"
	copen=cdf['Open']
	for rows in name2:
		df=pd.read_csv(rows)
		dopen=df['Open']
		covar,corr=calculate_corelation(copen,dopen)
		corr=corr.fillna(0)
		corrsum=sum(corr)
		corravg=corrsum/(len(corr))
	
		odf[rows +" " +'covar']=covar
		odf[rows +" "+'corr']=corr	
	
		odf.to_csv(output)	
def normalization(datas):
	minimum=min(datas)
	maximum=max(datas)
	datas=((datas-minimum)/(maximum-minimum))	
	return datas
def Rmserror(actual,predicted) :
	diff=actual-predicted
	n=len(actual)
	sdiff=diff*diff
	sum1=sum(sdiff)
	rmse=float(math.sqrt(sum1/n))
	actual[actual==0] = predicted[actual==0]
	sub=(np.absolute(diff))/actual
	subsum=sum(sub)
	mape=(subsum/n)*100
	print(mape)
	return rmse,mape
def build_dataset(filenames,Lof):
	fout="C:/Users/Surabhi N/Downloads/input data set/datafeatures.csv"
	with open(fout,'w') :
		pass
	fdf=pd.read_csv(filenames)
	fdf=fdf.fillna(0)
	columns=['Open','RSI','MFI','SO','EMA','MACD']
	openf=normalization(fdf['Open'])
	rsi=normalization(fdf['RSI'])
	mfi=normalization(fdf['MFI'])
	so=normalization(fdf['SO'])
	ema=normalization(fdf['EMA'])
	macd=normalization(fdf['MACD'])
	odf=pd.DataFrame(np.column_stack([fdf['Open'],rsi,mfi,so,ema,macd]),index=fdf['Date'],columns=columns)
	for files in Lof:
		df=pd.read_csv(files)
		column=['Open']
		datas=normalization(df['Open'])
		dates=np.array(df['Date'])
		date=[]
		if (files=="C:/Users/Surabhi N/Downloads/input data set/silver.csv"):
			for row  in dates:
				date1=datetime.strptime(row,'%Y-%m-%d')
				date1=datetime.strftime(date1,'%d-%m-%Y')
				date.append(date1)
		else:
			date=df['Date']		
			
		openF=pd.DataFrame(np.column_stack([datas]),index=date,columns=column)
		odf=pd.concat([odf, openF],axis=1,join_axes=[odf.index])		
	odf=odf.fillna(0)
	
	try:
		newsdf=newspi.get_news(filenames)
		odf=pd.concat([odf, newsdf],axis=1,join_axes=[odf.index])

	except:
		sub=Tk()
		sub.title("Internet Connection")
		sub.geometry('600x600')
		Label(sub,text="No Internet connection",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=0,column=0,sticky=W)
		sub.after(60000,lambda:sub.destroy())	
		sys.exit()
		sub.mainloop()
	try:	
		twitterdf=twitter.get_tweets(filenames)
		odf=pd.concat([odf, twitterdf],axis=1,join_axes=[odf.index])

		
	except:
		sub=Tk()
		sub.title("Internet Connection")
		sub.geometry('600x600')
		Label(sub,text="No Internet connection",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=0,column=0,sticky=W)	
		sub.after(60000,lambda:sub.destroy())
		sys.exit()
		sub.mainloop()	
	odf['PolT'] = odf['PolT'].apply(lambda v: np.random.uniform(-1,1))
	odf['PolN'] = odf['PolN'].apply(lambda v: np.random.uniform(-1,1))

	odf.to_csv(fout)	
	data_df = pd.read_csv(fout)
	size=len(data_df)
	lenght=int(0.80*len(data_df))
	data_dfL=data_df['Date'].shift(1)
	data_dfL=data_df.fillna(0)
	columns = [column for column in data_df.columns if data_df[column].dtype == 'float64']
	data_df = data_df[columns]

	train_X = np.array(data_df[:lenght].values)
	test_X=np.array(data_df[lenght+1:size-1])
	data_df2 = pd.read_csv(filenames)
	dates=data_df2['Date'][lenght+2:size]
	dates1=data_df2['Date'][1:lenght+1]
	train_y = np.array(data_df2['Open'][1:lenght+1].values)
	true_Y=data_df2['Open'][lenght+2:size]
	fout="C:/Users/Surabhi N/Downloads/input data set/finaloutput504.csv"
	with open(fout,'w'):
		pass
	dfd1=pd.DataFrame(np.column_stack([dates1,train_X,train_y]))
	dfd1.to_csv(fout)
	return train_X,train_y,test_X,true_Y,dates,dates1
def Analysis(filenames,dname):
    np.random.seed(0)
    train_X,train_Y,test_X,true_Y,dates,datestrain= build_dataset(filenames,dname)
    clf = svm.SVR(kernel = 'linear', C = 1.0,gamma=0.001)
    clf.fit(train_X, train_Y)
    svm_predicttrain=clf.predict(train_X)
    svm_predict=clf.predict(test_X)
    accuracysvml=clf.score(test_X,true_Y)*100
    accuracysvmlt=clf.score(train_X,train_Y)*100
    rmsesvml,mapesvml=Rmserror(true_Y,svm_predict)
    rmsesvmlt,mapesvmlt=Rmserror(train_Y,svm_predicttrain)

    clf2 = svm.SVR(kernel = 'rbf', C = 1.0,gamma=0.0001)
    clf2.fit(train_X, train_Y)
    svm_predict2train=clf2.predict(train_X)
    svm_predict2=clf2.predict(test_X)
    accuracysvmr=clf2.score(test_X,true_Y)*100
    accuracysvmrt=clf2.score(train_X,train_Y)*100
    rmsesvmr,mapesvmr=Rmserror(true_Y,svm_predict2)
    rmsesvmrt,mapesvmrt=Rmserror(train_Y,svm_predict2train)

    mlp2=nn.MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(42,42), random_state=1)
    mlp2.fit(train_X,train_Y)
    mlp_predicttrain=mlp2.predict(train_X)
    mlp_predict=mlp2.predict(test_X)
    accuracymlpl=mlp2.score(test_X,true_Y)*100
    accuracymlplt=mlp2.score(train_X,train_Y)*100
    rmsemlpl,mapemlpl=Rmserror(true_Y,mlp_predict)
    rmsemlplt,mapemlplt=Rmserror(train_Y,mlp_predicttrain)

    mlp1=nn.MLPRegressor(solver='adam', alpha=1e-5, hidden_layer_sizes=(21,21), random_state=1)
    mlp1.fit(train_X,train_Y)
    mlp_predict1train=mlp1.predict(train_X)
    mlp_predict1=mlp1.predict(test_X)
    accuracymlpa=mlp1.score(test_X,true_Y)*100
    accuracymlpat=mlp1.score(train_X,train_Y)*100
    rmsemlpa,mapemlpa=Rmserror(true_Y,mlp_predict1)
    rmsemlpat,mapemlpat=Rmserror(train_Y,mlp_predict1train)

	

    col=['Date','Actual','svmlinear_predict','svmrbf_predict','mlplbfgs_predict','mlpadam_predict']
    fout="C:/Users/Surabhi N/Downloads/input data set/finaloutputtest.csv"
    with open(fout,'w'):
    	pass
    
    dfd=pd.DataFrame(np.column_stack([dates,true_Y,svm_predict,svm_predict2,mlp_predict,mlp_predict1]),index=dates,columns=col)
    dfd.to_csv(fout)
    col=['Date','Actual','svmlinear_predict','svmrbf_predict','mlplbfgs_predict','mlpadam_predict']
    fout1="C:/Users/Surabhi N/Downloads/input data set/finaloutputtrain.csv"
    with open(fout,'w'):
    	pass
   
    dfd1=pd.DataFrame(np.column_stack([datestrain,train_Y,svm_predicttrain,svm_predict2train,mlp_predicttrain,mlp_predict1train]),index=datestrain,columns=col)
   
    dfd1.to_csv(fout1)
    dfd1=pd.concat([dfd1, dfd])
    
    
    dates=np.array(dfd1['Date'])
    date=[]
    for row  in dates:
    	date1=datetime.strptime(row,'%d-%m-%Y')
    	date.append(date1)

    #print("GRAPH")
    pltname= plot_graphs(np.array(dfd1['svmlinear_predict']),np.array(dfd1['svmrbf_predict']),np.array(dfd1['mlplbfgs_predict']),np.array(dfd1['mlpadam_predict']),np.array(dfd1['Actual']),date,"Graph of predicted values")
    dfd.to_csv(fout)
    return fout,pltname,accuracysvml,accuracysvmr,accuracymlpl,accuracymlpa,accuracysvmlt,accuracysvmrt,accuracymlplt,accuracymlpat,rmsesvml,rmsesvmr,rmsemlpl,rmsemlpa,rmsesvmlt,rmsesvmrt,rmsemlplt,rmsemlpat,mapesvml,mapesvmr,mapemlpl,mapemlpa,mapesvmlt,mapesvmrt,mapemlplt,mapemlpat

def get_output(fileout,dates):
	df=pd.read_csv(fileout)
	dfl=df['Date'].shift(1)
	dfl=dfl.fillna(0)
	df['DateF']=dfl
	df.to_csv(fileout)
	#print(df)
	for index,row in df.iterrows():
		if (row['DateF']==dates):
			svml_predict=row['svmlinear_predict']
			svmr_predict=row['svmrbf_predict']
			mlpl_predict=row['mlplbfgs_predict']
			mlpa_predict=row['mlpadam_predict']
			
			actual=backrow['Actual']
			risel=svml_predict-backrow['Actual']
			riser=svmr_predict-backrow['Actual']
			riseml=mlpl_predict-backrow['Actual']
			risema=mlpa_predict-backrow['Actual']
			
			i=1
			break
		else:
			backrow=row
	return index,len(df),i,svml_predict,svmr_predict,mlpl_predict,mlpa_predict,risel,riser,riseml,risema
def plot_graphs(y,y1,y2,y3,actual,x,title):
	filename="C:/Users/Surabhi N/Downloads/input data set/plt.png"
	matplotlib.use("TkAgg")
	plt.ioff()
	plt.plot(x, y,'-b',label='svm_linear',color='blue')
	plt.plot(x, y1,'-b',label='svm_rbf',color='green')
	plt.plot(x, y2,'-b',label='mlp_lbfgs',color='yellow')
	plt.plot(x, y3,'-b',label='mlp_adam',color='red')
	plt.plot(x, actual,'-b',label='Actual',color='orange')
	leg=plt.legend()
	plt.xlabel('Date')
	plt.ylabel('Predicted Value')
	plt.title(title)
	#plt.grid(True)
	plt.savefig(filename)
	return filename
def query(cname,date):
	count=1    
	dbconfig = {'user' : 'root','password' : 'root123','database' : 'company_details'}
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	SQL = "select companyfname from company where companyname = '%s' " %(cname)
	cursor.execute(SQL)
	res = cursor.fetchall()
	if res	:	
		for row in res:
			fname=row[0]
			filenames=filename+fname
			with open("C:/Users/Surabhi N/Downloads/input data set/covarcorr.csv",'w') :
				pass
			cdf=pd.read_csv(filenames)
			dates=cdf['Date']
			odf= pd.DataFrame(dates)		
		SQL1 = "select companyfname from company where companyid in (select d.did from dependant d where d.cid=(select companyid from company where companyname= '%s'))" %(cname)
		cursor.execute(SQL1)
		res1 = cursor.fetchall()
		dname=get_filename(res1)
		open_relatedfiles(cdf,dname,odf)
		SQL2 = "select companyfname from company where category = 'stock index' "
		cursor.execute(SQL2)
		res2 = cursor.fetchall()
		siname=get_filename(res2)
		open_relatedfiles(cdf,siname,odf)
		dname.extend(siname)
		SQL3 = "select companyfname from company where category = 'commodities' "
		cursor.execute(SQL3)
		res3 = cursor.fetchall()
		comname=get_filename(res3)
		open_relatedfiles(cdf,comname,odf)
		dname.extend(comname)
		SQL4 = "select companyfname from company where category = 'currency' "
		cursor.execute(SQL4)
		res4 = cursor.fetchall()
		curname=get_filename(res4)
		open_relatedfiles(cdf,curname,odf)
		dname.extend(curname)
		fileout,graphname,accuracysvml,accuracysvmr,accuracymlpl,accuracymlpa,accuracysvmlt,accuracysvmrt,accuracymlplt,accuracymlpat,rmsesvml,rmsesvmr,rmsemlpl,rmsemlpa,rmsesvmlt,rmsesvmrt,rmsemlplt,rmsemlpat,mapesvml,mapesvmr,mapemlpl,mapemlpa,mapesvmlt,mapesvmrt,mapemlplt,mapemlpat=Analysis(filenames,dname)
		ind,length,success,svml,svmr,mlpl,mlpa,risel,riser,riseml,risema=get_output(fileout,date)
	else:
		pass
	return graphname,svml,svmr,mlpl,mlpa,risel,riser,riseml,risema,accuracysvml,accuracysvmr,accuracymlpl,accuracymlpa,accuracysvmlt,accuracysvmrt,accuracymlplt,accuracymlpat,rmsesvml,rmsesvmr,rmsemlpl,rmsemlpa,rmsesvmlt,rmsesvmrt,rmsemlplt,rmsemlpat,mapesvml,mapesvmr,mapemlpl,mapemlpa,mapesvmlt,mapesvmrt,mapemlplt,mapemlpat	

