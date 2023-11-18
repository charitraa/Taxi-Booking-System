class Login:
    def __init__(self,_email,_password):
        self.email = _email
        self.password = _password
    
    #getters
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    #setters
    def setEmail(self, email):
        self.email = email
    
    def setPassword(self, password):
        self.password = password
