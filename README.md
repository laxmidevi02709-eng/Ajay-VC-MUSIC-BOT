# ✦ AJAY VC MUSIC BOT

Premium Telegram **Voice Chat music bot** — built with **Pyrogram v2 + PyTgCalls v2**.
Streams audio/video from **YouTube + Spotify** into Telegram group voice chats with a beautiful Now-Playing card and full inline controls.

➤ **Bᴏᴛ Oᴡɴᴇʀ -** @agajayofficial
➤ **Mᴀɪɴ Cʜᴀɴɴᴇʟ -** @AjayFFCommunity
➤ **Sᴇᴄᴏɴᴅ Cʜᴀɴɴᴇʟ -** https://t.me/agajayofficialgiveway
➤ **Pʀɪᴠᴀᴛᴇ Cʜᴀɴɴᴇʟ -** https://t.me/+K_QvCsPtHPNkNTdl

---

## ✦ Features
- `/play <song>` — search YouTube/Spotify, stream into VC
- `/vplay <song>` — HD 720p video stream
- Inline buttons: Pause / Resume / Skip / Stop / Vol± / Loop / Seek±10s
- Per-chat queue with auto-advance
- `/song`, `/video` — mp3/mp4 download
- Premium blurred Now-Playing thumbnail
- Stylish Unicode small-caps font
- Keep-alive HTTP for Render Web Service

---

## ✦ 1. Get Credentials

| Var | Where |
|---|---|
| `API_ID`, `API_HASH` | https://my.telegram.org → API development tools |
| `BOT_TOKEN` | https://t.me/BotFather → `/newbot` |
| `SESSION_STRING` | Run locally: `python -m AjayMusic.utils.gen_session` (USER account, NOT bot). Or use @StringFatherBot |
| `OWNER_ID` | @userinfobot |
| `SPOTIFY_*` | https://developer.spotify.com/dashboard (optional) |

⚠️ The user account whose `SESSION_STRING` you use **must be added to the group** so it can join the voice chat.

---

## ✦ 2. Run Locally

```bash
pip install -r requirements.txt
sudo apt install ffmpeg     # REQUIRED
cp .env.example .env        # fill values
python -m AjayMusic
```

---

## ✦ 3. Deploy on Render (Docker)

1. Push this folder to a **GitHub repo**.
2. Render → **New → Web Service** → connect repo.
3. Render auto-detects `Dockerfile` (or "New → Blueprint" with `render.yaml`).
4. Add env vars from `.env.example` in the Render dashboard.
5. Deploy. Bot starts; keep-alive HTTP on `$PORT`.

> Free plan: services sleep after 15 min idle. Use [UptimeRobot](https://uptimerobot.com) to ping the Render URL every 5 min.

---

## ✦ 4. Use in Group

1. Add **the bot** to the group → make it **admin**.
2. Add the **user account** (whose session string you used) to the group.
3. Start a **voice chat** in the group.
4. Send `/play <song name>` — done ✦

---

## ✦ Commands

| Command | Description |
|---|---|
| `/play <q>` | Audio in VC |
| `/vplay <q>` | Video in VC |
| `/pause` `/resume` | Toggle |
| `/skip` `/stop` | Skip / leave |
| `/volume <1-200>` | Volume |
| `/loop <0-10>` | Loop N times |
| `/playlist` | Show queue |
| `/song <q>` | Download mp3 |
| `/video <q>` | Download mp4 |
| `/ping` `/stats` | Bot info |

---

## ✦ Troubleshooting

- **"Can't join VC"** → start a voice chat first; ensure both bot & user account are in the group.
- **No audio** → ffmpeg missing (Dockerfile installs it).
- **Session expired** → regenerate `SESSION_STRING`.

---

➤ Mᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ **@agajayofficial**
➤ Jᴏɪɴ **@AjayFFCommunity**
