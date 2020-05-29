from app import db


class Course(db.Model):
    '''
    Course model:
    One course can belong to multiple "classes" and can be taught by 
    multiple teachers.
    '''
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

    # establish many-to-many relationships with Teacher & Class model
    teachers = db.relationship('Teacher', secondary='course_teachers',
                               backref='course', lazy='dynamic')
    courses = db.relationship('Class', secondary='course_classes',
                               backref='course', lazy='dynamic')
     
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Course> {}'.format(self.name)


# Mapping taple to establish the many-to-many relationship between courses
# and teachers
db.Table('course_teachers',
        db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
        db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'))
        )


db.Table('course_classes',
        db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
        db.Column('class_id', db.Integer, db.ForeignKey('class.id'))
        )
