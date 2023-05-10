from flask import Blueprint, render_template, request, url_for, redirect, flash
plan = Blueprint('plan', __name__, template_folder='plan_templates')
from flask_login import current_user, login_required
from app.models import User, Exercise, db


@plan.route('/my-plan')
def viewMyplan():
    exercise = current_user.planed
    plan_total = 0
    for e in exercise:
        plan_total += (p.price)
    return render_template('my_plan.html', exercise=exercise, total=plan_total)

@plan.route('/add/<int:exercise_id>')
def addToplan(exercise_id):
    exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
    exercise.saveToplan(current_user)
    exercise_name=exercise.title
    flash(f"{exercise_name} has been added!")
    return redirect(url_for('plan.viewAllExercise'))

@plan.route('/remove/<int:exercise_id>')
def removeFromplan(exercise_id):
    print(exercise_id)
    exercise_search = Exercise.query.get(exercise_id)
    print(exercise_search)
    exercise_search.deleteFromplan(current_user)
    return redirect(url_for('plan.viewMyplan'))   

@plan.route('/remote-all')
def removeAllFromplan():
    current_user.planed = []
    db.session.commit()
    return redirect(url_for('plan.viewMyplan'))

@plan.route('/view-singe-item/<int:exercise_id>')
def viewSingleExercise(exercise_id):
    exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
    return render_template('single_exercise.html',exercise=exercise)

@plan.route('/view-all-exercise')
def viewAllExercise():
    exercise = Exercise.query.order_by(Exercise.exercise_id).all()
    return render_template('all_exercise.html', exercise=exercise)