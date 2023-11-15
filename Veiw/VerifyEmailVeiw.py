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
        self.create_password_label = tk.Label(master, text="verify email address:")
        self.create_password_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.create_password_entry = tk.Entry(master)  # Entry widget with '*' to hide the password
        self.create_password_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Submit Button
        self.submit_button = tk.Button(master, text="Create Password", command=self.create_password)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

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
