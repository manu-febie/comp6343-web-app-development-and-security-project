from app import db


class AbstractBaseModel(db.Model):
    '''
    An abstract models that defines the default fields each model should have.
    '''
    pass
