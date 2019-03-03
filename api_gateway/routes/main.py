from flask import request

from api_gateway.setup import app, rpc_object as rpc


@app.route('/', methods=['POST'])
def main():
    rpc.main.handler_bot(request.get_json())
    return ""
