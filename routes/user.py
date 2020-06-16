from flask import Blueprint, current_app, request, jsonify
from config.models import Usuario
from config.serialize import UsuarioSchema



bp_user = Blueprint('usuarios',__name__)

@bp_user.route('/mostrar', methods = ['GET'])
def mostrar():
   us = UsuarioSchema(many = True)
   result = Usuario.query.all()
   return us.jsonify(result),200



@bp_user.route('/cadastrar', methods = ['POST'])
def cadastrar():
   us = UsuarioSchema()
   usuario, error = us.load(request.json)
   current_app.db.session.add(usuario)
   current_app.db.session.commit()
   return us.jsonify(usuario), 201



@bp_user.route('/deletar/<id>', methods = ['DELETE'])
def deletar(id):
    Usuario.query.filter(Usuario.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Objeto deletado!!!')


   

@bp_user.route('/editar', methods = ['PUT'])
def editar():
    us = UsuarioSchema()
    usuario = request.json
    print (usuario)
    query = Usuario.query.filter(Usuario.id == usuario['id'])
    query.update(book)
    current_app.db.session.commit()
    return us.jsonify(query.first())
