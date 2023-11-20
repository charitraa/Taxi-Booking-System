import tkinter as tk
from tkinter import messagebox
import NewPasswordVeiw
class VerifyEmail(tk.Tk):
    verifyemail = str
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Password Creation")
        self.geometry('300x300')
        # Label and Entry for Create New Password

        self.topic = tk.Label(master,text='At first you should verify your email')
        self.topic.place(x=50, y=20)
        self.emailaddress_label = tk.Label(master,
        text="email address:")
        self.emailaddress_label.place(x=70, y=50)

        self.emailaddress_entry = tk.Entry(master,textvariable=tk.StringVar())  # Entry widget with '*' to hide the password
        self.emailaddress_entry.place(x=70, y=75)

        # Submit Button
        self.submit_button = tk.Button(master, text="Create Password", command=self.emailaddress)
        self.submit_button.place(x=75, y=100)

    def emailaddress(self):
        verifyemail = self.emailaddress_entry.get()
        from Model.VerifyModel import Email
        verify = Email(_email=verifyemail)
        from Controller.CustomerController import CustomerDatabase
        emaill = CustomerDatabase()
        check = emaill._isValidEmail(verify)
        
        if check==True:
            messagebox.showinfo("verify", "email has been verify successful!")
            self.destroy()
            NewPasswordVeiw.PasswordCreation()
        else:
            messagebox.showerror("Error", "Email do not match. Please try again.")

if __name__ == "__main__":
    app = VerifyEmail()
    app.mainloop()
