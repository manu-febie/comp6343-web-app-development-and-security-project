from flask_wtf import FlaskForm
from wtforms import (BooleanField, FloatField, IntegerField, StringField, TextField,
                     SubmitField, SelectField)
from wtforms_sqlalchemy.fields import QuerySelectField
from app.courses.models import course_query



class CreateQuizForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    courses = SelectField('course', coerce=int)
    #course_choice = QuerySelectField(query_factory=course_query, allow_blank=False)
    submit = SubmitField('submit')

class CreateQuestionForm(FlaskForm):
    question = TextField('question')
    weight = FloatField('question, weight')
    submit = SubmitField('submit')


class AddMultipleChoiceAnswerForm(FlaskForm):
    answer = StringField('answer')
    correct = BooleanField('correct answer', default=False)

