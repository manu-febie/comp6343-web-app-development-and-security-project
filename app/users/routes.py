from app import db, login_manager
from app.users.models import User, Student
from app.schools.models import School
from app.users.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, url_for, redirect, flash, request
from werkzeug.security import generate_password_hash, check_password_hash

import bcrypt

users = Blueprint('users', __name__)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@login_manager.unauthorized_handler
def handle_needs_login():
    flash('Authentication is required!')
    return redirect(url_for('users.login', next=request.endpoint))

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
                password = generate_password_hash(form.password1.data, "sha256")
                )
        # add and commit to db
        db.session.add(user)
        db.session.commit()

        flash(f'Great! You can login with your email {form.email.data} now')

        return redirect(url_for('users.login'))
            
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
                password = generate_password_hash(form.password1.data, "sha256")
                )
        db.session.add(user)
        db.session.commit()

        flash('Great! You can login with your email now')

        return redirect(url_for('users.login'))
    
    return render_template('/users/register_educator.html', form=form)

@users.route('/u/update', methods=['GET', 'POST'])
def user_update():
    form = UserUpdateForm()
    
    # Display current user data
    form.firstname.data = current_user.firstname
    form.lastname.data = current_user.lastname
    form.email.data = current_user.email
    
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.email = form.email.data
        
        db.session.commit()

        flash('Your profile has been updated')
    else:
        print('Oh nono')

    return render_template('users/user_update.html', form=form)

# login route
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()

    if form.validate_on_submit():
        # Get user by email
        user = User.query.filter(User.email==form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            
            login_user(user)

            if user.school_id == None:
                return redirect(url_for('schools.school_user_choose'))
            else: 
                return redirect(url_for('pages.educator_dashboard'))

    return render_template('users/login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))
