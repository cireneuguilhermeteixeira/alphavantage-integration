from flask import Flask
from flask_migrate import Migrate
from config.database import configure as config_conn
from config.models import configure as config_db
from config.serialize import configure as config_ma
from routes.user import bp_user
from routes.alphavantage import bp_alphavantage


def create_app():

    app = Flask(__name__)
    config_conn(app)
    config_db(app)
    config_ma(app)
    Migrate(app, app.db)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_alphavantage)

    return app
