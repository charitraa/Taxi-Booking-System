import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from PIL import Image
import customtkinter as Ct
import tkinter as tk

class Dashboard():
    def __init__(self,master):
        self.master = master
        self.master.title('Customer Dashboard')
        
        self.options_frame = Ct.CTkFrame(self.master, fg_color='#00BF63',bg_color='#00BF63')

        self.profile = Ct.CTkImage(Image.open('image\\images-removebg-preview.png'), size=(200,200))
        self.img = Ct.CTkLabel(self.options_frame,image=self.profile, text="").place(x=25,y=0)

        self.name = Ct.CTkLabel(self.options_frame,text="Charitra", font=Ct.CTkFont(family='Times',size=30), text_color='white')
        self.name.place(x=70,y=180)

        self.dash = Ct.CTkButton(self.options_frame,text="Veiw Profile", fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False,command=lambda: self.indicate(self.proveiw, self.home_page))
        self.dash.place(x=60,y=250)

        self.proveiw = Ct.CTkFrame(self.options_frame, fg_color='white',width=127,height=3)
        self.proveiw.place(x=68,y=285)

        self.book = Ct.CTkButton(self.options_frame, text='Book Now',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.book_indicate, self.home_page))
        self.book.place(x=50,y=325)

        self.book_indicate = Ct.CTkFrame(self.options_frame, fg_color='white',width=110,height=3)
        self.book_indicate.place(x=65,y=360)

        self.veiw = Ct.CTkButton(self.options_frame, text='Veiw Book',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.menu_indicate,self.menu_page))
        self.veiw.place(x=50, y=400)

        self.menu_indicate = Ct.CTkLabel(self.options_frame, text='', bg_color='#c3c3c3')
        self.menu_indicate.place(x=3,y=300)

        self.history = Ct.CTkButton(self.options_frame, text='History',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.contact_indicate,self.about_page))
        self.history.place(x=50, y=475)

        self.contact_indicate = Ct.CTkLabel(self.options_frame, text='', bg_color='#c3c3c3')
        self.contact_indicate.place(x=3,y=400)

        self.change_password = Ct.CTkButton(self.options_frame, text='Change Password',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.about_indicate,self.about_page))
        self.change_password.place(x=30, y=550)

        self.about_indicate = Ct.CTkLabel(self.options_frame, text='', bg_color='#c3c3c3')
        self.about_indicate.place(x=3,y=200)

        self.delete = Ct.CTkButton(self.options_frame, text='Delete Account',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.about_indicate,self.about_page))
        self.delete.place(x=40, y=625)

        self.options_frame.pack(side=Ct.LEFT,padx=30)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=250,height=750)

        self.main_frame = Ct.CTkFrame(self.master, width=1150, height=750)
        # self.lb = Ct.CTkLabel(self.main_frame, text='home page\n\nPage: 1')
        # self.lb.pack()
        # self.test = Ct.CTkLabel(self.main_frame,text="200")
        # self.test.pack()
        self.main_frame.pack(side=Ct.LEFT)
        self.main_frame.pack_propagate(False)
        # self.main_frame.configure(height=750, width=1150)

    def home_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        # self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 1')
        # self.lb.place(x=500,y=500)
        # self.test = Ct.CTkLabel(self.home_frame,text="200")
        # self.test.place(x=800,y=500)
        self.home_frame.pack(side=Ct.LEFT)
    def about_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 2')
        self.lb.pack()
        self.home_frame.pack(pady=20)

    def menu_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 3')
        self.lb.pack()
        self.home_frame.pack(pady=20)

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def remove(self):
        self.home_indicate.configure(bg_color='#00BF63')
        self.menu_indicate.configure(bg_color='#00BF63')
        self.contact_indicate.configure(bg_color='#00BF63')
        self.about_indicate.configure(bg_color='#00BF63')

    def indicate(self,lb, page):
        self.remove()
        lb.configure(bg_color='white')
        self.delete_page()
        page()


if __name__ == '__main__':
    app = Ct.CTk()
    Dashboard(app)
    app.after(0,lambda:app.state('zoomed'))
    app.mainloop()