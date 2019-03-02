import os

from flask import Flask
from flask_nameko import FlaskPooledClusterRpcProxy

rpc_object = FlaskPooledClusterRpcProxy()

def create_app():
    app = Flask(__name__)
    app.config.update(dict(
        NAMEKO_AMQP_URI=os.environ['AMQP_URL'],
        SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
        SECRET_KEY='this-really-needs-to-be-changed'
    ))
    rpc_object.init_app(app)
    return app

app = create_app()
import api_gateway

