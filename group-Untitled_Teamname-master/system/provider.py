from flask_login import UserMixin

class provider(UserMixin):
    __id = 100

    def __init__(self, email, password, specialty, hours, work_days, rate, rating, appointments):
        self._id = self._generate_id()   
        self.email = email
        self.password = password
        self.specialty = specialty
        self._hours = hours
        self._work_days = work_days
        self.rate = rate
        self.rating = rating
        self.type = 'provider'
        
        #A list of appointment class instances
        self.appointments = appointments

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)


    @property
    def getEmail(self):
        return self.email
    
    @property
    def getSpecialty(self):
        return self.specialty
    
    @property
    def getHours(self):
        return self._hours
    
    @property
    def getWorkDays(self):
        return self.work_days
    
    @property
    def getRate(self):
        return self.rate
    
    @property
    def getRating(self):
        return self.rating

    @property
    def getType(self):
        return self.type

    def _generate_id(self):
        provider.__id += 1
        return provider.__id
    
    def addRating(self, rating):
        r = int(rating)
        self.rating = r
        return
        if (r <= 5) and (r >= 0):
            if self.rating == 'N':
                self.rating = r
            else:
                self.rating = (r + int(self.rating)*2)/3
            return 1
        else:
            return 0

    def __str__(self):
        return f'email: {self.email}, speciality: {self.specialty}'

    def addAppointment(self, appointment):
        self.appointments.append(appointment)
    
    def isAvailable(self, time, day):
        if (self.work_start_time <= time) and (self.work_finish_time >= time):
            if (day in self.work_days):
                #Now check whether the appointment space is free
                return 0
        return 1
