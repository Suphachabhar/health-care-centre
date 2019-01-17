from server import app
from flask import request, render_template, redirect, url_for
import csv
from run import *
from Booking import Booking
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from UserManager import *
from profile import *
from routes import *

def getPatientPage(email, HealthSystem):
    for patient in HealthSystem.getUsers:
        if (email == patient.getEmail):
            return render_template('patient.html',info=patient,type='patient')
    return 'Details not currently available'

def getProviderPage(email, HealthSystem,message=None):
    providers = HealthSystem.getProviders
    for provider in providers:
        if(email == provider.getEmail):
            centres = HealthSystem.getProviderCentres(email)
            rating = HealthSystem.getProviderRating(email)
            login_patient = 1
            for user in HealthSystem.getUsers:
                if user.getEmail == current_user.getEmail:
                    login_patient = 1
            return render_template('profile.html',info=provider,centres=centres,rating=rating, patient =login_patient,type='provider',messages=message)
    return 'Details not currently available'

def getCentrePage(centre, HealthSystem,message=None):

    centres = HealthSystem.getHCC()
    for c in centres:
        if (centre == c.getName):
            rating = HealthSystem.getHCCRating(centre)
            providers = c.getProviders
            login_patient = 1
            for user in HealthSystem.getUsers:
                if user.getEmail == current_user.getEmail:
                    login_patient = 1
            return render_template('profile.html',info=c,providers=providers,rating=rating,services=c.getServices, patient=login_patient,type='healthcentre',messages=message)

    return 'Details not currently available'
