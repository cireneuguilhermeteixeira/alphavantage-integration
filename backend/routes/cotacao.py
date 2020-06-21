from flask import Blueprint, current_app, request, jsonify
from config.models import Cotacao, Empresa
from config.serialize import CotacaoSchema, EmpresaSchema



bp_cotacao = Blueprint('cotacao',__name__)

@bp_cotacao.route('/cotacao/mostrar/<empresa_id>', methods = ['GET'])
def mostrar(empresa_id):
   try:
      ct = CotacaoSchema(many = True)
      result = Cotacao.query.filter(Cotacao.empresa_id == empresa_id)
      return ct.jsonify(result),200
   
   except Exception as exceptionMessage:
      return jsonify( {'message' : str(exceptionMessage)}),406


@bp_cotacao.route('/cotacao/cadastrar/', methods = ['POST'])
def cadastrar():
   try:
   
      emp = EmpresaSchema()
      ct = CotacaoSchema()
      empresa = Empresa.query.filter(Empresa.symbol == request.json[0]['symbol']).first()
      if(empresa is None):
         return jsonify({'message':'Impossível salvar cotações sem salvar empresa;'}), 406
      
      cotacoes = request.json
      for cotacao in cotacoes:
         cotacao['empresa_id'] = emp.jsonify(empresa).json['id']
         del cotacao['symbol']   

         cotacao_formatada = Cotacao(
         low= cotacao['low'], 
         high = cotacao['high'],
         open = cotacao['open'],
         close = cotacao[0]['close'],
         date = cotacao['date'],
         volume = cotacao['volume'],
         empresa_id = cotacao['empresa_id'])
         
         current_app.db.session.add(cotacao_formatada)
         current_app.db.session.commit()

      return ct.jsonify(cotacoes), 201
   
   except Exception as exceptionMessage:
      print (str(exceptionMessage))
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
   
