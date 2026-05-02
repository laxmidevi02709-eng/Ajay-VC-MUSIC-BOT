"""YouTube search + download using yt-dlp only (no extra search package)."""
import asyncio
import os
import re
import yt_dlp

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

YT_REGEX = re.compile(r"(youtube\.com|youtu\.be)")


def is_yt_url(text: str) -> bool:
    return bool(YT_REGEX.search(text))


def _fmt_duration(seconds) -> str:
    if not seconds:
        return "Live"
    try:
        s = int(seconds)
    except Exception:
        return "Live"
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def _ydl_search(query: str) -> dict | None:
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "noplaylist": True,
        "default_search": "ytsearch1",
        "extract_flat": False,
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            data = ydl.extract_info(query, download=False)
            if "entries" in data:
                if not data["entries"]:
                    return None
                v = data["entries"][0]
            else:
                v = data
            vid = v.get("id", "")
            return {
                "id": vid,
                "title": v.get("title", "Unknown"),
                "duration": _fmt_duration(v.get("duration")),
                "link": v.get("webpage_url") or f"https://www.youtube.com/watch?v={vid}",
                "thumbnail": (v.get("thumbnail") or
                              f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"),
                "channel": v.get("uploader", "Unknown"),
            }
    except Exception as e:
        print("yt search err:", e)
        return None


async def search(query: str) -> dict | None:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _ydl_search, query)


def _ydl_download(url: str, audio: bool = True) -> str | None:
    out_tmpl = f"{CACHE_DIR}/%(id)s.%(ext)s"
    if audio:
        opts = {
            "format": "bestaudio/best",
            "outtmpl": out_tmpl,
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
        }
    else:
        opts = {
            "format": "best[height<=720][ext=mp4]/best[height<=720]/best",
            "outtmpl": out_tmpl,
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
        }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


async def download(url: str, audio: bool = True) -> str | None:
    try:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, _ydl_download, url, audio)
    except Exception as e:
        print("yt download err:", e)
        return None
