import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "35828291"))
API_HASH = os.getenv("API_HASH", "c025ee9d01d73b9d738d4f3e5e6137e2")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8631333041:AAHWj3Ut17BSn4laROufER6gF24eA0Hqj2c")
SESSION_STRING = os.getenv("SESSION_STRING", "BQIiskMAVA6lEUPzkmTtQn7zh__KAJn0nzSuebU2tw30rtVbz4Tq4Ai03em8OlirqyZxa2ZNAgY2SBf87wY4hsiBin7uN7SYE6y4JSWtzKnGep3IfQe3rJE2-iGE1-0loCRhLLs_ZduSfyTIR7JXFP984-1_ZTwDQu_dGEXpc2a_2acwT4skZRj8mHUgT1SKW5JtEpf3CA8e2xiazKVHtz-jUI7w1wLHpQBm9iUGoaQ9poZQeMt1D8FhIDO335CzgUlwpZkYZ7B_gPg7gPXKfuz9V0OqFEYnZ5pYTNwRM45fWx_ozUfnNP8HAeJLhGRtGPtJeyI0Qyygui_2YSjjQ-Zd6vh5cQAAAAIHIiSYAA")

OWNER_ID = int(os.getenv("OWNER_ID", "7953454559"))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# Branding — AJAY VC MUSIC BOT
BOT_USERNAME = os.getenv("BOT_USERNAME", "AjayVCmusicBot")
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
