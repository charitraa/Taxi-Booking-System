
from tkinter import messagebox
from Controller import DataBaseConnection as con

class DriverDatabase:
    __connection__ = None
    def __init__(self):
        self.__connection__ = con.Database.Connect()
        
    def DriverLogin(self,LoginDriver):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("SELECT * FROM driver WHERE email='"+LoginDriver.getEmail()+"' AND password='"+LoginDriver.getPassword()+"'")
            record = cursor.fetchone()
            
        except Exception as e:
            print(e)
            
        return record
