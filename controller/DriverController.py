
from tkinter import messagebox
from Controller import DataBaseConnection as con

class DriverDatabase:
    __connection__ = None
    def __init__(self):
        self.__connection__ = con.Database.Connect()
    
    def _DriverRegister(self,DriveRegister):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `driver`(`driverid`,fullname,`phonenumber`, `Address`, `email`, `DOB`,`gender`,`liscenceno`, `password`) VALUES ('{DriveRegister.getId()}','{DriveRegister.getFirst()}','{DriveRegister.getPhone()}','{DriveRegister.getAddress()}','{DriveRegister.getEmail()}','{DriveRegister.getDOB()}','{DriveRegister.getGender()}','{DriveRegister.getLiscence()}','{DriveRegister.getPassword()}')"
            cursor.execute(query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
        
    def DriverLogin(self,LoginDriver):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("SELECT * FROM driver WHERE email='"+LoginDriver.getEmail()+"' AND password='"+LoginDriver.getPassword()+"'")
            record = cursor.fetchone()
            
        except Exception as e:
            print(e)
            
        return record
