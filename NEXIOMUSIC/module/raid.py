import pyrogram
import time
import time
from pyrogram import filters
from pyrogram import Client
from DAXXMUSIC import app
from DAXXMUSIC.misc import SUDOERS
#from NEXIOMUSIC.module.data import RAID

OWNER_ID = "5959548791"
SANATANI_TECH = "5959548791"

RAID = [
"𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 [ sᴀᴄʜɪɴ sᴀɴᴀᴛᴀɴɪ ] 𝗧𝗘𝗥𝗔 𝗕𝗔𝗔𝗣𝗣𝗣𝗣𝗣 𝗛𝗔𝗜 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘",
"ᴍᴀᴅᴀʀᴄʜᴏᴅ ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍᴇ ɢʜᴜᴛᴋᴀ ᴋʜᴀᴀᴋᴇ ᴛʜᴏᴏᴋ ᴅᴜɴɢᴀ 🤣🤣",
"ᴛᴇʀᴇ ʙᴇʜᴇɴ ᴋ ᴄʜᴜᴛ ᴍᴇ ᴄʜᴀᴋᴜ ᴅᴀᴀʟ ᴋᴀʀ ᴄʜᴜᴛ ᴋᴀ ᴋʜᴏᴏɴ ᴋᴀʀ ᴅᴜɢᴀ",
"ᴛᴇʀɪ ᴠᴀʜᴇᴇɴ ɴʜɪ ʜᴀɪ ᴋʏᴀ? 9 ᴍᴀʜɪɴᴇ ʀᴜᴋ ꜱᴀɢɪ ᴠᴀʜᴇᴇɴ ᴅᴇᴛᴀ ʜᴜ 🤣🤣🤩",
"ᴛᴇʀɪ ᴍᴀᴀ ᴋ ʙʜᴏꜱᴅᴇ ᴍᴇ ᴀᴇʀᴏᴘʟᴀɴᴇᴘᴀʀᴋ ᴋᴀʀᴋᴇ ᴜᴅᴀᴀɴ ʙʜᴀʀ ᴅᴜɢᴀ ✈️🛫",
"ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴄʜᴜᴛ ᴍᴇ ꜱᴜᴛʟɪ ʙᴏᴍʙ ꜰᴏᴅ ᴅᴜɴɢᴀ ᴛᴇʀɪ ᴍᴀᴀ ᴋɪ ᴊʜᴀᴀᴛᴇ ᴊᴀʟ ᴋᴇ ᴋʜᴀᴀᴋ ʜᴏ ᴊᴀʏᴇɢɪ💣",
"ᴛᴇʀɪ ᴍᴀᴀᴋɪ ᴄʜᴜᴛ ᴍᴇ ꜱᴄᴏᴏᴛᴇʀ ᴅᴀᴀʟ ᴅᴜɢᴀ👅",
]

@app.on_message(filters.command("raid", prefixes=".") & SUDOERS)
def spam_command(client, message):
    try:

        message.delete()
    except pyrogram.errors.exceptions.FloodWait as e:
        print(f"Error deleting message: {e}")
        pass  
        
    if message.reply_to_message and message.reply_to_message.text:
        user_to_tag = message.reply_to_message.from_user.mention()
        command_args = message.text.split(".raid", 1)[-1].strip()

        try:
            num_times, text_to_spam = command_args.split(maxsplit=1)
            num_times = int(num_times)
        except ValueError:
            num_times = 1
            reply = random.choice(RAID)
            text_to_spam = command_args

        for _ in range(num_times):
            message.reply_text(f"{user_to_tag} {reply}")
            time.sleep(1) 
    elif message.reply_to_message:
        user_to_tag = message.reply_to_message.from_user.mention()

        for _ in range(5):  
            message.reply_to_message.reply_text(f"{user_to_tag} {reply}")
            time.sleep(0.2)  
    else:
        message.reply_text("• AP ISKO USE NAHI KAR SAKTE SORRY")
