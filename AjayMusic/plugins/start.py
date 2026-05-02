from pyrogram import filters
from pyrogram.types import Message
from AjayMusic import bot
from AjayMusic.utils.buttons import start_buttons, help_buttons
import config


@bot.on_message(filters.command(["start"]) & filters.private)
async def start_cmd(_, m: Message):
    await m.reply_text(
        config.START_TEXT,
        reply_markup=start_buttons(),
        disable_web_page_preview=True,
    )


@bot.on_message(filters.command(["start"]) & filters.group)
async def start_grp(_, m: Message):
    await m.reply_text(
        f"**{config.BOT_NAME} ɪꜱ ᴀᴄᴛɪᴠᴇ ʜᴇʀᴇ.**\nUꜱᴇ /play `<ꜱᴏɴɢ ɴᴀᴍᴇ>` ᴛᴏ ᴘʟᴀʏ.",
        reply_markup=start_buttons(),
    )


@bot.on_message(filters.command(["help"]))
async def help_cmd(_, m: Message):
    await m.reply_text(config.HELP_TEXT, reply_markup=help_buttons())
