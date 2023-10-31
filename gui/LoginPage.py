import customtkinter as tk
# from controller import dbContext as db
# from model import LoginModel as md
# import TAXIBOOKINGSYSTEM.model
from ..model import LoginModel
# from ..model.LoginModel import Login as md
class LoginPage(tk.CTk):
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
        self.entry_username = tk.CTkEntry(self)
        self.entry_password = tk.CTkEntry(self, show="*")  # Show * for password
        
        # Create login button
        self.button_login = tk.CTkButton(self, text="Login", command=self.on_login)

        # Arrange widgets using grid
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, columnspan=2, pady=20)

    def on_login(self):
        pass
        # login = md()
        # login.setEmail(self.entry_username)
        # login.setPassword(self.entry_password)
        # user = db.database()
        # user.Login(login)
if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
