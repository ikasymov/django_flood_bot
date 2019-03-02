from flask import jsonify

from api_gateway.setup import app, rpc_object as rpc

@app.route('/', methods=['GET'])
def main():
    return jsonify(rpc.fucking_girls.get('name'))