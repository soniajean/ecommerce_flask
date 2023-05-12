from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()

Gym = db.Table(
    'gym',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), nullable=False)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
        

    def to_dict(self):
        return {
            'id': self.id,
            'username' : self.username
            
        }


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, nullable=False, unique=True)
    bodypart = db.Column(db.String(100), nullable=False, unique=True)
    equipment = db.Column(db.Numeric(10,2))
    gifUrl = db.Column(db.String)
    name = db.Column(db.String)
    target = db.Column(db.String, default='')
    gymed = db.relationship('User',
        secondary = 'gym',
        backref = 'gymed',
        lazy = 'dynamic'
    )

    def __init__(self, exercise_id, bodypart, equipment, name, target, gifurl=''):
        self.bodypart = bodypart
        self.equipment = equipment
        self.gifurl = gifurl
        self.exercise_id = exercise_id
        self.name = name
        self.target = target
        

    def to_dict(self):
        return {
            'exercise_id': self.exercise_id,
            'name' : self.name,
            'bodypart' : self.bodypart,
            'equipment' : self.equipment,
            'gifUrl' : self.gifUrl,
            'target' : self.target
                 
        }
        

    def saveExercise(self):
        db.session.add(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    def deleteExercise(self):
        db.session.delete(self)
        db.session.commit()


        
    

   

   
    
  
   