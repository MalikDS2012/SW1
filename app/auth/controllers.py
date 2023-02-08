from flask import render_template, session, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth
from .models import db, User
from .forms import SignupForm
from flask_login import login_user, login_required, logout_user
from .. import login_manager
#import os , app_instance_path
#import pandas as pd

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#APP_STATIC = os.path.join(app_instance_path,'static')

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@auth.route('/login', methods=['POST'])
def login():
	#df=pd.read_excel(os.path.join(APP_STATIC,'abc.xlsx'))
	name = request.form['username']
	pwd = request.form['password']
	user=User.query.filter_by(username=name).first()
	if check_password_hash(user.password,pwd):
		login_user(user)
		return render_template('login.html',user=user,pwd=1)
	else:
		return render_template('login.html',user=user,pwd=0)
	
@auth.route('/signup')
@login_required
def signup():
	form = SignupForm()
	
	return render_template('signup.html', form = form)


@auth.route('/register', methods=['GET','POST'])
def register():
	#if form.submit():
		#name = form.username.data
		#pwd = generate_password_hash(form.password.data)
	name = request.form['username']
	pwd = request.form['password']
	vpwd = request.form['vpassword']
	if (pwd == vpwd):
		pwd = generate_password_hash(pwd)
		user = User(username = name, password = pwd)
		db.session.add(user)
		db.session.commit()
	users = User.query.all()
	return render_template('register.html',users=users)
	#return render_template('signup.html')
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('main.index'))
