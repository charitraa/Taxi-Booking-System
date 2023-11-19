
from tkinter import messagebox
from Controller import DataBaseConnection as con

class DriverDatabase:
    __connection__ = None
    def __init__(self):
        self.__connection__ = con.Database.Connect()
    
    def DriverRegister(self,DriveRegister):
        if self.__isvalidDriverRegister(DriveRegister):
            if self.__isAuthentic(DriveRegister):
                messagebox.showinfo("register","Register Successfully")
            else:
                messagebox.showinfo("register","Register Failure")
        else:
            messagebox.showinfo("register","please write a valid information")
            
    def __isvalidDriverRegister(self,DriveRegister):
        if DriveRegister.getFirst()!="" and DriveRegister.getLast()!= "" and DriveRegister.getPhone()!="" and DriveRegister.getAddress()!="" and DriveRegister.getEmail()!="" and DriveRegister.getVechicle()!="" and DriveRegister.getLiscence()!="" and DriveRegister.getPassword()!="":
            return True
        return False
    
    def __isAuthentic(self,DriveRegister):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `driver`(`driverid`, `first name`, `last name`, `phone number`, `Address`, `email`, `liscence no`, `vechicle no`, `password`) VALUES ('{DriveRegister.getId()}','{DriveRegister.getFirst()}','{DriveRegister.getLast()}','{DriveRegister.getPhone()}','{DriveRegister.getAddress()}','{DriveRegister.getEmail()}','{DriveRegister.getLiscence()}','{DriveRegister.getVechicle()}','{DriveRegister.getPassword()}')"
            cursor.execute(query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def DriverLogin(self,LoginDriver):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM driver WHERE email='"+LoginDriver.getEmail()+"' AND password='"+LoginDriver.getPassword()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False