from app import db
from flask import Blueprint, render_template, redirect, url_for
from app.quiz.forms import CreateQuizForm, CreateQuestionForm, AddMultipleChoiceAnswerForm
from app.courses.models import Course
from app.quiz.models import Quiz, Question, MultipleChoiceAnswer

quiz = Blueprint('quiz', __name__)

@quiz.route('/quiz/create', methods=['GET', 'POST'])
def quiz_create():
    # get all courses from db
    course_list = Course.query.all()
    form = CreateQuizForm()
    # populate select field with courses from db
    form.courses.choices = [(course.id, course.name) for course in course_list]

    if form.validate_on_submit():
        quiz = Quiz(
                    name = form.name.data,
                    description = form.description.data,
                    course_id = form.courses.data
                )
        db.session.add(quiz)
        db.session.commit()
    
    return render_template('quiz/create_quiz.html', form=form)


