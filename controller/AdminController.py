
from tkinter import messagebox
from Controller import DataBaseConnection as con

class AdminDatabase:

    __connection__ = None
    def __init__(self):
        self.__connection__ = con.Database.Connect()

    def AdminLogin(self,LoginAdmin):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM admin WHERE email='"+LoginAdmin.getEmail()+"' AND password='"+LoginAdmin.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
