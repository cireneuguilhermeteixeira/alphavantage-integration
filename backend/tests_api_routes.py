from flask import Flask
from flask_testing import TestCase
import app as api



class MyTest(TestCase):

    def create_app(self):
        app = api.create_app()
        app.config['TESTING'] = True
        return app

    def test_server_is_up_and_running(self):
        response = self.client.get('/alphavantage/buscar-por-simbolo/')
        self.assertEqual(response.status_code, 200)