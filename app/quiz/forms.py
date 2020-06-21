from flask_wtf import FlaskForm
from wtforms import (BooleanField, FloatField, IntegerField, StringField, TextField,
                     SubmitField, SelectField, TextAreaField, FormField, Form)
from wtforms.fields.html5 import DateField

class QuestionCreateForm(Form):
    question = StringField('question')
    weight = IntegerField('Question weight')
 

class QuizCreateForm(FlaskForm):
    name = StringField('quiz title')
    description = StringField('Short description about the quiz')
    course = SelectField('course', coerce=int)
    due_date = DateField('due date')
    question = FormField(QuestionCreateForm)
    draft = BooleanField('draft', default=True)
    submit = SubmitField('submit')


   

