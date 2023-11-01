from tkinter import messagebox
import mysql.connector as c
# from model import LoginModel 
class CustomerDatabase:
    message = ""
    __connection__ = None
    try:
        @staticmethod
        def Connect():
            connection = c.connect(
                host='localhost',
                user = 'root',
                password = 'root',
                database = 'taxi'
            )
            if connection.is_connected():
                CustomerDatabase.message = "Connected"
                return connection
            connection.close()  
    except Exception as e:
        print(e)
        
    def __init__(self):
        self.__connection__ = CustomerDatabase.Connect()
    
    def Login(self,LoginUser):
        if self.__isvalidlogin(LoginUser):
            
            if self.__isAuthentic(LoginUser):
                messagebox.showinfo("login","Login sucessfully")
            else:
                messagebox.showinfo("login","invalid username and password")
        else:
            messagebox.showinfo("login","please write a username and password and try again")
    def __isvalidlogin(self,LoginUser):
        if LoginUser.getEmail()!="" and LoginUser.getPassword != "":
            return True
        return False
    def __isAuthentic(self,LoginUser):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM login WHERE Email='"+LoginUser.getEmail()+"' AND Password='"+LoginUser.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
        
