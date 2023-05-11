
from . import app

from flask import render_template, request, url_for, redirect

@app.route('/')
def homePage():
    return render_template('index.html')

