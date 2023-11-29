from tkinter import messagebox
from Controller import DataBaseConnection as con

class CustomerDatabase:
    __connection__ = None

    def __init__(self):
        self.__connection__ = con.Database.Connect()
        
    def _CustomerRegister(self,CusRegister):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `customer`(`customerid`, `first name`, `last name`, `email`, `DOB`, `phone number`, `address`, `password`) VALUES ('{CusRegister.getId()}','{CusRegister.getFirst()}','{CusRegister.getLast()}','{CusRegister.getEmail()}','{CusRegister.getDOB()}','{CusRegister.getPhone()}','{CusRegister.getAddress()}','{CusRegister.getPassword()}')"
            cursor.execute(query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def CustomerLogin(self,LoginCustomer):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("SELECT * FROM customer WHERE email='"+LoginCustomer.getEmail()+"' AND password='"+LoginCustomer.getPassword()+"'")
            record = cursor.fetchone()
        except Exception as e:
            print(e)
        return record
    
    def _isValidEmail(self,email):
        cursor = self.__connection__.cursor()
        cursor.execute("SELECT * FROM customer WHERE email='"+email.getEmail()+"'")
        record = cursor.fetchone()
        if (record!=None):
            return True
        return False
    
    def _ChangePassword(self,email):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute("UPDATE customer SET password ='"+email.getPassword()+"' WHERE email='"+email.getEmail()+"'")
            record = cursor.fetchone()
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)

    def _CustomerBook(self,CusBook):
        try:
            cursor = self.__connection__.cursor()
            query  = f"INSERT INTO `book`(`customerid`,`first name`, `last name`, `email`, `phone number`,`address`, `password`) VALUES ('{CusBook.getId()}','{CusBook.getFirst()}','{CusBook.getLast()}','{CusBook.getEmail()}','{CusBook.getPhone()}','{CusBook.getAddress()}','{CusBook.getPassword()}')"
            cursor.execute(query)
            self.__connection__.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            return False