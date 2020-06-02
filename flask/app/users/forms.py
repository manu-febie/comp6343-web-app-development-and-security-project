from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo


class RegisterBaseForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    email = StringField('email', validators=[Email()])
    password1 = PasswordField('password')
    password2 = PasswordField('confirm password', validators=[EqualTo('password1')])
    submit = SubmitField('register')


class EducatorRegisterForm(RegisterBaseForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    email = StringField('email', validators=[Email()])
    password1 = PasswordField('password')
    password2 = PasswordField('confirm password', validators=[EqualTo('password1')])
    submit = SubmitField('register')


class StudentRegisterForm(RegisterBaseForm):
    student_id = StringField('student id')
     

class UserLoginForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('login')
