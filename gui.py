from tkinter import *
import tkinter as tk
from PIL import ImageTk, ImageTk,Image
#import os
import sys
import project
import mysql.connector
import time
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
filename="C:/Users/Surabhi N/Downloads/input data set/"
gname="C:/Users/Surabhi N/Downloads/input data set/test.png" 
global textentry

#v.set(1)
import random
languages = [
    ("Wipro"),
    ("Infosys"),
    ("Reliance"),
    ("Reliance communications"),
    ("Tata Motors"),
    ("Mahindra & Mahindra"),
    ("Rolta"),
    ("ICICI"),
    ("SBI"),
    ("ONGC"),
    ("BPCL"),
    ("Hindustan Petroleum"),
    ("SENSEX"),
    ("NIFTY"),
    ("NASDAQ")

]


def quit(name):
	name.self.destroy()

def again():
	start()
def exit():
	sys.exit()
def graphs():
	project.plot_graphs2()
	sub=Toplevel()
	sub.title("CORELATION GRAPHS")	
	sub.geometry("3600x3600")
	sub.configure(background="#99FFFF")
	iframe7=Frame(sub,width=800,height=700,bg="#003366", bd=2, relief=SUNKEN)
	iframe0=Frame(iframe7,width=800,height=350,bg="#003366", bd=2, relief=SUNKEN)
	iframe1=Frame(iframe0,width=600,height=350,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe1,text="Corelation with respect to currency").pack()
	photo1=PhotoImage(file="C:/Users/Surabhi N/Downloads/input data set/currency.png")
	Label(iframe1,image=photo1,height=350,width=400,bg="#003366").pack()
	iframe1.pack(side=LEFT,anchor=E)
	iframe2=Frame(iframe0,width=600,height=350,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe2,text="Corelation with respect to commodities").pack()
	photo2=PhotoImage(file="C:/Users/Surabhi N/Downloads/input data set/commodities.png")
	Label(iframe2,image=photo2,height=350,width=400,bg="#003366").pack()
	iframe2.pack(side=LEFT,anchor=E)
	iframe0.pack(side=TOP,anchor=NW)
	iframe5=Frame(iframe7,width=800,height=350,bg="#99FFFF", bd=2, relief=SUNKEN)
	iframe3=Frame(iframe5,width=600,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe3,text="Corelation with respect to stock index").pack()
	photo3=PhotoImage(file="C:/Users/Surabhi N/Downloads/input data set/stockindex.png")
	Label(iframe3,image=photo3,height=350,width=400,bg="#003366").pack()
	iframe3.pack(side=LEFT,anchor=E)
	iframe4=Frame(iframe5,width=600,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe4,text="Corelation with respect to Public Sentiment").pack()
	photo4=PhotoImage(file="C:/Users/Surabhi N/Downloads/input data set/newsarticle.png")
	Label(iframe4,image=photo4,height=350,width=400,bg="#003366").pack()
	iframe4.pack(side=LEFT,anchor=E)
	iframe5.pack(side=TOP,anchor=NW)
	iframe7.pack(side=LEFT,anchor=NW)
	iframe6=Frame(sub,width=50,height=20,bg="#99FFFF", bd=2, relief=SUNKEN)
	Button(iframe6,text="CONTINUE",bg="#003366",fg="#99FFFF",width=20,command=start).pack(side=LEFT,anchor=N)
	Button(iframe6,text="EXIT",bg="#003366",fg="#99FFFF",width=20,command=exit).pack(side=LEFT,anchor=N)
	iframe6.pack(side =LEFT,anchor=CENTER)
	sub.after(120000,lambda:sub.destroy())
	sub.mainloop()
	
	
	
