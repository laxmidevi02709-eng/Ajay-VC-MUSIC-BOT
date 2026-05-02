"""Per-chat queue + state."""
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Deque, Dict, Optional


@dataclass
class Track:
    title: str
    duration: str
    link: str
    video_id: str
    file: str
    requested_by: str
    is_video: bool = False


@dataclass
class ChatState:
    queue: Deque[Track] = field(default_factory=deque)
    current: Optional[Track] = None
    volume: int = 100
    loop: int = 0


_state: Dict[int, ChatState] = defaultdict(ChatState)


def get(chat_id: int) -> ChatState:
    return _state[chat_id]


def clear(chat_id: int) -> None:
    if chat_id in _state:
        _state[chat_id].queue.clear()
        _state[chat_id].current = None
        _state[chat_id].loop = 0
