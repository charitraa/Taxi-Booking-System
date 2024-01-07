import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from PIL import Image
from tkinter import ttk
from time import strftime
from tkcalendar import DateEntry
from Controller import CustomerController
from Controller.DataBaseConnection import Database
from tkinter import messagebox
import LoginView
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
        self.company=Ct.CTkLabel(self.master,text="Whoiam.com",font=Ct.CTkFont(family="Times",size=25, weight='bold'))
        self.company.place(x=150,y=25)
        self.cmpic = Ct.CTkImage(Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\image\\Green White Simple Open Registration Facebook Post (3).png'), size=(100,100))
        self.cmimg = Ct.CTkLabel(self.master,image=self.cmpic, text="").place(x=50,y=-5)

        self.welcome=Ct.CTkLabel(self.master,text="Welcome Back,",font=Ct.CTkFont(family="Times",size=30, weight='bold'),text_color='#00BF63')
        self.welcome.place(x=400,y=25)
        self.user=Ct.CTkLabel(self.master,text="",font=Ct.CTkFont(family="Times",size=30, weight='bold'),text_color='#00BF63')
        self.user.place(x=610,y=25)
        self.user.configure(text=GobalVariable.Customer[1])

        self.lbl = Ct.CTkLabel(self.master,font=Ct.CTkFont(family="Times",size=30, weight='bold'))
        self.lbl.place(x=1200,y=25)
        self.lbl2 = Ct.CTkButton(self.master,text="logout",font=Ct.CTkFont(family="Times",size=30, weight='bold'),command=self.logout)
        self.lbl2.place(x=1350,y=25)
        self.time()
        self.connection = Database.Connect()
        self.options_frame = Ct.CTkFrame(self.master, fg_color='#00BF63',bg_color='#00BF63')

        self.profil = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\images-removebg-preview.png'), size=(150,150))
        self.img = Ct.CTkLabel(self.options_frame,image=self.profil, text="").place(x=50,y=0)

        self.name = Ct.CTkLabel(self.options_frame,text="", font=Ct.CTkFont(family='Times',size=30), text_color='white')
        self.name.place(x=50,y=120)
        self.name.configure(text=GobalVariable.Customer[1] + ' ' + GobalVariable.Customer[2])

        self.dash = Ct.CTkButton(self.options_frame,text="View Profile", fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False,command=lambda: self.indicate(self.proview, self.profile_page))
        self.dash.place(x=60,y=250)

        self.proview = Ct.CTkFrame(self.options_frame, fg_color='white',width=127,height=3)
        self.proview.place(x=68,y=285)

        self.book = Ct.CTkButton(self.options_frame, text='Book Now',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.book_indicate, self.book_page))
        self.book.place(x=50,y=325)

        self.book_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=110,height=3)
        self.book_indicate.place(x=65,y=360)

        self.view = Ct.CTkButton(self.options_frame, text='View Book',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.view_indicate,self.view_page))
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
            self.custime.set("{}:{} {}".format(*time))

            self.root.destroy()

    def view_page(self):
        self.view_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.view_frame.configure(fg_color= 'white')

        self.id = Ct.StringVar()
        self.Bookid = Ct.CTkEntry(self.view_frame)
        self.Bookid.place_forget()
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

        self.update=Ct.CTkButton(self.view_frame, text="Update",width=200,font=Ct.CTkFont(family="Times",size=25, weight='bold'),command=self.update_book)
        self.update.place(x=300,y=180)

        self.cancel_btn=Ct.CTkButton(self.view_frame, text="Cancel",width=200,font=Ct.CTkFont(family="Times",size=25, weight='bold'),command=self.cancel_book)
        self.cancel_btn.place(x=550,y=180)

        self.view_frame.pack(side=Ct.LEFT)

        # Create the Treeview
        column = ("Booking_id", "Pickup Address", "Drop-off Address","date_of_booking","time","Booking status")
        self.view_booking = ttk.Treeview(self.view_frame, columns=column, show="headings", height=30)
        self.view_booking.bind("<<TreeviewSelect>>", self.selectedRow)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=210)
            self.veiw_book()
        self.view_booking.place(x=100,y=300)
        self.view_frame.pack()

    def history_page(self):
        self.history_frame = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.history_frame.configure(fg_color= 'white')
        # Create the Treeview
        self.booklb = Ct.CTkLabel(self.history_frame, text='Booking History',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=400,y=50)
        column = ("id","Pickup Address", "Drop-off Address","date_of_booking","Booking status","Driver Name","Driverid","Phone_no","liscence no")
        self.history_booking = ttk.Treeview(self.history_frame, columns=column, show="headings", height=30)
        
        for col in column:
            self.history_booking.heading(col, text=col, anchor="center")
            self.history_booking.column(col, anchor="center", width=150)
            self.view_detail()
        self.history_booking.place(x=50,y=200)
        self.history_frame.pack()

    def change_page(self):
        self.change_frame = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.change_frame.configure(fg_color= 'white')

        self.cmpic = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\Screenshot 2023-12-30 153422.png'), size=(600,500))
        self.booklb = Ct.CTkLabel(self.change_frame, text='Change Password',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
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

        self.con_button=Ct.CTkButton(self.change_frame,text="Change",font=Ct.CTkFont(family="Times",size=25, weight='bold'),width=200,command=self.change)
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

        
        self.con_button=Ct.CTkButton(self.delete_fram,text="Delete Account",font=Ct.CTkFont(family="Times",size=30, weight='bold'),width=300,command=self.delete_acc)
        self.con_button.place(x=420,y=450,)


        
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
        self.view_profile()
        for i in self.profile:

            self.view_first = Ct.CTkLabel(frame,text="First Name:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_first.place(x=50,y=200)

            self.view_firstname = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_firstname.place(x=200,y=200)
            self.view_firstname.configure(text=i[0])

            self.view_last = Ct.CTkLabel(frame,text="Last Name:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_last.place(x=450,y=200)

            self.view_lastname = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_lastname.place(x=600,y=200)
            self.view_lastname.configure(text=i[1])

            self.view_gender = Ct.CTkLabel(frame,text="Gender:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_gender.place(x=850,y=200)

            self.view_genderdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_genderdata.place(x=950,y=200)
            self.view_genderdata.configure(text=i[4])

            self.view_Dob = Ct.CTkLabel(frame,text="Date of Birth:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_Dob.place(x=50,y=400)

            self.view_dobdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_dobdata.place(x=230,y=400)
            self.view_dobdata.configure(text=i[3])

            self.number = Ct.CTkLabel(frame,text="Phone Number:",font=Ct.CTkFont(family="Times",size=30,))
            self.number.place(x=450,y=400)

            self.view_numberdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_numberdata.place(x=650,y=400)
            self.view_numberdata.configure(text=i[5])

            self.view_add = Ct.CTkLabel(frame,text="Address:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_add.place(x=840,y=400)

            self.view_adddata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_adddata.place(x=950,y=400)
            self.view_adddata.configure(text=i[6])

            self.view_pay = Ct.CTkLabel(frame,text="Payment Method:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_pay.place(x=50,y=600)
            

            self.view_paydata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_paydata.place(x=280,y=600)
            self.view_paydata.configure(text=i[7])

            self.view_gmail = Ct.CTkLabel(frame,text="Email:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_gmail.place(x=500,y=600)

            self.view_gmaildata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_gmaildata.place(x=600,y=600)
            self.view_gmaildata.configure(text=i[2])

    def update_page(self):
        self.update_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)

        self.update_frame.configure(fg_color= 'white')
        Ct.set_default_color_theme("green") 

        for i in self.profile:
            self.profile_lbl=Ct.CTkLabel(self.update_frame,text="Edit Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
            self.profile_lbl.place(x=400,y=50)

            self.update_first = Ct.CTkLabel(self.update_frame,text="First Name:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_first.place(x=50,y=200)

            self.edit_first = Ct.StringVar()
            self.edit_first.set(i[0])
            self.update_firstname = Ct.CTkEntry(self.update_frame,textvariable=self.edit_first,font=Ct.CTkFont(family="Times",size=30,),width=180)
            self.update_firstname.place(x=200,y=200)

            self.edit_last = Ct.StringVar()
            self.edit_last.set(i[1])
            self.update_last = Ct.CTkLabel(self.update_frame,text="Last Name:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_last.place(x=450,y=200)

            self.update_lastname = Ct.CTkEntry(self.update_frame,textvariable=self.edit_last,font=Ct.CTkFont(family="Times",size=30,),width=180)
            self.update_lastname.place(x=600,y=200)

            self.update_gender = Ct.CTkLabel(self.update_frame,text="Gender:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_gender.place(x=800,y=200)

            self.edit_gender = Ct.StringVar()
            self.edit_gender.set(i[4])
            self.radio_btn =Ct.CTkRadioButton(self.update_frame, text="Male", variable=self.edit_gender, value="Male")
            self.radio_btn.place(x=950, y=200)
            self.radio_btn1 = Ct.CTkRadioButton(self.update_frame, text="Female", variable=self.edit_gender, value="Female")
            self.radio_btn1.place(x=1050, y=200)


            self.update_Dob = Ct.CTkLabel(self.update_frame,text="Date of Birth:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_Dob.place(x=50,y=400)

            self.edit_date = Ct.StringVar()
            self.edit_date.set(i[3])
            self.update_dobdata = DateEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),textvariable=self.edit_date,selectmode='day')
            self.update_dobdata.place(x=300,y=500)

            self.update_phone = Ct.CTkLabel(self.update_frame,text="Phone Number:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_phone.place(x=450,y=400)

            self.edit_phone = Ct.StringVar()
            self.edit_phone.set(i[5])

            self.update_phonedata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180,textvariable=self.edit_phone)
            self.update_phonedata.place(x=650,y=400)

            self.update_add = Ct.CTkLabel(self.update_frame,text="Address:",font=Ct.CTkFont(family="Times",size=30))
            self.update_add.place(x=840,y=400)

            self.edit_add = Ct.StringVar()
            self.edit_add.set(i[6])
            self.update_adddata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180,textvariable=self.edit_add)
            self.update_adddata.place(x=950,y=400)

            self.update_pay = Ct.CTkLabel(self.update_frame,text="Payment Method:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_pay.place(x=50,y=600)

            self.edit_pay = Ct.StringVar()
            self.edit_pay.set(i[7])
            self.update_paydata = Ct.CTkOptionMenu(self.update_frame,font=Ct.CTkFont(family="Times",size=30),variable=self.edit_pay, values=["Cash", "Banking", "Esewa"])
            self.update_paydata.place(x=280,y=600)

            self.update_mail = Ct.CTkLabel(self.update_frame,text="Email:",font=Ct.CTkFont(family="Times",size=30))
            self.update_mail.place(x=480,y=600)

            self.mail = Ct.StringVar()
            self.mail.set(i[2])

            self.update_maildata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=350,textvariable=self.mail)
            self.update_maildata.place(x=580,y=600)

            self.update_btn = Ct.CTkButton(self.main_frame,text="save",command=self.edit_profile,font= Ct.CTkFont(family="Times", size=30),width=100,fg_color='#00BF63')
            self.update_btn.place(x=850,y=700)

            self.update_btn = Ct.CTkButton(self.main_frame,text="back",command=self.back,font= Ct.CTkFont(family="Times", size=30),width=100,fg_color='#00BF63')
            self.update_btn.place(x=1000,y=700)

            self.update_frame.pack(side=Ct.RIGHT)
            self.update_frame.pack_propagate(False)
    
    def back(self):
        self.delete_frame()
        self.profile_page()

    def time(self):
        self.string = strftime('%I:%M:%p')
        self.lbl.configure(text=self.string)
        self.lbl.after(1000, self.time)

    def book_request(self):
        try:
            self.id = 0
            self.Cusid = GobalVariable.Customer[0]
            cursor = self.connection.cursor()
            query  = f"INSERT INTO `booking`(`bookingid`, `pickup_address`, `dropoff_address`, `date`, `time`, `status`, `customerid`) VALUES ('{self.id}','{self.pick_entry.get()}','{self.drop_entry.get()}','{self.date_entry.get_date()}','{self.custime.get()}','pending','{self.Cusid}')"
            cursor.execute(query)
            self.connection.commit()
            self.veiw_book()
            messagebox.showinfo("Booking", "Your Book has been requested",parent=self.master)
            self.pick_entry.delete(0,'end')
            self.drop_entry.delete(0,'end')
            self.time_pick_entry.delete(0,'end')
        except Exception as e:
            messagebox.showerror("Booking", "Something Error",parent=self.master)


    def edit_profile(self):

        try:
            customerid = GobalVariable.Customer[0]
            cursor =self.connection.cursor()
            query = f"UPDATE `customer` SET `firstname`='{self.edit_first.get()}',`lastname`='{self.edit_last.get()}',`email`='{self.mail.get()}',`DOB`='{self.update_dobdata.get_date()}',`Gender`='{self.edit_gender.get()}',`phonenumber`='{self.edit_phone.get()}',`address`='{self.edit_add.get()}',`Payment_Method`='{self.edit_pay.get()}' WHERE customerid={customerid}"
            cursor.execute(query)
            # Commit the transaction
            self.connection.commit()
            self.view_profile()
            messagebox.showinfo("Profile", "Profile has been updated",parent=self.master)
        except Exception as e:
            messagebox.showerror("Profile", f"Update Failure: {e}",parent=self.master)

    def veiw_book(self):
        self.cust_id=GobalVariable.Customer[0]
        try:
            cursor =self.connection.cursor()
            query = f"SELECT `bookingid`, `pickup_address`, `dropoff_address`, `date`, `time`, `status` FROM `booking` WHERE `customerid` ={self.cust_id} and `status` = 'pending' "
            cursor.execute(query)
            rows = cursor.fetchall()

            for item in self.view_booking.get_children():
                self.view_booking.delete(item)

            for row in rows:
                self.view_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5]))

        except Exception as err:
            print(f"Error: {err}")

    def selectedRow(self,event):
        selected_item = self.view_booking.focus()
        values = self.view_booking.item(selected_item, "values")

        if values:
            self.id.set(values[0])

            self.pick_entry.delete(0, "end")
            self.pick_entry.insert(0, values[1])

            self.drop_entry.delete(0, "end")
            self.drop_entry.insert(0, values[2])

            self.date_entry.delete(0, "end")
            self.date_entry.insert(0, values[3])

            self.custime.set(values[4])
    def update_book(self):
        try:
            cursor =self.connection.cursor() 
            query = f"UPDATE booking SET  `pickup_address`='{self.pick_entry.get()}', `dropoff_address`='{self.drop_entry.get()}', `date`='{self.date_entry.get_date()}',`time`='{self.custime.get()}' WHERE `bookingid`={self.id.get()}"

            cursor.execute(query)
            # Commit the transaction
            self.connection.commit()
            self.veiw_book()
            messagebox.showinfo("Booking", "Booking has been updated",parent=self.master)
        except Exception as err:
            messagebox.showerror("Booking", f"Update Failure: {err}",parent=self.master)

    def cancel_book(self):
        try:
            cursor =self.connection.cursor() 
            query = f"DELETE  FROM booking WHERE bookingid={self.id.get()}"
            cursor.execute(query)

            self.connection.commit()
            self.veiw_book()
            messagebox.showinfo("booking", "Your booking has been cancel",parent=self.master)
        except Exception as err:
            messagebox.showerror("booking", f" Failure: {err}",parent=self.master)

    def view_detail(self):
        self.cust_id=GobalVariable.Customer[0]
        try:
            cursor =self.connection.cursor()
            query = f'''SELECT customer.customerid,booking.pickup_address,booking.dropoff_address,booking.date,booking.status,driver.fullname,driver.driverid,driver.phonenumber,driver.liscenceno
            FROM customer
            JOIN booking
            ON customer.customerid =booking.customerid
            JOIN driver
            ON booking.driverid =driver.driverid
            where customer.customerid={self.cust_id}'''
            cursor.execute(query)
            rows = cursor.fetchall()

            for item in self.history_booking.get_children():
                self.history_booking.delete(item)

            for row in rows:
                self.history_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))

        except Exception as err:
            print(f"Error: {err}")
    
    def view_profile(self):
        self.cust_id=GobalVariable.Customer[0]
        try:
            cursor =self.connection.cursor()
            query = f'''SELECT `firstname`, `lastname`, `email`, `DOB`, `Gender`, `phonenumber`, `address`, `Payment_Method`FROM `customer` WHERE customerid={self.cust_id} '''
            cursor.execute(query)
            self.profile = cursor.fetchall()

        except Exception as err:
            print(f"Error: {err}")

    def delete_acc(self):
        self.cust_id=GobalVariable.Customer[0]
        try:
            cursor =self.connection.cursor()
            query1 = f"DELETE  FROM booking WHERE customerid={self.cust_id}"
            cursor.execute(query1)
            self.connection.commit()
            query = f"DELETE  FROM customer WHERE customerid={self.cust_id}"
            cursor.execute(query)
            self.connection.commit()
            value = messagebox.askyesno("Account","Do you want to delete your Account?",parent=self.master)
            if value:
                messagebox.showinfo("Account", "Your account has been deleted",parent=self.master)
                app = Ct.CTkToplevel()
                self.master.destroy()
                LoginView.LoginPage(app)
                app.after(0,lambda:app.state('zoomed'))
                app.lift()
                app.mainloop()
                
                
        except Exception as err:
            messagebox.showerror("Taxi", f" Failure: {err}",parent=self.master)

    def change(self):
                
            old_password=GobalVariable.Customer[9]
            customer_id = GobalVariable.Customer[0]

            current_password=self.new_pass_entry.get()
            new_password = self.pass_entry.get()
            re_password = self.pass_entry2.get()
            try:
                if current_password!= old_password:
                    messagebox.showerror("password","Please check the Old password")

                elif new_password ==re_password:
                    cursor =self.connection.cursor() 
                    query = f"UPDATE `customer` SET `password`='{new_password}' WHERE customerid = '{customer_id}'"
                    cursor.execute(query)       
                    self.connection.commit()
                    messagebox.showinfo("Success", "your password has been changed successfully!",parent=self.master)

            except Exception as err:
                messagebox.showerror("Error", err)
    def logout(self):
        self.master.destroy()
        app = Ct.CTkToplevel()
        app.after(0,lambda:app.state('zoomed'))
        LoginView.LoginPage(app)
        app.mainloop()

if __name__ == '__main__':
    apps = Ct.CTk()
    apps.after(0,lambda:apps.state('zoomed'))
    Dashboard(apps)
    apps.mainloop()