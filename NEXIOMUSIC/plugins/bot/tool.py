from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton
from NEXIOMUSIC import app
from NEXIOMUSIC.utils import help_pannel
from NEXIOMUSIC.utils.database import get_lang
from NEXIOMUSIC.utils.decorators.language import LanguageStart, languageCB
from NEXIOMUSIC.utils.inline.tool import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers

#------------------------------------------------------------------------------------------------------------------------
# MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | 
#------------------------------------------------------------------------------------------------------------------------

@app.on_message(filters.command(["thelp"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("tool_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["thelp"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("thelp_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hhb1":
        await CallbackQuery.edit_message_text(helpers.HELP_01, reply_markup=keyboard)
    elif cb == "hhb2":
        await CallbackQuery.edit_message_text(helpers.HELP_02, reply_markup=keyboard)
    elif cb == "hhb3":
        await CallbackQuery.edit_message_text(helpers.HELP_03, reply_markup=keyboard)
    elif cb == "hhb4":
        await CallbackQuery.edit_message_text(helpers.HELP_04, reply_markup=keyboard)
    elif cb == "hhb5":
        await CallbackQuery.edit_message_text(helpers.HELP_05, reply_markup=keyboard)
    elif cb == "hhb6":
        await CallbackQuery.edit_message_text(helpers.HELP_06, reply_markup=keyboard)
    elif cb == "hhb7":
        await CallbackQuery.edit_message_text(helpers.HELP_07, reply_markup=keyboard)
    elif cb == "hhb8":
        await CallbackQuery.edit_message_text(helpers.HELP_08, reply_markup=keyboard)
    elif cb == "hhb9":
        await CallbackQuery.edit_message_text(helpers.HELP_09, reply_markup=keyboard)
    elif cb == "hhb10":
        await CallbackQuery.edit_message_text(helpers.HELP_010, reply_markup=keyboard)
    elif cb == "hhb11":
        await CallbackQuery.edit_message_text(helpers.HELP_011, reply_markup=keyboard)
    elif cb == "hhb12":
        await CallbackQuery.edit_message_text(helpers.HELP_012, reply_markup=keyboard)
    elif cb == "hhb13":
        await CallbackQuery.edit_message_text(helpers.HELP_013, reply_markup=keyboard)
