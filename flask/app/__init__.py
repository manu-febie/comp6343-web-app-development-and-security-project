from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os

# load environment variables
load_dotenv('.env')

# Flask instance
app = Flask(__name__)

# Configs
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Database instance
db = SQLAlchemy(app)

# blueprints
from app.pages.routes import pages
from app.users.routes import users

app.register_blueprint(pages)
pp.register_blueprint(users)
