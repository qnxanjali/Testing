from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("˹ 🇸ʌᷟᴄᷣʜɪ֟፝η ˼", url="https://t.me/V_VIP_OWNER")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("𝝩‌𝞊‌𝝶𝘀𝝸𝝾‌𝝶‌ 𝗧𝞊‌𝗰𝗵", url="https://t.me/THE_TENSION"),
        ],
        [
            InlineKeyboardButton("ᴍσσɴ ʜᴜɢ", url="https://t.me/MOON_HUB"),
            InlineKeyboardButton("ɴєxɪσ ᴛєᴄʜ", url="https://t.me/NEXIO_TECH"),
        ],
        [
            InlineKeyboardButton("sυᴘᴘσʀᴛ", url="https://t.me/SANATANI_SUPPORT"),
            InlineKeyboardButton("υᴘᴅᴧᴛєs", url="https://t.me/ALL_SANATANI_BOT"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/V_VIP_OWNER"),
            InlineKeyboardButton("ʜᴇʟᴘ | ɪɴғᴏ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴀsɪᴄ ɢᴜɪᴅᴇ", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅᴏɴᴀᴛᴇ", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
