from app import db
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from app.quiz.forms import QuizCreateForm
from app.courses.models import Course, ClassCode
from app.quiz.models import Quiz, Question, MultipleChoiceAnswer, QuizClass

quiz = Blueprint('quiz', __name__)

@quiz.route('/quiz/management', methods=['GET', 'POST'])
@login_required
def quiz_list():
    quiz_list = Quiz.query.all()
    return render_template('quiz/quiz_list.html', quiz_list=quiz_list)

@quiz.route('/quiz/create', methods=['GET', 'POST'])
def quiz_create():
    course_list = Course.query.all()
    class_code = ClassCode.query.all()
    form = QuizCreateForm()
    form.course.choices = [(course.id, course.name) for course in course_list] 

    # 1. Create quiz
    # 2. Create questionss
    # 3. Create answers
    # 4. Set due date
    return render_template('quiz/create_quiz.html', form=form)
