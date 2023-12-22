import tkinter as tk
import customtkinter as CT
import sys
from tkcalendar import DateEntry
from tkinter import messagebox
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Model import CusRegistrationModel as cusmodel
from Controller import CustomerController as cusdb
import LoginVeiw

class RegistrationPage(CT.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title(" Customer Registration Page")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.id = 0
        self.first_name_CTkLabel = CT.CTkLabel(self, text="First Name:")
        self.first_name_CTkLabel.grid(row=0, column=0, padx=10, pady=5)
        self.first_name_CTkentry = CT.CTkEntry(self,textvariable=CT.StringVar())
        self.first_name_CTkentry.grid(row=0, column=1, padx=10, pady=5)

        self.last_name_CTkLabel = CT.CTkLabel(self, text="Last Name:")
        self.last_name_CTkLabel.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_CTkentry = CT.CTkEntry(self,textvariable=CT.StringVar())
        self.last_name_CTkentry.grid(row=1, column=1, padx=10, pady=5)

        self.email_CTkLabel = CT.CTkLabel(self, text="Email:")
        self.email_CTkLabel.grid(row=2, column=0, padx=10, pady=5)
        self.email_CTkentry = CT.CTkEntry(self,textvariable=CT.StringVar())
        self.email_CTkentry.grid(row=2, column=1, padx=10, pady=5)

        self.address_CTkLabel = CT.CTkLabel(self, text="Address:")
        self.address_CTkLabel.grid(row=3, column=0, padx=10, pady=5)
        self.address_CTkentry = CT.CTkEntry(self,textvariable=CT.StringVar())
        self.address_CTkentry.grid(row=3, column=1, padx=10, pady=5)
        
        self.date_CTklabel = CT.CTkLabel(self,text = 'DOB:')
        self.date_CTklabel.grid(row=4, column=0, padx=10, pady=5)

        self.date_CTkEntry = DateEntry(self,selectmode='day')
        self.date_CTkEntry.grid(row=4,column=1 ,padx=10, pady=5)

        self.phone_CTkLabel = CT.CTkLabel(self, text="Phone Number:")
        self.phone_CTkLabel.grid(row=5, column=0, padx=10, pady=5)
        self.phone_CTkentry = CT.CTkEntry(self,textvariable=CT.StringVar())
        self.phone_CTkentry.grid(row=5, column=1, padx=10, pady=5)
        
        self.pass_CTkLabel = CT.CTkLabel(self, text="Password:")
        self.pass_CTkLabel.grid(row=6, column=0, padx=10, pady=5)
        self.pass_CTkentry = CT.CTkEntry(self,textvariable=CT.StringVar())
        self.pass_CTkentry.grid(row=6, column=1, padx=10, pady=5)

        # Repeat this pattern for the remaining fields

        register_CTkbutton = CT.CTkButton(self, text="Register", command=self.register)
        register_CTkbutton.grid(row=8, column=0, pady=10)
        back_CTkbutton = CT.CTkButton(self, text="Back", command=self.Back)
        back_CTkbutton.grid(row=8, column=1, pady=10)

    def register(self):
        if self.first_name_CTkentry.get()!='' and self.last_name_CTkentry.get()!='' and self.phone_CTkentry.get()!='' and self.email_CTkentry.get()!='' and self.address_CTkentry.get()!='' and self.date_CTkEntry.get_date()!='' and self.pass_CTkentry.get()!='':
            cus = cusmodel.Customer(self.id, self.first_name_CTkentry.get(),self.last_name_CTkentry.get(),self.phone_CTkentry.get(),self.address_CTkentry.get(),self.date_CTkEntry.get_date(),self.email_CTkentry.get(),self.pass_CTkentry.get())
            reg = cusdb.CustomerDatabase()
            reg._CustomerRegister(cus)
            if reg:
                messagebox.showinfo('register','Registration Successfully')
                self.destroy()
                LoginVeiw.LoginPage()
            else:
                messagebox.showerror("register","Register Failure")
        else:
            messagebox.showinfo("register","please write a valid information")

    def Back(self):
        self.destroy()
        LoginVeiw.LoginPage()

if __name__ == "__main__":

    app = RegistrationPage()
    app.mainloop()
