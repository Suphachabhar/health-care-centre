from flask_login import LoginManager, login_user, current_user, login_required, logout_user
#User Manager class
class UserManager:
    def __init__(self, _users, _providers, _HCCs_by_provider, _ratings):
        self._users = _users
        self._providers = _providers
        self._HCCs_by_provider = _HCCs_by_provider
        self._ratings = _ratings
    
    @property
    def users(self):
        return self._users
        
    @property
    def providers(self):
        return self._providers
    
    def getCentres(self, ProviderEmail):
        #This function returns a list of the HCCs that the given provider works at
        centres = []
        for row in self._HCCs_by_provider:
            if row[0] == ProviderEmail:
                    centres.append(row[1])
        return centres
        
    def get_hcc_providers(self, HCC):
        h_providers = []
        for p in self._HCCs_by_provider:
            if (p[1] == HCC):
                h_providers.append(p[0])
        return h_providers
    
    def getRating(self, ProviderEmail):
        for provider in self._providers:
            if provider.getEmail == ProviderEmail:
                if provider.getRating == 'N':
                    return 'No ratings yet'
                else:
                    return format(int(provider.getRating), '.2f')
