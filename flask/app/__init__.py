from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import UserManager, SQLAlchemyAdapter
from flask_mail import Mail
from dotenv import load_dotenv

import os

# load environment variables
load_dotenv('.env')

# Flask instance
app = Flask(__name__)

# Configs
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False

# Flask Mail 
# app.config['MAIL_SERVER'] = 
# app.config['MAIL_PORT']
# app.config['MAIL_USE_TLS']
# app.config['MAIL_USE_SSL']
# app.config['MAIL_DEBUG']
# app.config['MAIL_USERNAME']
# app.config['MAIL_PASSWORD']
# app.config['MAIL_DEFAULT_SENDER']
# app.config['MAIL_MAX_EMAILS']
# app.config['MAIL_SUPRESS_SEND']
# app.config['MAIL_ASCII_ATTACHMENTS']

# Database instance
db = SQLAlchemy(app)
mail = Mail(app)
#migrate = Migrate(app, db)

# import models
from app.users.models import BaseUser, Role, UserRoles, Student, Educator
from app.schools.models import School
from app.courses.models import ClassCode, Course, CourseEnrollment, EducatorCourses
# from app.quiz.models import Quiz, Question, Answer

# setup Flask-User
user_manager = UserManager(app, db, BaseUser)
#db_adapter = SQLAlchemyAdapter(db, BaseUser)

# blueprints
from app.pages.routes import pages
from app.users.routes import users
from app.quiz.routes import quiz

app.register_blueprint(pages)
app.register_blueprint(users)
app.register_blueprint(quiz)
