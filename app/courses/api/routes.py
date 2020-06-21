from app.courses.api.schema import course_schemas, class_code_schemas
from app.courses.models import Course, ClassCode

from flask import Blueprint, jsonify

course_api = Blueprint('course_api', __name__)

@course_api.route('/api/classes', methods=['GET'])
def class_list():
    class_clode_list = ClassCode.query.all()
    result = class_code_schemas.dump(class_clode_list)

    return jsonify(result)
    

@course_api.route('/api/courses', methods=['GET'])
def course_list():
    course_list = Course.query.all()
    result = course_schemas.dump(course_list)

    return jsonify(result)
    
