from typing import Any

from telegram import Update

async def button(update: Update, context: Any) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "op1":
        await query.edit_message_text("Você escolheu a opção 1 ✅")
    elif query.data == "op2":
        await query.edit_message_text("Você escolheu a opção 2 ✅")
    elif query.data == "op3":
        await query.edit_message_text("Você escolheu a opção 3 ✅")
    else:
        await query.edit_message_text("Opção desconhecida ❓")
