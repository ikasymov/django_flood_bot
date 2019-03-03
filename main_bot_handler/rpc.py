import telebot
from nameko.rpc import rpc, RpcProxy

from register_services import services
from bot import bot
from tools import dump_telegram_object


class Main:
    name = 'main'

    @rpc
    def handler_bot(self, data):
        obj = telebot.types.Update.de_json(data)
        if obj.message or obj.channel_post:

            @bot.message_handler(commands=services)
            def dispath_service(message):
                getattr(self, message.text[1:]).handler_bot(dump_telegram_object(message))

            bot.process_new_messages([obj.message or obj.channel_post])
            return ""

for service in services:
    setattr(Main, service, RpcProxy(service))
