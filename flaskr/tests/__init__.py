import flask
import sys
import os.path as path
three_up = path.abspath(path.join(__file__ ,"../../.."))
sys.path.append(
    path.abspath(path.join(path.dirname(__file__), three_up)))
from flaskr.modelos.modelos import Usuario
import unittest
from flask import Flask

from flaskr.app import db

class BaseTestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_test_app('testing')

        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()
            BaseTestClass.create_user('admin@xyz.com', '1111')

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    @staticmethod
    def create_user(name, contrasena):
        nuevo_usuario = Usuario(nombre=name, contrasena=contrasena)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario

    def login(self, name, contrasena):
        return self.client.post('/logIn', data=dict(
            nombre=name,
            contrasena=contrasena
        ), follow_redirects=True)



def create_test_app(config_name):
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial_canciones_test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta-2'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app