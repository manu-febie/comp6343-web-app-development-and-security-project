from app import db
from app.courses.models import ClassCode, Course, ClassCourses
from flask import Blueprint, render_template, redirect, url_for

courses = Blueprint('courses', __name__)
