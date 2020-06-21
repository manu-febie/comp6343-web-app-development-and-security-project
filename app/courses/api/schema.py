from app import ma


class ClassCodeSchema(ma.Schema):
    class Meta:
        fields = ('id',  'name')


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'course_code')

class_code_schemas = ClassCodeSchema(many=True)
course_schemas = CourseSchema(many=True)
