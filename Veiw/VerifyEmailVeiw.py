import tkinter as tk
from tkinter import messagebox
import NewPasswordVeiw
class VerifyEmail(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Password Creation")
        self.geometry('300x300')
        # Label and Entry for Create New Password

        self.topic = tk.Label(master,text='At first you should verify your email')
        self.topic.place(x=50, y=20)
        self.create_password_label = tk.Label(master,
        text="verify email address:")
        self.create_password_label.place(x=70, y=50)

        self.create_password_entry = tk.Entry(master)  # Entry widget with '*' to hide the password
        self.create_password_entry.place()

        # Submit Button
        self.submit_button = tk.Button(master, text="Create Password", command=self.create_password)
        self.submit_button.place()

    def create_password(self):
        new_password = self.create_password_entry.get()
        

        # Here, you can implement your password creation logic.
        # For simplicity, let's just check if the passwords match.
        if new_password == 'stharabi@gmail.com':
            messagebox.showinfo("verify", "email has been verify successful!")
            self.destroy()
            NewPasswordVeiw.PasswordCreation()
        else:
            messagebox.showerror("Error", "Email do not match. Please try again.")

if __name__ == "__main__":
    app = VerifyEmail()
    app.mainloop()
