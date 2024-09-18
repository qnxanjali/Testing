from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("ᴀɪ | ᴄʜᴀᴛɢᴘᴛ", callback_data="NEXIOPLUS HELP_01"),
        ],
        [
            InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="NEXIOPLUS HELP_02"),
            InlineKeyboardButton("ᴛᴛs", callback_data="NEXIOPLUS HELP_03"),
            InlineKeyboardButton("ɪɴғᴏ", callback_data="NEXIOPLUS HELP_04"),
        ],
        [
            InlineKeyboardButton("ғᴏɴᴛ", callback_data="NEXIOPLUS HELP_05"),
            InlineKeyboardButton("ᴍᴀᴛʜ", callback_data="NEXIOPLUS HELP_06"),
            InlineKeyboardButton("ᴛᴀɢᴀʟʟ", callback_data="NEXIOPLUS HELP_07"),
        ],
        [
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="NEXIOPLUS HELP_08"),
            InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="NEXIOPLUS HELP_09"),
            InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="NEXIOPLUS HELP_10"),
        ],
        [
            InlineKeyboardButton("ғᴜɴ", callback_data="NEXIOPLUS HELP_11"),
            InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="NEXIOPLUS HELP_12"),
            InlineKeyboardButton("ᴛ-ᴅ", callback_data="NEXIOPLUS HELP_13"),
        ]
        ]
    
    MBUTTON = [
        [
            InlineKeyboardButton("• ᴀɪ •", callback_data="NEXIOPLUS HELP_ChatGPT"),
            InlineKeyboardButton("• ɪɴғᴏ •", callback_data="NEXIOPLUS HELP_Info"),
            InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="NEXIOPLUS HELP_Sticker")
        ],
        [
            InlineKeyboardButton("• ᴇxᴛꝛᴧ •", callback_data="NEXIOPLUS HELP_Extra"),
            InlineKeyboardButton("• ɪᴍᴧɢᴇ •", callback_data="NEXIOPLUS HELP_Image"),
            InlineKeyboardButton("• sᴇᴧꝛᴄʜ •", callback_data="NEXIOPLUS HELP_Search")
        ],
        [
            InlineKeyboardButton("• ǫᴜɪʟʏ •", callback_data="NEXIOPLUS HELP_Q")
        ],
        [
            InlineKeyboardButton("• ғᴏиᴛ •", callback_data="NEXIOPLUS HELP_Font"),
            InlineKeyboardButton("• ɢᴧᴍᴇ •", callback_data="NEXIOPLUS HELP_Game"),
            InlineKeyboardButton("• ᴛ-ɢꝛᴧᴘʜ •", callback_data="NEXIOPLUS HELP_TG")
        ],    
        [
            InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"MAIN_HELP_CP"), 
        ]
        ]
    SBUTTON = [
        [
            InlineKeyboardButton("TOOL", callback_data="TOOL_CP"),
            InlineKeyboardButton("MANAGEMENT", callback_data="MANAGEMENT_CP"),
        ],
        [
            InlineKeyboardButton("MUSIC", callback_data="settings_back_helper"),
            InlineKeyboardButton("HOME", callback_data="settingsback_helper"),
            
        ]
        ]
