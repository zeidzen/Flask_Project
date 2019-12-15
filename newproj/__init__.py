# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:06:01 2019

@author: zeidz
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World '

if __name__ == '__main__':
    app.run(debug = True)