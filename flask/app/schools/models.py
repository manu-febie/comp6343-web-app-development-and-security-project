from app import db


class School(db.Model):
    '''
    School data-model:
    can have multiple users and classes
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    
    # backref to classes and users
    users = db.relationship('User', backref='school', lazy='dynamic')
    classes = db.relationship('ClassCode', backref='school', lazy='dynamic')

    def __repr__(self):
        return self.name

