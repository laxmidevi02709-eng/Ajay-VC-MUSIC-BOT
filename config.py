import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "35828291"))
API_HASH = os.getenv("API_HASH", "c025ee9d01d73b9d738d4f3e5e6137e2")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8702378971:AAFl1ZWdY4p8hayE5k-7lEyh-hLw0kEloMs")
SESSION_STRING = os.getenv("SESSION_STRING", "BQIiskMAjDearX7JGPKA9xzx53OGMXRzE8RBZWsrMG9UDtxbYFkVCKvV3MuxI07QSEEl2X1XbWuz6lLj0BAp-md2Cr2hnVmvai8qT-6hHqm8tE61SuQjU8-aNcsj70YgxzOKaU6JUQQrUEgqHrkFkNpSZJ1in1eTHohfQE63t8h0iJYyLy08grUWluAX0daMFCmiMqQykw4ZBKzrJXoML3mcMBKFFxjPaDmY1kLvXsGUsqSoxqn6Xhw5mc7KyuuiUBPUGRr9RzS3ifjLfSIOxgRQgO2xr4saSaLQ-wl7x57tqiaxphtLZCfDmf2ZW6CtHCbBhrAv8Qsp4xotg17Hk8gqZjXcZgAAAAIJa0okAQ")

OWNER_ID = int(os.getenv("OWNER_ID", "7953454559"))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# Branding — AJAY VC MUSIC BOT
BOT_USERNAME = os.getenv("BOT_USERNAME", "AgajayVcMusicBot")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "agajayofficial")
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "https://t.me/AjayFFCommunity")
SECOND_CHANNEL = os.getenv("SECOND_CHANNEL", "https://t.me/agajayofficialgiveway")
PRIVATE_CHANNEL = os.getenv("PRIVATE_CHANNEL", "https://t.me/+K_QvCsPtHPNkNTdl")

PORT = int(os.getenv("PORT", "8080"))

BOT_NAME = "✦ AJAY VC MUSIC BOT"

START_TEXT = """**✦ Mᴜꜱɪᴄ ʙᴏᴛ - @{bot}**

➤ **Uꜱᴇ ᴛʜɪꜱ ᴍᴜꜱɪᴄ ʙᴏᴛ ꜰᴏʀ ꜰʀᴇᴇ**

➤ **Hᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴜꜱɪᴄ ʙᴏᴛ ?**
→ Aᴅᴅ ʙᴏᴛ ᴛᴏ ɢʀᴏᴜᴘ & ᴍᴀᴋᴇ ᴀᴅᴍɪɴ
→ Sᴛᴀʀᴛ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ
→ Sᴇᴀʀᴄʜ ꜱᴏɴɢ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ
→ Exᴀᴍᴘʟᴇ ( /ᴘʟᴀʏ ꜱᴏɴɢ ɴᴀᴍᴇ )

➤ **Bᴏᴛ Oᴡɴᴇʀ -** @agajayofficial
➤ **Mᴀɪɴ Cʜᴀɴɴᴇʟ -** @AjayFFCommunity
➤ **Sᴇᴄᴏɴᴅ Cʜᴀɴɴᴇʟ -** [Jᴏɪɴ Hᴇʀᴇ](https://t.me/agajayofficialgiveway)
➤ **Pʀɪᴠᴀᴛᴇ Cʜᴀɴɴᴇʟ -** [Jᴏɪɴ Hᴇʀᴇ](https://t.me/+K_QvCsPtHPNkNTdl)
➤ **Dᴇᴠᴇʟᴏᴘᴇʀ -** @agajayofficial""".format(bot=BOT_USERNAME)

HELP_TEXT = """**✦ AJAY VC MUSIC BOT - Hᴇʟᴘ Mᴇɴᴜ**

➤ **Pʟᴀʏ Cᴏᴍᴍᴀɴᴅꜱ**
→ /play `<song name / yt link / spotify link>`
→ /vplay `<query>` — video stream
→ /playlist — show queue

➤ **Cᴏɴᴛʀᴏʟ Cᴏᴍᴍᴀɴᴅꜱ** (ᴀᴅᴍɪɴ ᴏɴʟʏ)
→ /pause  /resume
→ /skip   /stop
→ /volume `<1-200>`
→ /loop `<0-10>`

➤ **Dᴏᴡɴʟᴏᴀᴅ**
→ /song `<query>` — download mp3
→ /video `<query>` — download mp4

➤ **Mɪꜱᴄ**
→ /ping  /stats

➤ **Bᴏᴛ Oᴡɴᴇʀ →** @agajayofficial
➤ **Mᴀɪɴ Cʜᴀɴɴᴇʟ →** @AjayFFCommunity"""
