import smtplib
import datetime
from tkinter import *
import random as r
import sqlite3
now=datetime.datetime.now()
date=now.strftime('%y-%m-%d %H:%M:%S')
conn=sqlite3.connect('Test.db')
print("opened successfully")
#Enable the following line for one time to create a table in database and them make it as a comment
#conn.execute('''CREATE TABLE DData(NAME TEXT,EMAIL VARCHAR(600),DATETIME REAL,VERIFY NUMBER)''')
#print("created successfully")
root=Tk()
win=Frame(root)
def ran():
    a=""
    for i in range(5):
        a+=str(r.randint(0,9))
    return a
otpvalue=ran()
def email1():
    FROM='0108shyamala@gmail.com'
    TO=txt2.get()
    SUBJECT='otp'
    TEXT='otpvalue'
    pwd='nalgonda'
    message="otp %s \n\n "%(otpvalue)
    #print(message)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(FROM,pwd)
    server.sendmail(FROM,TO,message)
    server.close()
    print('success')
def verify():
    a1=txt3.get()
    if(a1==otpvalue):
        verifyy=1
        l4=Label(win,text='Thank u')
        l4.grid(column=25,row=11)
        l4.config(bg='yellow',fg='blue',width=10)
        conn.execute('''INSERT INTO DData(NAME,EMAIL,DATETIME,VERIFY)VALUES(?,?,?,?)''',(txt1.get(),txt2.get(),date,verifyy))
        print("record created")
        conn.commit()
        conn.close()
    else:
        l2=Label(win,text='Wrong OTP')
        l2.grid(column=25,row=11)
        l2.config(bg='yellow',fg='red')
l1=Label(win,text='NAME')
l1.grid(column=0,row=0)
txt1=Entry(win,width=30)
txt1.grid(column=30,row=0)
l2=Label(win,text='EMAIL')
l2.grid(column=0,row=2)
txt2=Entry(win,width=30)
txt2.grid(column=30,row=2)
conn=sqlite3.connect('Test.db')
b1=Button(win,text='OTP',command=email1)
b1.grid(column=25,row=3)
l3=Label(win,text='OTP')
l3.grid(column=0,row=5)
txt3=Entry(win,width=30)
txt3.grid(column=30,row=5)
b2=Button(win,text='VERIFY',command=verify)
b2.grid(column=25,row=7)
win.grid()
win.pack()
root.mainloop()
