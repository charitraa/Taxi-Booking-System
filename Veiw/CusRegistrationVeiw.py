import tkinter as tk
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Model import CusRegistrationModel as cusmodel
from Controller import CustomerController as cusdb
import LoginVeiw

class RegistrationPage(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title(" Customer Registration Page")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        self.id = 0
        self.first_name_Label = tk.Label(self, text="First Name:")
        self.first_name_Label.grid(row=0, column=0, padx=10, pady=5)
        self.first_name_entry = tk.Entry(self,textvariable=tk.StringVar())
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.last_name_Label = tk.Label(self, text="Last Name:")
        self.last_name_Label.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry = tk.Entry(self,textvariable=tk.StringVar())
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_Label = tk.Label(self, text="Email:")
        self.email_Label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self,textvariable=tk.StringVar())
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_Label = tk.Label(self, text="Address:")
        self.address_Label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self,textvariable=tk.StringVar())
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        self.phone_Label = tk.Label(self, text="Phone Number:")
        self.phone_Label.grid(row=4, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self,textvariable=tk.StringVar())
        self.phone_entry.grid(row=4, column=1, padx=10, pady=5)

        self.pass_Label = tk.Label(self, text="Password:")
        self.pass_Label.grid(row=5, column=0, padx=10, pady=5)
        self.pass_entry = tk.Entry(self,textvariable=tk.StringVar())
        self.pass_entry.grid(row=5, column=1, padx=10, pady=5)

        # Repeat this pattern for the remaining fields

        register_button = tk.Button(self, text="Register", command=self.register)
        register_button.grid(row=8, column=0, pady=10)
        back_button = tk.Button(self, text="Back", command=self.Back)
        back_button.grid(row=8, column=1, pady=10)
    def register(self):
        cus = cusmodel.Customer(self.id, self.first_name_entry.get(),self.last_name_entry.get(),self.phone_entry.get(),self.address_entry.get(),self.email_entry.get(),self.pass_entry.get())
        reg = cusdb.CustomerDatabase()
        reg.CustomerRegister(cus)
    
    def Back(self):
        self.destroy()
        LoginVeiw.LoginPage()

if __name__ == "__main__":
    
    app = RegistrationPage()
    app.mainloop()
