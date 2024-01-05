import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from PIL import Image
import customtkinter as Ct
import tkinter as tkk
from tkinter import ttk
import tkintermapview
from time import strftime
from tkcalendar import DateEntry
from Controller.DataBaseConnection import Database
import GobalVariable
import LoginView
from tkinter import messagebox

class Dashboard():
    def __init__(self,master):
        self.master = master
        self.master.title('Driver Dashboard')
        Ct.set_default_color_theme("green") 
        self.master.attributes('-topmost',True)
        self.company=Ct.CTkLabel(self.master,text="Whoiam.com",font=Ct.CTkFont(family="Times",size=25, weight='bold'))
        self.company.place(x=150,y=25)
        self.connection = Database.Connect()
        self.cmpic = Ct.CTkImage(Image.open('D:\\Code\\Python\\python project\\TaxBookingSystem\\image\\Green White Simple Open Registration Facebook Post (3).png'), size=(100,100))
        self.cmimg = Ct.CTkLabel(self.master,image=self.cmpic, text="").place(x=50,y=-5)
        self.id = Ct.StringVar()
        book_id = Ct.CTkEntry(self.master,textvariable=self.id)
        book_id.place_forget()
        self.welcome=Ct.CTkLabel(self.master,text="Welcome Back,",font=Ct.CTkFont(family="Times",size=30, weight='bold'),text_color='#00BF63')
        self.welcome.place(x=400,y=25)
        self.user=Ct.CTkLabel(self.master,text="",font=Ct.CTkFont(family="Times",size=30, weight='bold'),text_color='#00BF63')
        self.user.place(x=610,y=25)
    
        self.user.configure(text=GobalVariable.Driver[1])
        self.lbl = Ct.CTkLabel(self.master,text="",font=Ct.CTkFont(family="Times",size=30, weight='bold'))
        self.lbl.place(x=1200,y=25)
        self.lbl2 = Ct.CTkButton(self.master,text="logout",font=Ct.CTkFont(family="Times",size=30, weight='bold'),command=self.logout)
        self.lbl2.place(x=1350,y=25)
        
        self.options_frame = Ct.CTkFrame(self.master, fg_color='#00BF63',bg_color='#00BF63')

        self.profile = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\images-removebg-preview.png'), size=(150,150))
        self.img = Ct.CTkLabel(self.options_frame,image=self.profile, text="").place(x=50,y=0)
        self.time()
        self.name = Ct.CTkLabel(self.options_frame,text="", font=Ct.CTkFont(family='Times',size=30), text_color='white')
        self.name.place(x=20,y=120)
        self.name.configure(text=GobalVariable.Driver[1])

        self.dash = Ct.CTkButton(self.options_frame,text="View Profile", fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False,command=lambda: self.indicate(self.proveiw, self.profile_page))
        self.dash.place(x=60,y=250)

        self.proveiw = Ct.CTkFrame(self.options_frame, fg_color='white',width=127,height=3)
        self.proveiw.place(x=68,y=285)

        self.veiw = Ct.CTkButton(self.options_frame, text='View Trip',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.veiw_indicate,self.veiw_page))
        self.veiw.place(x=50, y=330)

        self.veiw_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=115,height=3)
        self.veiw_indicate.place(x=65,y=370)

        self.history = Ct.CTkButton(self.options_frame, text='History',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.history_indicate,self.history_page))
        self.history.place(x=50, y=410)

        self.history_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=80,height=3)
        self.history_indicate.place(x=80,y=448)

        self.change_password = Ct.CTkButton(self.options_frame, text='Change Password',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.change_indicate,self.change_page))
        self.change_password.place(x=30, y=490)

        self.change_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=190,height=3)
        self.change_indicate.place(x=35,y=525)

        self.delete = Ct.CTkButton(self.options_frame, text='Delete Account',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.delete_indicate,self.delete_page))
        self.delete.place(x=40, y=570)

        self.delete_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=170,height=3)
        self.delete_indicate.place(x=40,y=600)

        self.options_frame.place(x=40,y=70)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=250,height=750)

        self.main_frame = Ct.CTkFrame(self.master, width=1150, height=750)
        self.main_frame.configure(fg_color='white')
        self.profile_lbl=Ct.CTkLabel(self.main_frame,text="Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=50)
        self.copy(self.main_frame)
        self.update_btn = Ct.CTkButton(self.main_frame,text="Edit",command=self.dulicate,font= Ct.CTkFont(family="Times", size=30),width=200,fg_color='#00BF63')
        self.update_btn.place(x=850,y=600)
        self.main_frame.place(x=350,y=70)
        self.main_frame.pack_propagate(False)
        # self.main_frame.configure(height=750, width=1150)

    def profile_page(self):
        ''' The gui for the veiw profile frame, it shows the details of the customer who has login '''

        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.home_frame.configure(fg_color='white')
        Ct.set_default_color_theme("green") 
        self.profile_lbl=Ct.CTkLabel(self.home_frame,text="Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=50)
        self.copy(self.main_frame)
        self.update_btn = Ct.CTkButton(self.home_frame,text="Edit",command=self.dulicate,font= Ct.CTkFont(family="Times", size=30),width=200,fg_color='#00BF63')
        self.update_btn.place(x=850,y=600)
        self.home_frame.pack(side=Ct.LEFT)
        
        self.home_frame.pack(side=Ct.RIGHT)


    def picktime(self):
        import tkinter as tk
        from tktimepicker import AnalogPicker

        self.root = tk.Tk()
        self.root.attributes('-topmost',True)
        self.time_picker = AnalogPicker(self.root)
        self.time_picker.pack(expand=True, fill="both")

        # theme = AnalogThemes(time_picker)
        # theme.setDracula()
        self.request = Ct.CTkButton(self.root, text="set",width=10,font=Ct.CTkFont(family="Times",size=20, weight='bold'),command=self.settime)
        self.request.place(x=250,y= 200)
        self.root.mainloop()
    
    def settime(self):
            time = self.time_picker.time()
            self.custime.set(time)
            self.root.destroy()

    def veiw_page(self):
        self.veiw_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.veiw_frame.configure(fg_color= 'white')
        self.profile_lbl=Ct.CTkLabel(self.veiw_frame,text="Veiw Pending Trip",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=30)
        self.click = Ct.CTkLabel(self.veiw_frame,text=
        ' To Confirm that you have completed the Trip . Please press the Buttton',font= Ct.CTkFont(family="Times", size=30))
        self.click.place(x=100,y=150)
        self.update=Ct.CTkButton(self.veiw_frame, text="Complete",width=20,command=self.make_complete)
        self.update.place(x=1020,y=150)
        self.veiw_frame.pack(side=Ct.LEFT)

        # Create the Treeview
        column = ("Booking_id", "Customer_Name","Mobile_no", "Pickup_Address", "Drop-off _Address","date_of_booking","Payment Method","Booking status")
        self.veiw_booking = ttk.Treeview(self.veiw_frame, columns=column, show="headings", height=30)
        self.veiw_booking.bind("<<TreeviewSelect>>",self.selectedRow)

        for col in column:
            self.veiw_booking.heading(col, text=col, anchor="center")
            self.veiw_booking.column(col, anchor="center", width=165)
            self.viewbooking()


        self.veiw_booking.place(x=70,y=250)
        self.veiw_frame.pack()

    def history_page(self):
        self.history_frame = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.history_frame.configure(fg_color= 'white')
        # Create the Treeview
        self.profile_lbl=Ct.CTkLabel(self.history_frame,text="Booking History",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.profile_lbl.place(x=400,y=30)
        column = ("Booking_id", "Customer_Name","Mobile_no", "Pickup_Address", "Drop-off _Address","date_of_booking","Payment Method","Booking status")

        self.veiw_booking = ttk.Treeview(self.history_frame, columns=column, show="headings", height=30)

        for col in column:
            self.veiw_booking.heading(col, text=col, anchor="center")
            self.veiw_booking.column(col, anchor="center", width=165)
            self.viewhistory()

        self.veiw_booking.place(x=50,y=200)
        self.history_frame.pack()

    def change_page(self):
        self.chan = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.chan.configure(fg_color= 'white')

        self.cmpic = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\Screenshot 2023-12-30 153422.png'), size=(600,500))
        self.booklb = Ct.CTkLabel(self.chan, text='Password change',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=400,y=50)
        self.cmimg = Ct.CTkLabel(self.chan,image=self.cmpic, text="").place(x=50,y=100)
        self.new_pass=Ct.CTkLabel(self.chan, text='Current Password:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.new_pass.place(x=700,y=150)
        self.new_pass_entry=Ct.CTkEntry(self.chan,height=30,width=200)
        self.new_pass_entry.place(x=700,y=200)

        self.password=Ct.CTkLabel(self.chan, text='New Password:',font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.password.place(x=700,y=250) # Place password
        self.pass_entry=Ct.CTkEntry(self.chan,height=30,width=200)
        self.pass_entry.place(x=700,y=300)
        
        self.password2=Ct.CTkLabel(self.chan, text="Conform Password:",font=Ct.CTkFont(family="Times",size=25, weight='bold'),text_color='black')
        self.password2.place(x=700,y=350)
        self.pass_entry2=Ct.CTkEntry(self.chan,height=30,width=200)
        self.pass_entry2.place(x=700,y=400)

        self.con_button=Ct.CTkButton(self.chan,text="change",font=Ct.CTkFont(family="Times",size=25, weight='bold'),width=200,command=self.change)
        self.con_button.place(x=700,y=450)
        self.chan.pack()


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
        self.proveiw.configure(fg_color='#00BF63')
        self.veiw_indicate.configure(fg_color='#00BF63')
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
        for i in self.driprofile:

            self.view_first = Ct.CTkLabel(frame,text="Full Name:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_first.place(x=50,y=200)

            self.view_firstname = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_firstname.place(x=200,y=200)
            self.view_firstname.configure(text=i[0])

            self.view_gender = Ct.CTkLabel(frame,text="Gender:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_gender.place(x=850,y=200)

            self.view_genderdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_genderdata.place(x=950,y=200)
            self.view_genderdata.configure(text=i[5])

            self.view_Dob = Ct.CTkLabel(frame,text="Date of Birth:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_Dob.place(x=50,y=400)

            self.view_dobdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_dobdata.place(x=230,y=400)
            self.view_dobdata.configure(text=i[4])

            self.number = Ct.CTkLabel(frame,text="Phone Number:",font=Ct.CTkFont(family="Times",size=30,))
            self.number.place(x=450,y=400)

            self.view_numberdata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_numberdata.place(x=650,y=400)
            self.view_numberdata.configure(text=i[1])

            self.view_add = Ct.CTkLabel(frame,text="Address:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_add.place(x=840,y=400)

            self.view_adddata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_adddata.place(x=950,y=400)
            self.view_adddata.configure(text=i[2])

            self.view_pay = Ct.CTkLabel(frame,text="Liscence No:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_pay.place(x=50,y=600)
            

            self.view_paydata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_paydata.place(x=280,y=600)
            self.view_paydata.configure(text=i[6])

            self.view_gmail = Ct.CTkLabel(frame,text="Email:",font=Ct.CTkFont(family="Times",size=30,))
            self.view_gmail.place(x=500,y=600)

            self.view_gmaildata = Ct.CTkLabel(frame,text="",font=Ct.CTkFont(family="Times",size=30,))
            self.view_gmaildata.place(x=600,y=600)
            self.view_gmaildata.configure(text=i[3])


    def update_page(self):
        self.update_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)

        self.update_frame.configure(fg_color= 'white')
        Ct.set_default_color_theme("green")  

        for i in self.driprofile:
            self.profile_lbl=Ct.CTkLabel(self.update_frame,text="Edit Your Profile",font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
            self.profile_lbl.place(x=400,y=50)

            self.update_first = Ct.CTkLabel(self.update_frame,text="Full Name:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_first.place(x=50,y=200)

            self.edit_first = Ct.StringVar()
            self.edit_first.set(i[0])
            self.update_firstname = Ct.CTkEntry(self.update_frame,textvariable=self.edit_first,font=Ct.CTkFont(family="Times",size=30,),width=180)
            self.update_firstname.place(x=200,y=200)

            self.update_gender = Ct.CTkLabel(self.update_frame,text="Gender:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_gender.place(x=800,y=200)

            self.edit_gender = Ct.StringVar()
            self.edit_gender.set(i[5])
            self.radio_btn =Ct.CTkRadioButton(self.update_frame, text="Male", variable=self.edit_gender, value="Male")
            self.radio_btn.place(x=950, y=200)
            self.radio_btn1 = Ct.CTkRadioButton(self.update_frame, text="Female", variable=self.edit_gender, value="Female")
            self.radio_btn1.place(x=1050, y=200)


            self.update_Dob = Ct.CTkLabel(self.update_frame,text="Date of Birth:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_Dob.place(x=50,y=400)

            self.edit_date = Ct.StringVar()
            self.edit_date.set(i[4])
            self.update_dobdata = DateEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),textvariable=self.edit_date,selectmode='day')
            self.update_dobdata.place(x=300,y=500)

            self.update_phone = Ct.CTkLabel(self.update_frame,text="Phone Number:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_phone.place(x=450,y=400)

            self.edit_phone = Ct.StringVar()
            self.edit_phone.set(i[1])

            self.update_phonedata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180,textvariable=self.edit_phone)
            self.update_phonedata.place(x=650,y=400)

            self.update_add = Ct.CTkLabel(self.update_frame,text="Address:",font=Ct.CTkFont(family="Times",size=30))
            self.update_add.place(x=840,y=400)

            self.edit_add = Ct.StringVar()
            self.edit_add.set(i[2])
            self.update_adddata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30,),width=180,textvariable=self.edit_add)
            self.update_adddata.place(x=950,y=400)

            self.update_pay = Ct.CTkLabel(self.update_frame,text="Liscence No:",font=Ct.CTkFont(family="Times",size=30,))
            self.update_pay.place(x=50,y=600)

            self.edit_pay = Ct.StringVar()
            self.edit_pay.set(i[6])
            self.update_paydata = Ct.CTkEntry(self.update_frame,font=Ct.CTkFont(family="Times",size=30),textvariable=self.edit_pay)
            self.update_paydata.place(x=280,y=600)

            self.update_mail = Ct.CTkLabel(self.update_frame,text="Email:",font=Ct.CTkFont(family="Times",size=30))
            self.update_mail.place(x=480,y=600)

            self.mail = Ct.StringVar()
            self.mail.set(i[3])

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

    def view_profile(self):
        self.cust_id=GobalVariable.Driver[0]
        try:
            cursor =self.connection.cursor()
            query = f'''SELECT `fullname`, `phonenumber`, `Address`, `email`, `DOB`, `gender`,`liscenceno` FROM `driver` WHERE driverid={self.cust_id} '''
            cursor.execute(query)
            self.driprofile = cursor.fetchall()

        except Exception as err:
            print(f"Error: {err}")

    def edit_profile(self):

        try:
            customerid = GobalVariable.Driver[0]
            cursor =self.connection.cursor()
            query = f"UPDATE `driver` SET `fullname`='{self.edit_first.get()}',`email`='{self.mail.get()}',`DOB`='{self.update_dobdata.get_date()}',`gender`='{self.edit_gender.get()}',`phonenumber`='{self.edit_phone.get()}',`Address`='{self.edit_add.get()}',`liscenceno`='{self.edit_pay.get()}' WHERE driverid={customerid}"
            cursor.execute(query)
            # Commit the transaction
            self.connection.commit()
            self.view_profile()
            messagebox.showinfo("Taxi", "Your profile has been Update",parent=self.master)
        except Exception as e:
            messagebox.showerror("Taxi", f"Update Failure: {e}",parent=self.master)

    def delete_acc(self):
        self.cust_id=GobalVariable.Driver[0]
        try:
            cursor =self.connection.cursor() 
            query = f"DELETE  FROM driver WHERE driverid={self.cust_id}"
            cursor.execute(query)


            self.connection.commit()
            value = messagebox.askyesno("Taxi","Do you want to delete your Account?",parent=self.master)
            if value:
                messagebox.showinfo("Taxi", "Your account has been deleted",parent=self.master)
                app = Ct.CTkToplevel()
                self.master.destroy()
                import LoginView
                LoginView.LoginPage(app)
                app.after(0,lambda:app.state('zoomed'))
                app.lift()
                app.mainloop()
                
                
        except Exception as err:
            messagebox.showerror("Taxi", f" Failure: {err}",parent=self.master)
    
    def change(self):

        old_password=GobalVariable.Driver[6]
        customer_id = GobalVariable.Driver[0]
        current_password=self.new_pass_entry.get()
        new_password = self.pass_entry.get()
        re_password = self.pass_entry2.get()
        try:
            if current_password!= old_password:
                messagebox.showerror("password","Please check the Old password")

            elif new_password ==re_password:
                cursor =self.connection.cursor() 
                query = f"UPDATE `driver` SET `password`='{new_password}' WHERE driverid = '{customer_id}'"
                cursor.execute(query)                
                self.connection.commit()
                messagebox.showinfo("Success", "your password has been changed successfully!",parent=self.master)

        
        except Exception as err:
            messagebox.showerror("Error", err)
    def viewbooking(self):
        try:
            driverid = GobalVariable.Driver[0]
            cursor =  self.connection.cursor()
            query = f'''SELECT booking.bookingid,customer.firstname,customer.phonenumber,booking.pickup_address,booking.dropoff_address,booking.date,customer.Payment_Method,booking.status
            FROM customer
            JOIN booking
            where booking.status="booked" and booking.driverid = "{driverid}" '''
            cursor.execute(query)
            rows = cursor.fetchmany(size=10)  # Adjust the size as needed

            for item in self.veiw_booking.get_children():
                self.veiw_booking.delete(item)

            for row in rows:
                self.veiw_booking.insert(parent='', index='end',values=(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

        except Exception as err:
            print(f"Error: {err}")
            messagebox.showerror("Taxi", f"Error fetching bookings: {err}",parent=self.master)
    

    def viewhistory(self):
        try:
            driverid = GobalVariable.Driver[0]
            cursor =  self.connection.cursor()
            query = f'''SELECT booking.bookingid,customer.firstname,customer.phonenumber,booking.pickup_address,booking.dropoff_address,booking.date,customer.Payment_Method,booking.status
            FROM customer
            JOIN booking
            where booking.status="completed" and booking.driverid = "{driverid}" '''
            cursor.execute(query)
            rows = cursor.fetchall()

            for item in self.veiw_booking.get_children():
                self.veiw_booking.delete(item)

            for row in rows:
                self.veiw_booking.insert(parent='', index='end',values=(row[0], row[1], row[2], row[3], row[4], row[5],row[6], row[7]))

        except Exception as err:
            print(f"Error: {err}")
            messagebox.showerror("Taxi", f"Error fetching bookings: {err}",parent=self.master)
    
    def make_complete(self):
        try:
            value = self.id.get()
            if value=='':
                messagebox.showinfo("Taxi", "please selected the row",parent=self.master)
            else:
                driverid = GobalVariable.Driver[0]
                cursor = self.connection.cursor()
                query = f"UPDATE booking SET `status`='completed' WHERE `bookingid`={self.id.get()}"
                query1 = f"UPDATE driver SET `status`='active' where `driverid`='{driverid}'"
                cursor.execute(query)
                cursor.execute(query1)
                # Commit the transaction
                self.connection.commit()
                self.viewbooking()

                messagebox.showinfo("Trip", "Your trip has been completed",parent=self.master)
        except Exception as err:

            messagebox.showerror("Trip", f"Failure: {err}",parent=self.master)

    def selectedRow(self,event):
        selected_item = self.veiw_booking.focus()
        values = self.veiw_booking.item(selected_item, "values")

        if values:
            self.id.set(values[0])

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