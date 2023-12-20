import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from tkinter import messagebox
from PIL import ImageTk, Image
from Controller import CustomerController as cusdb , DriverController as drivedb , AdminController as admindb
from Model import LoginModel as loginmd
import tkinter as tk
import customtkinter as CT
import RegistrationOptionVeiw , VerifyEmailVeiw , BookingVeiw , GobalVariable

class LoginPage(CT.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Login Page')
        width= self.winfo_screenwidth() 
        height= self.winfo_screenheight()
        # self.state('zoomed')
        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        # self.geometry("1000x1000")
        self.create_widgets()

    def create_widgets(self):
        # Create CTkLabels
        # Create CTkentry widgets for username and password
        
        self.background_image = CT.CTkImage(Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\image\\new.png'), size=(1000,1000))
        self.img = CT.CTkLabel(self,image=self.background_image, text="").place(x=0,y=0)
        self.CTkLabel_username = CT.CTkLabel(self, text="Email:").place(x=1100,y=300)
        self.CTkLabel_password = CT.CTkLabel(self, text="Password:").place(x=1100,y=500)

        self.email = CT.StringVar()
        self.password = CT.StringVar()
        self.CTkentry_username = CT.CTkEntry(self, textvariable=self.email,border_width=0).place(x=1100,y=400)
        self.CTkentry_password = CT.CTkEntry(self, textvariable= self.password , show='*').place(x=1100,y=600) # Show * for password
        
        # Create login button
        self.button_login = CT.CTkButton(self, text="Login", command=self.on_login).place(x=1100,y=700)
        self.button_SignUp = CT.CTkButton(self, text="SignUp", command=self.on_SignUp).place(x=1100,y=800)
        self.button_Forget = CT.CTkButton(self, text="Forget Password", command=self.on_forget).place(x=1300,y=800)
        # Arrange widgets using grid

    def on_SignUp(self):
        self.destroy()
        nextpage = CT.CTkToplevel()
        RegistrationOptionVeiw.OptionPage(nextpage)
    
    def on_forget(self):
        self.destroy()
        VerifyEmailVeiw.VerifyEmail()

    def on_login(self):
        username = self.CTkentry_username.get()
        password = self.CTkentry_password.get()
        login = loginmd.Login(_email=username, _password=password)
        customer = cusdb.CustomerDatabase()
        cus = customer.CustomerLogin(login)
        driver  = drivedb.DriverDatabase()
        dri = driver.DriverLogin(login)
        admin = admindb.AdminDatabase()
        ad = admin.AdminLogin(login)

        if cus!=None:
            messagebox.showinfo('Login','Customer Login Sucessfully')
            GobalVariable.Customer = cus
            self.destroy()
            BookingVeiw.Booking()
        elif dri!=None:
            messagebox.showinfo('Login','Driver Login Sucessfully')
            GobalVariable.Driver = dri
            self.destroy()
        elif ad!=None:
            messagebox.showinfo('Login','Admin Login Sucessfully')
            GobalVariable.Admin  = ad
            self.destroy()
        elif username=='' or password=='':
            messagebox.showwarning('Login','please write both email and password')
        elif username=='' and password =='':
            messagebox.showwarning('Login','please write email and password')
        else:
            messagebox.showinfo('Login','Incorrect email and password')

if __name__ == "__main__":
    
    app = LoginPage()
    app.mainloop()
