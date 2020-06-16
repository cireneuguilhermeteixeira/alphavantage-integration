from flask import Blueprint, current_app, request, jsonify
from config.models import Empresa
from config.serialize import EmpresaSchema



bp_empresa = Blueprint('empresa',__name__)

@bp_empresa.route('/empresa/mostrar', methods = ['GET'])
def mostrar():
   us = EmpresaSchema(many = True)
   result = Empresa.query.all()
   return us.jsonify(result),200



@bp_empresa.route('/empresa/cadastrar', methods = ['POST'])
def cadastrar():
   us = EmpresaSchema()
   empresa, error = us.load(request.json)
   current_app.db.session.add(empresa)
   current_app.db.session.commit()
   return us.jsonify(empresa), 201



@bp_empresa.route('/empresa/deletar/<id>', methods = ['DELETE'])
def deletar(id):
    Empresa.query.filter(Empresa.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Objeto deletado!!!')


   

@bp_empresa.route('/empresa/editar', methods = ['PUT'])
def editar():
    us = EmpresaSchema()
    empresa = request.json
    query = Empresa.query.filter(Empresa.id == empresa['id'])
    query.update(book)
    current_app.db.session.commit()
    return us.jsonify(query.first())
