import requests
from NEXIOMUSIC import app
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from MukeshAPI import api

BOT_NAME = "˹ ɴ ᴇ x ɪ ᴏ ˼"
BOT_USERNAME = "NEXIO_MUSIC_BOT"


@app.on_message(filters.command(["chatgpt","ai","ask","gpt","solve"],  prefixes=["/", ".", "!", "?", ""]))
async def chat_gpt(bot, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "❖ ᴜꜱᴀɢᴇ ➠ /gpt [ǫᴜᴇʀʏ]")
        else:
            a = message.text.split(' ', 1)[1]
            r=api.chatgpt(a,mode="elonmusk")["results"]
            await message.reply_text(f"❖ {r} \n\n❖ ʀᴇꜱᴜʟᴛꜱ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ [{BOT_NAME}](https://t.me{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"❖ ᴇʀʀᴏʀ ➠ {e} ")
