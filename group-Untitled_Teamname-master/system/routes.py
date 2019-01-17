from flask import request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from server import *
from Booking import Booking
from profile import *
import csv

### Login Page ###
@app.route('/',methods=["GET","POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if HealthSystem.login_patient(email, password):
            return redirect(url_for('index',username=email))
    return render_template("login.html")

### Login as Provider Page ###
@app.route('/loginProvider',methods=["GET","POST"])
def loginProvider():
    
    if request.method == "POST":
        
        email = request.form["email"]
        password = request.form["password"]
        if HealthSystem.login_provider(email, password):
            return redirect(url_for('index'))
    return render_template("loginProvider.html")

### Home Page ###
@app.route('/index')
@login_required
def index():
    username = request.args.get('username')
    return render_template("index.html",username=username)

### Booking Page ###
@app.route('/book', methods=['POST', 'GET'])
@login_required
def book():

    invalid=False 

    if request.method == 'POST':
        try:
            book_centre = request.form['HCC']
            if 'enter' in request.form:
                return redirect(url_for('book_provider', HCC=book_centre))
        except:
            invalid=True
            
    return render_template('book2.html', HCCS=HealthSystem.get_centre, invalid=invalid)   

### Select provider ###
@login_required
@app.route('/book/<HCC>', methods=['POST','GET'])
def book_provider(HCC):
    providers = HealthSystem.get_hcc_providers(HCC)
    invalid=False
    
    if request.method == 'POST':
        try:
            book_provider= request.form['HCP']
            if 'enter' in request.form:
                return redirect(url_for('book_time', HCC=HCC, HCP=book_provider))
        except:
            invalid=True
    return render_template('book.html', HCC=HCC, HCPS=providers, invalid=invalid)


### Select time and day ###
@login_required
@app.route('/book/<HCC>/<HCP>', methods=['POST', 'GET'])
def book_time(HCC, HCP):
    
    #will change, we will need to edit the CSV files to day days and times
    #load data from provider.csv
    days = HealthSystem.get_days(HCP)
    times = HealthSystem.get_time(HCP)
    
    invalid=False 
       
    if request.method == 'POST':
        try:
            day = request.form['day']
            time = request.form['time']
            try:
                reason.request.form['reason']
            except:
                reason = []
            booking = Booking(day, time, HCC, HCP, reason)
            if 'book' in request.form:
                HealthSystem.makeBooking(booking)
                return render_template('booking_confirm.html', booking=booking)
        except:
            print('hello')
            invalid=True        
    
    return render_template('makebooking.html', HCC=HCC, HCP=HCP, days=days, times=times, invalid=invalid)

### Search Page ###
@app.route('/search', methods=['POST', 'GET'])
@login_required
def search():
    squery=request.form.get('query')
    if request.method == 'GET':
        return render_template('search.html', search=0, searchby = 0, sq="")
    if request.method == 'POST':
        sb = 0
        if request.form.get('SearchBy') == 'email':
            sb = 'email'
        if request.form.get('SearchType') == 'provider':
            return render_template('search.html', search=1, searchby = sb, sq=squery, providers = HealthSystem.searchHCP(query=squery, sb=sb))
        if request.form.get('SearchType') == 'centre':
            return render_template('search.html', search=2, searchby = sb, sq=squery, centres = HealthSystem.searchHCC(query=squery, sb=sb))

### Patient Profile Page ###
@login_required
@app.route('/profile/patient/<email>')
def viewpatient(email):
    return getPatientPage(email,HealthSystem)

### Provider Profile Page ###
@app.route('/profile/provider/<email>', methods=['POST', 'GET'])
@login_required
def viewprovider(email):
    if request.method == 'GET':
        return getProviderPage(email, HealthSystem)
    if request.method == 'POST':
        rating = request.form.get('rating')
        for provider in HealthSystem.getProviders:
            if provider.getEmail == email:
                provider.addRating(rating)
        return getProviderPage(email, HealthSystem, message='successful')


@app.route('/AppointmentHistory')
def AppointmentHistory():
    return render_template('details.html')

### Healthcare Centre Profile Page ###
@login_required
@app.route('/profile/healthcentre/<centre>', methods=['POST', 'GET'])
def viewhealthcentre(centre):
    if request.method == 'GET':
        return getCentrePage(centre, HealthSystem)
    if request.method == 'POST':
        # rating = request.form.get('rating')
        # for hcc in HealthSystem.getHCC():
        #     if hcc.getName == centre:
        #         hcc.addRating(rating)  
        return getCentrePage(centre,HealthSystem,message='successful')

### Log Out Page ###
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

