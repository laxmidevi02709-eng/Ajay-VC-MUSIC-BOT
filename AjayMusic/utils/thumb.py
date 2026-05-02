import os
import aiohttp
import aiofiles
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)


async def download_image(url: str, path: str) -> str | None:
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(url) as r:
                if r.status != 200:
                    return None
                async with aiofiles.open(path, "wb") as f:
                    await f.write(await r.read())
        return path
    except Exception:
        return None


def _truncate(text: str, n: int) -> str:
    return text if len(text) <= n else text[: n - 3] + "..."


async def make_thumb(video_id: str, title: str, duration: str, requested_by: str) -> str | None:
    """Premium Now-Playing thumbnail: blurred bg + sharp center + branding."""
    if not video_id:
        return None
    out = f"{CACHE_DIR}/thumb_{video_id}.png"
    if os.path.exists(out):
        return out

    raw = f"{CACHE_DIR}/raw_{video_id}.jpg"
    ok = await download_image(f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg", raw)
    if not ok:
        ok = await download_image(f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg", raw)
    if not ok:
        return None

    try:
        base = Image.open(raw).convert("RGBA").resize((1280, 720))
        bg = base.copy().filter(ImageFilter.GaussianBlur(35))
        overlay = Image.new("RGBA", bg.size, (0, 0, 0, 130))
        bg = Image.alpha_composite(bg, overlay)

        thumb = base.resize((520, 520))
        bg.paste(thumb, (60, 100))

        draw = ImageDraw.Draw(bg)
        try:
            font_title = ImageFont.truetype("assets/font.ttf", 44)
            font_meta = ImageFont.truetype("assets/font.ttf", 30)
            font_brand = ImageFont.truetype("assets/font.ttf", 28)
        except Exception:
            font_title = ImageFont.load_default()
            font_meta = ImageFont.load_default()
            font_brand = ImageFont.load_default()

        draw.text((620, 140), "✦ NOW PLAYING", fill=(255, 80, 120), font=font_brand)
        draw.text((620, 200), _truncate(title, 28), fill="white", font=font_title)
        draw.text((620, 320), f"⏱  {duration}", fill=(220, 220, 220), font=font_meta)
        draw.text((620, 380), f"👤  {_truncate(requested_by, 20)}", fill=(220, 220, 220), font=font_meta)
        draw.text((620, 600), "@AjayVcMusicBot", fill=(255, 200, 80), font=font_brand)

        bg.convert("RGB").save(out, "PNG")
        try: os.remove(raw)
        except Exception: pass
        return out
    except Exception as e:
        print("thumb err:", e)
        return None
