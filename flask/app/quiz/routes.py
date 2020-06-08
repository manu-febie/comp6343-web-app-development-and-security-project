from app import db
from flask import Blueprint, render_template, redirect, url_for
from app.quiz.forms import CreateQuizForm, CreateQuestionForm, AddMultipleChoiceAnswerForm
from app.quiz.models import Quiz, Question, MultipleChoiceAnswer

quiz = Blueprint('quiz', __name__)


@quiz.route('/quiz/create', methods=['GET', 'POST'])
def quiz_create():
    form = CreateQuizForm()

    return render_template('quiz/create_quiz.html', form=form)


