from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import logout_user, login_user, current_user
from werkzeug.security import check_password_hash

from .forms import SignUpForm, LoginForm
from ..models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()
    print(request.method)
    if request.method == 'POST':
         print(request.method)
         if form.validate():
              username = form.username.data
              password = form.password.data
              
              user = User.query.filter_by(username=username).first()
            #   SELECT * FROM user WHERE username = <username variable>
              if user:
                   if check_password_hash(user.password, password): # <-- NEW
                        # user.password == password: -- OLD way
                        print("YAY, you're logged in!")
                        login_user(user)
                        print(current_user)
                        print(current_user.username)
                        return redirect(url_for('homePage'))
                   else:
                        flash("Incorrect Password!", "warning")
              else:
                   flash("Username is Incorrect!", "danger")
              return redirect(url_for('auth.loginPage'))
    return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def registerPage():
     form = SignUpForm()
     if request.method == 'POST':
          if form.validate():
               first_name = form.first_name.data
               last_name = form.last_name.data
               username = form.username.data
               email = form.email.data
               password = form.password.data
               if User.query.filter_by(username=username).first():
                    flash("That username already exists, please try another!", "warning")
                    return redirect(url_for('auth.registerPage'))
               if User.query.filter_by(email=email).first():
                    flash("That email has been used previously")
                    return redirect(url_for('auth.registerPage'))
               user = User(first_name, last_name, username, email, password)
               user.saveUser()
               flash(f"Welcome, {first_name.title()}!", "success")
               return redirect(url_for('auth.loginPage'))                
     return render_template('register.html', form=form)

@auth.route('/logout')
def logOut():
    logout_user()
    return redirect(url_for('homePage'))