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

@api.post('/createexercise')
def createExerciseAPI():
    data = request.json # This coming from the POST request body

    title = data['title']
    price = data['price']
    description = data['description']
    category = data['category']
    img_url = data['img_url']
   

    new = Exercise(title, price, description, category, img_url)
    new.saveExercise()
    return {
        'status' : 'ok',
        'message' : 'new exercise has been created!'
    }

@api.get('/exercise/item/<int:user_id>')
def getexerciseByUser(user_id):
    exercise = Exercise.query.filter(Exercise.user_id == user_id).all()
    # Just so we can see the other example of the same query above:
    # posts = Post.query.filter_by(user_id == user_id).all()

    if exercise:
        return {
            'status' : 'ok',
            'exercise' : [e.to_dict() for e in exercise]
        }
    return {
        'status' : ' NOT ok',
        'message' : 'No exercise available to return from that ID'
    }