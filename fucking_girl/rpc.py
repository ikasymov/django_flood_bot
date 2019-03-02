from nameko.rpc import rpc

class FuckingGirls:
    name = 'fucking_girls'

    @rpc
    def get(self, name):
        return {'result': name}