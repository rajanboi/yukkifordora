from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✘ᴄʟɪᴄᴋ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ɢғ✘",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✘ʜᴇʟᴘs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs✘",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✘sᴇᴛᴛɪɴɢs✘", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✘ʙᴏᴛ ᴏᴡɴᴇʀ✘", user_id=OWNER),
            InlineKeyboardButton(
                text="✘sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ✘", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✘ᴄʟɪᴄᴋ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ɢғ✘",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✘ʜᴇʟᴘs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs✘", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✘ʙᴏᴛ ᴏᴡɴᴇʀ✘", user_id=OWNER),
            InlineKeyboardButton(
                text="✘sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ✘", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="✘ᴄʟɪᴄᴋ ғᴏʀ ɢɪғᴛ✘", url=f"https://t.me/pirokid"
                )
        ],
     ]
    return buttons
