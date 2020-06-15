from app import db
from app.courses.forms import CourseCreateForm, ClassCodeCreateForm
from app.courses.models import ClassCode, Course, ClassCourses
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user

courses = Blueprint('courses', __name__)

@courses.route('/class/new', methods=['GET', 'POST'])
def class_create():
    form = ClassCodeCreateForm()
    
    if form.validate_on_submit():
        class_code = ClassCode(
                name = form.class_code.data,
                school_id = current_user.school.id
                )
        db.session.add(class_code)
        db.session.commit()

        flash('Class has been addded')

        return redirect(url_for('pages.educator_dashboard'))

    return render_template('courses/class_create.html', form=form)

@courses.route('/course/new', methods=['GET', 'POST'])
def course_create():
    class_code_list = ClassCode.query.all()
    form = CourseCreateForm()
    form.classes.choices = [(class_code.id, class_code.name) for class_code in class_code_list]

    if form.validate_on_submit():
        course = Course(
                    name = form.name.data,
                    course_code = form.course_code.data
                )
        # add new course to db
        db.session.add(course)
        db.session.commit()
        # establish many-to-many relationship
        
        # display success message
        # flash(f'{course.name} - {course.course_code} has successfully been added')

        return redirect(url_for('pages.educator_dashboard'))

    return render_template('courses/create.html', form=form)
