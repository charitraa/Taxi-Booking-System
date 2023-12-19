import customtkinter as CT

class ToplevelWindow(CT.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = CT.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)
        self.CTkLabel_username = CT.CTkLabel(self, text="Email:")
        self.CTkLabel_password = CT.CTkLabel(self, text="Password:")

        # Create CTkentry widgets for username and password
        
        # background_image = Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\Veiw\\1685725595.jpeg')
        # self.background_photo = ImageCT.PhotoImage(background_image)

        # self.img = CT.CTkLabel(image=self.background_photo).place(x=10,y=20)

        self.email = CT.StringVar()
        self.password = CT.StringVar()
        self.CTkentry_username = CT.CTkEntry(self, textvariable=self.email).pack()
        self.CTkentry_password = CT.CTkEntry(self, textvariable= self.password , show='*').pack()  # Show * for password
        
        # Create login button
        # self.button_login = CT.CTkButton(self, text="Login", command=self.on_login)
        # self.button_SignUp = CT.CTkButton(self, text="SignUp", command=self.on_SignUp)
        # self.button_Forget = CT.CTkButton(self, text="Forget Password", command=self.on_forget)
        # Arrange widgets using grid
        # self.CTkLabel_username.grid(row=0, column=0, padx=10, pady=10)
        # self.CTkentry_username.grid(row=0, column=1, padx=10, pady=10)
        # self.CTkLabel_password.grid(row=1, column=0, padx=10, pady=10)
        # self.CTkentry_password.grid(row=1, column=1, padx=10, pady=10)
        # self.button_login.place(x=110, y=100)
        # self.button_SignUp.place(x=110, y=150)
        # self.button_Forget.place(x=100, y=200)

