class Customer:
    #constructor
    def __init__(self,cusid=0,_first="",_last="",_phone="",_address="",_email="",_password=""):
        self.cusid = cusid
        self.first = _first
        self.last = _last
        self.phone = _phone
        self.address = _address
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
    
    def getAddress(self):
        return self.address

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

    def setAddress(self, Address):
        self.address = Address

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password