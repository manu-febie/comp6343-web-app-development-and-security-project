from app import db


class ClassCode(db.Model):
    '''
    ClassCode data-model:
    A unique code to relate students with
    '''
    __tablename__ = 'class_code'

    id = db.Column(db.Integer, primary_key=True)
    class_code = db.Column(db.String(20), unique=True)

    def __str__(self):
        return self.class_id


class Course(db.Model):
    '''
    Course model:
    One course can belong to multiple "classes" and can be taught by 
    multiple teachers.
    '''
    id = db.Column(db.Integer(), primary_key=True)
    course_id = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    # backref to quiz
    quizzes = db.relationship('Quiz', backref='course', lazy='dynamic')
 
    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Course> {}'.format(self.name)


class CourseEnrollment(db.Model):
    '''
    establish many-to-many relationship between courses and classes:
    i.e classes can be enrolled to many courses. Many courses can can have multiple classes
    '''
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'))
    class_code_id = db.Column(db.Integer, db.ForeignKey('class_code.id', ondelete='CASCADE'))


class EducatorCourses(db.Model):
    '''
    Educator Class data-model:
    An educator can have multiple classes.
    '''
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'))
    educator_id = db.Column(db.Integer, db.ForeignKey('educator.id', ondelete='CASCADE'))
