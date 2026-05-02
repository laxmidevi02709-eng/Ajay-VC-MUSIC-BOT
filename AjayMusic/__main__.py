import asyncio
from aiohttp import web
from AjayMusic import bot, user, LOGGER
from AjayMusic.core import streamer
from AjayMusic import plugins  # noqa: F401  (register handlers)
import config


async def _health(_):
    return web.Response(text="✦ AJAY VC MUSIC BOT is alive — @agajayofficial")


async def _start_keepalive():
    """Tiny HTTP server so Render Web Service stays alive."""
    app = web.Application()
    app.router.add_get("/", _health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", config.PORT)
    await site.start()
    LOGGER.info(f"Keep-alive HTTP on :{config.PORT}")


async def main():
    if not config.SESSION_STRING:
        raise SystemExit(
            "❌ SESSION_STRING is empty.\n"
            "Generate one with: python -m AjayMusic.utils.gen_session"
        )

    await bot.start()
    await user.start()
    await streamer.start()
    me = await bot.get_me()
    LOGGER.info(f"@{me.username} started ✦ AJAY VC MUSIC BOT")
    await _start_keepalive()
    await asyncio.Event().wait()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
