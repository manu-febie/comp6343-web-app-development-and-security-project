from app import db
from app.classes.models import Class


class AbstractBaseUser(db.Model):
    '''
    An abstract class for User models. 
    Does not create a table inside the database.
    '''
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(244), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False) 
    password = db.Column(db.String(255), nullable=False)
    password_confirm = db.Column(db.String(255), nullable=False)
    #birthdate = db.Date
    joined_on = db.Column(db.DateTime(), default=db.func.now())
    is_active = db.Column(db.Boolean(), default=True) 
    # avatar

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def __repr__(self):
        return '<User {} {}>'.format(self.firstname, self.lastname)


class Student(AbstractBaseUser):
    '''
    Student model inherits from AbstractBaseUser class. 
    Creates student of type :student:
    '''
    is_student = db.Column(db.Boolean(), default=True)
    student_id = db.Column(db.String(50), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))


class Teacher(AbstractBaseUser):
    '''
    Teacher model inherits from AbstractBaseUser class.
    '''
    is_teacher = db.Column(db.Boolean(), default=True)

