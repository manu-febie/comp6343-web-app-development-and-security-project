from flask import Blueprint, render_template, url_for
from app.institutions.models import Stage, Institution, EducationalStages

institutions = Blueprint('institutions', __name__)

