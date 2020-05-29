from app import db
from flask_user import UserMixin


class Role(db.Model):
    '''
    Define the role data-model
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __str__(self):
        return f'Role <{self.name}>'


class UserRoles(db.Model):
    '''
    Define the UserRoles association table
    '''
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'))


class User(db.Model, UserMixin):
    '''
    An abstract class for User models. 
    Does not create a table inside the database.
    ''' 
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(244), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False) 
    password = db.Column(db.String(255), nullable=False)
    #birthdate = db.Date
    joined_on = db.Column(db.DateTime(), default=db.func.now())
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')    
    roles = db.relationship('Role', secondary='user_roles', backref='user', lazy='dyanmic')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        return '<User {} {}>'.format(self.firstname, self.lastname)






