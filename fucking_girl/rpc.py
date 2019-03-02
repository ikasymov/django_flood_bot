from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession, Database

from .models import DeclarativeBase


class FuckingGirls:
    name = 'fucking_girls'
    db = DatabaseSession(DeclarativeBase)

    @rpc
    def get(self, name):
        return {'result': name}