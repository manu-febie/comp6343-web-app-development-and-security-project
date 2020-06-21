from app.schools.forms import SchoolRegisterForm, SchoolChoicesForm
from app.schools.models import School
from app.users.models import User
from app import db
from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user


schools = Blueprint('schools', __name__)

@schools.route('/u/school/', methods=['GET', 'POST'])
def school_user_choose():
    school_list = School.query.all()
    form = SchoolChoicesForm()
    form.school_choice.choices = [(school.id, school.name) for school in school_list]
    
    if form.validate_on_submit():
        current_user.school_id = form.school_choice.data
        db.session.add(current_user)
        db.session.commit()

        return redirect(url_for('pages.educator_dashboard'))
        
        
    return render_template('schools/create.html', form=form)
