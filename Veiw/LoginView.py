
#importing the libary and files
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from tkinter import messagebox
from PIL import Image
from controller import CustomerController as cusdb , DriverController as drivedb , AdminController as admindb
from Model import LoginModel as loginmd
import tkinter as tk
import customtkinter as CT
import Veiw.VerifyEmailView as VerifyEmailView , Veiw.RegistrationView as RegistrationView , GobalVariable, CustomerDashboard, DriverDashboardBoard ,AdminDashboard

# create the class
class LoginPage():
    # create the constructor
    def __init__(self,master):
        self.master = master
        self.master.title('Login Page')#titlename
        self.master.config(background="white")#background   
        CT.set_default_color_theme("green")
        
        # decleare the font for text
        my_font = CT.CTkFont(family="Times", size=50,weight="bold")

        #create Background Image
        self.background_image = CT.CTkImage(Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\image\\Home.png'), size=(1000,850))
        self.img = CT.CTkLabel(self.master,image=self.background_image, text="").place(x=0,y=0)

        # Create CTkLabels
        self.welcome = CT.CTkLabel(self.master,text="Welcome Back", font=my_font,text_color="#00BF63", fg_color="white")
        my_font.configure(family="TImes")
        self.welcome.place(x=1100,y=100)

        self.txt = CT.CTkLabel(self.master,text=" Sign in to your account", font= CT.CTkFont(family="Times", size=30),fg_color="white")
        self.txt.place(x=1100,y=200)

        self.CTkLabel_username = CT.CTkLabel(self.master, text="Email:", font= CT.CTkFont(family="Times",size=30),text_color="#00BF63",fg_color="white").place(x=1110,y=300)
        self.CTkLabel_password = CT.CTkLabel(self.master, text="Password:",font=CT.CTkFont(family="Times",size=30),text_color="#00BF63", fg_color="white").place(x=1110,y=400)

        self.register = CT.CTkLabel(self.master,text="Haven't your register?", font=CT.CTkFont(family="Times",size=20), bg_color="white").place(x=1110,y=630)

        # Create CTkentry widgets for username and password
        self.CTkentry_username = CT.CTkEntry(self.master, textvariable=CT.StringVar(),width=300, border_color="#00BF63")
        self.CTkentry_username.place(x=1110,y=350)
        self.show = CT.StringVar()
        self.CTkentry_password = CT.CTkEntry(self.master, textvariable=  self.show,width=300 , show='*',border_color="#00BF63", border_width=2)
        self.CTkentry_password.place(x=1110,y=450) # Show * for passwords
        self.sh = CT.IntVar(value=0)
        def my_show():
            if(  self.sh.get()==1):
                self.CTkentry_password.configure(show='') # display the chars
            else:
                self.CTkentry_password.configure(show='*')# hide the chars using mask
        # create check box
        self.remember = CT.CTkCheckBox(self.master,text="Show Password", bg_color="white", font=CT.CTkFont(family="Times", size=20),variable=self.sh,onvalue=1,offvalue=0,command=my_show).place(x=1110,y=510) 
        
        # Create login button
        self.button_login = CT.CTkButton(self.master, text="Login", command=self.on_login, width=300, height=40, text_color="white", font=CT.CTkFont(family="Times", size=20),hover=False).place(x=1110,y=560)
        self.button_SignUp = CT.CTkButton(self.master, text="Signup", command=self.on_SignUp,fg_color='white', text_color='#00BF63', bg_color="white",hover=False, width=30,font=CT.CTkFont(family="Times",size=20)).place(x=1285,y=630)
        self.button_Forget = CT.CTkButton(self.master, text="Forget Password ?", command=self.on_forget, fg_color="white", bg_color="white", text_color="#00BF63", font=CT.CTkFont(family="Times", size=18), hover=False).place(x=1280,y=510)

        # create the signup function
    def on_SignUp(self):
        # self.master.destroy()
        reg = CT.CTkToplevel()
        RegistrationView.RegistrationPage(reg)
        reg.mainloop()
        
    # create the forget function
    def on_forget(self):
        reg = CT.CTkToplevel()
        VerifyEmailView.VerifyEmail(reg)
        reg.mainloop()
        
    # create the login function
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
            messagebox.showinfo('Login','Customer Login Sucessfully',parent=self.master)
            GobalVariable.Customer = cus
            self.master.destroy()
            reg = CT.CTkToplevel()
            CustomerDashboard.Dashboard(reg)
            reg.after(0,lambda:reg.state('zoomed'))
            reg.mainloop()

        elif dri!=None:
            messagebox.showinfo('Login','Driver Login Sucessfully',parent=self.master)
            GobalVariable.Driver = dri
            self.master.destroy()
            reg = CT.CTkToplevel()
            DriverDashboardBoard.Dashboard(reg)
            reg.after(0,lambda:reg.state('zoomed'))
            reg.mainloop()

        elif ad!=None:
            messagebox.showinfo('Login','Admin Login Sucessfully',parent=self.master)
            GobalVariable.Admin  = ad
            self.master.destroy()
            reg = CT.CTkToplevel()
            AdminDashboard.Dashboard(reg)
            reg.after(0,lambda:reg.state('zoomed'))
            reg.mainloop()
        elif username=='' or password=='':
            messagebox.showwarning('Login','please write both email and password',parent=self.master)
        elif username=='' and password =='':
            messagebox.showwarning('Login','please write email and password',parent=self.master)
        else:
            messagebox.showerror('Login','Incorrect email and password',parent=self.master)
#create the name function
if __name__ == "__main__":
    
    app = CT.CTk()
    app.after(0,lambda:app.state('zoomed'))
    LoginPage(app)
    # CT.deactivate_automatic_dpi_awareness()
    
    app.mainloop()
