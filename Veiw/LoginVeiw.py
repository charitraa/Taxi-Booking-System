import tkinter as tk
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Controller import CustomerController as cusdb , DriverController as drivedb , AdminController as admindb
from Model import LoginModel as loginmd
from tkinter import messagebox
import RegistrationOptionVeiw , VerifyEmailVeiw
import BookingVeiw
import GobalVariable
class LoginPage(tk.Tk):

    email = str
    password = str
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.title('Login Page')
        self.geometry("300x300")
        self.create_widgets()
        
    def create_widgets(self):
        # Create labels
        self.label_username = tk.Label(self, text="Email:")
        self.label_password = tk.Label(self, text="Password:")

        # Create entry widgets for username and password
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.entry_username = tk.Entry(self, textvariable=self.email)
        self.entry_password = tk.Entry(self, textvariable= self.password , show='*')  # Show * for password
        
        # Create login button
        self.button_login = tk.Button(self, text="Login", command=self.on_login)
        self.button_SignUp = tk.Button(self, text="SignUp", command=self.on_SignUp)
        self.button_Forget = tk.Button(self, text="Forget Password", command=self.on_forget)
        # Arrange widgets using grid
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.place(x=110, y=100,width=75)
        self.button_SignUp.place(x=110, y=150,width=75)
        self.button_Forget.place(x=100, y=200,width=100)
    def on_SignUp(self):
        self.destroy()
        RegistrationOptionVeiw.OptionPage()
    
    def on_forget(self):
        
        self.destroy()
        VerifyEmailVeiw.VerifyEmail()
    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
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
