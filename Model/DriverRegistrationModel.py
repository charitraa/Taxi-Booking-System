class Driver:
    #constructor
    def __init__(self,_driverid,_first,_last,_phone,_address,_email,_dob,_liscence,_vechicle,_password):
        self.driverid = _driverid
        self.first = _first
        self.last = _last
        self.phone = _phone
        self.address = _address
        self.email = _email
        self.DOB = _dob
        self.liscence = _liscence
        self.vechicle = _vechicle
        self.password = _password
    
    #getters
    def getId(self):
        return self.driverid

    def getFirst(self):
        return self.first
    
    def getLast(self):
        return self.last
        
    def getPhone(self):
        return self.phone
    
    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email
    
    def getDOB(self):
        return self.DOB
    
    def getVechicle(self):
        return self.vechicle
    
    def getLiscence(self):
        return self.liscence
    
    def getPassword(self):
        return self.password
    
    #setters

    def setId(self, Uid):
        self.driverid = Uid

    def setFirst(self,first ):
        self.first = first

    def setLast(self, last):
        self.last = last

    def setPhone(self, phone):
        self.phone = phone

    def setAddress(self, Address):
        self.address = Address

    def setEmail(self, email):
        self.email = email

    def setDOB(self, DOB):
        self.DOB = DOB

    def setLiscence(self, Liscence):
        self.liscence = Liscence

    def setVechicle(self, Vechicle):
        self.vechicle = Vechicle

    def setPassword(self, password):
        self.password = password