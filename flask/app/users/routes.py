from app import db
from flask import Blueprint, render_template, url_for
from app.users.models import Role, User, Student, Educator
from app.users.forms import EducatorRegisterForm, StudentRegisterForm

users = Blueprint('users', __name__)

@users.route('/student/register', methods=['GET', 'POST'])
def student_register():
    '''
    Register a student
    '''
    form = StudentRegisterForm()

    if form.validate_on_submit():
        # fill User object with -> firstname, lastname, email, password
        user = User(
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=form.password1.data,
                )
        # assign Role -> student
        user.roles.append(Role(name='student'))
        # commit new User object 
        db.session.add(user)
        db.session.commit()

        # establish one-to-one connection to Student data-model
        student =  Student(
                    id=user.id,
                    student_id=form.student_id.data
                    )
        # commit to db
        db.session.add(student)
        db.session.commit()

        print('Commit success')
        
    return render_template('users/register_student.html', form=form)

@users.route('/educator/register', methods=['GET', 'POST'])
def educator_register():
    '''
    Register an educator
    '''
    form = EducatorRegisterForm()
    user = User()
    
    if form.validate_on_submit():
        # fill User object with -> firstname, lastname, email, password
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.email = form.email.data
        user.password = form.password1.data 
        # assign Role -> educator
        user.roles.append(Role(name='educator'))
        # establish one-to-one connection to Educator object
        
        # Commit to db
        db.session.add(user)
        db.session.add(educator)
        db.session.commit()

        print('successfully added new educator')

    return render_template('/users/register_educator.html', form=form)

# login route
