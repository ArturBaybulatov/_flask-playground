from flask import Flask
from flask_cors import CORS

import api, models, routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    CORS(app)
    models.db.init_app(app)
    app.register_blueprint(routes.example)

    api.manager.init_app(app, flask_sqlalchemy_db=models.db)
    api.set_endpoints(app)

    return app
