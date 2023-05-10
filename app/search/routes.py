from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import CreateExerForm, UpdateExerForm
from app.models import Exercise

search = Blueprint('search', __name__, template_folder='search_templates')

@search.route('/search', methods=['GET'])
def search_home():
    exer = Exercise.query.order_by(Exercise.date_created.desc()).all()
    return render_template('shop_home.html', exer = exer)

@search.route('/search/create', methods=['GET', 'POST'])
def createExer():
    form = CreateExerForm()
    if request.method == 'POST':
        if form.validate():
            exercise_id = form.id.data
            id = form.id.data
            title = form.title.data
            price = form.price.data
            desc = form.desc.data
            category = form.category.data
            img_url = form.img_url.data
            date_created = form.date_created.data

            new = Exercise(id, exercise_id, title, price, desc, category, img_url, date_created)
            new.saveExercise()
            flash('Exercise created!', category='success')
            return redirect(url_for('search.search_home'))
    return render_template('create_exer.html', form=form)

@search.route('/search/exercise/<int:exer_id>')
def indExer(exer_id):
    exer = Exercise.query.get(exer_id)
    return render_template('exercise.html', exer = exer)

@search.route('/search/update/<int:exer_id>', methods=['GET', 'POST'])
def updateExer(exer_id):
    form = UpdateExerForm()
    exer = Exercise.query.get(exer_id)
    if request.method == 'POST':
       exercise_id = form.exercise_id.data
       id = form.id.data
       title = form.title.data
       price = form.price.data
       desc = form.desc.data
       category = form.category.data
       img_url = form.img_url.data
       date_created = form.date_created.data

       exer.exer_id = exercise_id
       exer.id = id
       exer.title = title
       exer.price = price
       exer.desc = desc
       exer.category = category
       exer.img_url = img_url
       date_created = date_created
       exer.saveChanges()
       flash('Exercise updated!', category='success')
       return redirect(url_for('shop.indProd', exer_id=exer_id))
    return render_template('update_exer.html', exer=exer, form=form)

@search.get('/search/delete/<int:exer_id>')
def delProd(exer_id):
    exer = Exercise.query.get(exer_id)
    exer.deleteExercise()
    flash('Exercise has been deleted- Byebye!', category='danger')
    return redirect(url_for('search.search_home'))