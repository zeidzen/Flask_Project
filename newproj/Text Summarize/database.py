"""
Establish a connection with the database Mysql
"""
# MY SQL 
import pymysql

class DataBase () :
    
        def __init__(self) :
            #Connect to the DataBase 
            self.connection = pymysql.connect(host='localhost',#Server
                                         user='root', #your username
                                         password='2020',#your password
                                         db="database_final_project")#Name DB
            
        def Insert_Data (self ,table,**value) : 
            """
            """
            name=str(tuple(value.keys()))
            name=name.replace('\'',' ')
            sql="INSERT INTO "+table+" "+name+" VALUES "+str(tuple(value.values()))
            mycursor = self.connection.cursor()
            mycursor.execute(sql)  
            self.connection.commit()
            
        def Select_Data_One_Row (self,sql) :
            """
            """
            mycursor = self.connection.cursor()
            mycursor.execute(sql)
            data =mycursor.fetchone()
            self.connection.commit()
            return data

        
        def Select_Data_More_Row (self,sql) : 
            """
            """
            mycursor = self.connection.cursor()
            mycursor.execute(sql)
            data =mycursor.fetchall()
            self.connection.commit()
            return data
        
        
        
        
        def Update_Data_All_Coulmn_String(self,table,Id,**value) :
            items=''
            i=0
            for  name , val in value.items():
                i=i+1
                if (i < len(value.keys())) :
                    items=items+str(name)+' = '+'\''+str(val)+'\''+' , '
                else :
                    items=items+str(name)+' = '+'\''+str(val)+'\''

            sql="UPDATE {} SET {} WHERE Id={} ;".format(table,items,Id)
            print(sql)
            mycursor = self.connection.cursor()
            mycursor.execute(sql)  
            self.connection.commit()
            
            
            
        def Update_Data_one_Coulmn (self,table,Id,name,value) : 
            sql="UPDATE {} SET {} ='{}' WHERE Id={} ;".format(table,name,value,Id)
            print(sql)
            mycursor = self.connection.cursor()
            mycursor.execute(sql)  
            self.connection.commit()
    
    
        def Delete_Data (self,table,name,value) : 
            sql ="DELETE FROM {} WHERE {}='{}';".format(table,name,value)
            mycursor = self.connection.cursor()
            mycursor.execute(sql)  
            self.connection.commit()

