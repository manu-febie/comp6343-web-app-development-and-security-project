from app import db
from app.users.models import User
from app.users.api.schema import user_schema, users_schema

from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

user_api = Blueprint('user_api', __name__)

@user_api.route('/api/student/add', methods=['POST'])
def user_add():
    new_student = User(
                    is_student=True,
                    firstname=request.json['firstname'],
                    lastname=request.json['lastname'],
                    email=request.json['email'],
                    password=generate_password_hash(request.json['password'])
                    )
    db.session.add(new_student)
    db.session.commit()
    
    return user_schema.jsonify(new_student)

@user_api.route('/api/users', methods=['GET'])
def user_get():
    user_list = User.query.all()
    result = users_schema.dump(user_list)

    return jsonify(result)


