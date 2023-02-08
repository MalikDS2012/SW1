from .. import db
from flask_login import UserMixin


class User(UserMixin,db.Model):
	__tablename__ = 'user_table_name'
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
