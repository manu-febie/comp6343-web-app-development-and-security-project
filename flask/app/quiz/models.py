from app import db


class Quiz(db.Model):
    '''
    Quiz model:
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    # due_date_time = db.Column()

    # reference to questions
    questions = db.relationship('Question', backref='quiz', lazy='dynamic')
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Question(db.Model):
    '''
    Question model:
    A "question" belonging to a Quiz. Can have multiple answers.
    '''
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

    # reference to the answers
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    def __str__(self):
        return self.id


class Answer(db.Model):
    '''
    '''
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.Text, nullable=False)
    correct = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))








