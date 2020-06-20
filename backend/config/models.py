from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db



##Modelo do usuário
class Usuario(db.Model):
    __tablename__ = 'usuario'

    id          = db.Column(db.Integer,     primary_key = True)
    nome        = db.Column(db.String(255), nullable=False)
    idade       = db.Column(db.String(255), nullable=False)
    profissao   = db.Column(db.String(255), nullable=False)


##Modelo do usuário
class Empresa(db.Model):
    __tablename__ = 'empresa'

    id          = db.Column(db.Integer,     primary_key = True)
    symbol      = db.Column(db.String(255), nullable=False)
    name        = db.Column(db.String(255), nullable=False)
    type        = db.Column(db.String(255), nullable=False)
    region      = db.Column(db.String(255), nullable=False)
    marketOpen  = db.Column(db.String(255), nullable=False)
    marketClose = db.Column(db.String(255), nullable=False)
    timezone    = db.Column(db.String(255), nullable=False)
    currency    = db.Column(db.String(255), nullable=False)
    matchScore  = db.Column(db.String(255), nullable=False)
    cotacoes    = relationship("Cotacao",   back_populates="empresa")


class Cotacao(db.Model):
    __tablename__ = 'cotacao'

    id          = db.Column(db.Integer,     primary_key = True)
    open        = db.Column(db.String(255), nullable=False)
    high        = db.Column(db.String(255), nullable=False)
    low         = db.Column(db.String(255), nullable=False)
    close       = db.Column(db.String(255), nullable=False)
    volume      = db.Column(db.String(255), nullable=False)
    date        = db.Column(db.String(255), nullable=False)
    empresa_id  = db.Column(db.Integer,     db.ForeignKey('empresa.id'))
    empresa     = relationship("Empresa",   back_populates="cotacoes")
