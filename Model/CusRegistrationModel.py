class Customer:
    #constructor
    def __init__(self,_cusid=None,_first=None,_last=None,_phone=None,_payment_method=None,_Gender=None,_address=None,_dob=None,_email=None,_password=None):
        self.cusid = _cusid
        self.first = _first
        self.last = _last
        self.phone = _phone
        self.payment = _payment_method
        self.Gender = _Gender
        self.address = _address
        self.dob = _dob
        self.email = _email
        self.password = _password
    
    #getters
    def getId(self):
        return self.cusid

    def getFirst(self):
        return self.first
    
    def getLast(self):
        return self.last
        
    def getPhone(self):
        return self.phone
    
    def getPayment(self):
        return self.payment
    
    def getGender(self):
        return self.Gender
    
    def getAddress(self):
        return self.address

    def getDOB(self):
        return self.dob
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    #setters

    def setId(self, Uid):
        self.cusid = Uid

    def setFirst(self,first ):
        self.first = first

    def setLast(self, last):
        self.last = last

    def setPhone(self, phone):
        self.phone = phone

    def setPayment(self, payment):
        self.payment = payment

    def setGender(self, gender):
        self.Gender = gender
        

    def setAddress(self, Address):
        self.address = Address

    def setDOB(self, DOB):
        self.dob = DOB

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password