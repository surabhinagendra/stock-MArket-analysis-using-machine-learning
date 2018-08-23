import pandas as pd 
import numpy as np
import csv
import datetime
import mysql.connector
from datetime import datetime

window_length=14
filename="C:/Users/Surabhi N/Downloads/input data set/"
def calculate_RSI(df):
	close = df['Adj Close']
	delta=close.diff()
	delta=delta[1:]
	up,down=delta.copy(),delta.copy()
	up[up<0] = 0
	down[down>0] = 0
	roll_up2 = pd.Series.rolling(up,window_length).mean()
	roll_down2=pd.Series.rolling(down.abs(),window_length).mean()
	RS2 = roll_up2/roll_down2
	RSI = 100.0-(100.0/(1.0+RS2))
	RSI[0:14] = 0
	return RSI

def calculate_MFI(df, periods=14):
    typical_price = (df.High + df.Low + df.Close) / 3
    raw_money_flow = typical_price * df.Volume

    direction = []
    close_old = 0;

    for index, value in df['Adj Close'].iteritems():
        if(index == 0):
            direction.append(0)
        else:
            direction.append(-1 if value - close_old < 0 else 1)
        close_old = value

    raw_money_flow =  raw_money_flow.to_frame(name='raw_money_flow')
    raw_money_flow['direction'] = direction

    mfi = pd.DataFrame(index=df.index)
    mfi = df['Adj Close']*0
    for i in reversed(range(len(df.index))):
        if i >= 14:
            pos_mf_prd = raw_money_flow[i-periods:i ][raw_money_flow.direction > 0].raw_money_flow.sum()
            neg_mf_prd = raw_money_flow[i-periods:i][raw_money_flow.direction < 0].raw_money_flow.sum()
            mf = 100 - 100/(1 + pos_mf_prd/neg_mf_prd)
        else:
            mf = 0
        mfi.iloc[i] = mf
      
    return mfi

def calculate_so(df):
	low=df['Low']
	high=df['High']
	close=df['Close']
	STOK = ((close - pd.Series.rolling(low, window_length).min()) / (pd.Series.rolling(high, window_length).max() - pd.Series.rolling(low, window_length).min())) * 100
	STOK[0:13]=0
	return STOK

def calculate_ema(values, window):
  
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a
def calculate_macd(ema):
	macd=0.75*ema-0.15*ema
	return macd
def calculate_corr(techind,df):
	mean1 = np.mean(techind)
	openP = df['Open']
	mean2 = np.mean(openP)
	std1 = np.std(techind)
	std2 = np.std(openP)
	covar = ((openP-mean2*(techind-mean1))/(len(openP)-1))
	corr = (covar/(std1*std2))
	return covar,corr

def calculate_ti(filename,d):
	df=pd.read_csv(filename)
	date=[]
	for row in df['Date']:
		try:
			date1=datetime.strptime(row,'%Y-%m-%d')
			date1=datetime.strftime(date1,'%d-%m-%Y')
			date.append(date1)
			df['Date']	=date

		except:
			pass	

		print(df['Date'])
	if ((df['Date'][1] == "2018-03-29") or (df['Date'][1] == "2018-04-01") or (df['Date'][1] == "2018-04-02")or (df['Date'][1] == "29-03-2018") or (df['Date'][1] == "01-04-2018") or (df['Date'][1] == "02-04-2018")):
		df=df.iloc[::-1] 	
	df=df.fillna(9999)	
	df=df.drop_duplicates(keep='first')	
	RSI=calculate_RSI(df)
	df['RSI'] = RSI
	covar,corr=calculate_corr(RSI,df)
	df['covarRSI']=covar
	df['corrRSI']=corr
	mfi=calculate_MFI(df)
	df['MFI'] = mfi
	covar,corr=calculate_corr(mfi,df)
	df['covarMFI']=covar
	df['corrMFI']=corr
	so=calculate_so(df)
	df['SO'] = so
	covar,corr=calculate_corr(so,df)
	df['covarSO']=covar
	df['corrSO']=corr
	Ema=calculate_ema(df['Close'],window_length)
	df['EMA'] = Ema
	covar,corr=calculate_corr(Ema,df)
	df['covarEMA']=covar
	df['corrEMA']=corr
	macd=calculate_macd(Ema)
	df['MACD']=macd
	covar,corr=calculate_corr(macd,df)
	df['covarMACD']=covar
	df['corrMACD']=corr
	df.to_csv(filename)


 

