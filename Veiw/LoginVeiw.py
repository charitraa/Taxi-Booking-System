import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from tkinter import messagebox
from PIL import ImageTk, Image
from Controller import CustomerController as cusdb , DriverController as drivedb , AdminController as admindb
from Model import LoginModel as loginmd
import tkinter as tk
import customtkinter as CT
import VerifyEmailVeiw , BookingVeiw , RegistrationVeiw , GobalVariable

# create the class
class LoginPage(CT.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Login Page')
        self.config(background="white")
        self.create_widgets()

    def create_widgets(self):
        # decleare the font for text
        my_font = CT.CTkFont(family="Times", size=50,weight="bold")
        #create Background Image
        self.background_image = CT.CTkImage(Image.open('image\\frontpage.png'), size=(1000,850))
        self.img = CT.CTkLabel(self,image=self.background_image, text="").place(x=0,y=0)

        # Create CTkLabels
        self.welcome = CT.CTkLabel(self,text="Welcome Back", font=my_font,text_color="green", fg_color="white")
        my_font.configure(family="new name")
        self.welcome.place(x=1100,y=100)

        self.txt = CT.CTkLabel(self,text=" Sign in to your account", font= CT.CTkFont(family="Times", size=30),fg_color="white")
        self.txt.place(x=1100,y=200)

        self.CTkLabel_username = CT.CTkLabel(self, text="Email:", font= CT.CTkFont(family="Times",size=30),text_color="green",fg_color="white").place(x=1110,y=300)
        self.CTkLabel_password = CT.CTkLabel(self, text="Password:",font=CT.CTkFont(family="Times",size=30),text_color="green", fg_color="white").place(x=1110,y=400)

        # Create CTkentry widgets for username and password
        self.CTkentry_username = CT.CTkEntry(self, textvariable=CT.StringVar(),width=300, border_color="green").place(x=1110,y=350)
        self.CTkentry_password = CT.CTkEntry(self, textvariable= CT.StringVar(),width=300 , show='*',border_color="green", border_width=2).place(x=1110,y=450) # Show * for passwords

        # create check box

        self.remember = CT.CTkCheckBox(self,text="Remember me", bg_color="white", font=CT.CTkFont(family="Times", size=20)).place(x=1110,y=500) 
        
        # Create login button
        self.button_login = CT.CTkButton(self, text="Login", command=self.on_login, width=300, height=40, fg_color="green", text_color="white", font=CT.CTkFont(family="Times", size=20)).place(x=1110,y=550)
        self.button_SignUp = CT.CTkButton(self, text="SignUp", command=self.on_SignUp,fg_color='white', text_color='black', bg_color="white").place(x=1100,y=800)
        self.button_Forget = CT.CTkButton(self, text="Forget Password ?", command=self.on_forget, fg_color="white", bg_color="white", text_color="green", font=CT.CTkFont(family="Times", size=15), hover=False).place(x=1280,y=500)
        # Arrange widgets using grid

    def on_SignUp(self):
        self.destroy()
        RegistrationVeiw.RegistrationPage()
    
    def on_forget(self):

        self.destroy()
        page = CT.CTkToplevel()
        VerifyEmailVeiw.VerifyEmail(page)

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
    app.after(0,lambda:app.state('zoomed'))
    app.mainloop()
