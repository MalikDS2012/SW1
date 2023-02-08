#!/usr/bin/py
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from config import DevConfig
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'index'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
login_manager.init_app(app)

class User(UserMixin,db.Model):
	__tablename__ = 'user_table_name'
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['POST'])
#@login_required
def login():
	name = request.form['username']
	pwd = request.form['password']
	user=User.query.filter_by(username=name).first()
	if check_password_hash(user.password,pwd):
		login_user(user)
		return render_template('login.html',user=user,name = name, pwd=1)
	else:
		return render_template('login.html',user=user,name = name, pwd=0)


@app.route('/user/<name>/<pwd>')
@login_required
def user(name,pwd):
	user = User.query.filter_by(username=name).first()
	if check_password_hash(user.password,pwd):
		return render_template('login.html',user=user,name = name, pwd=1)
	else:
		return render_template('login.html',user=user,name = name, pwd=0)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)