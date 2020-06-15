from app.schools.forms import SchoolRegisterForm
from app.schools.models import School
from app import db
from flask import Blueprint, render_template, redirect, url_for


schools = Blueprint('schools', __name__)

@schools.route('/school/add')
def school_add():
    form = SchoolRegisterForm()

    if form.validate_on_submit():
        school = School(name=form.name.data)
        db.session.add(school)
        db.session.commit()

    return render_template('school/create.html', form=form)
