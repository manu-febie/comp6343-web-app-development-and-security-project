from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField


class CourseCreateForm(FlaskForm):
    name = StringField('name')
    course_code = StringField('course code')
    classes = SelectMultipleField('classes', coerce=int)
    submit = SubmitField('submit')


class ClassCodeCreateForm(FlaskForm):
    class_code = StringField('class code')
    submit = SubmitField()

