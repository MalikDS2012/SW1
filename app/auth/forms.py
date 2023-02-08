
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
    username = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    vpassword = PasswordField('vPassword', validators=[DataRequired()])
    submit = SubmitField('Register')
