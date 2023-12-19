import tkinter as tk
import customtkinter as CT
import CusRegistrationVeiw , DriverRegistrationVeiw
class OptionPage():

    def __init__(self, root):
        self.root = root
        self.root.title('Option Page')
        self.root.geometry("500x300")
        self.create_widgets()
        
    def create_widgets(self):
        # Create CTklabels
        self.label_username = CT.CTkLabel(self.root, text="As a Customer")
        self.CTklabel_password = CT.CTkLabel(self.root, text="As a Driver:")

        
        # Create login CTkbutton
        self.button_Customer = CT.CTkButton(self.root, text="Customer", command=self.on_Customer)
        self.CTkbutton_Driver = CT.CTkButton(self.root, text='Driver', command=self.on_Driver)
        # Arrange widgets using grid
        self.label_username.place(x=110,y=50)
        self.CTklabel_password.place(x=310,y=50)
        self.button_Customer.place(x=110, y=100)
        self.CTkbutton_Driver.place(x=300,y=100)

    def on_Customer(self):
        self.root.destroy()
        CusRegistrationVeiw.RegistrationPage()


    def on_Driver(self):
        self.root.destroy()
        DriverRegistrationVeiw.DriverRegistrationVeiw()

if __name__ == "__main__":
    root = CT.CTk()
    app = OptionPage(root)
    root.mainloop()
