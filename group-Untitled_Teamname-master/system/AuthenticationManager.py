from flask_login import current_user, login_required, login_user, logout_user
from flask import redirect, url_for

class AuthenticationManager():

    def __init__(self,login_manager):
        self._login_manager = login_manager
        self._default_page = 'home'

    def login(self, user, username, password):
        if user.email == username and user.password == password:
            login_user(user)
            return user
        return None
