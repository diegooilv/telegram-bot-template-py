from typing import Any

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update

async def menu(update: Update, context: Any)-> None:
    keyboard = [
        [InlineKeyboardButton("Inter", callback_data="op1")],
        [InlineKeyboardButton("Empate", callback_data="op2")],
        [InlineKeyboardButton("Grêmio", callback_data="op3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text("Escolha uma opção:", reply_markup=reply_markup)