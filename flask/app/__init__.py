from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECREY_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = ''

# blueprints
from app.pages.routes import pages

app.register_blueprint(pages)
