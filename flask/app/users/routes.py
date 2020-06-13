from app import db, user_manager, login_manager
from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_user, logout_user, login_required
from app.users.models import UserRoles, Role, BaseUser, Student, Educator
from app.users.forms import EducatorRegisterForm, StudentRegisterForm, UserLoginForm

users = Blueprint('users', __name__)

# user loader
@login_manager.user_loader
def load_user(id):
    return BaseUser.query.get(int(id))

@users.route('/student/register', methods=['GET', 'POST'])
def student_register():
    '''
    Register a student
    '''
    form = StudentRegisterForm()
    role = Role.query.filter(Role.name=='student').first()

    if form.validate_on_submit():
        # fill User object with -> firstname, lastname, email, password
        user = BaseUser(
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    # NOTE! password needst to be hashed
                    password=user_manager.hash_password(form.password1.data)
                )
        # commit new User object 
        db.session.add(user)
        db.session.commit()

        # assign Role -> student to user
        role = UserRoles(
                        user_id=user.id,
                        role_id=role.id
                    ) 
        # commit to db
        db.session.add(role)
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
    role = Role.query.filter(Role.name=='educator').first()
    
    if form.validate_on_submit():
        # fill User object with -> firstname, lastname, email, password
        user = BaseUser(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            email = form.email.data,
            password = user_manager.hash_password(form.password1.data),
            )

        # add and commit user to db
        db.session.add(user)
        db.session.commit()

        # assign Role -> educator
        new_educator = UserRoles(
                            user_id=user.id,
                            role_id=role.id
                )
        db.session.add(new_educator)
        db.session.commit()
 
        # establish one-to-one connection to Educator object
        educator = Educator(
                    id = user.id
                )
        # Commit to db
        db.session.add(educator)
        db.session.commit()

        # redirect to institution page

    return render_template('/users/register_educator.html', form=form)

# login route
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()

    if form.validate_on_submit():
        # Get user by email
        user = BaseUser.query.filter(BaseUser.email==form.email.data).first()

        if user and user_manager.verify_password(form.password.data, user.password):
            login_user(user)
            return redirect(url_for('pages.educator_dashboard'))
        else:
            print('OOhh Nooo')

    return render_template('users/login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))
