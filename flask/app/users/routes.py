from app import db, user_manager, login_manager
from flask import Blueprint, render_template, url_for, redirect
from flask_login import login_user, logout_user, login_required
from app.users.models import User, Student
from app.users.forms import UserLoginForm, UserRegisterForm

users = Blueprint('users', __name__)

# user loader
@login_manager.user_loader
def load_user(id):
    return BaseUser.query.get(int(id))

@users.route('/student/register', methods=['GET', 'POST'])
def student_register():
    # load form
    form = UserRegisterForm()

    if form.validate_on_submit():
        # create user with student flag: True
        user = User(
                is_student = True,
                firstname = form.firstname.data,
                lastname = form.lastname.data,
                email = form.email.data,
                password = user_manager.hash_password(form.password1.data)
                )
        # add and commit to db
        db.session.add(user)
        db.session.commit()
        print(f'{user.email} has been added')
            
    return render_template('users/register_student.html', form=form)

@users.route('/educator/register', methods=['GET', 'POST'])
def educator_register():
    form = UserRegisterForm()
    
    if form.validate_on_submit():
        user = User(
                is_educator = True,
                firstname = form.firstname.data,
                lastname = form.lastname.data,
                email = form.email.data,
                password = user_manager.hash_password(form.password1.data)
                )
        db.session.add(user)
        db.session.commit()
        print(f'{user.email} has been added')
    
    return render_template('/users/register_educator.html', form=form)

@users.route('/u/update', methods=['GET', 'POST'])
def user_update():
    return render_template('user_update.html')

# login route
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()

    if form.validate_on_submit():
        # Get user by email
        user = User.query.filter(User.email==form.email.data).first()

        if user and user_manager.verify_password(form.password.data, user.password):
            if user.is_educator:
                login_user(user)
                return redirect(url_for('pages.educator_dashboard'))
                print(f'Welcome {user.email}')
        else:
            print('OOhh Nooo')

    return render_template('users/login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))
