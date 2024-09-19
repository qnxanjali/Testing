from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton
from NEXIOMUSIC import app
from NEXIOMUSIC.utils import help_pannel
#from NEXIOMUSIC.utils import help_pannell
from NEXIOMUSIC.utils.database import get_lang
from NEXIOMUSIC.utils.decorators.language import LanguageStart, languageCB
from NEXIOMUSIC.utils.inline.help import help_back_markup, private_help_panel
from NEXIOMUSIC.utils.inline.tool import help_back_markupp, private_help_panell
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from strings import thelpers
from NEXIOMUSIC.help.buttons import BUTTONS
from NEXIOMUSIC.help.helper import Helper





#------------------------------------------------------------------------------------------------------------------------
# MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | 
#------------------------------------------------------------------------------------------------------------------------





@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
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


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)


        
        
        
        
        

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
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markupp(_)
    if cb == "hhb1":
        await CallbackQuery.edit_message_text(thelpers.HELP_01, reply_markup=keyboard)
    elif cb == "hhb2":
        await CallbackQuery.edit_message_text(thelpers.HELP_02, reply_markup=keyboard)
    elif cb == "hhb3":
        await CallbackQuery.edit_message_text(thelpers.HELP_03, reply_markup=keyboard)
    elif cb == "hhb4":
        await CallbackQuery.edit_message_text(thelpers.HELP_04, reply_markup=keyboard)
    elif cb == "hhb5":
        await CallbackQuery.edit_message_text(thelpers.HELP_05, reply_markup=keyboard)
    elif cb == "hhb6":
        await CallbackQuery.edit_message_text(thelpers.HELP_06, reply_markup=keyboard)
    elif cb == "hhb7":
        await CallbackQuery.edit_message_text(thelpers.HELP_07, reply_markup=keyboard)
    elif cb == "hhb8":
        await CallbackQuery.edit_message_text(thelpers.HELP_08, reply_markup=keyboard)
    elif cb == "hhb9":
        await CallbackQuery.edit_message_text(thelpers.HELP_09, reply_markup=keyboard)
    elif cb == "hhb10":
        await CallbackQuery.edit_message_text(thelpers.HELP_10, reply_markup=keyboard)
    elif cb == "hhb11":
        await CallbackQuery.edit_message_text(thelpers.HELP_11, reply_markup=keyboard)
    elif cb == "hhb12":
        await CallbackQuery.edit_message_text(thelpers.HELP_12, reply_markup=keyboard)
    elif cb == "hhb13":
        await CallbackQuery.edit_message_text(thelpers.HELP_13, reply_markup=keyboard)
