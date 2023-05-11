from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.models import Exercise
from .forms import ViewExerForm

search = Blueprint('search', __name__, template_folder='search_templates')

@search.route('/search', methods=['GET'])
def search_home():
    exers = Exercise.query.order_by(Exercise.date_created.desc()).all()
    return render_template('search_home.html', exers = exers)



@search.route('/search/exercise/<int:exer_id>')
def indExer(exer_id):
    exer = Exercise.query.get(exer_id)
    return render_template('exercise.html', exer = exer)


@search.get('/search/delete/<int:exer_id>')
def delExer(exer_id):
    exer = Exercise.query.get(exer_id)
    exer.deleteExercise()
    flash('Exercise has been deleted- Byebye!', category='danger')
    return redirect(url_for('search.search_home'))