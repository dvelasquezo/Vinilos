import sys
import os.path as path
three_up = path.abspath(path.join(__file__ ,"../../.."))
sys.path.append(
    path.abspath(path.join(path.dirname(__file__), three_up)))
from flaskr.tests import BaseTestClass
from flaskr.modelos.modelos import Usuario, db
from flaskr.app import app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import unittest
import json

class RelacionarUsuarioCancionTestCase(BaseTestClass):
    def test_compartir_album_endpoint(self):
        with app.test_client() as client:
            url = '/album/1/compartir'
            result = client.get(
                url
            )
            self.assertEqual(
                result.status_code,
                405
            )

if __name__ == '__main__':
    unittest.main()
