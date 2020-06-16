from flask import Blueprint, current_app, request, jsonify
from requests import get
from utils.defines import URL_ALPHAVANTAGE, API_KEY, BOVESPA_SIMBOL, INTERVAL_DIC, TIME_SERIES_INTRADAY, SYMBOL_SEARCH 



bp_alphavantage = Blueprint('alphavantage',__name__)


@bp_alphavantage.route('/buscar-por-simbolo/', methods = ['GET'])
def pontos_bovespa():
    try:
        symbol = request.args.get('symbol')
        interval = request.args.get('interval')
        if symbol is None:
            symbol = BOVESPA_SIMBOL

        if interval is None:
            interval = '5'
        interval = int(interval)
        
    except Exception as exceptionMessage:
        return jsonify( {'message' : str(exceptionMessage)}),406

    if(interval not in INTERVAL_DIC):
        return jsonify({'message' : 'Erro encontrado. Tempo informado inválido'} ), 406
    
    return get(URL_ALPHAVANTAGE+'/query?'+
           'function='+TIME_SERIES_INTRADAY+
           '&symbol='+symbol+
           '&interval='+INTERVAL_DIC[interval]+
           "&outputsize= full"+
           '&apikey='+API_KEY).json()


@bp_alphavantage.route('/buscar-por-chave/<keywords>', methods = ['GET'])
def buscar_por_chave(keywords):
    return get(URL_ALPHAVANTAGE+'/query?'+
        'function='+SYMBOL_SEARCH+
        '&keywords='+keywords+
        '&apikey='+API_KEY).json()
