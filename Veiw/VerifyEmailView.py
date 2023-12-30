import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from tkinter import messagebox
from Model.VerifyModel import Email
from Controller.CustomerController import CustomerDatabase
import tkinter as tk
import GobalVariable
import customtkinter as CT
import Veiw.NewPasswordView as NewPasswordView

class VerifyEmail():
    verifyemail = str
    def __init__(self, master):
        
        self.master = master
        self.master.title("Forget Password")
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        width = 500
        height =300
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f"{width}x{height}+{x}+{y}")
        CT.set_default_color_theme("green")
        self.master.config(background="white")
        self.master.attributes('-topmost',True)
        # Label and Entry for Create New Password

        self.topic = CT.CTkLabel(self.master,text='Forget Password?',bg_color="white", font=CT.CTkFont(family='Times', size=30, weight="bold"))
        self.topic.place(x=150, y=20)

        self.worries = CT.CTkLabel(self.master,text="No worries, we'll rest your password please enter the email for verfication.",bg_color="white").place(x=50,y=60)
        
        self.emailaddress_label = CT.CTkLabel(self.master,
        text="Email Address:",bg_color="white")
        self.emailaddress_label.place(x=150, y=100)

        self.emailaddress_entry = CT.CTkEntry(self.master,textvariable=CT.StringVar(), width=200)  # Entry widget with '*' to hide the password
        self.emailaddress_entry.place(x=150, y=130)

        # Submit Button
        self.submit_button = CT.CTkButton(self.master, text="Reset Password", command=self.emailaddress, width=200)
        self.submit_button.place(x=150, y=170)
        self.back_btn = CT.CTkButton(self.master, text="<- Back to log in ",fg_color="white",text_color="black",bg_color="white",hover=False, command=self.back, width=200)
        self.back_btn.place(x=150, y=210)

    
    def emailaddress(self):
        verifyemail = self.emailaddress_entry.get()
        verify = Email(_email=verifyemail)
        emaill = CustomerDatabase()
        check = emaill._isValidEmail(verify)
        
        if check==True:
            GobalVariable.email = self.emailaddress_entry.get()
            messagebox.showinfo("verify", "email has been verify successful!",parent=self.master)
            self.master.destroy()
            reg = CT.CTkToplevel()
            NewPasswordView.PasswordCreation(reg)
            reg.mainloop()
            
        else:
            messagebox.showerror("Error", "Email do not match. Please try again.",parent=self.master)
    def back(self):
        self.master.destroy()

if __name__ == "__main__":
    app = CT.CTk()
    VerifyEmail(app)
    app.mainloop()
