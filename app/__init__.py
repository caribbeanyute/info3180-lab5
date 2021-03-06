from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
#app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:info3180lab5@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
