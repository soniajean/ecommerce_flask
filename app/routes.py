
from . import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user

from .api.services import get_products
from .models import User, Product

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/about-us')
def aboutUs():
    return render_template('aboutus.html')