from tkinter import messagebox
from Controller import DataBaseConnection as con

class CustomerDatabase:
    __connection__ = None

    def __init__(self):
        self.__connection__ = con.Database.Connect()
    
    def CustomerRegister(self,CusRegister):
        if self.__isvalidCustomerRegister(CusRegister):
            if self.__isAuthentic(CusRegister):
                messagebox.showinfo('register','Registration Successfully')
            else:
                messagebox.showerror("register","Register Failure")
        else:
            messagebox.showinfo("register","please write a valid information")
            
    def __isvalidCustomerRegister(self,CusRegister):
        if CusRegister.getFirst()!="" and CusRegister.getLast()!= "" and CusRegister.getPhone()!="" and CusRegister.getAddress()!="" and CusRegister.getEmail()!="" and CusRegister.getPassword()!="":
            return True
        return False
    def __isAuthentic(self,CusRegister):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `customer`(`customerid`,`first name`, `last name`, `email`, `phone number`,`address`, `password`) VALUES ('{CusRegister.getId()}','{CusRegister.getFirst()}','{CusRegister.getLast()}','{CusRegister.getEmail()}','{CusRegister.getPhone()}','{CusRegister.getAddress()}','{CusRegister.getPassword()}')"
            cursor.execute(query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def CustomerLogin(self,LoginCustomer):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM customer WHERE email='"+LoginCustomer.getEmail()+"' AND password='"+LoginCustomer.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
    
    def _isValidEmail(self,email):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM customer WHERE email='"+email.getEmail()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
