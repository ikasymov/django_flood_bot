import telebot

from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession

from girl.models import DeclarativeBase, Girl
from bot import bot


class FuckingGirls:
    name = 'girl'
    db = DatabaseSession(DeclarativeBase)

    @rpc
    def handler_bot(self, data):
        message = telebot.types.Message.de_json(data)
        bot.reply_to(message, 'Idi na huy')
        return ""
