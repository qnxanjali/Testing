import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from AnonXMusic import app  


NEXIO = [
"https://graph.org/file/e509753cf069de86e52f8.jpg",
"https://graph.org/file/babb71b593f36549218ce.jpg",
"https://graph.org/file/4a254d425fb4bf09b7470.jpg",
"https://graph.org/file/51f37e3c2d4aaff5cf80e.jpg",
"https://graph.org/file/df01978f91c14b16292f1.jpg",
"https://graph.org/file/a6e3e9d54c8b2e01787b6.jpg",
"https://graph.org/file/49bcbc23be713fbe06bac.jpg",
"https://graph.org/file/809651f9be99ee2bf76ab.jpg",
"https://graph.org/file/134c9f52f4ba0f7691cd1.jpg",
"https://graph.org/file/4b5c2174d7f38b4b4abd7.jpg",
"https://graph.org/file/80feff5bb4a03cf331945.jpg",
"https://graph.org/file/0379defeb51910065beac.jpg",
"https://graph.org/file/323b07bccd5e5e1f81f61.jpg",
"https://graph.org/file/cbe5c31b9ea5220b17969.jpg",
"https://graph.org/file/1a4e7071b3e64c620e003.jpg",
"https://graph.org/file/d37dd94135f355f9b6866.jpg",
]



@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"❖ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ ❖\n\n"
               
                f"❍ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {message.chat.title}\n"
                f"❍ ɢʀᴏᴜᴘ ɪᴅ ➠ {message.chat.id}\n"
                f"❍ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ➠ @{message.chat.username}\n"
                f"❍ ɢʀᴏᴜᴘ ʟɪɴᴋ ➠ {link}\n"
                f"❍ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ➠ {count}\n\n"
                f"❖ ᴀᴅᴅᴇᴅ ʙʏ ➠ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(NEXIO), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id
        left = f"❖ #ʟᴇғᴛ_ɢʀᴏᴜᴘ ᴀ ɢʀᴏᴜᴘ ❖\n\n❍ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n\n❍ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n\n❍ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n\n❖ ʙᴏᴛ ɴᴀᴍᴇ ➠ ɴ ᴇ x ɪ ᴏ"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(NEXIO), caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))