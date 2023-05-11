# This is how flask knows what to do with it's self. This explains flask is
from flask import Flask
from config import Config
from .api.routes import api
from .models import db, User, Exercise
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_moment import Moment

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
login = LoginManager()
moment = Moment(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view='auth.loginPage'

app.register_blueprint(api)


from . import routes 