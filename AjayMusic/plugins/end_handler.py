"""Auto-advance to next track when current ends."""
from pytgcalls import filters as fl
from pytgcalls.types import Update
from AjayMusic import call_py, LOGGER
from AjayMusic.core import streamer


@call_py.on_update(fl.stream_end())
async def on_end(_, update: Update):
    try:
        chat_id = update.chat_id
        await streamer.skip(chat_id)
    except Exception as e:
        LOGGER.warning(f"end_handler err: {e}")
