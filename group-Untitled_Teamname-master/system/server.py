import pickle       #Pickle is used to save and load the system object at startup and end
import atexit       #atexit allows a function to be called on exit, for example, the system object being savedfrom flask import Flask

from flask import Flask
from flask_login import LoginManager
from AuthenticationManager import AuthenticationManager
from patient import patient
from provider import provider

from system import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Another_highly_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

auth_manager = AuthenticationManager(login_manager)


CSV = 1     #CSV = 1 for load from CSV, 0 for load from pickle

HealthSystem = System(CSV)
if (CSV == 0):
    system_in = open("data/system.pickle", "rb")
    HealthSystem = pickle.load(system_in)
    system_in.close()

#define the function for saving the system on program exit
def saveSystem():
    print('Saving System...')
    
    system_out = open("data/system.pickle", "wb")
    pickle.dump(HealthSystem, system_out)
    system_out.close()

#add the saveSystem function to what is called on the exit of the program
atexit.register(saveSystem)

@login_manager.user_loader
def load_user(user_id):
    if int(user_id) < 99:
        return HealthSystem.get_user_by_id(user_id)
    elif int(user_id) > 99:
        return HealthSystem.get_provider_by_id(user_id)

