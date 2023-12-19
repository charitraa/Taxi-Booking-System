import customtkinter

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        import Practise.ttkk as ttkk
        self.toplevel_window = ttkk.ToplevelWindow(self)  # create window if its None or destroyed


app = App()
app.mainloop()