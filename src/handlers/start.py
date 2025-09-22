from typing import Any
from telegram import Update

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
async def start(update: Update, context: Any) -> None:
    await update.message.reply_text(
        "<b>Olá, eu sou um Bot Template para Telegram!</b> 🤖\n\n"
        "Aqui estão os comandos disponíveis:\n"
        "• <b>/menu</b> – Exibe o menu interativo com opções\n"
        "• <b>/info</b> – Mostra informações detalhadas sobre você e o chat\n"
        "• <b>/botinfo</b> – Explica a função do bot e mostra o link para o template\n"
        "• <b>/start</b> – Exibe esta mensagem de boas-vindas\n\n"
        "Use os comandos acima para explorar as funcionalidades!\n"
        "Se encontrar algum erro, ele será tratado automaticamente 😉"
    )
