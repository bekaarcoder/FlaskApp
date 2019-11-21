# setup db inside __init__.py
from project import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

bcrypt = Bcrypt()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

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
