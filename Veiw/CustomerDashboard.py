import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from PIL import Image
from tkinter import ttk
from time import strftime
from tkcalendar import DateEntry
from Model import BookingModel
from Controller import CustomerController
from tkinter import messagebox
import customtkinter as Ct
import tkinter as tkk
import tkintermapview
import GobalVariable


class Dashboard():
    def __init__(self,master):
        self.master = master
        self.master.title('Customer Dashboard')
        Ct.set_default_color_theme("green") 
        self.master.attributes('-topmost',True)
        self.company=Ct.CTkLabel(self.master,text="Whoami.com",font=Ct.CTkFont(family="Times",size=25, weight='bold'))
        self.company.place(x=150,y=25)
        self.cmpic = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\Green White Simple Open Registration Facebook Post (3).png'), size=(100,100))
        self.cmimg = Ct.CTkLabel(self.master,image=self.cmpic, text="").place(x=50,y=-5)

        self.welcome=Ct.CTkLabel(self.master,text="Welcome Back,",font=Ct.CTkFont(family="Times",size=30, weight='bold'),text_color='#00BF63')
        self.welcome.place(x=400,y=25)
        self.user=Ct.CTkLabel(self.master,text="",font=Ct.CTkFont(family="Times",size=30, weight='bold'),text_color='#00BF63')
        self.user.place(x=610,y=25)
        self.user.configure(text=GobalVariable.Customer[1])

        self.lbl = Ct.CTkLabel(self.master,font=Ct.CTkFont(family="Times",size=30, weight='bold'))
        self.lbl.place(x=1200,y=25)
        
        self.time()

        self.options_frame = Ct.CTkFrame(self.master, fg_color='#00BF63',bg_color='#00BF63')

        self.profile = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\images-removebg-preview.png'), size=(150,150))
        self.img = Ct.CTkLabel(self.options_frame,image=self.profile, text="").place(x=50,y=0)

        self.name = Ct.CTkLabel(self.options_frame,text="", font=Ct.CTkFont(family='Times',size=30), text_color='white')
        self.name.place(x=50,y=120)
        self.name.configure(text=GobalVariable.Customer[1] + ' ' + GobalVariable.Customer[2])

        self.dash = Ct.CTkButton(self.options_frame,text="view Profile", fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False,command=lambda: self.indicate(self.proview, self.profile_page))
        self.dash.place(x=60,y=250)

        self.proview = Ct.CTkFrame(self.options_frame, fg_color='white',width=127,height=3)
        self.proview.place(x=68,y=285)

        self.book = Ct.CTkButton(self.options_frame, text='Book Now',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.book_indicate, self.book_page))
        self.book.place(x=50,y=325)

        self.book_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=110,height=3)
        self.book_indicate.place(x=65,y=360)

        self.view = Ct.CTkButton(self.options_frame, text='view Book',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.view_indicate,self.view_page))
        self.view.place(x=50, y=400)

        self.view_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=115,height=3)
        self.view_indicate.place(x=65,y=435)

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

        self.options_frame.place(x=40,y=70)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=250,height=750)

        self.main_frame = Ct.CTkFrame(self.master, width=1150, height=750)
        self.main_frame.configure(fg_color='white')
        self.profile_lbl=Ct.CTkLabel(self.main_frame,text="Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=50)
        self.copy(self.main_frame)
        self.update_btn = Ct.CTkButton(self.main_frame,text="Edit",command=self.dulicate,font= Ct.CTkFont(family="Times", size=30),width=200,fg_color='#00BF63')
        self.update_btn.place(x=850,y=700)
        self.main_frame.place(x=350,y=70)
        self.main_frame.pack_propagate(False)
        # self.main_frame.configure(height=750, width=1150)

    def profile_page(self):
        ''' The gui for the view profile frame, it shows the details of the customer who has login '''

        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.home_frame.configure(fg_color='white')
        Ct.set_default_color_theme("green") 
        self.profile_lbl=Ct.CTkLabel(self.home_frame,text="Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=50)
        self.copy(self.main_frame)
        self.update_btn = Ct.CTkButton(self.home_frame,text="Edit",command=self.dulicate,font= Ct.CTkFont(family="Times", size=30),width=200,fg_color='#00BF63')
        self.update_btn.place(x=850,y=700)
        self.home_frame.pack(side=Ct.LEFT)
        
        self.home_frame.pack(side=Ct.RIGHT)



    def book_page(self):
        self.book_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.booklb = Ct.CTkLabel(self.book_frame, text='Create Booking',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=400,y=50)
        self.book_frame.configure(fg_color= 'white')
        Ct.set_default_color_theme("green")

        map_widget = tkintermapview.TkinterMapView(self.book_frame, width=850, height=700, corner_radius=0)
        map_widget.set_address("kathmandu, nepal")
        map_widget.place(x=600,y=250)
        self.pick=Ct.CTkLabel(self.book_frame, text='Pick up Address:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.pick.place(x=50,y=200)
        self.pick_entry=Ct.CTkEntry(self.book_frame,width=200)
        self.pick_entry.place(x=230,y=200)

        self.drop=Ct.CTkLabel(self.book_frame, text='Drop off Address:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.drop.place(x=50,y=280)
        self.drop_entry=Ct.CTkEntry(self.book_frame,width=200)
        self.drop_entry.place(x=240,y=280)

        self.date=Ct.CTkLabel(self.book_frame, text='Book Date:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.date.place(x=50,y=360)
        self.date_entry=DateEntry(self.book_frame,width=40)
        self.date_entry.place(x=220,y=460)

        self.time_pick=Ct.CTkLabel(self.book_frame, text='Pickup Time',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.time_pick.place(x=50,y=440)

        self.custime = Ct.StringVar()

        self.time_pick_entry=Ct.CTkEntry(self.book_frame,width=200,textvariable=self.custime)
        self.time_pick_entry.place(x=210,y=440)

        
        self.time_entry=Ct.CTkButton(self.book_frame, text="get time",width=10,command=self.picktime)
        self.time_entry.place(x=420,y=440)

        self.book_frame.pack(side=Ct.LEFT)

        self.request = Ct.CTkButton(self.book_frame, text="Request Book",width=200,font=Ct.CTkFont(family="Times",size=25, weight='bold'),command=self.book_request)
        self.request.place(x=210,y= 520)

    def picktime(self):
        import tkinter as tk
        from tktimepicker import AnalogPicker, AnalogThemes

        self.root = tk.Tk()
        self.root.attributes('-topmost',True)
        self.time_picker = AnalogPicker(self.root)
        self.time_picker.pack(expand=True, fill="both")
        
        theme = AnalogThemes(self.time_picker)
        theme.setDracula()
        self.request = Ct.CTkButton(self.root, text="set",width=10,font=Ct.CTkFont(family="Times",size=20, weight='bold'),command=lambda: self.settime(self.time_picker.time()))
        self.request.place(x=250,y= 200)
        self.root.mainloop()
    
    def settime(self,time):
            self.custime.set("{}:{}:{}".format(*time))

            self.root.destroy()

    def view_page(self):
        self.view_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.view_frame.configure(fg_color= 'white')

        self.pick=Ct.CTkLabel(self.view_frame, text='Pick up Address:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.pick.place(x=50,y=50)
        self.pick_entry=Ct.CTkEntry(self.view_frame,width=200)
        self.pick_entry.place(x=230,y=50)

        self.drop=Ct.CTkLabel(self.view_frame, text='Drop off Address:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.drop.place(x=600,y=50)
        self.drop_entry=Ct.CTkEntry(self.view_frame,width=200)
        self.drop_entry.place(x=800,y=50)

        self.date=Ct.CTkLabel(self.view_frame, text='Book Date:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.date.place(x=50,y=120)
        self.date_entry=DateEntry(self.view_frame,width=20,height=50)
        self.date_entry.place(x=220,y=160)

        self.time_pick=Ct.CTkLabel(self.view_frame, text='Pickup Time:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.time_pick.place(x=600,y=120)

        self.custime = Ct.StringVar()

        self.time_pick_entry=Ct.CTkEntry(self.view_frame,width=200,textvariable=self.custime)
        self.time_pick_entry.place(x=800,y=120)
 
        
        self.time_entry=Ct.CTkButton(self.view_frame, text="clock",width=10,command=self.picktime)
        self.time_entry.place(x=1020,y=120)

        self.update=Ct.CTkButton(self.view_frame, text="Update",width=200,font=Ct.CTkFont(family="Times",size=25, weight='bold'))
        self.update.place(x=300,y=180)

        self.cancel_btn=Ct.CTkButton(self.view_frame, text="Cancel",width=200,font=Ct.CTkFont(family="Times",size=25, weight='bold'))
        self.cancel_btn.place(x=550,y=180)

        self.view_frame.pack(side=Ct.LEFT)

        # Create the Treeview
        column = ("Booking_id", "Pickup Address", "Drop-off Address","date_of_booking","Booking status")
        self.view_booking = ttk.Treeview(self.view_frame, columns=column, show="headings", height=30)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=250)

        self.view_booking.place(x=100,y=300)
        self.view_frame.pack()

    def history_page(self):
        self.history_frame = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.history_frame.configure(fg_color= 'white')
        # Create the Treeview
        self.booklb = Ct.CTkLabel(self.history_frame, text='Booking History',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=400,y=50)
        column = ("Booking_id", "Pickup Address", "Drop-off Address","date_of_booking","Booking status")
        self.view_booking = ttk.Treeview(self.history_frame, columns=column, show="headings", height=30)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=260)

        self.view_booking.place(x=50,y=200)
        self.history_frame.pack()

    def change_page(self):
        self.change_frame = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.change_frame.configure(fg_color= 'white')

        self.cmpic = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\Screenshot 2023-12-30 153422.png'), size=(600,500))
        self.booklb = Ct.CTkLabel(self.change_frame, text='Password Change',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=400,y=50)
        self.cmimg = Ct.CTkLabel(self.change_frame,image=self.cmpic, text="").place(x=50,y=100)
        self.new_pass=Ct.CTkLabel(self.change_frame, text='Current Password:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.new_pass.place(x=700,y=150)
        self.new_pass_entry=Ct.CTkEntry(self.change_frame,height=30,width=200)
        self.new_pass_entry.place(x=700,y=200)

        self.password=Ct.CTkLabel(self.change_frame, text='New Password:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.password.place(x=700,y=250) # Place password
        self.pass_entry=Ct.CTkEntry(self.change_frame,height=30,width=200)
        self.pass_entry.place(x=700,y=300)
        
        self.password2=Ct.CTkLabel(self.change_frame, text="Conform Password:",font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.password2.place(x=700,y=350)
        self.pass_entry2=Ct.CTkEntry(self.change_frame,height=30,width=200)
        self.pass_entry2.place(x=700,y=400)

        self.con_button=Ct.CTkButton(self.change_frame,text="Change",font=Ct.CTkFont(family="Times",size=25, weight='bold'),width=200)
        self.con_button.place(x=700,y=450)


        
        self.change_frame.pack()

    def delete_page(self):
        self.delete_fram = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.delete_fram.configure(fg_color= 'white')
        self.booklb = Ct.CTkLabel(self.delete_fram, text='Delete Your Account',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=350,y=100)
        self.booklb = Ct.CTkLabel(self.delete_fram, text='''
                    Are You sure you want to delete your Whoami Account? 
                            
                if you're having problems, please contact us we can help you.
        
            Deleting your account will remove all of your information from our database. 
            This cannot be undone.''',font=Ct.CTkFont(family="Times",size=30))
        self.booklb.place(x=0,y=150)

        
        self.con_button=Ct.CTkButton(self.delete_fram,text="Delete Account",font=Ct.CTkFont(family="Times",size=30, weight='bold'),width=300)
        self.con_button.place(x=420,y=450)


        
        self.delete_fram.pack()
    

    def delete_frame(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def remove(self):
        self.proview.configure(fg_color='#00BF63')
        self.view_indicate.configure(fg_color='#00BF63')
        self.book_indicate.configure(fg_color='#00BF63')
        self.change_indicate.configure(fg_color='#00BF63')
        self.delete_indicate.configure(fg_color='#00BF63')
        self.history_indicate.configure(fg_color='#00BF63')

    def indicate(self,lb, page):
        self.remove()
        lb.configure(fg_color='white')
        self.delete_frame()
        page()

    def dulicate(self):
        self.delete_frame()
        self.update_page()

    def copy(self,frame):
        
        self.view_first = Ct.CTkLabel(frame,text="First Name:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_first.place(x=50,y=200)

        self.view_firstname = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_firstname.place(x=200,y=200)
        self.view_firstname.configure(text=GobalVariable.Customer[1])

        self.view_last = Ct.CTkLabel(frame,text="Last Name:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_last.place(x=450,y=200)

        self.view_lastname = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_lastname.place(x=600,y=200)
        self.view_lastname.configure(text=GobalVariable.Customer[2])

        self.view_gender = Ct.CTkLabel(frame,text="Gender:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_gender.place(x=850,y=200)

        self.view_genderdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_genderdata.place(x=950,y=200)
        self.view_genderdata.configure(text=GobalVariable.Customer[5])

        self.view_Dob = Ct.CTkLabel(frame,text="Date of Birth:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_Dob.place(x=50,y=400)

        self.view_dobdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_dobdata.place(x=230,y=400)
        self.view_dobdata.configure(text=GobalVariable.Customer[4])

        self.number = Ct.CTkLabel(frame,text="Phone Number:",font=Ct.CTkFont(family="Times",size=30,))
        self.number.place(x=450,y=400)

        self.view_numberdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_numberdata.place(x=650,y=400)
        self.view_numberdata.configure(text=GobalVariable.Customer[6])

        self.view_add = Ct.CTkLabel(frame,text="Address:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_add.place(x=840,y=400)

        self.view_adddata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_adddata.place(x=950,y=400)
        self.view_adddata.configure(text=GobalVariable.Customer[7])

        self.view_pay = Ct.CTkLabel(frame,text="Payment Method:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_pay.place(x=50,y=600)
        

        self.view_paydata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_paydata.place(x=280,y=600)
        self.view_paydata.configure(text=GobalVariable.Customer[8])

        self.view_gmail = Ct.CTkLabel(frame,text="Email:",font=Ct.CTkFont(family="Times",size=30,))
        self.view_gmail.place(x=500,y=600)

        self.view_gmaildata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
        self.view_gmaildata.place(x=600,y=600)
        self.view_gmaildata.configure(text=GobalVariable.Customer[3])

    def update_profile(self):
        pass

    def update_page(self):
        self.update_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)

        self.update_frame.configure(fg_color= 'white')
        Ct.set_default_color_theme("green")  

        self.profile_lbl=Ct.CTkLabel(self.update_frame,text="Edit Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=50)

        self.update_first = Ct.CTkLabel(self.update_frame,text="First Name:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_first.place(x=50,y=200)

        self.update_firstname = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_firstname.place(x=200,y=200)

        self.update_last = Ct.CTkLabel(self.update_frame,text="Last Name:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_last.place(x=450,y=200)

        self.update_lastname = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_lastname.place(x=600,y=200)

        self.update_gender = Ct.CTkLabel(self.update_frame,text="Gender:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_gender.place(x=850,y=200)

        self.update_genderdata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_genderdata.place(x=950,y=200)

        self.update_Dob = Ct.CTkLabel(self.update_frame,text="Date of Birth:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_Dob.place(x=50,y=400)

        self.update_dobdata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_dobdata.place(x=230,y=400)

        self.update_phone = Ct.CTkLabel(self.update_frame,text="Phone Number:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_phone.place(x=450,y=400)

        self.update_phonedata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_phonedata.place(x=650,y=400)

        self.update_add = Ct.CTkLabel(self.update_frame,text="Address:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_add.place(x=840,y=400)

        self.update_adddata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_adddata.place(x=950,y=400)

        self.update_pay = Ct.CTkLabel(self.update_frame,text="Payment Method:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_pay.place(x=50,y=600)

        self.update_paydata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180)
        self.update_paydata.place(x=280,y=600)

        self.update_mail = Ct.CTkLabel(self.update_frame,text="Email:",font=Ct.CTkFont(family="Times",size=30,))
        self.update_mail.place(x=480,y=600)

        self.update_maildata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=250)
        self.update_maildata.place(x=580,y=600)

        self.update_btn = Ct.CTkButton(self.main_frame,text="save",command=self.dulicate,font= Ct.CTkFont(family="Times", size=30),width=100,fg_color='#00BF63')
        self.update_btn.place(x=850,y=700)

        self.update_btn = Ct.CTkButton(self.main_frame,text="back",command=self.back,font= Ct.CTkFont(family="Times", size=30),width=100,fg_color='#00BF63')
        self.update_btn.place(x=1000,y=700)

        self.update_frame.pack(side=Ct.RIGHT)
        self.update_frame.pack_propagate(False)
    
    def back(self):
        self.delete_frame()
        self.profile_page()

    def time(self):
        self.string = strftime('%H:%M:%S %p')
        self.lbl.configure(text=self.string)
        self.lbl.after(1000, self.time)

    def book_request(self):
        try:
            self.id = 0
            
            self.Cusid = GobalVariable.Customer[0]
            book = BookingModel.Booking(self.id,self.pick_entry.get(),self.drop_entry.get(),self.date_entry.get_date(),self.custime.get(),self.Cusid)
            request = CustomerController.CustomerDatabase()
            result = request._CustomerBook(book)

            if result:

                messagebox.showinfo("Booking", "Your Book has been requested",parent=self.master)
                self.pick_entry.delete(0,'end')
                self.drop_entry.delete(0,'end')
                self.time_pick_entry.delete(0,'end')
            else:
                messagebox.showerror("Booking", "Something Error",parent=self.master)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    apps = Ct.CTk()
    apps.after(0,lambda:apps.state('zoomed'))
    Dashboard(apps)
    apps.mainloop()