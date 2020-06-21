from app import db
from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user
from app.courses.models import ClassCode, Course, ClassEnrollment, ClassCourses
from app.users.models import User
from app.quiz.models import Quiz

pages = Blueprint('pages', __name__)

@pages.route('/docs')
def docs():
    return render_template('pages/docs.html')

@pages.route('/')
@login_required
def educator_dashboard():
    # left join query filter user class
    class_list = db.session.query(ClassCode, ClassEnrollment)\
                .outerjoin(ClassCode, ClassEnrollment.class_code_id == ClassCode.id)\
                .filter(ClassEnrollment.user_id == current_user.id)
    # display all courses
    # course_list = Course.query.all()
    
    # get courses based on class_code
    class_course_list = db.session.query(Course.name, ClassCourses.course_id, ClassEnrollment)\
                        .outerjoin(Course, ClassCourses.course_id == Course.id)\
                        .filter(ClassEnrollment.user_id == current_user.id)
    quiz_list = Quiz.query.all()

    for course in class_course_list:
        print(course.name)

    return render_template('pages/educator_dashboard.html',
                            class_list=class_list,
                            class_course_list=class_course_list,
                            quiz_list=quiz_list)
