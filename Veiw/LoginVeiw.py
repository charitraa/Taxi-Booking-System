import tkinter as tk
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Controller import CusLoginController as cusdb
from Controller import DriveLoginController as drivedb
from Model import LoginModel as loginmd
import CusRegistrationVeiw as cusregveiw
from tkinter import messagebox

class LoginPage(tk.Tk):

    email = str
    password = str
    def __init__(self, master=None):
        super().__init__()
        self.master = master
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

        # Arrange widgets using grid
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, columnspan=2, pady=20)

    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        login = loginmd.Login(_email=username, _password=password)
        customer = cusdb.LoginDatabase()
        cus = customer.Login(login)
        driver  = drivedb.LoginDatabase()
        dri = driver.Login(login)
        
        if cus==True:
            messagebox.showinfo('Login','Customer Login Sucessfully')
            self.destroy()
                

        elif dri==True:
            messagebox.showinfo('Login','Driver Login Sucessfully')
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
