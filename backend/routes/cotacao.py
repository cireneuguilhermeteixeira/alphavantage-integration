from flask import Blueprint, current_app, request, jsonify
from config.models import Cotacao
from config.serialize import CotacaoSchema



bp_cotacao = Blueprint('cotacao',__name__)

@bp_cotacao.route('/cotacao/mostrar/', methods = ['GET'])
def mostrar():
   try:
      ct = CotacaoSchema(many = True)
      result = Cotacao.query.all()
      return ct.jsonify(result),200
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406


@bp_cotacao.route('/cotacao/cadastrar/', methods = ['POST'])
def cadastrar():
   try:
      ct = CotacaoSchema()
      cotacao, error = ct.load(request.json)
      current_app.db.session.add(cotacao)
      current_app.db.session.commit()
      return ct.jsonify(cotacao), 201
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406
   


@bp_cotacao.route('/cotacao/deletar/<id>', methods = ['DELETE'])
def deletar(id):
   try:
      Cotacao.query.filter(Cotacao.id == id).delete()
      current_app.db.session.commit()
      return jsonify('Objeto deletado!!!')
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406
   
   

@bp_cotacao.route('/cotacao/editar/', methods = ['PUT'])
def editar():
   try:
      ct = CotacaoSchema()
      cotacao = request.json
      print (cotacao)
      query = Cotacao.query.filter(Cotacao.id == cotacao['id'])
      query.update(cotacao)
      current_app.db.session.commit()
      return ct.jsonify(query.first())
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406
   
