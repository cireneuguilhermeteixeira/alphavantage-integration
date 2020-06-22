from flask import Blueprint, current_app, request, jsonify
from config.models import Empresa, Cotacao
from config.serialize import EmpresaSchema



bp_empresa = Blueprint('empresa',__name__)

@bp_empresa.route('/empresa/mostrar/', methods = ['GET'])
def mostrar():
   try:
      us = EmpresaSchema(many = True)
      result = Empresa.query.all()
      return us.jsonify(result),200
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406

  



@bp_empresa.route('/empresa/cadastrar/', methods = ['POST'])
def cadastrar():
   try:
      us = EmpresaSchema()
      empresa, error = us.load(request.json)      
      query = Empresa.query.filter(Empresa.symbol == empresa.symbol)
      if(query.first() is None):
         current_app.db.session.add(empresa)
         current_app.db.session.commit()
         return us.jsonify(empresa), 201   
      else:
         return jsonify({'message':'Essa empresa já foi salva.'}), 406
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406
   



@bp_empresa.route('/empresa/deletar/<id>', methods = ['DELETE'])
def deletar(id):
   try:
      Cotacao.query.filter(Cotacao.empresa_id == id).delete()
      Empresa.query.filter(Empresa.id == id).delete()
      current_app.db.session.commit()
      return jsonify('Objeto deletado!!!'),200
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406


  


   

@bp_empresa.route('/empresa/editar/', methods = ['PUT'])
def editar():
   try:
      us = EmpresaSchema()
      empresa = request.json
      print(empresa)
      query = Empresa.query.filter(Empresa.id == empresa['id'])
      query.update(empresa)
      current_app.db.session.commit()
      return us.jsonify(query.first()), 201
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406


  
