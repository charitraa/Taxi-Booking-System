from tkcalendar import DateEntry
from tkinter import messagebox
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Model import CusRegistrationModel as cusmodel
from Controller import CustomerController as cusdb
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import customtkinter as CT
import LoginView
#create a registration class
class RegistrationPage():
    # create the constructor
    def __init__(self,master):
        self.master = master
        self.master.title("Customer Registration Page")#titlename
        self.master.geometry("1000x600")
        CT.set_default_color_theme("green") 
        #set the window at top of the page
        self.master.attributes('-topmost',True)

        #create the background Image
        self.background_image = CT.CTkImage(Image.open('image\\registration.png'), size=(550,600))
        
        self.img = CT.CTkLabel(self.master,image=self.background_image, text="").place(x=0,y=0)

        self.id = 0
        #create the Label and Entry  for registration Page
        self.create =  CT.CTkLabel(self.master, text="Create a Account", font=CT.CTkFont(family="Times",size=50, weight='bold'), text_color='#00BF63' ).place(x=580,y=10)
        self.first_name_CTkLabel = CT.CTkLabel(self.master, text="First Name:",font=CT.CTkFont(family="Times",size=20))
        self.first_name_CTkLabel.place(x=630,y=80)
        self.first_name_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.first_name_CTkentry.place(x=770,y=80)

        self.last_name_CTkLabel = CT.CTkLabel(self.master, text="Last Name:",font=CT.CTkFont(family="Times",size=20))
        self.last_name_CTkLabel.place(x=630,y=130)
        self.last_name_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.last_name_CTkentry.place(x=770,y=130)

        self.email_CTkLabel = CT.CTkLabel(self.master, text="Email:",font=CT.CTkFont(family="Times",size=20))
        self.email_CTkLabel.place(x=630,y=430)
        self.email_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.email_CTkentry.place(x=770,y=430)

        self.address_CTkLabel = CT.CTkLabel(self.master, text="Address:",font=CT.CTkFont(family="Times",size=20))
        self.address_CTkLabel.place(x=630,y=180)
        self.address_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.address_CTkentry.place(x=770,y=180)
        
        self.date_CTklabel = CT.CTkLabel(self.master,text = 'DOB:',font=CT.CTkFont(family="Times",size=20))
        self.date_CTklabel.place(x=630,y=230)
        self.date_CTkEntry = DateEntry(self.master,width=30,selectmode='day')
        self.date_CTkEntry.place(x=960,y=300)

        self.gender_CTkLabel = CT.CTkLabel(self.master, text="Gender:",font=CT.CTkFont(family="Times",size=20))
        self.gender_CTkLabel.place(x=630,y=280)
        self.var_gender = CT.StringVar()
        self.radio_btn =CT.CTkRadioButton(self.master, text="Male", variable=self.var_gender, value="Male")
        self.radio_btn.place(x=770, y=285)
        self.radio_btn1 = CT.CTkRadioButton(self.master, text="Female", variable=self.var_gender, value="Female")
        self.radio_btn1.place(x=870, y=285)

        self.pay1=CT.CTkLabel(self.master,text='Payment Method:',font=CT.CTkFont(family="Times",size=20))
        self.pay1.place(x=630,y=330)

        self.var=CT.StringVar()
        self.var.set("Select payment method")

        self.pay=tk.OptionMenu(self.master,self.var,"Cash", "Mobile Banking", "Esewa")
        self.pay.place(x=1000,y=415)

        self.phone_CTkLabel = CT.CTkLabel(self.master, text="Phone Number:",font=CT.CTkFont(family="Times",size=20))
        self.phone_CTkLabel.place(x=630,y=380)
        self.phone_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.phone_CTkentry.place(x=770,y=380)
        
        self.pass_CTkLabel = CT.CTkLabel(self.master, text="Password:",font=CT.CTkFont(family="Times",size=20))
        self.pass_CTkLabel.place(x=630,y=480)
        self.pass_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.pass_CTkentry.place(x=770,y=480)
        # Repeat this pattern for the remaining fields

        #create the buttons
        register_CTkbutton = CT.CTkButton(self.master, text="Register", font=CT.CTkFont(family="Times", size=20), command=self.register)
        register_CTkbutton.place(x=600,y=530)
        back_CTkbutton = CT.CTkButton(self.master, text="Back",font=CT.CTkFont(family="Times", size=20), command=self.Back)
        back_CTkbutton.place(x=770,y=530)

        #create the register function
    def register(self):
        self.gender = "Male" if self.var_gender.get() == 'Male' else "Female"
        self.pay_method = self.var.get()
        if self.first_name_CTkentry.get()!='' and self.last_name_CTkentry.get()!=''and self.var_gender.get()!=''and self.var.get!='' and self.phone_CTkentry.get()!='' and self.email_CTkentry.get()!='' and self.address_CTkentry.get()!='' and self.date_CTkEntry.get_date()!='' and self.pass_CTkentry.get()!='':
            cus = cusmodel.Customer(self.id, self.first_name_CTkentry.get(),self.last_name_CTkentry.get(),self.phone_CTkentry.get(),self.pay_method,self.gender,self.address_CTkentry.get(),self.date_CTkEntry.get_date(),self.email_CTkentry.get(),self.pass_CTkentry.get())
            reg = cusdb.CustomerDatabase()
            reg._CustomerRegister(cus)
            if reg:
                self.first_name_CTkentry.delete(0,'end')
                self.last_name_CTkentry.delete(0,'end')
                self.email_CTkentry.delete(0,'end')
                self.phone_CTkentry.delete(0,'end')
                self.address_CTkentry.delete(0,'end')
                self.pass_CTkentry.delete(0,'end')
                messagebox.showinfo('register','Registration Successfully',parent=self.master)
                

                self.master.destroy()
            else:
                messagebox.showerror("register","Register Failure",parent=self.master)
        else:
            messagebox.showinfo("register","please write a valid information",parent=self.master)

    def Back(self):
        self.master.destroy()

if __name__ == "__main__":

    app = CT.CTk()
    RegistrationPage(app)
    # app.eval('tk::PlaceWindow . top')
    app.mainloop()
