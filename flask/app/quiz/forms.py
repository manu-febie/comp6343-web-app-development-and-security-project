from flask_wtf import FlaskForm
from wtforms import (BooleanField, FloatField, IntegerField, StringField, TextField,
                     SubmitField, SelectField, TextAreaField, FormField, Form)

class QuestionCreateForm(Form):
    question = StringField('question')
    weight = IntegerField('Question weight')
 

class QuizCreateForm(FlaskForm):
    name = StringField('quiz title')
    description = StringField('Short description about the quiz')
    question = FormField(QuestionCreateForm)
    submit = SubmitField('submit')


   

