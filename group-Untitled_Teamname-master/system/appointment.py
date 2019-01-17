class appointment:
    def __init__(self, time, date, reason):
        self.time = time
        self.date = date
        self.reason = reason
    
    @property
    def getTime(self):
        return self.time
        
    @property
    def getDate(self):
        return self.date
    
    @property
    def getReason(self):
        return self.reason
        
