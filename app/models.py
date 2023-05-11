from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()

plan = db.Table(
    'my_plan',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), nullable=False),
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False )
    
    def __init__(self,username, email, password):
     
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveUser(self):
        db.session.add(self)
        db.session.commit()


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.String(50), nullable=True, )
    name = db.Column(db.String(100), nullable=False, unique=True )
    type = db.Column(db.String(100), nullable=False, unique=False )
    muscle = db.Column(db.String(100), nullable=False, unique=False)
    equipment = db.Column(db.String)
    difficulty = db.Column(db.String)
    instructions = db.Column(db.String)
    planed = db.relationship('User',
        secondary = 'my_plan',
        backref = 'planed',
        lazy = 'dynamic'
    )


    def __init__(self, id, exercise_id, name, type, muscle, equipment, difficulty, instructions):
        self.id = id
        self.exercise_id = exercise_id
        self.name = name
        self.type = type
        self.muscle = muscle
        self.equipment = equipment
        self.difficulty = difficulty
        self.instructions = instructions

    def to_dict(self):
        return {
            'id': self.id,
            'exercise_id' : self.exercise_id,
            'name' : self.name,
            'type' : self.type,
            'muscle' : self.muscle,
            'equipment' : self.equipment,
            'difficulty' : self.difficulty,   
            'instructions' : self.instructions       
        }
        

    def saveExercise(self):
        db.session.add(self)
        db.session.commit()

    def saveChanges(self):
        db.session.commit()

    def deleteExercise(self):
        db.session.delete(self)
        db.session.commit()

    def saveToPlan(self, user):
        self.planed.append(user)
        db.session.commit()

    def deleteFromPlan(self, user):
        self.planed.remove(user)
        db.session.commit()
        
    

   

   
    
  
   