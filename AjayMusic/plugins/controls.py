from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from AjayMusic import bot
from AjayMusic.core import streamer, queue as q


async def _is_admin(m: Message) -> bool:
    if not m.from_user:
        return False
    try:
        member = await m.chat.get_member(m.from_user.id)
        return member.status in (ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR)
    except Exception:
        return False


@bot.on_message(filters.command(["pause"]) & filters.group)
async def pause_cmd(_, m: Message):
    if not await _is_admin(m): return
    await streamer.pause(m.chat.id)
    await m.reply_text("⏸ **Pᴀᴜꜱᴇᴅ.**")


@bot.on_message(filters.command(["resume"]) & filters.group)
async def resume_cmd(_, m: Message):
    if not await _is_admin(m): return
    await streamer.resume(m.chat.id)
    await m.reply_text("▶ **Rᴇꜱᴜᴍᴇᴅ.**")


@bot.on_message(filters.command(["skip", "next"]) & filters.group)
async def skip_cmd(_, m: Message):
    if not await _is_admin(m): return
    nxt = await streamer.skip(m.chat.id)
    if nxt:
        await m.reply_text(f"⏭ **Sᴋɪᴘᴘᴇᴅ.**\nNᴏᴡ: `{nxt.title}`")
    else:
        await m.reply_text("⏹ **Qᴜᴇᴜᴇ ᴇɴᴅᴇᴅ. Lᴇꜰᴛ VC.**")


@bot.on_message(filters.command(["stop", "end"]) & filters.group)
async def stop_cmd(_, m: Message):
    if not await _is_admin(m): return
    await streamer.leave(m.chat.id)
    await m.reply_text("⏹ **Sᴛᴏᴘᴘᴇᴅ & ʟᴇꜰᴛ VC.**")


@bot.on_message(filters.command(["volume", "vol"]) & filters.group)
async def vol_cmd(_, m: Message):
    if not await _is_admin(m): return
    if len(m.command) < 2 or not m.command[1].isdigit():
        return await m.reply_text("Uꜱᴀɢᴇ: /volume `<1-200>`")
    v = int(m.command[1])
    await streamer.set_volume(m.chat.id, v)
    await m.reply_text(f"🔊 **Vᴏʟᴜᴍᴇ →** `{v}`")


@bot.on_message(filters.command(["loop"]) & filters.group)
async def loop_cmd(_, m: Message):
    if not await _is_admin(m): return
    n = int(m.command[1]) if len(m.command) > 1 and m.command[1].isdigit() else 0
    q.get(m.chat.id).loop = max(0, min(10, n))
    await m.reply_text(f"🔁 **Lᴏᴏᴘ →** `{q.get(m.chat.id).loop}`")
