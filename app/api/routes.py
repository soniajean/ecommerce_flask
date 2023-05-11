from flask import Blueprint, request
from ..models import Exercise, User
import requests
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

@api.post('/plan/add')
def addtoPlan():
    user_id=request.json.get('user_id')
    exercise_id=request.json.get('exercise_id')
    current_user=User.query.get(user_id)
    current_exercise=Exercise.query.get(exercise_id)
    current_user.saveToPlan(current_exercise)
    return {
        'status' : 'ok',
        'message' : 'That exercise added to plan!!'
    }

@api.post('/plan/delete')
def deleteFromPlan():
    user_id=request.json.get('user_id')
    exercise_id=request.json.get('exercise_id')
    current_user=User.query.get(user_id)
    current_exercise=Exercise.query.get(exercise_id)
    current_user.deleteFromPlan(current_exercise)
    return {
        'status' : 'ok',
        'message' : 'That exercise deleted from plan!!'
    }

@api.post('/user/create')
def createUser():
    username=request.json.get('username')
    password=request.json.get('password')
    new_user=User(username,password)
    new_user.saveUser()
   
    return {
        'status' : 'ok',
        'message' : 'User successfully created!!'
    }


@api.post('/user/login')
def loginUser():
    username=request.json.get('username')
    password=request.json.get('password')
    current_user=User.query.filter_by(username=username).first()
   
    return {
        'status' : 'ok',
        'message' : 'User successfully created!!','user':current_user.to_dict()
    }
@api.get('/apiexercise')
def get_api_exercise():
    url = "https://exercisedb.p.rapidapi.com/exercises"
    headers = {
	"X-RapidAPI-Key": "28dfc0e2a6mshfd18a7f7d3c3901p173983jsncd5d692debd5",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

    response = requests.get(url, headers=headers)
    if response.ok:
        data = response.json()
        print(data)
        return data
    else:
        return None



