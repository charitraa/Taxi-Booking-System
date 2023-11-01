import customtkinter as tk
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Model import CusRegistrationModel as cusmodel
from Controller import CusRegistrationController as cusdb

class RegistrationPage(tk.CTk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Registration Page")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        self.id = 0
        self.first_name_CTKLabel = tk.CTkLabel(self, text="First Name:")
        self.first_name_CTKLabel.grid(row=0, column=0, padx=10, pady=5)
        self.first_name_entry = tk.CTkEntry(self,textvariable=tk.StringVar())
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.last_name_CTKLabel = tk.CTkLabel(self, text="Last Name:")
        self.last_name_CTKLabel.grid(row=1, column=0, padx=10, pady=5)
        self.last_name_entry = tk.CTkEntry(self,textvariable=tk.StringVar())
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_CTKLabel = tk.CTkLabel(self, text="Email:")
        self.email_CTKLabel.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.CTkEntry(self,textvariable=tk.StringVar())
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_CTKLabel = tk.CTkLabel(self, text="Address:")
        self.address_CTKLabel.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.CTkEntry(self,textvariable=tk.StringVar())
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.phone_CTKLabel = tk.CTkLabel(self, text="Phone Number:")
        self.phone_CTKLabel.grid(row=4, column=0, padx=10, pady=5)
        self.phone_entry = tk.CTkEntry(self,textvariable=tk.StringVar())
        self.phone_entry.grid(row=4, column=1, padx=10, pady=5)

        self.pass_CTKLabel = tk.CTkLabel(self, text="Password:")
        self.pass_CTKLabel.grid(row=5, column=0, padx=10, pady=5)
        self.pass_entry = tk.CTkEntry(self,textvariable=tk.StringVar())
        self.pass_entry.grid(row=5, column=1, padx=10, pady=5)

        # Repeat this pattern for the remaining fields

        register_button = tk.CTkButton(self, text="Register", command=self.register)
        register_button.grid(row=8, column=1, pady=10)
    def register(self):
        cus = cusmodel.Customer()
        cus.setId(self.id)
        cus.setFirst(self.first_name_entry.get())
        cus.setLast(self.last_name_entry.get())
        cus.setAddress(self.address_entry.get())
        cus.setPhone( self.phone_entry.get())
        cus.setEmail(self.email_entry.get())
        cus.setPassword(self.pass_entry.get())
        reg = cusdb.CustomerDatabase()
        reg.Register(cus)

if __name__ == "__main__":
    
    app = RegistrationPage()
    app.mainloop()
