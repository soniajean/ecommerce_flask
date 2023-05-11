from flask import Blueprint, render_template, request, url_for, redirect, flash
plan = Blueprint('plan', __name__, template_folder='plan_templates')
from flask_login import current_user, login_required
from app.models import User, Exercise, db


@plan.route('/my-plan')
def viewMyPlan():
    exercises = current_user.planed
    plan_total = 0
    for e in exercises:
        plan_total += (e.price)
    return render_template('my_plan.html', exercises=exercises, total=plan_total)

@plan.route('/add/<int:exercise_id>')
def addToPlan(exercise_id):
    exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
    exercise.saveToPlan(current_user)
    exercise_name=exercise.title
    flash(f"{exercise_name} has been added!")
    return redirect(url_for('plan.viewAllExercises'))

@plan.route('/remove/<int:exercise_id>')
def removeFromPlan(exercise_id):
    print(exercise_id)
    exercise_search = Exercise.query.get(exercise_id)
    print(exercise_search)
    exercise_search.deleteFromPlan(current_user)
    return redirect(url_for('plan.viewMyPlan'))   

@plan.route('/remote-all')
def removeAllFromPlan():
    current_user.planed = []
    db.session.commit()
    return redirect(url_for('plan.viewMyPlan'))

@plan.route('/view-single-item/<int:exercise_id>')
def viewSingleExercise(exercise_id):
    exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
    return render_template('single_exercise.html',exercise=exercise)

@plan.route('/view-all-exercise')
def viewAllExercises():
    exercise = Exercise.query.order_by(Exercise.exercise_id).all()
    return render_template('all_exercise.html', exercise=exercise)