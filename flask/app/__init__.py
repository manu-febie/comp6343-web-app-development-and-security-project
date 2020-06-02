from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_user import UserManager
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

# Database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import models
from app.users.models import BaseUser, Role, UserRoles, Student, Educator
from app.institutions.models import Stage, EducationalStages, Institution
# from app.classes.models import Class
# from app.courses.models import Course
# from app.quiz.models import Quiz, Question, Answer

# setup Flask-User
user_manager = UserManager(app, db, BaseUser)

# blueprints
from app.pages.routes import pages
from app.users.routes import users

app.register_blueprint(pages)
app.register_blueprint(users)
