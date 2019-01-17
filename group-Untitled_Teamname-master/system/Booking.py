class Booking(object):
    
    def __init__(self,  day, time, HCC, HCP, reason):
        self._day = day
        self._time = time
        self._HCC = HCC
        self._HCP = HCP
        self._reason = reason
    
    @property
    def day(self):
        return self._day
    
    @property    
    def time(self):
        return self._time
    
    @property    
    def HCC(self):
        return self._HCC
    
    @property    
    def HCP(self):
        return self._HCP
    
    '''
    def add_reason(self, reason):
        self._reason.append(reason)
    '''
    @property
    def reason(self):
        return self._reason
        
    def __str__(self):
        return f'Booking made for {self._time} on {self._day} with {self._HCP} at {self._HCC}.'
