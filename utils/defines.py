###Configurações do banco de dados###
import os

POSTGRES_USER = os.environ['POSTGRES_USER']

POSTGRES_PW = os.environ['POSTGRES_PW']

POSTGRES_URL = os.environ['POSTGRES_URL']

POSTGRES_DB =os.environ['POSTGRES_DB']





###Parâmetros da query no Alphavantage###

URL_ALPHAVANTAGE  = 'https://www.alphavantage.co'

#chave de acesso da alphavantage
API_KEY = '3QFZFC6P6CZ8LQRAs'

#symbols
BOVESPA_SIMBOL = '^BVSP'

#functions
TIME_SERIES_INTRADAY = 'TIME_SERIES_INTRADAY'
SYMBOL_SEARCH = 'SYMBOL_SEARCH'

#intervals
INTERVAL_DIC = {
    1: '1min',
    5: '5min',
    15: '15min',
    30: '30min',
    60: '60min'
}