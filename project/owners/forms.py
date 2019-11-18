from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    name = StringField('Owner Name')
    task_id = IntegerField('Task Id')
    submit = SubmitField('Add Owner')
