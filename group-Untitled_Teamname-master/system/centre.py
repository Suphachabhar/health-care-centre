class centre:
    def __init__(self, abn, type, name, phone, suburb, rating, services, providers):
        self._abn = abn
        self._type = type
        self._name = name
        self._phone = phone
        self._suburb = suburb
        self._rating = rating
        self._services = services
        self._providers = providers
        
    @property
    def getAbn(self):
        return self._abn
    
    @property
    def getType(self):
        return self._type
        
    @property
    def getName(self):
        return self._name
    
    @property
    def getPhone(self):
        return self._phone
        
    @property
    def getSuburb(self):
        return self._suburb
        
    @property
    def getRating(self):
        return self._rating
    
    @property
    def getServices(self):
        return self._services
    
    @property
    def getProviders(self):
        return self._providers
