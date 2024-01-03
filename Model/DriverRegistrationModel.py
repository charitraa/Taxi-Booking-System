class Driver:
    #constructor
    def __init__(self,_driverid,_first,_phone,_address,_email,_dob,_liscence,_gender,_password):
        self.driverid = _driverid
        self.first = _first
        self.gender = _gender
        self.phone = _phone
        self.address = _address
        self.email = _email
        self.DOB = _dob
        self.liscence = _liscence
        self.password = _password
    
    #getters
    def getId(self):
        return self.driverid

    def getFirst(self):
        return self.first
    
    def getGender(self):
        return self.gender
        
    def getPhone(self):
        return self.phone
    
    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email
    
    def getDOB(self):
        return self.DOB

    
    def getLiscence(self):
        return self.liscence
    
    def getPassword(self):
        return self.password
    
    #setters

    def setId(self, Uid):
        self.driverid = Uid

    def setFirst(self,first ):
        self.first = first

    def setGender(self, gender):
        self.gender = gender

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



    def setPassword(self, password):
        self.password = password