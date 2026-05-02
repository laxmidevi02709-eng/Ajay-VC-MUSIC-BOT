"""PyTgCalls v2 wrapper."""
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality
from AjayMusic import call_py, LOGGER
from AjayMusic.core import queue as q


async def start():
    await call_py.start()
    LOGGER.info("PyTgCalls started")


async def play_track(chat_id: int, track: q.Track):
    if track.is_video:
        stream = MediaStream(
            track.file,
            audio_flags=MediaStream.Flags.REQUIRED,
            video_flags=MediaStream.Flags.REQUIRED,
            audio_parameters=AudioQuality.HIGH,
            video_parameters=VideoQuality.HD_720p,
        )
    else:
        stream = MediaStream(
            track.file,
            audio_flags=MediaStream.Flags.REQUIRED,
            video_flags=MediaStream.Flags.IGNORE,
            audio_parameters=AudioQuality.HIGH,
        )
    await call_py.play(chat_id, stream)
    q.get(chat_id).current = track


async def skip(chat_id: int) -> q.Track | None:
    state = q.get(chat_id)
    if state.loop > 0 and state.current:
        state.loop -= 1
        await play_track(chat_id, state.current)
        return state.current
    if not state.queue:
        await leave(chat_id)
        return None
    nxt = state.queue.popleft()
    await play_track(chat_id, nxt)
    return nxt


async def pause(chat_id: int):
    await call_py.pause(chat_id)


async def resume(chat_id: int):
    await call_py.resume(chat_id)


async def leave(chat_id: int):
    try:
        await call_py.leave_call(chat_id)
    except Exception:
        pass
    q.clear(chat_id)


async def set_volume(chat_id: int, vol: int):
    vol = max(1, min(200, vol))
    try:
        await call_py.change_volume_call(chat_id, vol)
    except Exception as e:
        LOGGER.warning(f"vol err: {e}")
    q.get(chat_id).volume = vol
