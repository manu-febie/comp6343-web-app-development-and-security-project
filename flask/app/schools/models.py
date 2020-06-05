from app import db


class School(db.Model):
    '''
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    users = db.relationship('educator.id', backref='school', lazy='dynamic')

    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
