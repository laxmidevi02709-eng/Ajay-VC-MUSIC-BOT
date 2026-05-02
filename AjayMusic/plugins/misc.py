import time
from pyrogram import filters
from pyrogram.types import Message
from AjayMusic import bot


@bot.on_message(filters.command(["ping"]))
async def ping_cmd(_, m: Message):
    t = time.time()
    r = await m.reply_text("🏓 ...")
    await r.edit(f"🏓 **Pᴏɴɢ!** `{round((time.time()-t)*1000)}ms`\n→ @AjayVcMusicBot")


@bot.on_message(filters.command(["stats"]))
async def stats_cmd(_, m: Message):
    from AjayMusic.core import queue as q
    active = sum(1 for s in q._state.values() if s.current)
    await m.reply_text(
        f"**✦ AJAY VC MUSIC - Sᴛᴀᴛꜱ**\n→ Aᴄᴛɪᴠᴇ VC: `{active}`\n→ Oᴡɴᴇʀ: @agajayofficial"
    )
