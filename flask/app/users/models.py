from app import app, db
from flask_user import UserMixin, UserManager
from datetime import datetime


class Role(db.Model):
    '''
    Define the role data-model
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class UserRoles(db.Model):
    '''
    Define the UserRoles association table
    '''
    __tablename__ = 'user_roles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('base_user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'))


class BaseUser(db.Model, UserMixin):
    '''
    User data-model: Represents either a student or a teacher.
    email attribute is used for authentication
    '''
    __tablename__ = 'base_user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, nullable=False, server_default='1')
    joined = db.Column(db.DateTime, default=datetime.utcnow())
    school_id = db.Column(db.Integer, db.ForeignKey('school.id', ondelete='CASCADE'))

    # backref to roles
    roles = db.relationship('Role', secondary='user_roles', backref='user', lazy='dynamic')
     
    def __str__(self):
        return f'User <{self.firstname} {self.lastname}>'


class Student(db.Model):
    '''
    Student data-model: some additional fields for user of type 'student'.
    Has one-to-one relationship with User data-model - (extending the User data-model).
    '''
    id = db.Column(db.Integer, db.ForeignKey('base_user.id', ondelete='CASCADE'), primary_key=True)
    student_id = db.Column(db.String(50), unique=True)
    
    def __str__(self):
        return self.student_id

    def __repr__(self):
        return self.student_id
 

class Educator(db.Model):
    '''
    Educator data-model: some aditional fields for user of type 'educator'
    '''
    id = db.Column(db.Integer, db.ForeignKey('base_user.id', ondelete='CASCADE'), primary_key=True)
