from tkcalendar import DateEntry
from tkinter import messagebox
import sys
sys.path.append("D:\Code\Python\python project\TaxBookingSystem")
from Model import CusRegistrationModel as cusmodel
from Controller import CustomerController as cusdb
from PIL import ImageTk, Image
import tkinter as tk
import customtkinter as CT
import LoginVeiw
#create a registration class
class RegistrationPage():
    # create the constructor
    def __init__(self,master):
        self.master = master
        self.master.title("Customer Registration Page")#titlename
        self.master.geometry("1000x550")
        CT.set_default_color_theme("green") 
        #set the window at top of the page
        self.master.attributes('-topmost',True)

        #create the background Image
        self.background_image = CT.CTkImage(Image.open('image\\registration.png'), size=(550,550))
        
        self.img = CT.CTkLabel(self.master,image=self.background_image, text="").place(x=0,y=0)

        self.id = 0
        #create the Label and Entry  for registration Page
        self.create =  CT.CTkLabel(self.master, text="Create a Account", font=CT.CTkFont(family="Times",size=50, weight='bold'), text_color='#00BF63' ).place(x=580,y=15)
        self.first_name_CTkLabel = CT.CTkLabel(self.master, text="First Name:",font=CT.CTkFont(family="Times",size=20))
        self.first_name_CTkLabel.place(x=630,y=100)
        self.first_name_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.first_name_CTkentry.place(x=770,y=100)

        self.last_name_CTkLabel = CT.CTkLabel(self.master, text="Last Name:",font=CT.CTkFont(family="Times",size=20))
        self.last_name_CTkLabel.place(x=630,y=150)
        self.last_name_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.last_name_CTkentry.place(x=770,y=150)

        self.email_CTkLabel = CT.CTkLabel(self.master, text="Email:",font=CT.CTkFont(family="Times",size=20))
        self.email_CTkLabel.place(x=630,y=200)
        self.email_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.email_CTkentry.place(x=770,y=200)

        self.address_CTkLabel = CT.CTkLabel(self.master, text="Address:",font=CT.CTkFont(family="Times",size=20))
        self.address_CTkLabel.place(x=630,y=250)
        self.address_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.address_CTkentry.place(x=770,y=250)
        
        self.date_CTklabel = CT.CTkLabel(self.master,text = 'DOB:',font=CT.CTkFont(family="Times",size=20))
        self.date_CTklabel.place(x=630,y=300)
        self.date_CTkEntry = DateEntry(self.master,selectmode='day',)
        self.date_CTkEntry.place(x=980,y=380)

        self.phone_CTkLabel = CT.CTkLabel(self.master, text="Phone Number:",font=CT.CTkFont(family="Times",size=20))
        self.phone_CTkLabel.place(x=630,y=350)
        self.phone_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.phone_CTkentry.place(x=770,y=350)
        
        self.pass_CTkLabel = CT.CTkLabel(self.master, text="Password:",font=CT.CTkFont(family="Times",size=20))
        self.pass_CTkLabel.place(x=630,y=400)
        self.pass_CTkentry = CT.CTkEntry(self.master,textvariable=CT.StringVar())
        self.pass_CTkentry.place(x=770,y=400)
        # Repeat this pattern for the remaining fields

        #create the buttons
        register_CTkbutton = CT.CTkButton(self.master, text="Register", font=CT.CTkFont(family="Times", size=20), command=self.register)
        register_CTkbutton.place(x=600,y=470)
        back_CTkbutton = CT.CTkButton(self.master, text="Back",font=CT.CTkFont(family="Times", size=20), command=self.Back)
        back_CTkbutton.place(x=770,y=470)

        #create the register function
    def register(self):
        if self.first_name_CTkentry.get()!='' and self.last_name_CTkentry.get()!='' and self.phone_CTkentry.get()!='' and self.email_CTkentry.get()!='' and self.address_CTkentry.get()!='' and self.date_CTkEntry.get_date()!='' and self.pass_CTkentry.get()!='':
            cus = cusmodel.Customer(self.id, self.first_name_CTkentry.get(),self.last_name_CTkentry.get(),self.phone_CTkentry.get(),self.address_CTkentry.get(),self.date_CTkEntry.get_date(),self.email_CTkentry.get(),self.pass_CTkentry.get())
            reg = cusdb.CustomerDatabase()
            reg._CustomerRegister(cus)
            if reg:
                messagebox.showinfo('register','Registration Successfully')
                self.master.destroy()
            else:
                messagebox.showerror("register","Register Failure")
        else:
            messagebox.showinfo("register","please write a valid information")

    def Back(self):
        self.master.destroy()

if __name__ == "__main__":

    app = CT.CTk()
    RegistrationPage(app)
    # app.eval('tk::PlaceWindow . top')
    app.mainloop()
