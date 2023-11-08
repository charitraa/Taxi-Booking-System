from tkinter import messagebox
import mysql.connector as c


class CustomerDatabase:
    message = ""
    __connection__ = None
    try:
        @staticmethod
        def Connect():
            connection = c.connect(
                host='localhost',
                user = 'root',
                password = 'root',
                database = 'taxi' 
            )
            if connection.is_connected():
                CustomerDatabase.message = "Connected"
                return connection
            connection.close()  
    except Exception as e:
        print(e)
        
    def __init__(self):
        self.__connection__ = CustomerDatabase.Connect()
    
    def Register(self,CusRegister):
        if self.__isvalidRegister(CusRegister):
            if self.__isAuthentic(CusRegister):
                messagebox.showinfo("register","Register Successfully")
                
            else:
                messagebox.showinfo("register","Register Failure")
        else:
            messagebox.showinfo("register","please write a valid information")
    def __isvalidRegister(self,CusRegister):
        if CusRegister.getFirst()!="" and CusRegister.getLast()!= "" and CusRegister.getPhone()!="" and CusRegister.getAddress()!="" and CusRegister.getEmail()!="" and CusRegister.getPassword()!="":
            return True
        return False
    def __isAuthentic(self,CusRegister):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `customer`(`customerid`,`first name`, `last name`, `email`, `phone number`,`address`, `password`) VALUES ('{CusRegister.getId()}','{CusRegister.getFirst()}','{CusRegister.getLast()}','{CusRegister.getPhone()}','{CusRegister.getAddress()}','{CusRegister.getEmail()}','{CusRegister.getPassword()}')"
            cursor.execute(query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
        
