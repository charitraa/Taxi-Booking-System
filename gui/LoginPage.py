import customtkinter as tk
from tkinter import messagebox


class LoginPage(tk.CTk):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Login Page")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        # Create labels
        label_username = tk.CTkLabel(self, text="Username:")
        label_password = tk.CTkLabel(self, text="Password:")

        # Create entry widgets for username and password
        entry_username = tk.CTkEntry(self)
        entry_password = tk.CTkEntry(self, show="*")  # Show * for password

        # Create login button
        button_login = tk.CTkButton(self, text="Login", command=self.on_login)

        # Arrange widgets using grid
        label_username.grid(row=0, column=0, padx=10, pady=10)
        entry_username.grid(row=0, column=1, padx=10, pady=10)
        label_password.grid(row=1, column=0, padx=10, pady=10)
        entry_password.grid(row=1, column=1, padx=10, pady=10)
        button_login.grid(row=2, columnspan=2, pady=20)

    def on_login(self):
        messagebox.showinfo("showinfo", "Login Successfully")


if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
