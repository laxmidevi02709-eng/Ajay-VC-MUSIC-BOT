import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

SP_REGEX = re.compile(r"open\.spotify\.com/(track|playlist|album)/([A-Za-z0-9]+)")

_sp = None
if config.SPOTIFY_CLIENT_ID and config.SPOTIFY_CLIENT_SECRET:
    try:
        _sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=config.SPOTIFY_CLIENT_ID,
                client_secret=config.SPOTIFY_CLIENT_SECRET,
            )
        )
    except Exception as e:
        print("spotify init err:", e)


def is_spotify_url(text: str) -> bool:
    return bool(SP_REGEX.search(text))


def track_to_query(url: str) -> str | None:
    if not _sp:
        return None
    m = SP_REGEX.search(url)
    if not m:
        return None
    kind, sid = m.group(1), m.group(2)
    try:
        if kind == "track":
            t = _sp.track(sid)
            artists = ", ".join(a["name"] for a in t["artists"])
            return f"{t['name']} {artists}"
        if kind == "album":
            a = _sp.album(sid)
            t = a["tracks"]["items"][0]
            return f"{t['name']} {a['artists'][0]['name']}"
        if kind == "playlist":
            p = _sp.playlist(sid)
            t = p["tracks"]["items"][0]["track"]
            return f"{t['name']} {t['artists'][0]['name']}"
    except Exception as e:
        print("spotify err:", e)
    return None
