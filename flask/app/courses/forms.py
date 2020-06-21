from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms import ValidationError
from app.courses.models import ClassCode


class CourseCreateForm(FlaskForm):
    name = StringField('name')
    course_code = StringField('course code')
    classes = SelectMultipleField('classes', coerce=int)
    submit = SubmitField('submit')


class ClassCodeCreateForm(FlaskForm):
    class_code = StringField('class code')
    submit = SubmitField()


class ClassJoinForm(FlaskForm):
    name = StringField('class code')
    submit = SubmitField('submit') 



