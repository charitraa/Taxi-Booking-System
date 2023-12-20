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
        
        self.geometry("1000x1000")
        self.create_widgets()
        
    def create_widgets(self):
        # Create CTkLabels
        self.CTkLabel_username = CT.CTkLabel(self, text="Email:")
        self.CTkLabel_password = CT.CTkLabel(self, text="Password:")

        # Create CTkentry widgets for username and password
        
        # background_image = Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\Veiw\\1685725595.jpeg')
        # self.background_photo = ImageCT.PhotoImage(background_image)

        # self.img = CT.CTkLabel(image=self.background_photo).place(x=10,y=20)

        self.email = CT.StringVar()
        self.password = CT.StringVar()
        self.CTkentry_username = CT.CTkEntry(self, textvariable=self.email,border_width=0)
        self.CTkentry_password = CT.CTkEntry(self, textvariable= self.password , show='*')  # Show * for password
        
        # Create login button
        self.button_login = CT.CTkButton(self, text="Login", command=self.on_login)
        self.button_SignUp = CT.CTkButton(self, text="SignUp", command=self.on_SignUp)
        self.button_Forget = CT.CTkButton(self, text="Forget Password", command=self.on_forget)
        # Arrange widgets using grid
        self.CTkLabel_username.grid(row=0, column=0, padx=10, pady=10)
        self.CTkentry_username.grid(row=0, column=1, padx=10, pady=10)
        self.CTkLabel_password.grid(row=1, column=0, padx=10, pady=10)
        self.CTkentry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.place(x=110, y=100)
        self.button_SignUp.place(x=110, y=150)
        self.button_Forget.place(x=100, y=200)

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
