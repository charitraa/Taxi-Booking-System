
from tkinter import messagebox
from Controller import DataBaseConnection as con

class DriverDatabase:
    __connection__ = None
    def __init__(self):
        self.__connection__ = con.Database.Connect()
    
    def _DriverRegister(self,DriveRegister):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `driver`(`driverid`, `first name`, `last name`, `phone number`, `Address`, `email`, `DOB`, `liscence no`, `vechicle no`, `password`) VALUES ('{DriveRegister.getId()}','{DriveRegister.getFirst()}','{DriveRegister.getLast()}','{DriveRegister.getPhone()}','{DriveRegister.getAddress()}','{DriveRegister.getEmail()}','{DriveRegister.getDOB()}','{DriveRegister.getLiscence()}','{DriveRegister.getVechicle()}','{DriveRegister.getPassword()}')"
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