def Enter(accuracysvml,accuracysvmr,accuracymlpl,accuracymlpa,accuracysvmlt,accuracysvmrt,accuracymlplt,accuracymlpat,rmsesvml,rmsesvmr,rmsemlpl,rmsemlpa,rmsesvmlt,rmsesvmrt,rmsemlplt,rmsemlpat,mapesvml,mapesvmr,mapemlpl,mapemlpa,mapesvmlt,mapesvmrt,mapemlplt,mapemlpat):
	sub=Tk()
	sub.title("Performance Eva")
	sub.geometry('800x1200')
	sub.configure(background="#99FFFF")
	iframe0 = Frame(sub,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe0,text="PERFORMANCE EVALUATION",bg="#99FFFF",fg="#003366",font="Verdana 18 bold").grid(row=0,column=0,sticky=W)
	iframe1 = Frame(iframe0,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe1,text="TESTING DATA SET",bg="#003366",fg="#99FFFF",font="Verdana 18 bold").grid(row=0,column=0,sticky=W)
	Label(iframe1,text="Accuracy are:",bg="#003366",fg="#99FFFF",font="Verdana 14 bold").grid(row=1,column=0,sticky=W)
	iframe2 = Frame(iframe1,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe2,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=1,sticky=W)
	Label(iframe2,text="SVM RBF",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=2,sticky=W)
	Label(iframe2,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="none 14").grid(row=0,column=3,sticky=W)
	Label(iframe2,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="none 12 ").grid(row=0,column=4,sticky=W)
	output1 = Text(iframe2,width=20,height=2,fg="#003366",bg="#99FFFF")
	output1.grid(row=1,column=1,sticky=W)
	output2 = Text(iframe2,width=20,height=2,fg="#003366",bg="#99FFFF")
	output2.grid(row=1,column=2,sticky=W)
	output3 = Text(iframe2,width=20,height=2,fg="#003366",bg="#99FFFF")
	output3.grid(row=1,column=3,sticky=W)
	output4 = Text(iframe2,width=20,height=2,fg="#003366",bg="#99FFFF")
	output4.grid(row=1,column=4,sticky=W)
	iframe2.grid(row=3,column=0,sticky=W)
	iframe3= Frame(iframe1,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe1,text="Root Mean Square ERROR:",bg="#003366",fg="#99FFFF",font="Verdana 14 bold").grid(row=4,column=0,sticky=W)
	Label(iframe3,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=1,sticky=W)
	Label(iframe3,text="SVM RBF",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=2,sticky=W)
	Label(iframe3,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=3,sticky=W)
	Label(iframe3,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="none 12 ").grid(row=0,column=4,sticky=W)
	output5 = Text(iframe3,width=20,height=1,fg="#003366",bg="#99FFFF")
	output5.grid(row=1,column=1,sticky=W)
	output6 = Text(iframe3,width=20,height=1,fg="#003366",bg="#99FFFF")
	output6.grid(row=1,column=2,sticky=W)
	output7 = Text(iframe3,width=20,height=1,fg="#003366",bg="#99FFFF")
	output7.grid(row=1,column=3,sticky=W)
	output8 = Text(iframe3,width=20,height=1,fg="#003366",bg="#99FFFF")
	output8.grid(row=1,column=4,sticky=W)
	iframe3.grid(row=5,column=0,sticky=W)
	iframe4= Frame(iframe1,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe1,text="Mean Absolute Percentage Error:",bg="#003366",fg="#99FFFF",font="Verdana 14 bold").grid(row=6,column=0,sticky=W)
	Label(iframe4,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=1,sticky=W)
	Label(iframe4,text="SVM RBF",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=2,sticky=W)
	Label(iframe4,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=3,sticky=W)
	Label(iframe4,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="none 12 ").grid(row=0,column=4,sticky=W)
	output9 = Text(iframe4,width=20,height=1,fg="#003366",bg="#99FFFF")
	output9.grid(row=1,column=1,sticky=W)
	output10 = Text(iframe4,width=20,height=1,fg="#003366",bg="#99FFFF")
	output10.grid(row=1,column=2,sticky=W)
	output11 = Text(iframe4,width=20,height=1,fg="#003366",bg="#99FFFF")
	output11.grid(row=1,column=3,sticky=W)
	output12 = Text(iframe4,width=20,height=1,fg="#003366",bg="#99FFFF")
	output12.grid(row=1,column=4,sticky=W)
	iframe4.grid(row=7,column=0,sticky=W)

	Label(iframe1,text="TRAINING DATA SET",bg="#003366",fg="#99FFFF",font="Verdana 18 bold").grid(row=8,column=0,sticky=W)
	Label(iframe1,text="Accuracy are:",bg="#003366",fg="#99FFFF",font="Verdana 14 bold").grid(row=9,column=0,sticky=W)
	iframe5=Frame(iframe1,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe5,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=1,sticky=W)
	Label(iframe5,text="SVM RBF",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=2,sticky=W)
	Label(iframe5,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=3,sticky=W)
	Label(iframe5,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="none 12 ").grid(row=0,column=4,sticky=W)
	output13 = Text(iframe5,width=20,height=2,fg="#003366",bg="#99FFFF")
	output13.grid(row=1,column=1,sticky=W)
	output14 = Text(iframe5,width=20,height=2,fg="#003366",bg="#99FFFF")
	output14.grid(row=1,column=2,sticky=W)
	output15 = Text(iframe5,width=20,height=2,fg="#003366",bg="#99FFFF")
	output15.grid(row=1,column=3,sticky=W)
	output16 = Text(iframe5,width=20,height=2,fg="#003366",bg="#99FFFF")
	output16.grid(row=1,column=4,sticky=W)
	iframe5.grid(row=10,column=0,sticky=W)
	iframe6=Frame(iframe1,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe1,text="Root Mean Square ERROR:",bg="#003366",fg="#99FFFF",font="Verdana 14 bold").grid(row=11,column=0,sticky=W)
	Label(iframe6,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=1,sticky=W)
	Label(iframe6,text="SVM RBF",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=2,sticky=W)
	Label(iframe6,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=3,sticky=W)
	Label(iframe6,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="none 12 ").grid(row=0,column=4,sticky=W)
	output17 = Text(iframe6,width=20,height=1,fg="#003366",bg="#99FFFF")
	output17.grid(row=1,column=1,sticky=W)
	output18 = Text(iframe6,width=20,height=1,fg="#003366",bg="#99FFFF")
	output18.grid(row=1,column=2,sticky=W)
	output19 = Text(iframe6,width=20,height=1,fg="#003366",bg="#99FFFF")
	output19.grid(row=1,column=3,sticky=W)
	output20= Text(iframe6,width=20,height=1,fg="#003366",bg="#99FFFF")
	output20.grid(row=1,column=4,sticky=W)
	iframe6.grid(row=12,column=0,sticky=W)
	iframe7=Frame(iframe1,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Label(iframe1,text="Mean Absolute Percentage Error:",bg="#003366",fg="#99FFFF",font="Verdana 14 bold").grid(row=13,column=0,sticky=W)
	Label(iframe7,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=1,sticky=W)
	Label(iframe7,text="SVM RBF",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=2,sticky=W)
	Label(iframe7,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="none 12").grid(row=0,column=3,sticky=W)
	Label(iframe7,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="none 12 ").grid(row=0,column=4,sticky=W)
	output21 = Text(iframe7,width=20,height=1,fg="#003366",bg="#99FFFF")
	output21.grid(row=1,column=1,sticky=W)
	output22 = Text(iframe7,width=20,height=1,fg="#003366",bg="#99FFFF")
	output22.grid(row=1,column=2,sticky=W)
	output23 = Text(iframe7,width=20,height=1,fg="#003366",bg="#99FFFF")
	output23.grid(row=1,column=3,sticky=W)
	output24 = Text(iframe7,width=20,height=1,fg="#003366",bg="#99FFFF")
	output24.grid(row=1,column=4,sticky=W)
	iframe7.grid(row=14,column=0,sticky=W)
	iframe1.grid(row=1,column=0,sticky=W)
	iframe0.grid(row=0,column=0,sticky=W)
	output1.insert(END,str(accuracysvml))
	output2.insert(END,str(accuracysvmr))
	output3.insert(END,str(accuracymlpl))
	output4.insert(END,str(accuracymlpa))
	output5.insert(END,str(rmsesvml))
	output6.insert(END,str(rmsesvmr))
	output7.insert(END,str(rmsemlpl))
	output8.insert(END,str(rmsemlpa))
	output9.insert(END,str(mapesvml))
	output10.insert(END,str(mapesvmr))
	output11.insert(END,str(mapemlpl))
	output12.insert(END,str(mapemlpa))
	output13.insert(END,str(accuracysvmlt))
	output14.insert(END,str(accuracysvmrt))
	output15.insert(END,str(accuracymlplt))
	output16.insert(END,str(accuracymlpat))
	output17.insert(END,str(rmsesvmlt))
	output18.insert(END,str(rmsesvmrt))
	output19.insert(END,str(rmsemlplt))
	output20.insert(END,str(rmsemlpat))
	output21.insert(END,str(mapesvmlt))
	output22.insert(END,str(mapesvmrt))
	output23.insert(END,str(mapemlplt))
	output24.insert(END,str(mapemlpat))
	iframe8=Frame(iframe0,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	Button(iframe8,text="CONTINUE",bg="#003366",fg="#99FFFF",width=20,command=graphs).grid(row=0,column=0,sticky=W)
	Button(iframe8,text="EXIT",bg="#003366",fg="#99FFFF",width=20,command=exit).grid(row=0,column=1 ,sticky=W)
	iframe8.grid(row=2,column=0,sticky=W)
	iframe0.grid(row=0,column=0,sticky=W)
	sub.after(120000,lambda:sub.destroy())
	sub.mainloop()
	

def click(v,textdate):
	
	
	print("no",v.get())
	if(v.get()==0):
		textentry="wipro"
	elif(v.get()==1):
	    textentry="infosys"
	elif(v.get()==2):  
	    textentry="reliance"
	elif(v.get()==3):    
	    textentry="reliance communications"
	elif(v.get()==4):  
	    textentry="tata motors"
	elif(v.get()==5):  
	    textentry="mahindra and mahindra"
	elif(v.get()==6):  
	    textentry="rolta"
	elif(v.get()==7):  
	    textentry="ICICI"
	elif(v.get()==8):  
	    textentry="SBI"
	elif(v.get()==9):  
	    textentry="ONGC"
	elif(v.get()==10):  
	    textentry="BPCL"
	elif(v.get()==11):  
	    textentry="hindustan petroleum"
	elif(v.get()==12):  
	    textentry="SENSEX"
	elif(v.get()==13):  
	    textentry="NIFTY"
	elif(v.get()==14):  
	    textentry="NASDAQ"	
	print("textentry",textentry)  
	entered_text=textentry  
	dbconfig = {'user' : 'root','password' : 'root123','database' : 'company_details'}
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	SQL = "select companyfname from company where companyname = '%s' " %(entered_text)
	cursor.execute(SQL)
	res = cursor.fetchall()
	if res	:	
		for row in res:
			fname=row[0]
			fname=filename+fname
	df=pd.read_csv(fname)
	size=len(df)
	length=int(0.80*size)
	datedf=np.array(df['Date'])
	datadf=datedf[length+2:size]
	entered_date=textdate.get()
	date=datetime.strptime(entered_date,'%d-%m-%Y')
	dateL=datetime.strptime("10-04-2017",'%d-%m-%Y')
	dateH=datetime.strptime("02-04-2018",'%d-%m-%Y')
	if(date < dateL or date > dateH):
		sub1=Tk()
		Label(sub1,text="Date : Out of range.Retype the date",bg="black",fg="white",font="none 18 bold").grid(row=0,column=1,sticky=W)
		#sub1.after(3000,lambda:sub1.destroy())	
		sub1.mainloop()
	else:
		index=0
		s=0
		for row in datedf:
			if(date.strftime("%d-%m-%Y") == row ):
				index=index+1
				s=1
				break
			else:
				index=index+1	
		if(index > size-1 and s==0):
			sub1=Tk()
			Label(sub1,text="Date Specified corresponds to a holiday.Retype the date",bg="black",fg="white",font="none 18 bold").grid(row=0,column=1,sticky=W)
			sub1.after(3000,lambda:sub1.destroy())
			sub1.mainloop()
			

		else:			
			dates=date.strftime("%d-%m-%Y")
			print(dates)
			graphname,svml,svmr,mlpl,mlpa,risel,riser,riseml,risema,accuracysvml,accuracysvmr,accuracymlpl,accuracymlpa,accuracysvmlt,accuracysvmrt,accuracymlplt,accuracymlpat,rmsesvml,rmsesvmr,rmsemlpl,rmsemlpa,rmsesvmlt,rmsesvmrt,rmsemlplt,rmsemlpat,mapesvml,mapesvmr,mapemlpl,mapemlpa,mapesvmlt,mapesvmrt,mapemlplt,mapemlpat=project.query(entered_text,dates)
			print("hello")	
			sub=Toplevel()
			sub.title("Predicted Value")
			sub.geometry('1600x1600')
			sub.configure(background='#003366')
			iframe0 = Frame(sub,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
			iframe1 = Frame(iframe0,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
			Label(iframe1,text="The Predicted Value :",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=0,column=0,sticky=W)
			Label(iframe1,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="times 14").grid(row=0,column=1,sticky=W)
			Label(iframe1,text="SVM RBF",bg="#003366",fg="#99FFFF",font="times 14").grid(row=0,column=2,sticky=W)
			Label(iframe1,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="times 14").grid(row=0,column=3,sticky=W)
			Label(iframe1,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="times 14 ").grid(row=0,column=4,sticky=W)
			output1 = Text(iframe1,width=12,height=2,bg="#99FFFF")
			output1.grid(row=1,column=1,sticky=W)
			output2 = Text(iframe1,width=12,height=2,bg="#99FFFF")
			output2.grid(row=1,column=2,sticky=W)
			output3 = Text(iframe1,width=12,height=2,bg="#99FFFF")
			output3.grid(row=1,column=3,sticky=W)
			output4 = Text(iframe1,width=12,height=2,bg="#99FFFF")
			output4.grid(row=1,column=4,sticky=W)
			Label(iframe1,text="RISE/DROP in values:",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=2,column=0,sticky=W)
			Label(iframe1,text="SVM LINEAR",bg="#003366",fg="#99FFFF",font="times 14").grid(row=2,column=1,sticky=W)
			Label(iframe1,text="SVM RBF",bg="#003366",fg="#99FFFF",font="times 14").grid(row=2,column=2,sticky=W)
			Label(iframe1,text="MLP LBFGS",bg="#003366",fg="#99FFFF",font="times 14").grid(row=2,column=3,sticky=W)
			Label(iframe1,text="MLP ADAM",bg="#003366",fg="#99FFFF",font="times 14 ").grid(row=2,column=4,sticky=W)
			output5 = Text(iframe1,width=10,height=1,bg="#99FFFF")
			output5.grid(row=3,column=1,sticky=W)
			output6 = Text(iframe1,width=10,height=1,bg="#99FFFF")
			output6.grid(row=3,column=2,sticky=W)
			output7 = Text(iframe1,width=10,height=1,bg="#99FFFF")
			output7.grid(row=3,column=3,sticky=W)
			output8 = Text(iframe1,width=10,height=1,bg="#99FFFF")
			output8.grid(row=3,column=4,sticky=W)
			iframe1.grid(row=0,column=0,sticky=W)
			iframe2 = Frame(iframe0,width=100,height=400, bd=2, bg="#003366",relief=RAISED)
			Label(iframe2,text="The best Predicted Value is SVM",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=0,column=0,sticky=W)
			Label(iframe2,text="The Value is: ",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=1,column=0,sticky=W)
			output9 = Text(iframe2,width=10,height=1,bg="#99FFFF")
			output9.grid(row=1,column=0,sticky=E)
			Label(iframe2,text="The Rise/Drop in Value is :",bg="#003366",fg="#99FFFF",font="times 18 bold").grid(row=2,column=0,sticky=W)
			output10 = Text(iframe2,width=10,height=1,bg="#99FFFF")
			output10.grid(row=2,column=1,sticky=E)
			iframe2.grid(row=0,column=1,sticky=W)
			iframe0.grid(row=0,column=0,sticky=W)
			output1.insert(END,str(svml))
			output2.insert(END,str(svmr))
			output3.insert(END,str(mlpl))
			output4.insert(END,str(mlpa))
			output5.insert(END,str(risel))
			output6.insert(END,str(riser))
			output7.insert(END,str(riseml))
			output8.insert(END,str(risema))
			output9.insert(END,str(svml))
			output10.insert(END,str(risel))
			iframe3 = Frame(sub,width=1600,height=500, bd=2, bg="#003366",relief=SUNKEN)
			photo1=PhotoImage(file=graphname)
			Label(iframe3,image=photo1,height=500,width=1600,bg="#003366").grid(row=0,column=0,sticky=W)
			iframe3.grid(row=1,column=0,sticky=W)
			iframe4 = Frame(iframe3,width=100,height=100, bd=2, bg="#003366",relief=SUNKEN)
			Label(iframe4,text="PERFORMANCE EVALUATION :",bg="#003366",fg="#99FFFF",font="Arial 28 italic").grid(row=0,column=0,sticky=W)
			Button(iframe4,text="CLICK",width=6,bg="#99FFFF",fg="#003366",command= lambda:Enter(accuracysvml,accuracysvmr,accuracymlpl,accuracymlpa,accuracysvmlt,accuracysvmrt,accuracymlplt,accuracymlpat,rmsesvml,rmsesvmr,rmsemlpl,rmsemlpa,rmsesvmlt,rmsesvmrt,rmsemlplt,rmsemlpat,mapesvml,mapesvmr,mapemlpl,mapemlpa,mapesvmlt,mapesvmrt,mapemlplt,mapemlpat)).grid(row=0,column=1,sticky=W)
			Button(iframe4,text="EXIT",width=6,bg="#99FFFF",fg="#003366",command=exit).grid(row=0,column=2,sticky=W)
			iframe4.grid(row=2,column=0,sticky=W)
			sub.after(30000,lambda:sub.destroy())
			sub.mainloop()
			

def start():
	login()
	window=Tk()
	window.title("Stock Market Analysis")
	window.geometry("800x800")
	window.configure(background='#003366')

	Label(window,text="STOCK MARKET PREDICTION",bg="#003366",fg="#99FFFF",font="Arial 24 bold").pack(side=TOP,anchor=CENTER)
	iframe1 = Frame(window,width=100,height=400, bd=2, relief=SUNKEN,bg="#003366")
	Label(iframe1, text="Enter the company of your choice:",bg="#003366",fg="#99FFFF",font="times 18 bold",justify = LEFT).pack(side=TOP,anchor=W)
	new_root = Toplevel()
	new_root.minsize(width=300, height=300)
	v = new_root.var = IntVar()
	v.set(0)
	for val, language in enumerate(languages):
		Radiobutton(iframe1,text=language,bg="#99FFFF",fg="#003366",font="times 12 bold",justify=LEFT,padx = 10, variable=v,value=val).pack(side=TOP,fill=BOTH,anchor=NW)
	iframe1.pack(expand=1,pady=0)
		
		#Button(window,text="ENTRY",width=6,command=lambda:ShowChoice(v)).pack()
		#Label(window,text="Enter the company Name",bg="#003366",fg="#99FFFF",font="Arial 18 bold").grid(row=1,column=1,sticky=W)
		#textentry=Entry(window,width=20,bg="white")
		#textentry.grid(row=2,column=1,sticky=W)
	iframe2 = Frame(window,width=100,height=400, bd=2, relief=SUNKEN,bg="#003366")
	Label(iframe2,text="Enter the date from 10-04-2017 to 02-04-2018 :",bg="#003366",fg="#99FFFF",font="times 18 bold",justify = LEFT).pack(side=TOP,anchor=W)
	textdate=Entry(iframe2,width=10,bg="#99FFFF",fg="#003366",font="times 14 bold")
	textdate.pack(side=TOP,anchor=CENTER)
	iframe2.pack(expand=1,pady=0)
	print(v.get())
	Button(window,text="SUBMIT",width=10,bg="#99FFFF",fg="#003366",font="times 16 bold",command=lambda:click(v,textdate)).pack(side=TOP,anchor=CENTER)
	window.after(120000,lambda:window.destroy())
	window.mainloop()
			

def logging(textentry,passwordentry):
	window=Tk()
	window.title("Login")
	window.geometry('300x300')
	username=textentry.get()
	pwd=passwordentry.get()
	dbconfig = {'user' : 'root','password' : 'root123','database' : 'login_details'}
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	SQL = "select password from login where username = '%s' " %(username)
	cursor.execute(SQL)
	res = cursor.fetchall()
	loging=0
	output = Text(window,width=20,height=3,bg="white")
	output.grid(row=3,column=0,sticky=W)
	#Button(window,text="Continue",width=10,command=start).grid(row=6,column=1,sticky=W)

	if res	:	
		for row in res:
			print(row)
			if(row[0]==pwd):
				loging=1
			else:
				loging=0
	else:
		loging=0	

	if(loging==1):
		output.insert(END,"Successful Login")	

	else:
		text="invalid username or password"
		#time.sleep(3)
		output.insert(END,text)
		start()
	window.after(1000,lambda:window.destroy())	
	window.mainloop()
		

def signup():
	window=Tk()
	window.title("Sign Up")
	window.geometry('400x400')
	window.configure(background='#99FFFF',height=300,width=100)
	frame0=Frame(window,bg='#99FFFF',height=300,width=300, relief=SUNKEN)
	sect=Frame(frame0,bg='#99FFFF',bd=4,height=100,width=100, relief=SUNKEN)
	Label(sect,text="Enter Username",fg="#003366",bg="#99FFFF",font="Courier 14 bold").grid(row=0,column=0,stick=W)
	usernameentry=Entry(sect,width=20,fg="#003366")
	usernameentry.grid(row=1,column=0,sticky=W)
	sect.grid(row=1,column=0,sticky=W)
	sect2=Frame(frame0,bg='#99FFFF',bd=4,height=100,width=100, relief=SUNKEN)
	Label(sect2,text="Enter Password",fg="#003366",bg="#99FFFF",font="Courier 14 bold").grid(row=0,column=0,stick=W)
	passwordentry=Entry(sect2,width=20,fg="#003366")
	passwordentry.grid(row=1,column=0,sticky=W)
	sect2.grid(row=2,column=0,sticky=W)
	sect3=Frame(frame0,bg='#99FFFF',bd=4,height=100,width=100, relief=SUNKEN)
	Label(sect3,text="Enter email address",fg="#003366",bg="#99FFFF",font="Courier 14 bold").grid(row=0,column=0,sticky=W)
	emailentry=Entry(sect3,width=20,fg="#003366")#003366
	emailentry.grid(row=1,column=0,sticky=W)
	sect3.grid(row=3,column=0,sticky=W)
	sect4=Frame(frame0,bg='#99FFFF',bd=4,height=100,width=100, relief=SUNKEN)
	Button(sect4,text="Sign up",width=6,fg="#003366",bg="#99FFFF",command=lambda:signingup(usernameentry,passwordentry,emailentry)).grid(row=1,column=1,sticky=W)
	Button(sect4,text="BACK",width=6,fg="#003366",bg="#99FFFF",command=login).grid(row=1,column=2,sticky=W)
	sect4.grid(row=4,column=0,sticky=W)
	frame0.grid(row=0,column=0,sticky=W)
	window.after(60000,lambda:window.destroy())
	window.mainloop()
	


def signingup(usernameentry,passwordentry,emailentry):
	pwd=passwordentry.get()
	dbconfig = {'user' : 'root','password' : 'root123','database' : 'login_details'}
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	username=usernameentry.get()
	password=passwordentry.get()
	email=emailentry.get()
	SQL="insert into login(username,password,email) values('%s','%s','%s')" %(username,password,email)
	try:
		cursor.execute(SQL)
		conn.commit()
		start()
	except:
		signup()	



def login():
	window=Tk()
	print("HI")
	window.title("Login Page")
	window.geometry('400x400')
	window.configure(background='#003366',bd=4,height=300,width=300)
	#sect1=Frame(window,bg='blue',bd=4,height=300,width=300).grid(row=1,column=2,sticky=W)
	
	Label(window,text="WELCOME ",bg="#003366",fg="#99FFFF",font="Arial 18 bold").grid(row=0,column=1,sticky=W)
	iframe=Frame(window,width=100,height=400,bg="#003366", bd=2, relief=SUNKEN)
	iframe1=Frame(iframe,width=100,height=100,bg="#003366", bd=2, relief=RAISED)
	Label(iframe1,text="Username",bg="#003366",fg="#99FFFF",font="Helvetica 18 bold").grid(row=0,column=1,sticky=W)
	textentry=Entry(iframe1,width=30,fg="#003366",bg="#99FFFF")
	textentry.grid(row=1,column=1,sticky=W)
	iframe1.grid(row=0,column=1,sticky=W)
	iframe2=Frame(iframe,width=100,height=100,bg="#003366", bd=2, relief=RAISED)
	Label(iframe2,text="Password",bg="#003366",fg="#99FFFF",font="Helvetica 18 bold").grid(row=0,column=1,sticky=W)
	passwordentry=Entry(iframe2,width=30,fg="#003366",bg="#99FFFF",show="*")
	passwordentry.grid(row=1,column=1,sticky=W)
	iframe2.grid(row=1,column=1,sticky=W)
	iframe3=Frame(iframe,width=100,height=100,bg="#003366", bd=2, relief=RAISED)
	Button(iframe3,text="Login",width=6,bg="#003366",fg="#99FFFF",font="none 12 bold",command=lambda:logging(textentry,passwordentry)).grid(row=0,column=0,sticky=W)
	Button(iframe3,text="Signup",width=6,bg="#003366",fg="#99FFFF",font="none 12 bold",command=signup).grid(row=0,column=1,sticky=W)
	iframe3.grid(row=2,column=1,sticky=W)
	iframe.grid(row=2,column=1,sticky=W)
	window.after(20000,lambda:window.destroy())
	window.mainloop()
	
start()	