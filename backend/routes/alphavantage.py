from flask import Blueprint, current_app, request, jsonify
from requests import get
from utils.defines import URL_ALPHAVANTAGE, API_KEY, BOVESPA_SIMBOL, INTERVAL_DIC, TIME_SERIES_INTRADAY, SYMBOL_SEARCH 



bp_alphavantage = Blueprint('alphavantage',__name__)



@bp_alphavantage.route('/alphavantage/buscar-por-simbolo/', methods = ['GET'])
def buscar_por_simbolo():
    try:
        symbol = request.args.get('symbol')
        interval = request.args.get('interval')
        outputsize = request.args.get('outputsize')
        print(symbol)
        if outputsize is None or (outputsize != 'full' and outputsize != 'compact'):
            outputsize = 'full'
        if symbol is None:
            symbol = BOVESPA_SIMBOL

        if interval is None:
            interval = '5'
        interval = int(interval)
    except Exception as exceptionMessage:
        return jsonify( {'message' : str(exceptionMessage)}),406

    if(interval not in INTERVAL_DIC):
        return jsonify({'message' : 'Erro encontrado. Tempo informado inválido'} ), 406
    
    url_to_request = URL_ALPHAVANTAGE+'/query?'+'function='+TIME_SERIES_INTRADAY+'&symbol='+symbol+'&interval='+INTERVAL_DIC[interval]+'&outputsize='+outputsize+'&apikey='+API_KEY

    return jsonify(get(url_to_request).json()),200


@bp_alphavantage.route('/alphavantage/buscar-por-chave/<keywords>', methods = ['GET'])
def buscar_por_chave(keywords):
    
    url_to_request = URL_ALPHAVANTAGE+'/query?'+'function='+SYMBOL_SEARCH+'&keywords='+keywords+'&apikey='+API_KEY
    return jsonify (get(url_to_request).json()),200
