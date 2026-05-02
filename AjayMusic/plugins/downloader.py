import os
from pyrogram import filters
from pyrogram.types import Message
from AjayMusic import bot
from AjayMusic.utils import youtube, spotify


@bot.on_message(filters.command(["song"]))
async def song_cmd(_, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("Uꜱᴀɢᴇ: /song `<query>`")
    qstr = m.text.split(None, 1)[1]
    if spotify.is_spotify_url(qstr):
        sq = spotify.track_to_query(qstr); qstr = sq or qstr
    s = await m.reply_text("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
    info = await youtube.search(qstr)
    if not info: return await s.edit("❌ Nᴏᴛ ꜰᴏᴜɴᴅ.")
    await s.edit("⬇️ **Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀᴜᴅɪᴏ...**")
    f = await youtube.download(info["link"], audio=True)
    if not f or not os.path.exists(f): return await s.edit("❌ Fᴀɪʟᴇᴅ.")
    await m.reply_audio(f, title=info["title"], performer=info.get("channel", ""),
                        caption=f"🎵 **{info['title']}**\n\n➤ @AjayVcMusicBot")
    await s.delete()


@bot.on_message(filters.command(["video"]))
async def video_cmd(_, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("Uꜱᴀɢᴇ: /video `<query>`")
    qstr = m.text.split(None, 1)[1]
    s = await m.reply_text("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
    info = await youtube.search(qstr)
    if not info: return await s.edit("❌ Nᴏᴛ ꜰᴏᴜɴᴅ.")
    await s.edit("⬇️ **Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴠɪᴅᴇᴏ...**")
    f = await youtube.download(info["link"], audio=False)
    if not f or not os.path.exists(f): return await s.edit("❌ Fᴀɪʟᴇᴅ.")
    await m.reply_video(f, caption=f"**{info['title']}**\n\n➤ @AjayVcMusicBot")
    await s.delete()
