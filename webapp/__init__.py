from flask import Flask
from flask_login import LoginManager

from webtrack.webapp.db import db
from webtrack.webapp.user.models import User
from webtrack.webapp.weather import weather_by_city
from webtrack.webapp.config import SECRTET_KEY

from webtrack.webapp.user.views import blueprint as user_blueprint
from webtrack.webapp.admin.views import blueprint as admin_blueprint
from webtrack.webapp.news.views import blueprint as news_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config['SECRET_KEY'] = SECRTET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
