# -*- coding: utf-8 -*-

import database as db
import hashlib, binascii
import os 


class Register_And_login () : 
    
    def __init__(self) :
         self.con=db.DataBase()
                  
    def hash_password(self,password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
    
    
    def verify_password(self,stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                      provided_password.encode('utf-8'), 
                                      salt.encode('ascii'), 
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
    
    
    
    def Register_func (self ,**info) :   
        """
        This function adds information to the database
        that the user entered in the fields in the (Sinup) interface :
        ( First Name , Last Name , Username , Email , Phone , Password ,Birthday,
          Gender ,City , Country  )
        
        Initially it checks whether the entry is correct or incorrect and
        returns an error message in this case
        
        After , data is sent to the database to make sure the entered data
        is not duplicate
        
        If correct returns a message that the operation completed
        successfully and if there is an error returns an error message with
        the duplicate data specified
        """
        self.con.Insert_Data(table='users',**info)
        return True
    
    
    
    def Login_func ( self,username , password) :   
            """
            This function makes sure that the logon information is correct
            """
            info=dict()
            
            #UserName 
            UserName=str(username).lower().strip()
            if UserName!='' : 
                    info['UserName'] =UserName
            else : 
                 return  'Please Enter Username'
            #======================================================================
            #Password
            Password = password
            if Password!='' : 
                if  len(password) >=8 :   
                    info['password'] =password
                else : 
                   return 'Please enter a password of more than 8 digits'
            else : 
                 return 'Please Enter Password'
    
            #======================================================================
            sql="SELECT Id ,Email,Phone,Password  FROM users WHERE Email='{}' OR Phone='{}' ; ".format(info['UserName'],
                                                 info['UserName'])
            data=self.con.Select_Data_One_Row(sql)
            try : 
                if data[1]==info['UserName'] or data[2]==info['UserName']   :
                    if self.verify_password(data[3],password) :
                        return True
                    else :
                        return 'Please enter a valid password'
                else :
                    return 'Please enter a valid username or email address'
            except :
                    return 'Please enter a valid username or email address'