from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from NEXIOMUSIC import app


def help_pannell(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"MAIN_CP",),]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_[""], callback_data="thelp_callback hhb1",),
            ],
            [
                InlineKeyboardButton(text=_["HH_B_2"], callback_data="thelp_callback hhb2",),
                InlineKeyboardButton(text=_["HH_B_3"], callback_data="thelp_callback hhb3",),
                InlineKeyboardButton(text=_["HH_B_4"], callback_data="thelp_callback hhb4",),
            ],
            [
                InlineKeyboardButton(text=_["HH_B_5"], callback_data="thelp_callback hhb5",),
                InlineKeyboardButton(text=_["HH_B_6"], callback_data="thelp_callback hhb6",),
                InlineKeyboardButton(text=_["HH_B_7"], callback_data="thelp_callback hhb7",),
            ],
            [
                InlineKeyboardButton(text=_["HH_B_8"], callback_data="thelp_callback hhb8",),
                InlineKeyboardButton(text=_["HH_B_9"], callback_data="thelp_callback hhb9",),
                InlineKeyboardButton(text=_["HH_B_10"], callback_data="thelp_callback hhb10",),
            ],
            [
                InlineKeyboardButton(text=_["HH_B_11"], callback_data="thelp_callback hhb11",),
                InlineKeyboardButton(text=_["HH_B_12"], callback_data="thelp_callback hhb12",),
                InlineKeyboardButton(text=_["HH_B_13"], callback_data="thelp_callback hhb13",),
            ],
            mark,
        ]
    )
    return upl


def help_back_markupp(_):
    upl = InlineKeyboardMarkup(
        [
        [
                InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"tool_back_helper",),
        ]
        ]
    )
    return upl


def private_help_panell(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_4"], url=f"https://t.me/{app.username}?start=thelp",),
        ],
    ]
    return buttons
