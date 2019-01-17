from Booking import Booking

class BookingManager:
    def __init__(self, booking):
        self._bookings = []
     
    @property
    def getBooking(self):
        return self._booking()
    
    def makeBooking(self, booking):
        return self._bookings.append(booking) 
        
        '''              
    @property
    def getAppointments(self):
        return self.appointments
    
    @property
    def addAppointment(self, appointment):
        self.appointments.append(appointment)'''
