# Template de Bot – Telegram

Um template enxuto e modular para você criar bots no Telegram com rapidez e boas práticas. Este projeto serve como base para iniciar novos bots, com estrutura organizada, comandos prontos e fácil expansão.

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4.svg)](https://core.telegram.org/bots)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Demonstração

- Veja o bot online: [@TemplateBot](https://t.me/template_github_diegooilv_bot)
- Hospedagem sugerida: [fps.ms – Free Telegram Bot Hosting](https://fps.ms/free-telegram-bot-hosting/)

---

## Principais recursos

- Estrutura modular (cada comando em seu próprio handler).
- Registro centralizado de comandos e callbacks.
- Mensagens com formatação HTML e teclado inline.
- Pronto para logs configuráveis via variável de ambiente (`LOG_LEVEL`).
- Fácil de adaptar, testar e fazer deploy.

---

## Estrutura do projeto

```
src/
├─ run.py                      # Inicia o bot (Application, carregamento do .env e bootstrap)
└─ handlers/
   ├─ commands.py              # Registro de todos os handlers (comandos, callbacks, erros)
   ├─ start.py                 # /start
   ├─ menu.py                  # /menu
   ├─ info.py                  # /info e /botinfo
   ├─ callbacks.py             # CallbackQueryHandler (botões)
   └─ error.py                 # Tratamento de erros
```

> Dica: acrescente `__init__.py` nas pastas para facilitar imports.

---

## Requisitos

- Python 3.13+  
- Token de bot do Telegram (via [@BotFather](https://t.me/BotFather))

---

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
TELEGRAM_BOT_TOKEN=coloque_seu_token_aqui
LOG_LEVEL=INFO
```

- `LOG_LEVEL` pode ser: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

---

## Instalação

```bash
# (opcional) crie e ative um ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# instale as dependências
pip install -r requirements.txt
```

---

## Execução local

```bash
python src/run.py
```

Por padrão, o template utiliza Long Polling. Para produção com Webhook, ajuste a configuração conforme sua hospedagem.

---

## Comandos disponíveis

- `/start` – Mensagem de boas-vindas e lista de comandos.
- `/menu` – Exibe o menu interativo com botões.
- `/info` – Mostra informações do usuário/chat/mensagem.
- `/botinfo` – Explica que o projeto é um template e aponta para o GitHub.

Callbacks e tratamento de erros são registrados automaticamente no `handlers/commands.py`.

---

## Exemplos

### Handler do /start

```python
# src/handlers/start.py
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
        "Se encontrar algum erro, ele será tratado automaticamente 😉",
        parse_mode="HTML",
    )
```

### Registro centralizado dos handlers

```python
# src/handlers/commands.py
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from . import start, menu, info, callbacks, error

def register_handlers(app: Application) -> None:
    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("menu", menu.menu))
    app.add_handler(CommandHandler("info", info.info))
    app.add_handler(CommandHandler("botinfo", info.bot_info))
    app.add_handler(CallbackQueryHandler(callbacks.button))
    app.add_error_handler(error.error)
```

### Inicialização do bot

```python
# src/run.py
from __future__ import annotations

import os

from dotenv import load_dotenv
from pathlib import Path

from telegram.constants import ParseMode
from telegram.ext import Defaults, Application

from handlers.commands import registrar_comandos

def main() -> None:
    load_dotenv()
    bot_env = Path(__file__).resolve().parent / ".env"
    if bot_env.exists():
        load_dotenv(dotenv_path=bot_env, override=True)
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise RuntimeError("Defina o Token do Bot em .env! TELEGRAM_BOT_TOKEN=")
    defaults = Defaults(parse_mode=ParseMode.HTML)
    app = (
        Application.builder()
        .token(bot_token)
        .defaults(defaults)
        .build()
    )
    registrar_comandos(app)
    try:
        app.run_polling()
    except KeyboardInterrupt:
        print("Bot interrompido!")

if __name__ == "__main__":
    main()
```

---

## Deploy

- [fps.ms – Free Telegram Bot Hosting](https://fps.ms/free-telegram-bot-hosting/)

---

## Contribuindo

Contribuições são bem-vindas!  
Abra uma issue, envie um PR ou sugira melhorias.

---

## Licença

[MIT](LICENSE)