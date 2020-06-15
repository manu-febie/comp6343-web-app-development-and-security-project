from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField


class SchoolRegisterForm(FlaskForm):
    name = StringField('school name')
    submit = SubmitField('submit')


