from tkinter import messagebox
# from Controller import Connection as con
import mysql.connector as c
class LoginDatabase:
    message = ""
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
                LoginDatabase.message = "Connected"
                return connection
            connection.close()  
    except Exception as e:
        print(e)

        
    def __init__(self):
        self.__connection__ = LoginDatabase.Connect()
        
    def Login(self,LoginUser):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM driver WHERE email='"+LoginUser.getEmail()+"' AND password='"+LoginUser.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
        
