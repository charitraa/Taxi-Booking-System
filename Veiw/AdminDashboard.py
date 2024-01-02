import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from PIL import Image
import customtkinter as Ct
import tkinter as tk
from tkinter import ttk 
from tkcalendar import DateEntry
from tkinter import messagebox
import GobalVariable
from Controller.DataBaseConnection import Database

class Dashboard():
    def __init__(self,master):
        self.master = master
        self.master.title('Customer Dashboard')
        self.connection = Database.Connect()
        Ct.set_default_color_theme("green")
        # self.master.configure(fg_color='white')
        self.options_frame = Ct.CTkFrame(self.master, fg_color='#00BF63',bg_color='#00BF63')

        self.profile = Ct.CTkImage(Image.open('image\\images-removebg-preview.png'), size=(150,150))
        self.img = Ct.CTkLabel(self.options_frame,image=self.profile, text="").place(x=50,y=0)

        self.name = Ct.CTkLabel(self.options_frame,text="Charitra Shrestha", font=Ct.CTkFont(family='Times',size=30), text_color='white')
        self.name.place(x=20,y=120)

        self.dash = Ct.CTkButton(self.options_frame,text="Assign Driver", fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False,command=lambda: self.indicate(self.proveiw, self.profile_page))
        self.dash.place(x=60,y=250)

        self.proveiw = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=127,height=3)
        self.proveiw.place(x=68,y=285)

        self.book = Ct.CTkButton(self.options_frame, text='Add Driver',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.book_indicate, self.driver_register))
        self.book.place(x=50,y=325)

        self.book_indicate = Ct.CTkFrame(self.options_frame, fg_color='#00BF63',width=110,height=3)
        self.book_indicate.place(x=65,y=360)

        self.veiw = Ct.CTkButton(self.options_frame, text='customer details',fg_color='#00BF63', border_width=0, bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'),text_color='white',hover=False, command=lambda: self.indicate(self.veiw_indicate,self.cust_details))
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
        self.main_frame.configure(fg_color='white')
        self.booking_id = Ct.CTkLabel(self.main_frame, text="Booking ID", fg_color='#00BF63', bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.booking_id.place(x=40,y=40)
        self.bookingid = Ct.StringVar()
        self.booking_id_entry = Ct.CTkEntry(self.main_frame,textvariable=self.bookingid)
        self.booking_id_entry.place(x=180, y=40)

        self.booking_status = Ct.CTkLabel(self.main_frame, text="Booking Status", fg_color='#00BF63', bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.booking_status.place(x=380,y=40)
        self.var1=Ct.StringVar()
        self.var1.set("Select payment method")

        self.status=tk.OptionMenu(self.main_frame,self.var1,"Booked", "Pending")
        self.status.place(x=690,y=50, width=200, height=40)

        self.driver=Ct.CTkLabel(self.main_frame, text="Driver ID", fg_color='#00BF63', bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.driver.place(x=810, y=40)
        self.var2=Ct.StringVar()
        self.var2.set("Select payment method")

        self.driver_option=tk.OptionMenu(self.main_frame,self.var2,"Booked", "Pending")
        self.driver_option.place(x=1160,y=50, width=200, height=40)

        self.assign=Ct.CTkButton(self.main_frame, text="Assign", fg_color='#00BF63', bg_color='#00BF63', font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.assign.place(x=450, y=150)

        column = ("Booking_id", "Customer_Name","Mobile_no", "Pickup_Address", "Drop-off _Address","date_of_booking","Payment Method","Booking status")
        self.view_booking = ttk.Treeview(self.main_frame, columns=column, show="headings", height=30)
        self.view_booking.bind("<<TreeviewSelect>>", self.selectedRow)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=165)
            self.veiw_customer()

        self.view_booking.place(x=60,y=300)


        self.main_frame.pack(side=Ct.LEFT,padx=30)
        self.main_frame.pack_propagate(False)
        # self.main_frame.configure(height=750, width=1150)

    def profile_page(self):
        ''' The gui for the veiw profile frame, it shows the details of the customer whio has login '''
        self.home_frame = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.home_frame.configure(fg_color='white')
        self.booking_id = Ct.CTkLabel(self.home_frame, text="Booking ID", fg_color='#00BF63', bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.booking_id.place(x=40,y=40)
        self.bookingid = Ct.StringVar()
        self.booking_id_entry = Ct.CTkEntry(self.home_frame,textvariable=self.bookingid)
        self.booking_id_entry.place(x=180, y=40)

        self.booking_status = Ct.CTkLabel(self.home_frame, text="Booking Status", fg_color='#00BF63', bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.booking_status.place(x=380,y=40)
        self.var1=Ct.StringVar()
        self.var1.set("Select payment method")

        self.status=tk.OptionMenu(self.home_frame,self.var1,"Booked", "Pending")
        self.status.place(x=690,y=50, width=200, height=40)

        self.driver=Ct.CTkLabel(self.home_frame, text="Driver ID", fg_color='#00BF63', bg_color='#00BF63',font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.driver.place(x=810, y=40)
        self.var2=Ct.StringVar()
        self.var2.set("Select payment method")

        self.driver_option=tk.OptionMenu(self.home_frame,self.var2,"Booked", "Pending")
        self.driver_option.place(x=1160,y=50, width=200, height=40)

        self.assign=Ct.CTkButton(self.home_frame, text="Assign", fg_color='#00BF63', bg_color='#00BF63', font=Ct.CTkFont(family='Times',size=25,weight='bold'))
        self.assign.place(x=450, y=150)

        column = ("Booking_id", "Customer_Name","Mobile_no", "Pickup_Address", "Drop-off _Address","date_of_booking","Payment Method","Booking status")
        self.view_booking = ttk.Treeview(self.home_frame, columns=column, show="headings", height=30)
        self.view_booking.bind("<<TreeviewSelect>>", self.selectedRow)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=165)
            self.veiw_customer()

        self.view_booking.place(x=60,y=300)
        self.home_frame.pack(side=Ct.LEFT)


    def driver_register(self):
        self.driver_reg = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.full_name_CTkLabel =Ct.CTkLabel(self.driver_reg, text="Full Name:",font=Ct.CTkFont(family="Times",size=20))
        self.driver_reg.configure(fg_color='white')
        self.full_name_CTkLabel.place(x=30,y=50)
        self.full_name_CTkentry =Ct.CTkEntry(self.driver_reg,textvariable=Ct.StringVar())
        self.full_name_CTkentry.place(x=140,y=50)

        self.address_CTkLabel =Ct.CTkLabel(self.driver_reg, text="Address:",font=Ct.CTkFont(family="Times",size=20))
        self.address_CTkLabel.place(x=400,y=50)
        self.address_CTkentry =Ct.CTkEntry(self.driver_reg,textvariable=Ct.StringVar())
        self.address_CTkentry.place(x=490,y=50)
        
        self.date_CTklabel =Ct.CTkLabel(self.driver_reg,text = 'DOB:',font=Ct.CTkFont(family="Times",size=20))
        self.date_CTklabel.place(x=750,y=50)
        self.date_CTkEntry = DateEntry(self.driver_reg,width=30,selectmode='day')
        self.date_CTkEntry.place(x=1020,y=70)

        self.email_CTkLabel =Ct.CTkLabel(self.driver_reg, text="Email:",font=Ct.CTkFont(family="Times",size=20))
        self.email_CTkLabel.place(x=30,y=150)
        self.email_CTkentry =Ct.CTkEntry(self.driver_reg,textvariable=Ct.StringVar())
        self.email_CTkentry.place(x=140,y=150)

        self.pass_CTkLabel =Ct.CTkLabel(self.driver_reg, text="Password:",font=Ct.CTkFont(family="Times",size=20))
        self.pass_CTkLabel.place(x=400,y=150)
        self.pass_CTkentry =Ct.CTkEntry(self.driver_reg,textvariable=Ct.StringVar())
        self.pass_CTkentry.place(x=490,y=150)

        self.phone_CTkLabel =Ct.CTkLabel(self.driver_reg, text="Phone Number:",font=Ct.CTkFont(family="Times",size=20))
        self.phone_CTkLabel.place(x=750,y=150)
        self.phone_CTkentry =Ct.CTkEntry(self.driver_reg,textvariable=Ct.StringVar())
        self.phone_CTkentry.place(x=890,y=150)

        self.gender_CTkLabel =Ct.CTkLabel(self.driver_reg, text="Gender:",font=Ct.CTkFont(family="Times",size=20))
        self.gender_CTkLabel.place(x=30,y=250)
        self.var_gender =Ct.StringVar()
        self.radio_btn =Ct.CTkRadioButton(self.driver_reg, text="Male", variable=self.var_gender, value="Male")
        self.radio_btn.place(x=120, y=250)
        self.radio_btn1 =Ct.CTkRadioButton(self.driver_reg, text="Female", variable=self.var_gender, value="Female")
        self.radio_btn1.place(x=180, y=250)

        self.license=Ct.CTkLabel(self.driver_reg,text='License No:',font=Ct.CTkFont(family="Times",size=20))
        self.license.place(x=400,y=250)
        self.license=Ct.CTkEntry(self.driver_reg, textvariable=Ct.StringVar())
        self.license.place(x=520,y=250)

        self.register = Ct.CTkButton(self.driver_reg, text="Register", font=Ct.CTkFont(family="Times",size=20))
        self.register.place(x=750, y=250)
        
        column = ("Booking_id", "Customer Name", "Pickup Address", "Drop-off Address", "Mobile no.","date_of_booking","Payment Method","Booking status")
        self.view_booking = ttk.Treeview(self.driver_reg, columns=column, show="headings", height=30)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=165)

        self.view_booking.place(x=60,y=360)

        self.driver_reg.pack(side=Ct.LEFT)

    def cust_details(self):

        self.cus_det = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.cus_det.configure(fg_color='white')
        column = ("Booking_id", "Customer Name", "Pickup Address", "Drop-off Address", "Mobile no.","date_of_booking","Payment Method","Booking status")
        self.view_booking = ttk.Treeview(self.cus_det, columns=column, show="headings", height=40)

        for col in column:
            self.view_booking.heading(col, text=col, anchor="center")
            self.view_booking.column(col, anchor="center", width=165)

        self.view_booking.place(x=60,y=20)

        self.cus_det.pack()

    def history_page(self):
        self.history_frame = Ct.CTkFrame(self.main_frame,width=1125, height=750)
        self.history_frame.configure(fg_color= 'white')
        # Create the Treeview
        self.booklb = Ct.CTkLabel(self.history_frame, text='Booking History',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
        self.booklb.place(x=400,y=50)
        column = ("id","Pickup Address", "Drop-off Address","date_of_booking","Booking status","Driverid","Driver Name","Phone_no","Vechicle_no")
        self.history_booking = ttk.Treeview(self.history_frame, columns=column, show="headings", height=30)
        
        for col in column:
            self.history_booking.heading(col, text=col, anchor="center")
            self.history_booking.column(col, anchor="center", width=150)

        self.history_booking.place(x=50,y=200)
        self.history_frame.pack()

    def change_page(self):
        self.chan = Ct.CTkFrame(self.main_frame,width=1150, height=750)
        self.chan.configure(fg_color= 'white')

        self.cmpic = Ct.CTkImage(Image.open('D:\Code\Python\python project\TaxBookingSystem\image\Screenshot 2023-12-30 153422.png'), size=(600,500))
        self.booklb = Ct.CTkLabel(self.chan, text='Password chan',font=Ct.CTkFont(family="Times",size=50, weight='bold'),text_color='#00BF63')
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

        self.con_button=Ct.CTkButton(self.chan,text="change",font=Ct.CTkFont(family="Times",size=25, weight='bold'),width=200)
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
        self.book_indicate.configure(fg_color='#00BF63')
        self.change_indicate.configure(fg_color='#00BF63')
        self.delete_indicate.configure(fg_color='#00BF63')
        self.history_indicate.configure(fg_color='#00BF63')

    def indicate(self,lb, page):
        self.remove()
        lb.configure(fg_color='white')
        self.delete_frame()
        page()

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
    
    def delete_acc(self):
        self.cust_id=GobalVariable.Customer[0]
        try:
            cursor =self.connection.cursor() 
            query = f"DELETE  FROM customer WHERE customerid={self.cust_id}"
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
    def veiw_customer(self):
        try:
            cursor =self.connection.cursor()
            query = f'''SELECT booking.bookingid,customer.firstname,customer.phonenumber,booking.pickup_address,booking.dropoff_address,booking.date,customer.Payment_Method,booking.status
            FROM customer
            JOIN booking
            where customer.customerid=booking.customerid'''
            cursor.execute(query)
            rows = cursor.fetchall()

            for item in self.view_booking.get_children():
                self.view_booking.delete(item)

            for row in rows:
                self.view_booking.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7]))

        except Exception as err:
            print(f"Error: {err}")
    
    
    def selectedRow(self,event):
        selected_item = self.view_booking.focus()
        values = self.view_booking.item(selected_item, "values")


        if values:
            self.bookingid.set(values[0])

            self.var1.set(values[7])

if __name__ == '__main__':
    app = Ct.CTk()
    Dashboard(app)
    app.after(0,lambda:app.state('zoomed'))
    app.mainloop()