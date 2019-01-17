import csv
from HCCManager import *
from BookingManager import *
from UserManager import *
from patient import *
from provider import *
from centre import *
from AuthenticationManager import AuthenticationManager


class System:
    def __init__(self, CSV):
        
        # User Manager
        self._users = []
        self._providers = []
        self._HCCs_by_provider = []
        self._user_ratings = []
        # HCC Manager
        self._HCCs = []
        self._HCC_ratings = [] 
        self._book_HCCs = []
        self._book_providers = []

        #auth manager
        self._auth_manager = AuthenticationManager

        
        # Load from CSV files if CSV = true
        if (CSV == 1):
            self.loadFromCSV()
        else:
            self.loadFromPICKLE()
        
        # Create the managers
        self._user_manager = UserManager(self._users, self._providers, self._HCCs_by_provider, self._user_ratings)
        self._hcc_manager = HCCManager(self._HCCs, self._HCC_ratings)
        self._booking_manager = BookingManager([])
        
        #functions for booking
    ##will need to move ###
    @property    
    def get_centre(self):
        return self._book_HCCs   
        
    def get_user_by_id(self,user_id):
        for u in self._users:
            if u.get_id() == user_id:
                return u
        return None

    def get_provider_by_id(self,user_id):
        for p in self._providers:
            if p.get_id() == user_id:
                return p
        return None
    
    def get_days(self, HCP):
        days = []
        for p in self._book_providers:
            if p[0] == HCP:
                days.append(p[4])
                days = days[0].split()
        return days
        
    def get_time(self, HCP):
        time = []
        for p in self._book_providers:
            if p[0] == HCP:
                time.append(p[3])
                time = time[0].split()
        return time
    #########################
        
    
    #System Functions
    def searchHCP(self, query, sb):
        found_providers = []
        #if searchby = email
        if sb == 'email':
            for provider in self._user_manager._providers:
                if (provider.getEmail.lower().find(query.lower()) != -1):
                    found_providers.append(provider)
            return found_providers
        else:
            for provider in self._user_manager._providers:
                if (provider.getSpecialty.lower().find(query.lower()) != -1):
                    found_providers.append(provider)
            return found_providers
    
    def searchHCC(self, query, sb):
        found_centres = []
        #if searchby = email
        if sb == 'email':
            for centre in self._hcc_manager._HCCs:
                if (centre.getName.lower().find(query.lower()) != -1):
                    found_centres.append(centre)
            return found_centres
        else:
            for centre in self._hcc_manager._HCCs:
                if (centre.getSuburb.lower().find(query.lower()) != -1):
                    found_centres.append(centre)
            return found_centres
            
    def getHCCNames(self):
        HCCs = self._hcc_manager.getHCCs
        names = []
        for hcc in HCCs:
            names.append(hcc.getName)
        print(names)
        return names
    
    def getProviderNames(self):
        Prov = self._user_manager.getProviders
        names = []
        for provider in Prov:
            names.append(provider.getName)
        print(names)
        return names
    
    #User Manager Functions
    @property
    def getUsers(self):
        return self._user_manager.users
    
    @property
    def getProviders(self):
        return self._user_manager.providers

    
    def getProviderCentres(self, ProviderEmail):
        return self._user_manager.getCentres(ProviderEmail)
    
    def get_hcc_providers(self, HCC):
        return self._user_manager.get_hcc_providers(HCC)

    def getProviderRating(self, ProviderEmail):
        return self._user_manager.getRating(ProviderEmail)

    def getHCC(self):
        return self._hcc_manager.getHCCs
        
    #Booking Manager Functions
    @property
    def getBooking(self):
        return self._booking_manager.booking()
    
    def makeBooking(self, booking):
        self._booking_manager.makeBooking(booking)
    
    #HCC Manager Functions

    def getHCCProviders(self, HCC):
        return self._hcc_manager.getProviders(HCC)

    
    def getHCCRating(self, HCCName):
        return self._hcc_manager.getRating(HCCName)
    
    ### Persistance
    def loadFromPICKLE(self):
        #Do nothing
        pass
    
    def loadFromCSV(self):
        #Scan in all the csv files on initiation (this should make it easy to change to pickle in future)
        HCC_provider_dict = dict()
        HCC_service_dict = dict()
        #User Manager
        with open('../patient.csv') as patient_file:
            reader = csv.reader(patient_file, delimiter=',')
            for row in reader:
                new_user = patient(row[2], row[3], row[4], row[0], row[1], ['N','N','N','N','N','N','N','N'], ['N','N','N','N','N','N'])
                self._users.append(new_user)
        with open('../provider.csv') as providers_file:
            reader = csv.reader(providers_file, delimiter=',')
            for row in reader:
                new_provider = provider(row[0], row[1], row[2], row[3], row[4], row[5], 'N', [])
                self._providers.append(new_provider)
                self._book_providers.append(row)
                
        with open('../provider_health_centre.csv') as ph_file:
            reader = csv.reader(ph_file, delimiter=',')
            
            for row in reader:
                if row[1] in HCC_provider_dict:
                    HCC_provider_dict[row[1]].append(row[0])
                else :
                    HCC_provider_dict[row[1]] = []
                    HCC_provider_dict[row[1]].append(row[0])
                
                for _provider in self._providers:
                    if (_provider.getEmail == row[0]):
                        service = _provider.getSpecialty
                        if row[1] in HCC_service_dict:
                            HCC_service_dict[row[1]].add(service)
                        else:
                            HCC_service_dict[row[1]] = set()
                            HCC_service_dict[row[1]].add(service)
                self._HCCs_by_provider.append(row)
        
        with open('../ratings.csv') as ratings_file:
            reader = csv.reader(ratings_file, delimiter=',')
            for row in reader:
                self._user_ratings.append(row)
        

        #HCC Manager
        with open('../health_centres.csv') as providers_file:
            reader = csv.reader(providers_file, delimiter=',')
            for row in reader:
                provider_list = []
                service_list = []
                if row[2] in HCC_provider_dict:
                    provider_list = HCC_provider_dict[row[2]]
                if row[2] in HCC_service_dict:
                    service_list = list(HCC_service_dict[row[2]])
                new_centre = centre(row[1], row[0], row[2], row[3], row[4], 'N', service_list,provider_list )
                self._HCCs.append(new_centre)
                self._book_HCCs.append(row[2])

        
        with open('../hccRatings.csv') as hratings_file:
            reader = csv.reader(hratings_file, delimiter=',')
            for row in reader:
                self._HCC_ratings.append(row)

    #login functions
    def login_patient(self, username, password):
        for patient in self._users:
            if self._auth_manager.login(self, patient, username, password):
                return True
        return False

    def login_provider(self, username, password):
        for provider in self._providers:
            if self._auth_manager.login(self, provider, username, password):
                return True
        return False
