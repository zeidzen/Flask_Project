# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:06:01 2019

@author: zeidz
"""

import config as con
from flask import Flask , request ,url_for , redirect ,session
from flask import render_template
import  Register_And_Login
import database as db


app = Flask(__name__ )
app.secret_key = 'any random string'

data = dict()
data['image'] = "/static/Home/images/_thumb1.jpg"
data['desc'] = ''' Elementum ea, nibh et, velit sed sagittis. Ipsum libero. Viverra integer enim, sed dolor. Inceptos elit, vitae et. Eget eget nec, lectus nisl, vehicula est feugiat. cum condimentum mattis dui fusce ut, vel convallis suspendisse suspendisse sed in. Libero blandit curae at magna ut, id mauris suspendisse ligula neque integer non.'''

@app.route('/set/')
def set():
    session['title'] = 'FLASK'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('title', 'not set')



@app.route('/') 
def index():
   return redirect(url_for('Home_page'))

@app.route('/Home') 
def Home_page():
   title ='test' #session['username']
   return render_template ('Home.html',title=title ,data=data)


@app.route('/login/')
def login():
    if 'username' in session : 
        return redirect(url_for('Home_page'))
    else : return render_template("login.html")

@app.route('/login',methods=['POST'] ) 
def Login_page():
   if  request.method=='POST' :
       username= request.form ['username']
       password= request.form ['password']
       opj= Register_And_Login.Register_And_login()
       status=opj.Login_func(username =username , password=password )
       if status == True :
           session['username'] =username 
           return redirect(url_for('Home_page' ))
       else : 
           return render_template ('login.html')
   else : 
       return render_template ('login.html')
 
    
@app.route('/sinup/')
def sinup():
    return render_template("sinup.html")


@app.route('/sinup_func',methods=['POST' , 'GET'])
def sinup_func():
   if  request.method=='GET' :
       info=dict()
       info['FirstName']= request.args.get('first_name')
       info['LastName']= request.args.get('last_name')
#       info['Birthday']= b[::-1]
       if request.args.get('gender')   == 'Male' :  info['Gender'] ='M'
       elif request.args.get('gender')   == 'Female' :info['Gender'] ='F'
       info['Email']= request.args.get('email')
       info['Phone']= request.args.get('phone')          
       info['Country']= 1
       info['Password']= request.args.get('password')
       
       opj= Register_And_Login.Register_And_login()
       status=opj.Register_func(**info)
       if status == True :
           return redirect(url_for('login'))
       else : 
           return render_template ('Home.html')
   else : 
       return redirect(url_for('sinup'))
   

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('Home_page'))
    
if __name__ == '__main__':
    app.run(debug = con.debug ,port=con.port , host = con.host)
