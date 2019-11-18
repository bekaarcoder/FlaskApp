from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Add Task')

class DeleteForm(FlaskForm):
    id = IntegerField('Task Id')
    submit = SubmitField('Delete Task')
