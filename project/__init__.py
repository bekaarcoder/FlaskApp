from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# secret key setup
app.config['SECRET_KEY'] = 'secretkey'

# db setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Import Blueprints
from project.owners.views import owners_blueprint
from project.tasks.views import tasks_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
