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

        self.profile = Ct.CTkImage(Image.open('image\\images-removebg-preview.png'), size=(150,150))
        self.img = Ct.CTkLabel(self.options_frame,image=self.profile, text="").place(x=50,y=0)

        self.name = Ct.CTkLabel(self.options_frame,text="Charitra Shrestha", font=Ct.CTkFont(family='Times',size=30), text_color='white')
        self.name.place(x=20,y=120)

        self.dash = Ct.CTkButton(self.options_frame,text="Veiw Profile", fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False,command=lambda: self.indicate(self.proveiw, self.profile_page))
        self.dash.place(x=60,y=250)

        self.proveiw = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=127,height=3)
        self.proveiw.place(x=68,y=285)

        self.book = Ct.CTkButton(self.options_frame, text='Book Now',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.book_indicate, self.book_page))
        self.book.place(x=50,y=325)

        self.book_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=110,height=3)
        self.book_indicate.place(x=65,y=360)

        self.veiw = Ct.CTkButton(self.options_frame, text='Veiw Book',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.veiw_indicate,self.veiw_page))
        self.veiw.place(x=50, y=400)

        self.veiw_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=115,height=3)
        self.veiw_indicate.place(x=65,y=435)

        self.history = Ct.CTkButton(self.options_frame, text='History',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.history_indicate,self.history_page))
        self.history.place(x=50, y=475)

        self.history_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=80,height=3)
        self.history_indicate.place(x=80,y=510)

        self.change_password = Ct.CTkButton(self.options_frame, text='Change Password',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.change_indicate,self.change_page))
        self.change_password.place(x=30, y=550)

        self.change_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=190,height=3)
        self.change_indicate.place(x=35,y=590)

        self.delete = Ct.CTkButton(self.options_frame, text='Delete Account',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.delete_indicate,self.delete_page))
        self.delete.place(x=40, y=625)

        self.delete_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=170,height=3)
        self.delete_indicate.place(x=40,y=660)

        self.options_frame.pack(side=Ct.LEFT,padx=30)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=250,height=750)

        self.main_frame = Ct.CTkFrame(self.master, width=1150, height=750)
        # self.lb = Ct.CTkLabel(self.main_frame, text='home page\n\nPage: 1')
        # self.lb.pack()
        # self.test = Ct.CTkLabel(self.main_frame,text="200")
        # self.test.pack()
        self.main_frame.pack(side=Ct.LEFT,padx=30)
        self.main_frame.pack_propagate(False)
        # self.main_frame.configure(height=750, width=1150)

    def profile_page(self):
        ''' The gui for the veiw profile frame, it shows the details of the customer whio has login '''
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        # self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 1')
        # self.lb.place(x=500,y=500)
        # self.test = Ct.CTkLabel(self.home_frame,text="200")
        # self.test.place(x=800,y=500)
        self.home_frame.pack(side=Ct.LEFT)
    def book_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 2')
        self.lb.pack()
        self.home_frame.pack(side=Ct.LEFT)

    def veiw_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 3')
        self.lb.pack()
        self.home_frame.pack(pady=20)

    def history_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 3')
        self.lb.pack()
        self.home_frame.pack(pady=20)

    def change_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 3')
        self.lb.pack()
        self.home_frame.pack(pady=20)

    def delete_page(self):
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.lb = Ct.CTkLabel(self.home_frame, text='home page\n\nPage: 3')
        self.lb.pack()
        self.home_frame.pack(pady=20)
    

    def delete_frame(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def remove(self):
        self.proveiw.configure(fg_color='#00BF63')
        self.veiw_indicate.configure(fg_color='#00BF63')
        self.book_indicate.configure(fg_color='#00BF63')
        self.change_indicate.configure(fg_color='#00BF63')
        self.delete_indicate.configure(fg_color='#00BF63')
        self.history_indicate.configure(fg_color='#00BF63')

    def indicate(self,lb, page):
        self.remove()
        lb.configure(fg_color='white')
        self.delete_frame()
        page()


if __name__ == '__main__':
    app = Ct.CTk()
    Dashboard(app)
    app.after(0,lambda:app.state('zoomed'))
    app.mainloop()