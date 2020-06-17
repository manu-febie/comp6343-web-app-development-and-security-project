from app import db


class ClassCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id', ondelete='CASCADE'))
    courses = db.relationship('Course', 'class_courses', backref='class_code', lazy='dynamic')
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    course_code = db.Column(db.String(10))
    quizzes = db.relationship('Quiz', backref='course', lazy='dynamic')

    def __repr__(self):
        return self.name


class ClassCourses(db.Model):
    '''
    many-to-many relationship to prevent duplicate courses
    '''
    id = db.Column(db.Integer, primary_key=True)
    class_code_id = db.Column(db.Integer, db.ForeignKey('class_code.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))



