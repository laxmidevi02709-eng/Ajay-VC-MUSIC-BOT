"""Run locally:  python -m AjayMusic.utils.gen_session
Generates a Pyrogram v2 session string for your USER account (needed for VC).
"""
from pyrogram import Client

print("=== AJAY VC MUSIC — Session String Generator ===")
api_id = int(input("API_ID: ").strip())
api_hash = input("API_HASH: ").strip()

with Client("gen", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
    s = app.export_session_string()
    print("\nSESSION_STRING=", s, sep="")
    try:
        app.send_message("me", f"`{s}`")
    except Exception:
        pass
