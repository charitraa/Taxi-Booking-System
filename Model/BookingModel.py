class Customer:
    #constructor
    def __init__(self,_bid,_pickup,_dropoff,_date,_time,_cusid):
        self.bid = _bid
        self.pickup = _pickup
        self.dropoff = _dropoff
        self.date = _date
        self.time= _time
        self.cusid = _cusid
    
    #getters
    def getId(self):
        return self.bid

    def getPickup(self):
        return self.pickup
    
    def getDropoff(self):
        return self.dropoff
        
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    def getUID(self):
        return self.cusid
    
    #setters

    def setId(self, Uid):
        self.bid = Uid

    def setPickup(self,pickup):
        self.pickup = pickup

    def setDropoff(self, dropoff):
        self.dropoff = dropoff

    def setDate(self, date):
        self.date = date

    def setTime(self, time):
        self.time = time

    def setUid(self, uid):
        self.cusid = uid