from flask_marshmallow import Marshmallow
from config.models import Usuario, Empresa, Cotacao

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UsuarioSchema(ma.ModelSchema):
    class Meta:
        model = Usuario

class EmpresaSchema(ma.ModelSchema):
    class Meta:
        model = Empresa

class CotacaoSchema(ma.ModelSchema):
    class Meta:
        model = Cotacao