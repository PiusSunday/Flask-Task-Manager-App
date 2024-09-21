from flask import Flask
from config import Config
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(Config)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .tasks import tasks as tasks_blueprint
    app.register_blueprint(tasks_blueprint)

    from .data_viz import data_viz as data_viz_blueprint
    app.register_blueprint(data_viz_blueprint)

    return app