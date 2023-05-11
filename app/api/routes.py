from flask import Blueprint, request
from ..models import Exercise

api = Blueprint('api', __name__, url_prefix='/api')



@api.get('/exercise')
def getExercise():
    exercise = Exercise.query.all()
    exerciselist = [e.to_dict() for e in exercise]
    return {
        'status': 'ok',
        'data': exerciselist
    }

@api.get('/exercise/<int:exercise_id>')
def getSingleExercise(exercise_id):
    e = Exercise.query.get(exercise_id)
    if e:
        exercise = e.to_dict()
        return {
            'status': 'ok',
            'data' : exercise
        }
    return {
        'status' : 'NOT ok',
        'message' : 'That exercise is not available!!'
    }



