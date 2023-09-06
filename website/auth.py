from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.homepage'))
            elif check_password_hash(user.google_password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.homepage'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    if current_user.is_authenticated:
        flash('You are already logged in', category='error')
        return redirect(url_for('views.homepage'))
    elif not current_user.is_authenticated:
        user_agent = request.headers.get('User-Agent')
        user_agent = user_agent.lower()
        if "iphone" in user_agent:
            return render_template('mobile/login.html', user=current_user)
        elif "android" in user_agent:
            return render_template('mobile/login.html', user=current_user)
        else:
            return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        google_password=request.form.get('google_password')
        if password1 == "pleasesendtogooglepasswordpage":
            if password2 == "pleasesendtogooglepasswordpage":
                return render_template('StudyLobbyPassword.html', email=email, first_name=first_name,google_password=google_password)
        f = open('mysite/website/static/leaderboard.txt', 'r')
        for line in f:
            wr = open('mysite/website/static/leaderboard.txt', 'a')
            if line.startswith("{'"+first_name+"'"+": "):
                namenottaken=False
            else:
                namenottaken=True
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif namenottaken==False:
            flash('Name Already Taken', category='error')
        else:
            try:
                new_user = User(email=email, first_name=first_name,password=generate_password_hash(password1, method='sha256'),google_password=generate_password_hash(google_password, method='sha256'))
            except:
                new_user = User(email=email, first_name=first_name,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            file_object = open('mysite/website/static/leaderboard.txt', 'a')
            string=str('\n{'+"'"+first_name+"'"+': 0}')
            file_object.write(string)
            file_object.close()
            return redirect('https://studylobby.pythonanywhere.com')
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()
    if "iphone" in user_agent:
        return render_template('mobile/sign_up.html', user=current_user)
    elif "android" in user_agent:
        return render_template('mobile/sign_up.html', user=current_user)
    else:
        return render_template('sign_up.html', user=current_user)
