from flask_login import UserMixin

class patient(UserMixin):
    __id = -1

    def __init__(self, first_name, last_name, phone, email, password, provider_ratings, centre_ratings):
        self._id = self._generate_id()     
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.type = 'patient'
        
        #A list of ratings for providers (in the same order as the providers list within the system)
        self.provider_ratings = provider_ratings
        
        #A list of ratings for centres (in the same order as the centres list within the system)
        self.centre_ratings = centre_ratings
    
    @property
    def getID(self):
        return self._id

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    # for call current user
    def get_id(self):
        return str(self._id)

    @property
    def getEmail(self):
        return self.email
    
    @property
    def getPhone(self):
        return self.phone
        
    @property
    def getFirstName(self):
        return self.first_name
    
    @property
    def getLastName(self):
        return self.last_name

    @property
    def getType(self):
        return self.type

    def _generate_id(self):
        patient.__id += 1
        return patient.__id
    
    def addProviderRating(self, num, rating):
        self.provider_ratings[num] = rating
    
    def __str__(self):
        return f'first: {self.first_name}, First: {self.last_name}, email: {self.email}, phone: {self.phone}, password: {self.password}'
    
    def checkPassword(self, password):
        if (self.password == password):
            return 1
        else:
            return 0
