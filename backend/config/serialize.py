from flask_marshmallow import Marshmallow
from config.models import Usuario, Empresa, Cotacao
from marshmallow import fields


ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UsuarioSchema(ma.ModelSchema):
    class Meta:
        model = Usuario

    nome        = fields.Str(required=True)
    idade       = fields.Str(required=True)
    profissao   = fields.Str(required=True)

class EmpresaSchema(ma.ModelSchema):
    class Meta:
        model = Empresa

    symbol      = fields.Str(required=True)
    name        = fields.Str(required=True)
    type        = fields.Str(required=True)
    region      = fields.Str(required=True)
    marketOpen  = fields.Str(required=True)
    marketClose = fields.Str(required=True)
    timezone    = fields.Str(required=True)
    currency    = fields.Str(required=True)
    matchScore  = fields.Str(required=True)


class CotacaoSchema(ma.ModelSchema):
    class Meta:
        model = Cotacao
    open        = fields.Str(required=True)
    high        = fields.Str(required=True)
    low         = fields.Str(required=True)
    close       = fields.Str(required=True)
    volume      = fields.Str(required=True)
    empresa_id  = fields.Str(required=True)