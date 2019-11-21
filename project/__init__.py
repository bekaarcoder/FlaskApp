from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

# secret key setup
app.config['SECRET_KEY'] = 'secretkey'

# db setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Import Blueprints
from project.owners.views import owners_blueprint
from project.tasks.views import tasks_blueprint
from project.users.views import users_blueprint

app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
app.register_blueprint(users_blueprint, url_prefix='/users')
