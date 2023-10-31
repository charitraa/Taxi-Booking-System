from tkinter import messagebox
from LoginController import LoginController
# from model import LoginModel 
class database:
    __connection__ = None
    # LoginUser = LoginModel.Login()
    def __init__(self):
        self.__connection__ = LoginController.Connect()
    
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
        if  LoginUser.getEmail()== "admin" and  LoginUser.getPassword() =="admin":
            
            return True
        return False
