import os

from flask import Flask
from flask_nameko import FlaskPooledClusterRpcProxy


rpc_object = FlaskPooledClusterRpcProxy()

def create_app():
    app = Flask(__name__)
    app.config.update(dict(
        NAMEKO_AMQP_URI=os.environ['AMQP_URL'],
        SECRET_KEY='this-really-needs-to-be-changed',
        SQLALCHEMY_TRACK_MODIFICATIONS=True
    ))
    rpc_object.init_app(app)
    return app

app = create_app()

from .routes import *

