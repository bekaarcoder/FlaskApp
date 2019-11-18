from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Task
from project.tasks.forms import AddForm, DeleteForm

tasks_blueprint = Blueprint('tasks', __name__, template_folder='templates/tasks')

@tasks_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        task = form.task.data
        new_task = Task(task)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html', form=form)

@tasks_blueprint.route('/admin', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        id = form.id.data
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('delete.html', form=form)
