from app import db
from app.courses.models import Course


class Class(db.Model):
    '''
    Class model:
    One class can have multiple students and Courses.
    '''
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.String(25), nullable=False)

    # reference to Student & Course
    students = db.relationship('Student', backref='student', lazy='dynamic')


    def __str__(self):
        return self.class_id

    def __repr__(self):
        return self.class_id
