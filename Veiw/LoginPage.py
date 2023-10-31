import customtkinter as tk

import LoginModel as md
import dbContext as db
class LoginPage(tk.CTk):

    email = str
    password = str
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Login Page")
        self.geometry("300x300")
        self.create_widgets()
        
    def create_widgets(self):
        # Create labels
        self.label_username = tk.CTkLabel(self, text="Email:")
        self.label_password = tk.CTkLabel(self, text="Password:")

        # Create entry widgets for username and password
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.entry_username = tk.CTkEntry(self, textvariable=self.email)
        self.entry_password = tk.CTkEntry(self, textvariable= self.password )  # Show * for password
        
        # Create login button
        self.button_login = tk.CTkButton(self, text="Login", command=self.on_login)

        # Arrange widgets using grid
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, columnspan=2, pady=20)

    def on_login(self):
        login = md.Login()
        login.setEmail(self.email.get())
        login.setPassword(self.password.get())
        user = db.database()
        user.Login(login)
if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
