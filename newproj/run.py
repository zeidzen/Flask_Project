# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:06:01 2019

@author: zeidz
"""

import config as con
from flask import Flask , request ,url_for , redirect 
from flask import render_template
import  Register_And_Login

app = Flask(__name__ )
app.config.from_object("config")


@app.route('/') 
def hello_world():
   return 'Hello World '

@app.route('/about') 
def about_page():
   return 'about page'

@app.route('/user2/<username>') 
def user_page(username):
   return 'Welcome {}'.format(username)

@app.route('/post/<int:id_post>') 
def post_page(id_post):
   return 'Post Id is  {}'.format(id_post)

@app.route('/path/<path:sub_bath>') 
def path_page(sub_bath):
   return 'path :   {}'.format(sub_bath)

@app.route('/members') 
def show_user_profile ():
    first_name=request.args.get('first_name')
    last_name=request.args.get('last_name')
    return '<h3> First Name : {} , last Name : {} </h3>'.format(first_name , last_name)

@app.route('/admin') 
def admin ():
    return '<h3> Hello Admin </h3>'

@app.route('/guset/<guset>') 
def guset (guset):
    return '<h3> Hello {} as guset  </h3>'.format(guset)

@app.route('/user/<user>') 
def user (user):
    if user == 'admin' : 
       return redirect (url_for('admin'))
    else : 
       return redirect (url_for('guset' , guset=user ))
   
request_method=['POST','GET','PUT','PATCH','DELETE','COPY','HEAD','OPTIONS',
                'LINK' ,'UNLINK','PURGE','LOCK','UNLOCK','PROPFIND','VIEW']   
@app.route('/login',methods=request_method) 
def login ():
    if request.method == 'POST' : 
       return 'You are using POST Method'
   
    elif request.method == 'GET' : 
       return 'You are using GET Method'
   
    elif request.method == 'PUT' : 
       return 'You are using PUT Method'
   
    elif request.method == 'PATCH' : 
       return 'You are using PATCH Method'    

    elif request.method == 'DELETE' : 
       return 'You are using DELETE Method'          

    elif request.method == 'COPY' : 
       return 'You are using COPY Method' 
   
    elif request.method == 'HEAD' : 
       return 'You are using HEAD Method' 
 
    elif request.method == 'OPTIONS' : 
       return 'You are using OPTIONS Method' 
   
    elif request.method == 'LINK' : 
       return 'You are using LINK Method' 
   
    elif request.method == 'UNLINK' : 
       return 'You are using UNLINK Method' 
   
    elif request.method == 'PURGE' : 
       return 'You are using PURGE Method' 

    elif request.method == 'LOCK' : 
       return 'You are using LOCK Method' 

    elif request.method == 'UNLOCK' : 
       return 'You are using UNLOCK Method' 
   
    elif request.method == 'PROPFIND' : 
       return 'You are using PROPFIND Method' 

    elif request.method == 'VIEW' : 
       return 'You are using VIEW Method' 


@app.route('/login2',methods=['GET'])
def login2():
   if  request.method=='GET' :
       username= request.args.get('username')
       password= request.args.get('password')
       
       o1= Register_And_Login.Register_And_login()
       status=o1.Login_func(username =username , password=password )
       if status == True :
           return redirect(url_for('user_page' , username=username))
       else : 
           return redirect(url_for('user_page',username='Error'))
   else : 
       return render_template ('login/index.html')
   
    
@app.route('/sinup',methods=['GET'])
def sinup():
   if  request.method=='GET' :
       info=dict()
       info['FirstName']= request.args.get('first_name')
       info['LastName']= request.args.get('last_name')
       info['Birthday']= request.args.get('birthday')
       info['Gender']= request.args.get('gender')   
       info['Email']= request.args.get('email')
       info['Phone']= request.args.get('phone')          
       info['UserName']= request.args.get('username')
       info['Country']= request.args.get('country')          
       info['City']= request.args.get('city')
       info['Password']= request.args.get('password')
       
       o1= Register_And_Login.Register_And_login()
       status=o1.Register_func(**info)
       if status :
           return redirect(url_for('user_page' , username=info['UserName']))
       else : 
           return redirect(url_for('user_page',username=status))
   else : 
       return render_template ('sinup/index.html')
   
    
@app.route('/test') 
def test ():
        posts=['Post1','Post2','Post3','Post4','Post5','Post6']
        posts2={'Post1':1,'Post2':2,'Post3':3,'Post4':4,'Post5':5,'Post6':6}

        return render_template('test.html',title="Test Flask ",posts=[posts,posts2])
        #{% ..... %} statment code
        #{{ ..... }} vatiables
        #{# ..... #} comment 
        #{extends "layout.html"} inheritance
  

@app.route('/test2') 
def test2 ():
        return render_template('sinup/index.html')
    
    

if __name__ == '__main__':
    app.run(debug = con.debug ,port=con.port , host = con.host)