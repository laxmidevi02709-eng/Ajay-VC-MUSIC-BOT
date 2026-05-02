from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config


def start_buttons() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Aᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{config.BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("📚 Hᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("✦ Aʙᴏᴜᴛ", callback_data="about"),
        ],
        [
            InlineKeyboardButton("📢 Mᴀɪɴ Cʜᴀɴɴᴇʟ", url=config.MAIN_CHANNEL),
            InlineKeyboardButton("🎁 Gɪᴠᴇᴀᴡᴀʏ", url=config.SECOND_CHANNEL),
        ],
        [InlineKeyboardButton("🔒 Pʀɪᴠᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=config.PRIVATE_CHANNEL)],
        [InlineKeyboardButton("👨‍💻 Oᴡɴᴇʀ - @agajayofficial",
            url=f"https://t.me/{config.OWNER_USERNAME}")],
    ])


def help_buttons() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="start")]])


def player_buttons(chat_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⏪ -10s", callback_data=f"ctrl|seekback|{chat_id}"),
            InlineKeyboardButton("⏯ Pᴀᴜꜱᴇ", callback_data=f"ctrl|pause|{chat_id}"),
            InlineKeyboardButton("⏩ +10s", callback_data=f"ctrl|seek|{chat_id}"),
        ],
        [
            InlineKeyboardButton("▶ Rᴇꜱᴜᴍᴇ", callback_data=f"ctrl|resume|{chat_id}"),
            InlineKeyboardButton("⏭ Sᴋɪᴘ", callback_data=f"ctrl|skip|{chat_id}"),
            InlineKeyboardButton("⏹ Sᴛᴏᴘ", callback_data=f"ctrl|stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton("🔊 Vᴏʟ +", callback_data=f"ctrl|volup|{chat_id}"),
            InlineKeyboardButton("🔉 Vᴏʟ -", callback_data=f"ctrl|voldn|{chat_id}"),
            InlineKeyboardButton("🔁 Lᴏᴏᴘ", callback_data=f"ctrl|loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton("📢 Cʜᴀɴɴᴇʟ", url=config.MAIN_CHANNEL),
            InlineKeyboardButton("👨‍💻 Oᴡɴᴇʀ", url=f"https://t.me/{config.OWNER_USERNAME}"),
        ],
    ])
