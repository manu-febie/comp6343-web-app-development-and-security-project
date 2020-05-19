from flask import Blueprint, render_template, url_for

users = Blueprint('users', __name__)

@users.route('/student/login')
def student_login():
    eturn render_template('student_login.html')
