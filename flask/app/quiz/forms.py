from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, StringField, TextField, SubmitField


class CreateQuizForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    submit = SubmitField('submit')

class CreateQuestionForm(FlaskForm):
    question = TextField('question')
    weight = FloatField('question, weight')
    submit = SubmitField('submit')


class AddMultipleChoiceAnswerForm(FlaskForm):
    answer = StringField('answer')
    correct = BooleanField('correct answer', default=False)

