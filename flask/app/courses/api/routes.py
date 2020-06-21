from app.courses.api.schema import course_schemas, class_code_schemas
from app.courses.models import Course

from flask import Blueprint, jsonify

course_api = Blueprint('course_api', __name__)

@course_api.route('/api/classes', methods=['GET'])
def course_all_get():
    course_list = Course.query.all()
    result = course_schemas.dump(course_list)

    return jsonify(result)
    
