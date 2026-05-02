from pyrogram import filters
from pyrogram.types import Message
from AjayMusic import bot, LOGGER
from AjayMusic.utils import youtube, spotify
from AjayMusic.utils.thumb import make_thumb
from AjayMusic.utils.buttons import player_buttons
from AjayMusic.core import queue as q
from AjayMusic.core import streamer


async def _resolve(query: str) -> dict | None:
    if spotify.is_spotify_url(query):
        sq = spotify.track_to_query(query)
        if sq:
            query = sq
    return await youtube.search(query)


async def _play_or_queue(chat_id: int, m: Message, video: bool):
    if len(m.command) < 2 and not (m.reply_to_message and m.reply_to_message.text):
        return await m.reply_text("**Uꜱᴀɢᴇ:** /play `<ꜱᴏɴɢ ɴᴀᴍᴇ>`")

    if len(m.command) > 1:
        query = m.text.split(None, 1)[1]
    else:
        query = m.reply_to_message.text

    status = await m.reply_text("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")

    info = await _resolve(query)
    if not info:
        return await status.edit("❌ Nᴏ ʀᴇꜱᴜʟᴛꜱ ꜰᴏᴜɴᴅ.")

    await status.edit(f"⬇️ **Dᴏᴡɴʟᴏᴀᴅɪɴɢ:** `{info['title']}`")
    file = await youtube.download(info["link"], audio=not video)
    if not file:
        return await status.edit("❌ Dᴏᴡɴʟᴏᴀᴅ ꜰᴀɪʟᴇᴅ.")

    requested_by = m.from_user.first_name if m.from_user else "Unknown"
    track = q.Track(
        title=info["title"],
        duration=info["duration"],
        link=info["link"],
        video_id=info["id"],
        file=file,
        requested_by=requested_by,
        is_video=video,
    )

    state = q.get(chat_id)
    if state.current is None:
        try:
            await streamer.play_track(chat_id, track)
        except Exception as e:
            LOGGER.exception("play err")
            return await status.edit(
                f"❌ **Cᴀɴ'ᴛ ᴊᴏɪɴ VC.**\n`{e}`\n\n→ Sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜰɪʀꜱᴛ & ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ."
            )
        thumb = await make_thumb(track.video_id, track.title, track.duration, requested_by)
        caption = (
            f"**✦ Nᴏᴡ Pʟᴀʏɪɴɢ**\n\n"
            f"🎵 **{track.title}**\n"
            f"⏱  `{track.duration}`\n"
            f"👤  {requested_by}\n\n"
            f"➤ **Bᴏᴛ Oᴡɴᴇʀ:** @agajayofficial"
        )
        await status.delete()
        if thumb:
            await m.reply_photo(thumb, caption=caption, reply_markup=player_buttons(chat_id))
        else:
            await m.reply_text(caption, reply_markup=player_buttons(chat_id))
    else:
        state.queue.append(track)
        await status.edit(
            f"➕ **Aᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ #{len(state.queue)}**\n🎵 `{track.title}`",
        )


@bot.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, m: Message):
    await _play_or_queue(m.chat.id, m, video=False)


@bot.on_message(filters.command(["vplay", "vp"]) & filters.group)
async def vplay_cmd(_, m: Message):
    await _play_or_queue(m.chat.id, m, video=True)


@bot.on_message(filters.command(["playlist", "queue"]) & filters.group)
async def queue_cmd(_, m: Message):
    state = q.get(m.chat.id)
    if not state.current:
        return await m.reply_text("📭 **Qᴜᴇᴜᴇ ɪꜱ ᴇᴍᴘᴛʏ.**")
    text = f"**✦ Nᴏᴡ:** `{state.current.title}`\n\n"
    if state.queue:
        text += "**Uᴘ Nᴇxᴛ:**\n"
        for i, t in enumerate(list(state.queue)[:10], 1):
            text += f"`{i}.` {t.title}\n"
    await m.reply_text(text)
