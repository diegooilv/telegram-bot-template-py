from telegram.ext import CommandHandler, CallbackQueryHandler
from . import start, info, callbacks, menu, error

def registrar_comandos(app):
    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("menu", menu.menu))
    app.add_handler(CommandHandler("info", info.info))
    app.add_handler(CommandHandler("botinfo", info.bot_info))
    app.add_handler(CallbackQueryHandler(callbacks.button))
    app.add_error_handler(error.error)
