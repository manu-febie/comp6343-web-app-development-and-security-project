from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv

import os

# load environment variables
load_dotenv('.env')

# Flask instance
app = Flask(__name__)
bc = Bcrypt(app)

# Configs
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_user:password@mysql-quiz-db.cwlufssxaaja.us-east-1.rds.amazonaws.com:3306/aws_quizdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False

# Database instance
db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)

login_manager.login_view = 'users.login'
login_manager.login_message = ''

# import models
from app.courses.models import ClassCode, Course, ClassCourses
from app.users.models import User, Student
from app.schools.models import School
from app.quiz.models import Quiz

# blueprints
from app.courses.routes import courses
from app.pages.routes import pages
from app.schools.routes import schools
from app.users.routes import users
from app.quiz.routes import quiz

app.register_blueprint(courses)
app.register_blueprint(pages)
app.register_blueprint(schools)
app.register_blueprint(users)
app.register_blueprint(quiz)
