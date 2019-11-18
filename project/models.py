# setup db inside __init__.py
from project import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)
    owner = db.relationship('Owner', backref='tasks', uselist=False)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        if self.owner:
            return f"Task: #{self.id} - {self.task}. Added by {self.owner.name}"
        else:
            return f"Task: #{self.id} - {self.task}."

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))

    def __init__(self, name, task_id):
        self.name = name
        self.task_id = task_id
