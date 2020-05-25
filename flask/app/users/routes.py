from flask import Blueprint, render_template, url_for
from .models import Student, Teacher

users = Blueprint('users', __name__)

@users.route('/student/login')
def student_login():
    return render_template('student_login.html')

