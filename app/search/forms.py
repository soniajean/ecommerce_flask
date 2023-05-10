from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class CreateExerForm(FlaskForm):
    id = StringField('id') 
    exer_id = StringField('exer_id') 
    title = StringField("Title", validators = [DataRequired()])
    price = IntegerField('Price')
    desc = StringField("Description")
    category = StringField("Category")
    img_url = StringField("Img_url")
    rating = IntegerField('Rating')
    date_created = StringField('Date Created')
    submit = SubmitField()


class UpdateExerForm(FlaskForm):
    id = StringField('id') 
    exer_id = StringField('exer_id') 
    title = StringField('Name of Exercise')
    price = IntegerField('Price')
    desc = StringField("Description")
    category = StringField("Category")
    img_url = StringField("Img_url")
    rating = IntegerField('Rating')
    date_created = StringField('Date Created')
    submit = SubmitField()
