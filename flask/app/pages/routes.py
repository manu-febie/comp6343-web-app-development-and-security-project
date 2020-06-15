from flask import Blueprint, render_template, url_for
from flask_login import login_required
from app.courses.models import ClassCode, Course
from app.quiz.models import Quiz

pages = Blueprint('pages', __name__)

@pages.route('/')
def index():
    '''
    Pages route that returns the homepage of the web app

    :return: homepage
    '''

    return render_template('index.html')

@pages.route('/docs')
def docs():
    return render_template('pages/docs.html')

@pages.route('/e/dashboard')
@login_required
def educator_dashboard():
    '''
    '''
    class_list = ClassCode.query.all()
    course_list = Course.query.all()
    quiz_list = Quiz.query.all()

    return render_template('pages/educator_dashboard.html',
                            class_list=class_list,
                            course_list=course_list,
                            quiz_list=quiz_list)
