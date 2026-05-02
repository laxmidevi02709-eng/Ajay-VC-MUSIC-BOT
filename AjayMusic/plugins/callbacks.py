from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery
from AjayMusic import bot
from AjayMusic.core import streamer, queue as q
from AjayMusic.utils.buttons import start_buttons, help_buttons
import config


async def _edit(c: CallbackQuery, text: str, markup):
    try:
        await c.message.edit_text(text, reply_markup=markup, disable_web_page_preview=True)
    except Exception:
        try:
            await c.message.edit_caption(text, reply_markup=markup)
        except Exception:
            pass


@bot.on_callback_query(filters.regex("^start$"))
async def cb_start(_, c: CallbackQuery):
    await _edit(c, config.START_TEXT, start_buttons())


@bot.on_callback_query(filters.regex("^help$"))
async def cb_help(_, c: CallbackQuery):
    await _edit(c, config.HELP_TEXT, help_buttons())


@bot.on_callback_query(filters.regex("^about$"))
async def cb_about(_, c: CallbackQuery):
    txt = (
        f"**{config.BOT_NAME}**\n\n"
        f"→ Bᴜɪʟᴛ ᴡɪᴛʜ Pʏʀᴏɢʀᴀᴍ + PʏTɢCᴀʟʟꜱ\n"
        f"→ Bᴏᴛ Oᴡɴᴇʀ: @{config.OWNER_USERNAME}\n"
        f"→ Mᴀɪɴ Cʜᴀɴɴᴇʟ: @AjayFFCommunity"
    )
    await _edit(c, txt, help_buttons())


@bot.on_callback_query(filters.regex("^close$"))
async def cb_close(_, c: CallbackQuery):
    try: await c.message.delete()
    except Exception: pass


@bot.on_callback_query(filters.regex(r"^ctrl\|"))
async def cb_ctrl(_, c: CallbackQuery):
    try:
        _, action, chat_id = c.data.split("|")
        chat_id = int(chat_id)
    except Exception:
        return await c.answer("Bᴀᴅ ᴄᴀʟʟʙᴀᴄᴋ.", show_alert=True)

    try:
        member = await c.message.chat.get_member(c.from_user.id)
        if member.status not in (ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR):
            return await c.answer("Aᴅᴍɪɴ ᴏɴʟʏ.", show_alert=True)
    except Exception:
        pass

    state = q.get(chat_id)
    try:
        if action == "pause":
            await streamer.pause(chat_id); await c.answer("Pᴀᴜꜱᴇᴅ ⏸")
        elif action == "resume":
            await streamer.resume(chat_id); await c.answer("Rᴇꜱᴜᴍᴇᴅ ▶")
        elif action == "skip":
            nxt = await streamer.skip(chat_id)
            await c.answer("Sᴋɪᴘᴘᴇᴅ ⏭" if nxt else "Qᴜᴇᴜᴇ ᴇɴᴅᴇᴅ")
        elif action == "stop":
            await streamer.leave(chat_id); await c.answer("Sᴛᴏᴘᴘᴇᴅ ⏹")
        elif action == "volup":
            await streamer.set_volume(chat_id, state.volume + 20); await c.answer(f"🔊 {state.volume}")
        elif action == "voldn":
            await streamer.set_volume(chat_id, state.volume - 20); await c.answer(f"🔉 {state.volume}")
        elif action == "loop":
            state.loop = (state.loop + 1) % 6; await c.answer(f"🔁 Lᴏᴏᴘ {state.loop}")
        elif action in ("seek", "seekback"):
            await c.answer("Sᴇᴇᴋ ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ꜰᴏʀ ᴛʜɪꜱ ꜱᴛʀᴇᴀᴍ ʏᴇᴛ.", show_alert=False)
        else:
            await c.answer()
    except Exception as e:
        await c.answer(f"Eʀʀᴏʀ: {e}", show_alert=True)
