from app import db

class Stage(db.Model):
    '''
    A model representing an Educational Stage.
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    

    def __str__(self):
        return self.name


class EducationalStages(db.Model):
    '''
    Define Educatinal Stages association table:
    Establish many-to-many relationship between Stage and Institution data-model
    '''
    __tablename__ = 'educational_stages'

    id = db.Column(db.Integer, primary_key=True)
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id', ondelete='CASCADE')) 
    institution_id = db.Column(db.Integer, db.ForeignKey('institution.id', ondelete='CASCADE'))


class Institution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    # educators belonging to an institution
    educators = db.relationship('Educator', backref='institution', lazy='dynamic')
        
    # back reference
    stages = db.relationship('Stage', secondary='educational_stages')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
