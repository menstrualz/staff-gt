from enum import IntEnum, Enum


class Color(IntEnum):
    GRAY = 0x2F3136
    GREEN = 0x1ee164
    RED = 0xFF0000
    WHITE = 0xFFFFFF


class RolesIds(IntEnum):
    SUPPORT = 1105487112121368596
    HELPER = 1105487112121368596
    MODERATOR = 1105487112121368596
    CONTROL = 1105487112121368596
    CREATIVE = 1105487112121368596
    EVENTMAKER = 1105487112121368596
    TRIBUNEMOD = 1105487112121368596
    CLOSEMAKER = 1105487112121368596
    CONTENTMAKER = 1105487112121368596
    AWAITING = 1107782247454617750


class ChannelId(IntEnum):
    TARGET = 1211023754260512870


class EmojiIds(Enum):
    emoji1 = "<:arrow:1211096117169627186>"