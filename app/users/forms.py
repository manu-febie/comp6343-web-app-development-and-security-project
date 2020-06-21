from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Email, EqualTo


class UserRegisterForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    email = StringField('email', validators=[Email()])
    password1 = PasswordField('password')
    password2 = PasswordField('confirm password', validators=[EqualTo('password1')])
    submit = SubmitField('submit')


class UserUpdateForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    email = StringField('email', validators=[Email()])
    submit = SubmitField('update')
     

class UserLoginForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('login')
