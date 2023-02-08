from flask import render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

from . import main
from .forms import LoginForm
from flask_login import login_required
from sklearn import datasets
import requests
import os
#from .models import db, User

@main.route('/')
def index():
	#return '<h1>Salam!</h1>'
	form = LoginForm()
	return render_template('index.html', form = form)

#@main.route('/login', methods=['POST'])
#def login():
	#name = request.form['username']
	#pwd = request.form['password']
	#user=User.query.filter_by(username=name).first()
	#if check_password_hash(user.password,pwd):
		#return render_template('login.html',user=user,pwd=1)
	#else:
		#return render_template('login.html',user=user,pwd=0)
@main.route('/model')
@login_required
def model():	
	digits = datasets.load_digits()
	dt = digits.data[1620:1625]
	url = 'http://localhost:5001/api'
	r = requests.post(url,json={'exp':dt.tolist()})
	#print(r.json())
	return render_template('model.html', a = r.json())

@main.route('/welcome')
def welcome():
    return render_template('welcome.html')

#@main.route('/archive', methods=['GET','POST'])
#def archive():
	#lst = os.listdir('X:\DCCM Scans\\')
	#return render_template('archive.html',lst=lst)
