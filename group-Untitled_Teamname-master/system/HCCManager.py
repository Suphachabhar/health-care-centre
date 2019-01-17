class HCCManager:
    def __init__(self, _HCCs, _ratings):
        self._HCCs = _HCCs
        self._ratings = _ratings
    
    @property
    def getHCCs(self):
        return self._HCCs
           
    def getRatingProv(self, Sys, HCCName):
        #Gets the ratings of the provdiers at an hcc to give an average for the hcc
        providers = self.getProviders(HCCName)
        ratings = []
        for prov in providers:
            if Sys._user_manager.getRating(prov) != 'No ratings yet':
                ratings.append(Sys._user_manager.getRating(prov))
        rating = 0
        if len(ratings) == 0:
            return 'No ratings yet'
        for num in ratings:
            rating += float(num)
        return format(rating / len(ratings), '.2f')
    
    def getRating(self, HCCName):
        #Reads from the hccRatings.csv file to get ratings
        rfile = self._ratings
        #Look through the file for the matching provider
        ID = -1
        for hcc in range(len(rfile[0])):
            if HCCName == rfile[0][hcc]:
                ID = int(hcc) + 1
                break
        if ID == -1:
            return 'HCC does not exist in hccRatings.csv'
        else:
            rating = 0
            rate_count = 0
            i = 0
            for patient in rfile:
                if i == 0:
                    i = 1
                    continue
                if patient[ID] != 'N':
                    rating += int(patient[ID])
                    rate_count += 1
            if rate_count == 0:
                return "No ratings yet"
            return format(rating / rate_count, '.2f')

