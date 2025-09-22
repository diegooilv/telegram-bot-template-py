from typing import Any

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def info(update: Update, context: Any) -> None:
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    info_text = (
        f"🧑 <b>Informações do Usuário</b>\n"
        f"ID: <code>{user.id}</code>\n"
        f"Nome: <code>{user.first_name} {user.last_name or ''}</code>\n"
        f"Username: <code>@{user.username or 'Não tem'}</code>\n"
        f"Idioma: <code>{user.language_code or 'Desconhecido'}</code>\n"
        f"É bot?: <code>{'Sim' if user.is_bot else 'Não'}</code>\n\n"
        f"💬 <b>Informações do Chat</b>\n"
        f"ID: <code>{chat.id}</code>\n"
        f"Tipo: <code>{chat.type}</code>\n"
        f"Título: <code>{chat.title or 'Não tem'}</code>\n"
        f"Username: <code>@{chat.username or 'Não tem'}</code>\n\n"
        f"📝 <b>Informações da Mensagem</b>\n"
        f"ID: <code>{message.message_id}</code>\n"
        f"Data: <code>{message.date.strftime('%Y-%m-%d %H:%M:%S')}</code>\n"
        f"Texto: <code>{message.text or 'Não é texto'}</code>\n"
    )

    await update.message.reply_text(info_text, parse_mode="HTML")

async def bot_info(update: Update, context: Any) -> None:
    info_text = (
        "<b>🤖 Bot Template</b>\n\n"
        "Este bot foi criado como <b>template</b> para desenvolvedores que desejam iniciar seus próprios projetos de bot no Telegram.\n"
        "Com exemplos práticos de comandos, menus interativos e integração com bibliotecas modernas, ele serve como ponto de partida para qualquer tipo de bot!\n\n"
        "Principais características:\n"
        "• Estrutura fácil de entender\n"
        "• Comandos prontos para editar e expandir\n"
        "• Menu interativo e respostas personalizadas\n"
        "• Pronto para deploy na nuvem\n\n"
        "👉 Para acessar o código-fonte, exemplos e documentação, clique no botão abaixo:\n"
    )

    github_url = "https://github.com/diegooilv/telegram-bot-template-py"
    keyboard = [
        [InlineKeyboardButton("🌐 GitHub do Template", url=github_url)],
        [InlineKeyboardButton("📚 Documentação Python Telegram Bot",
                              url="https://docs.python-telegram-bot.org/en/stable/")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        info_text,
        reply_markup=reply_markup
    )