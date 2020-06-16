from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db



##Modelo do usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255))
    idade = db.Column(db.String(255))
    profissao = db.Column(db.String(255))


##Modelo do usuário
class Empresa(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    symbol      = db.Column(db.String(255))
    name        = db.Column(db.String(255))
    type        = db.Column(db.String(255))
    region      = db.Column(db.String(255))
    marketOpen  = db.Column(db.String(255))
    marketClose = db.Column(db.String(255))
    timezone    = db.Column(db.String(255))
    currency    = db.Column(db.String(255))
    matchScore  = db.Column(db.String(255))
    nome        = db.Column(db.String(255))


class Cotacao(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    open = db.Column(db.String(255))
    high = db.Column(db.String(255))
    low = db.Column(db.String(255))
    close = db.Column(db.String(255))
    volume = db.Column(db.String(255))
