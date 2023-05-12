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

@api.get('/exercise/<int:id>')
def SingleExercise(id):
    e = Exercise.query.get(id)
    if e:
        exercise = e.to_dict()
        return {
        'status' : 'ok',
        'message' : 'Single Exercise!!'
    }
    return {
        'status' : 'NOT OK',
        'messsage': 'no'
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
