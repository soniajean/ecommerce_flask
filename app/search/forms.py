from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class CreateExerForm(FlaskForm):
    id = StringField('id') 
    exer_id = StringField('exer_id') 
    name = StringField("Name", validators = [DataRequired()])
    type = StringField("Type")
    muscle = StringField("Muscle")
    equipment = StringField("Equipment")
    difficulty = StringField("Difficulty")
    instructions = IntegerField('Instructions')
    date_created = StringField('Date Created')
    submit = SubmitField()


class UpdateExerForm(FlaskForm):
    id = StringField('id') 
    exer_id = StringField('exer_id') 
    name = StringField("Name", validators = [DataRequired()])
    type = StringField("Type")
    muscle = StringField("Muscle")
    equipment = StringField("Equipment")
    difficulty = StringField("Difficulty")
    instructions = IntegerField('Instructions')
    date_created = StringField('Date Created')
    submit = SubmitField()