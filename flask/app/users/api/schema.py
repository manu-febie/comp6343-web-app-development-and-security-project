from app import ma

from app.users.models import User, Student, QuizEnrollment


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firstname', 'lastname', 'email', 'password')

class StudentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        include_fk = True


class QuizEnrollment(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QuizEnrollment
        include_fk = True

user_schema = UserSchema()
users_schema = UserSchema(many=True, only=('firstname', 'lastname', 'email'))
