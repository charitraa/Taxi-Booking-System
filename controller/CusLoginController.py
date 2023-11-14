from tkinter import messagebox
from Controller import Connection as con

class LoginDatabase:

        
    def __init__(self):
        self.__connection__ = con.Database.Connect()
    
    # def Login(self,LoginUser):
    #     if self.__isvalidlogin(LoginUser):
            
    #         if(self.__isAuthentic(LoginUser)):
    #             return True

    #     else:
    #         return False
    # def __isvalidlogin(self,LoginUser):
    #     if LoginUser.getEmail()!="" and LoginUser.getPassword != "":
    #         return True
    #     return False
    def Login(self,LoginUser):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM customer WHERE email='"+LoginUser.getEmail()+"' AND password='"+LoginUser.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
        
