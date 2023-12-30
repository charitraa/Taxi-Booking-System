import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Controller import CustomerController
from Model import LoginModel
from tkinter import messagebox
import customtkinter as CT
import GobalVariable
import tkinter as tk
import Veiw.LoginView as LoginView
class PasswordCreation():
    def __init__(self, master):
        self.master = master
        self.master.title("Password Change")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        width = 500
        height =350
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f"{width}x{height}+{x}+{y}")
        # self.master.geometry('500x350')
        CT.set_default_color_theme("green")
        self.master.attributes('-topmost',True)
        self.create_widget()
    def create_widget(self):
        # Label and Entry for Create New Password
        self.topic = CT.CTkLabel(self.master, text='Change Password',font=CT.CTkFont(family='Times', size=30, weight="bold")).place(x=150, y=30)

        self.requied = self.topic = CT.CTkLabel(self.master, text='''Password must contain one lowercase lettter, one number, 
        and be atleast 6 character long.''').place(x=100, y=70)
        self.create_password_label = CT.CTkLabel(self.master, text="Create New Password:")
        self.create_password_label.place(x=150,y=110)

        self.create_password_entry = CT.CTkEntry(self.master, show="*",textvariable=CT.StringVar(), width=200)  # Entry widget with '*' to hide the password
        self.create_password_entry.place(x=150,y=140)

        # Label and Entry for Re-type New Password
        self.retype_password_label = CT.CTkLabel(self.master, text="Re-type New Password:")
        self.retype_password_label.place(x=150, y=180)

        self.retype_password_entry = CT.CTkEntry(self.master, show="*",textvariable=CT.StringVar(), width=200)
        self.retype_password_entry.place(x=150, y=210)

        # Submit Button
        self.submit_button = CT.CTkButton(self.master, text="Submit", command=self.create_password, width=200)
        self.submit_button.place(x=150, y=260)

    def create_password(self):
        new_password = self.create_password_entry.get()
        retype_password = self.retype_password_entry.get()

        if new_password == retype_password:
            try:
                gmail = GobalVariable.email
                send = LoginModel.Login(_email=gmail,_password=new_password)
                
                var = CustomerController.CustomerDatabase()
                var._ChangePassword(send)
                if var:
                    messagebox.showinfo("Password Created", "Your password has been changed",parent=self.master)
                    self.master.destroy()
                    # LoginVeiw.LoginPage()
                
            except Exception as e:
                print(e)

        else:
            messagebox.showerror("Password Error", "Passwords do not match. Please try again.",parent=self.master)

if __name__ == "__main__":

    app = CT.CTk()
    PasswordCreation(app)
    app.mainloop()
