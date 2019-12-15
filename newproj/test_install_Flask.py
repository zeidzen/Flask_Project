# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:06:01 2019

@author: zeidz
"""

from flask import Flask ,url_for ,render_template ,redirect , request
app = Flask(__name__)

@app.route('/home')
def hello_admin():
   return 'Hello Admin'

@app.route('/guset/<guset>')
def hello_guset(guset):
   return 'Hello  %s as Guest'% guset

@app.route('/user/<name>')
def hello_user (name):
   if name=='admin' :  
       return redirect (url_for('hello_admin' ))
   else : return redirect (url_for('hello_guset' , guset=name ))


@app.route('/success/<name>')
def success (name):
       return'hello %s'% name     
@app.route('/login',methods=['POST' , 'GET'])
def login():
   if  request.method=='POST' :
       username= request.form['username']
       password= request.form['password']
       
       if username=='zeid' and password=='zen' :
           return redirect(url_for('home',username))
       else : 
           return redirect(url_for('home','Error'))
   else : 
       return render_template ('login/index.html')

@app.route('/Sinup')
def Sinup():
   return render_template ('login/index.html')

if __name__ == '__main__':
    app.run(debug = True)