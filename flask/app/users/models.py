from app import app, db
from datetime import datetime
from flask_user import UserMixin


class User(db.Model, UserMixin):
    '''
    User data-model: Represents either a student or a teacher.
    email attribute is used for authentication
    '''
    id = db.Column(db.Integer, primary_key=True)
    is_student = db.Column(db.Boolean, default=False)
    is_educator = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, server_default='1')
    joined = db.Column(db.DateTime, default=datetime.utcnow())
    school_id = db.Column(db.Integer, db.ForeignKey('school.id', ondelete='CASCADE'))

    def __str__(self):
        return f'User <{self.firstname} {self.lastname}>'


class Student(db.Model):
    '''
    Student data-model:
    Some additional extra fields. One-to-one relation with User.
    '''
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)


class QuizEnrollment(db.Model):
    '''
    Table to know if student has finished quiz
    '''
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id', ondelete='CASCADE'))

