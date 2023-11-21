import tkinter as tk
from tkinter import messagebox
import LoginVeiw
class PasswordCreation(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Password Creation")
        self.geometry('300x300')
        self.create_widget()
    def create_widget(self):
        # Label and Entry for Create New Password
        self.create_password_label = tk.Label(self, text="Create New Password:")
        self.create_password_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.create_password_entry = tk.Entry(self, show="*",textvariable=tk.StringVar())  # Entry widget with '*' to hide the password
        self.create_password_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label and Entry for Re-type New Password
        self.retype_password_label = tk.Label(self, text="Re-type New Password:")
        self.retype_password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.retype_password_entry = tk.Entry(self, show="*",textvariable=tk.StringVar())
        self.retype_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Submit Button
        self.submit_button = tk.Button(self, text="Create Password", command=self.create_password)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def create_password(self):
        new_password = self.create_password_entry.get()
        retype_password = self.retype_password_entry.get()

        if new_password == retype_password:
            try:
                from Model import LoginModel
                import GobalVariable
                gmail = GobalVariable.email
                send = LoginModel.Login(_email=gmail,_password=new_password)
                
                from Controller import CustomerController
                var = CustomerController.CustomerDatabase()
                var._ChangePassword(send)
                if var:
                    messagebox.showinfo("Password Created", "Your password has been changed")
                    self.destroy()
                    LoginVeiw.LoginPage()
                
            except Exception as e:
                print(e)

        else:
            messagebox.showerror("Password Error", "Passwords do not match. Please try again.")

if __name__ == "__main__":

    app = PasswordCreation()
    app.mainloop()
