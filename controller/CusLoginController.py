from tkinter import messagebox
from Controller import Connection as con

class LoginDatabase:

        
    def __init__(self):
        self.__connection__ = con.Database.Connect()

    def Login(self,LoginUser):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM customer WHERE email='"+LoginUser.getEmail()+"' AND password='"+LoginUser.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
        
