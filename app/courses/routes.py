from app import db
from app.courses.forms import CourseCreateForm, ClassCodeCreateForm, ClassJoinForm
from app.courses.models import ClassCode, Course, ClassCourses, ClassEnrollment
from app.users.models import User

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required

courses = Blueprint('courses', __name__)

@courses.route('/class/new', methods=['GET', 'POST'])
@login_required
def class_create():
    form = ClassCodeCreateForm()
    
    if form.validate_on_submit():
        class_code = ClassCode(
                name = form.class_code.data,
                school_id = current_user.school.id
                )
        # add class
        db.session.add(class_code)
        db.session.commit()
        
        # add current_user to this class
        class_enrollment = ClassEnrollment(
                    class_code_id = class_code.id,
                    user_id = current_user.id
                )
        db.session.add(class_enrollment)
        db.session.commit()

        flash('Class has been addded')

        return redirect(url_for('courses.class_list'))

    return render_template('courses/class_create.html', form=form)

@courses.route('/class/management', methods=['GET', 'POST'])
@login_required
def class_list():
    class_list = db.session.query(ClassCode, ClassEnrollment)\
                .outerjoin(ClassCode, ClassEnrollment.class_code_id == ClassCode.id)\
                .filter(ClassEnrollment.user_id == current_user.id)

    return render_template('courses/class_list.html', class_list=class_list)

@courses.route('/student/join/class', methods=['GET', 'POST'])
@login_required
def class_join():
    # select class, add to user
    form = ClassJoinForm()

    if form.validate_on_submit():
        class_code = ClassCode.query.filter(ClassCode.name == form.name.data).first()
        
        if not class_code:
            flash('class_code does not exist')

        class_enroll = ClassEnrollment(
                    class_code_id = class_code.id,
                    user_id = current_user.id)
        db.session.add(class_enroll)
        db.session.commit()

        flash(f'Yey! You joined {class_code.name}')

        return redirect(url_for('pages.educator_dashboard'))


    return render_template('courses/class_join.html', form=form)

@courses.route('/class/delete')
@login_required
def class_delete():
    return redirect(url_for('courses.class_list'))

@courses.route('/course/management')
@login_required
def course_list():
    course_list = Course.query.all()

    return render_template('courses/course_list.html', course_list=course_list)

@courses.route('/course/new', methods=['GET', 'POST'])
@login_required
def course_create():
    class_code_list = ClassCode.query.all()
    form = CourseCreateForm()
    form.classes.choices = [(class_code.id, class_code.name) for class_code in class_code_list]

    if form.is_submitted():
        selections = form.classes.data
        course = Course(
                    name = form.name.data,
                    course_code = form.course_code.data
                ) 
        db.session.add(course)
        db.session.commit()
        
        # Establish many to many relationship between the classess and course
        for selection in selections:
            class_course = ClassCourses(
                        class_code_id = selection,
                        course_id = course.id
                    )
            db.session.add(class_course)
            db.session.commit()

        flash(f'{course.name} has been created')
        
        return redirect(url_for('pages.educator_dashboard'))

    return render_template('courses/create.html', form=form)













