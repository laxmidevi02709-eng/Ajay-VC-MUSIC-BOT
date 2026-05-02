import logging
from pyrogram import Client
from pytgcalls import PyTgCalls

import config

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)

LOGGER = logging.getLogger("AjayMusic")

# Bot client (handles commands)
bot = Client(
    name="AjayBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
)

# User client (joins voice chats)
user = Client(
    name="AjayUser",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION_STRING,
    in_memory=True,
)

# PyTgCalls instance bound to the user client
call_py = PyTgCalls(user)
