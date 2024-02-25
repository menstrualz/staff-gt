from enum import IntEnum, Enum


class Color(IntEnum):
    GRAY = 0x2F3136
    GREEN = 0x1ee164
    RED = 0xFF0000
    WHITE = 0xFFFFFF


class RolesIds(IntEnum):
    SUPPORT = 1
    HELPER = 1
    MODERATOR = 1
    CONTROL = 1
    CREATIVE = 1
    EVENTMAKER = 1
    TRIBUNEMOD = 1
    CLOSEMAKER = 1
    CONTENTMAKER = 1
    AWAITING = 1


class ChannelId(IntEnum):
    TARGET = 1


class EmojiIds(Enum):
    emoji1 = "emoji here"
