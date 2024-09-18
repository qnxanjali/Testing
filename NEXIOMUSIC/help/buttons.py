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
        ],
        [
            InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"MAIN_HELP_CP"), 
        ]
        ]
    
    MBUTTON = [
                [
            InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="NEXIOPLUS HELP_25"),
        ],
        [
            InlineKeyboardButton("ʙᴀɴ", callback_data="NEXIOPLUS HELP_14"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="NEXIOPLUS HELP_15"),
            InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="NEXIOPLUS HELP_16"),
        ],
        [
            InlineKeyboardButton("ᴘɪɴ", callback_data="NEXIOPLUS HELP_17"),
            InlineKeyboardButton("sᴛᴀғғ", callback_data="NEXIOPLUS HELP_18"),
            InlineKeyboardButton("sᴇᴛ-ᴜᴘ", callback_data="NEXIOPLUS HELP_19"),
        ],
        [
            InlineKeyboardButton("ᴢᴏᴍʙɪᴇ", callback_data="NEXIOPLUS HELP_20"),
            InlineKeyboardButton("ɢᴀᴍᴇ", callback_data="NEXIOPLUS HELP_21"),
            InlineKeyboardButton("ɪᴍᴘᴏsᴛᴇʀ", callback_data="NEXIOPLUS HELP_22"),
        ],
        [
            InlineKeyboardButton("sɢ", callback_data="NEXIOPLUS HELP_23"),
            InlineKeyboardButton("ᴛʀ", callback_data="NEXIOPLUS HELP_24"),
            InlineKeyboardButton("ɢʀᴀᴘʜ", callback_data="NEXIOPLUS HELP_26"),
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
