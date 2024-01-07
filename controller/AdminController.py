# import the file and tkinter library
from tkinter import messagebox
from Controller import DataBaseConnection as con
#create a  AdminDatabase Class
class AdminDatabase:

    __connection__ = None
    #create a constructor
    def __init__(self):
        self.__connection__ = con.Database.Connect()
    #create  a Adminlogin Methods
    def AdminLogin(self,LoginAdmin):
        try:
            
            cursor = self.__connection__.cursor()
            #write a Select Query
            cursor.execute("SELECT * FROM admin WHERE email='"+LoginAdmin.getEmail()+"' AND password='"+LoginAdmin.getPassword()+"'")
            record = cursor.fetchone()
            
        except Exception as e:
            print(e)
        return record