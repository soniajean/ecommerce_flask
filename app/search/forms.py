from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class ViewExerForm(FlaskForm):
    id = StringField('id') 
    exercise_id = StringField('exer_id') 
    name = StringField("Name", validators = [DataRequired()])
    type = IntegerField('Type')
    muscle = StringField("Muscle")
    difficuty = StringField("Difficulty")
    equipment = StringField("Equipment")
    instructions = IntegerField('Instructions')
    date_created = StringField('Date Created')
    submit = SubmitField()



