from models import Exercise
from api.services import get_exercise
from flask_login import current_user

x = get_exercise(12)
print(f"~~~~{x}")

e = Exercise(title=x['exercise_name'],price=x['price'],description=x['description'],category=x['category'],img_url=x['exercise_image'])

e.saveExercise()

# TO add to DB
@app.route('/sendit')
def sendIt():
    x = get_exercise(20)
    print("ADDED TO DB")
    e = Exercise(exercise_id=x['exercise_id'],title=x['exercise_name'],price=x['price'],description=x['description'],category=x['category'],img_url=x['exercise_image'])
    e.saveExercise()
    return render_template('index.html')

#html for it
        # <a class="btn btn-outline-dark justify-content-end" href="{{ url_for('sendIt') }}"
        # role="button">DONT PRESS THIS BUTTON. ITS A FUNCITON TO ADD ITEMS TO DB</a>


#delete from db
 