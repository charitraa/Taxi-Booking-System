import tkinter as tk
import CusRegistrationVeiw , DriverRegistrationVeiw
class OptionPage(tk.Tk):

    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.title('Option Page')
        self.geometry("500x300")
        self.create_widgets()
        
    def create_widgets(self):
        # Create labels
        self.label_username = tk.Label(self, text="As a Customer")
        self.label_password = tk.Label(self, text="As a Driver:")

        
        # Create login button
        self.button_Customer = tk.Button(self, text="Customer", command=self.on_Customer)
        self.button_Driver = tk.Button(self, text='Driver', command=self.on_Driver)
        # Arrange widgets using grid
        self.label_username.place(x=110,y=50)
        self.label_password.place(x=310,y=50)
        self.button_Customer.place(x=110, y=100,width=75)
        self.button_Driver.place(x=300,y=100,width=75)

    def on_Customer(self):
        self.destroy()
        CusRegistrationVeiw.RegistrationPage()


    def on_Driver(self):
        self.destroy()
        DriverRegistrationVeiw.DriverRegistrationVeiw()

if __name__ == "__main__":
    app = OptionPage()
    app.mainloop()
