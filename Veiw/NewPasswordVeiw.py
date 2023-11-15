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

        self.create_password_entry = tk.Entry(self, show="*")  # Entry widget with '*' to hide the password
        self.create_password_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label and Entry for Re-type New Password
        self.retype_password_label = tk.Label(self, text="Re-type New Password:")
        self.retype_password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.retype_password_entry = tk.Entry(self, show="*")
        self.retype_password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Submit Button
        self.submit_button = tk.Button(self, text="Create Password", command=self.create_password)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def create_password(self):
        new_password = self.create_password_entry.get()
        retype_password = self.retype_password_entry.get()

        # Here, you can implement your password creation logic.
        # For simplicity, let's just check if the passwords match.
        if new_password == retype_password:
            messagebox.showinfo("Password Created", "Password creation successful!")
            self.destroy()
            LoginVeiw.LoginPage()
        else:
            messagebox.showerror("Password Error", "Passwords do not match. Please try again.")

if __name__ == "__main__":

    app = PasswordCreation()
    app.mainloop()
