from flask import Blueprint, current_app, request, jsonify
from config.models import Usuario
from config.serialize import UsuarioSchema



bp_usuario = Blueprint('usuario',__name__)

@bp_usuario.route('/usuario/mostrar/', methods = ['GET'])
def mostrar():
   try:
      us = UsuarioSchema(many = True)
      result = Usuario.query.all()
      return us.jsonify(result),200
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406


   



@bp_usuario.route('/usuario/cadastrar/', methods = ['POST'])
def cadastrar():
   try:
      us = UsuarioSchema()
      usuario, error = us.load(request.json)
      print(usuario)
      current_app.db.session.add(usuario)
      current_app.db.session.commit()
      return us.jsonify(usuario), 201
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406





@bp_usuario.route('/usuario/deletar/<id>', methods = ['DELETE'])
def deletar(id):
   try:
      Usuario.query.filter(Usuario.id == id).delete()
      current_app.db.session.commit()
      return jsonify('Objeto deletado!!!')
  
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406
       
    

   

@bp_usuario.route('/usuario/editar/', methods = ['PUT'])
def editar():
   try:
      us = UsuarioSchema()
      usuario = request.json
      print (usuario)
      query = Usuario.query.filter(Usuario.id == usuario['id'])
      query.update(usuario)
      current_app.db.session.commit()
      return us.jsonify(query.first()), 201
   except Exception as exceptionMessage:   
      return jsonify( {'message' : str(exceptionMessage)}),406


   
