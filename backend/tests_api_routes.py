from flask import Flask
from flask_testing import TestCase
import app as api
import json
from random import randint



class MyTest(TestCase):

    def create_app(self):
        app = api.create_app()
        app.config['TESTING'] = True
        return app

    #### endpoints Alphavantage ####
    def test_busca_por_simbolo(self):
        response = self.client.get('/alphavantage/buscar-por-simbolo/?symbol=^BVSP&interval=5&outputsize=full')
        self.assertEqual(response.status_code, 200)

    def test_busca_por_chave(self):
        response = self.client.get('/alphavantage/buscar-por-chave/vale')
        self.assertEqual(response.status_code, 200)

    
    #### endpoints Usuário ####
    def test_cadastrar_usuario(self):
        dado = {
            "nome":'Usuário teste',
            "idade": '25',
            "profissao":'Astronauta'
        }
        response = self.client.post('/usuario/cadastrar/', json=dado)
        self.assertEqual(response.status_code, 201)


    def test_editar_usuario(self):
        dado = {
            "nome":'Usuário teste',
            "idade": '25',
            "profissao":'Astronauta',
            "id": 6,
        }
        response = self.client.put('/usuario/editar/', json=dado)
        self.assertEqual(response.status_code, 201)


    def test_listar_usuario(self):
        response = self.client.get('/usuario/mostrar/')
        self.assertEqual(response.status_code, 200)


    def test_deletar_usuario(self):
        response = self.client.delete('/usuario/deletar/6')
        self.assertEqual(response.status_code, 200)



    #### endpoints Empresas ####
    def test_cadastrar_empresa(self):
        dado = {	
            "symbol": "APLE"+str(randint(0,9999999)),
            "name": "Apple Hospitality REIT Inc.",
            "type": "Equity",
            "region": "United States",
            "marketOpen": "09:30",
            "marketClose": "16:00",
            "timezone": "UTC-05",
            "currency": "USD",
            "matchScore": "1.0000"
        }
        response = self.client.post('/empresa/cadastrar/', json=dado)
        self.assertEqual(response.status_code, 201)


    def test_editar_empresa(self):
        dado = {
            "id": "200",
            "symbol": "APLE(editado)",
            "name": "Apple Hospitality REIT Inc.",
            "type": "Equity",
            "region": "United States",
            "marketOpen": "09:30",
            "marketClose": "16:00",
            "timezone": "UTC-05",
            "currency": "USD",
            "matchScore": "1.0000"
        }
        response = self.client.put('/empresa/editar/', json=dado)
        self.assertEqual(response.status_code, 201)


    def test_listar_empresa(self):
        response = self.client.get('/empresa/mostrar/')
        self.assertEqual(response.status_code, 200)


    def test_deletar_empresa(self):
        response = self.client.delete('/empresa/deletar/6')
        self.assertEqual(response.status_code, 200)


    #### endpoints Cotações ####
    def test_cadastrar_cotacao(self):
        dados = [
            {
                "symbol": "VALE",
                "date": "2020-06-19 14:21:00",
                "open": "10.3350",
                "high": "10.3400",
                "low": "10.3200",
                "close": "10.3200",
                "volume": "71779"
            },
            {
                "symbol": "VALE",
                "date": "2020-06-19 14:22:00",
                "open": "10.3250",
                "high": "10.3450",
                "low": "10.3200",
                "close": "10.3400",
                "volume": "68944"
            }

        ]
        response = self.client.post('/cotacao/cadastrar/', json=dados)
        self.assertEqual(response.status_code, 201)


    def test_editar_cotacao(self):
        dado =  {
                "close": "10.3200",
                "date": "2020-06-19 14:21:00",
                "empresa_id": "16",
                "high": "10.3400(editado)",
                "id": "4900",
                "low": "10.3200",
                "open": "10.3350",
                "volume": "71779"
        }
        response = self.client.put('/cotacao/editar/', json=dado)
        self.assertEqual(response.status_code, 201)


    def test_listar_cotacao(self):
        response = self.client.get('/cotacao/mostrar/16')
        self.assertEqual(response.status_code, 200)


    def test_deletar_cotacao(self):
        response = self.client.delete('/cotacao/deletar/1')
        self.assertEqual(response.status_code, 200)

        