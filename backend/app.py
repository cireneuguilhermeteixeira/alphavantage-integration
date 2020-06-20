from flask import Flask
from flask_migrate import Migrate
from config.database import configure as config_conn
from config.models import configure as config_db
from config.serialize import configure as config_ma
from routes.usuario import bp_usuario
from routes.empresa import bp_empresa
from routes.cotacao import bp_cotacao
from routes.alphavantage import bp_alphavantage
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    CORS(app)
    config_conn(app)
    config_db(app)
    config_ma(app)
    Migrate(app, app.db)
    app.register_blueprint(bp_alphavantage)
    app.register_blueprint(bp_usuario)
    app.register_blueprint(bp_empresa)
    app.register_blueprint(bp_cotacao)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()