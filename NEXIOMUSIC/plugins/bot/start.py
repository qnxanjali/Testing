import asyncio
import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from NEXIOMUSIC import app
from NEXIOMUSIC.misc import _boot_
from NEXIOMUSIC.plugins.sudo.sudoers import sudoers_list
from NEXIOMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from NEXIOMUSIC.utils.decorators.language import LanguageStart
from NEXIOMUSIC.utils.formatters import get_readable_time
from NEXIOMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

STICKERS = [
    "CAACAgUAAxkBAAEBc_Nm9reyuuFoy3Neq2_3KQfKNCxxXwACsRIAAk3CoVcRpQ6OPeMXSh4E",
    "CAACAgUAAxkBAAEBc_Nm9reyuuFoy3Neq2_3KQfKNCxxXwACsRIAAk3CoVcRpQ6OPeMXSh4E",
    "CAACAgUAAxkBAAEBc_Nm9reyuuFoy3Neq2_3KQfKNCxxXwACsRIAAk3CoVcRpQ6OPeMXSh4E",
    "CAACAgUAAxkBAAEBc_Nm9reyuuFoy3Neq2_3KQfKNCxxXwACsRIAAk3CoVcRpQ6OPeMXSh4E",
]

NEXIO = [
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    "https://files.catbox.moe/t1jsp2.jpg",
    ]

async def delete_sticker_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            sticker_message = await message.reply_sticker(sticker=random.choice(STICKERS))
            asyncio.create_task(delete_sticker_after_delay(sticker_message, 2))

            return await message.reply_photo(
                photo=random.choice(NEXIO),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
                searched_text = _["start_7"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                [
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                ],
                ]
            )
            await m.delete()
            await app.send_photo(chat_id=message.chat.id, photo=thumbnail, caption=searched_text, reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        nexio = await message.reply_text(f"**■□□□□□□□□□ 1⩇%**")
        await nexio.edit_text(f"**■■□□□□□□□□ 2⩇%**")
        await nexio.edit_text(f"**■■■□□□□□□□ 3⩇%**")
        await nexio.edit_text(f"**■■■■□□□□□□ 4⩇%**")
        await nexio.edit_text(f"**■■■■■□□□□□ 5⩇%**")
        await nexio.edit_text(f"**■■■■■■□□□□ 6⩇%️**")
        await nexio.edit_text(f"**■■■■■■■□□□ 7⩇%**")
        await nexio.edit_text(f"**■■■■■■■■□□ 8⩇%**")
        await nexio.edit_text(f"**■■■■■■■■■□ 9⩇%**")
        await nexio.edit_text(f"**■■■■■■■■■■ 1⩇⩇%**")
        await nexio.edit_text(f"**𝗟𝗲𝘁'𝘀 𝗚𝗼 𝗕𝗮𝗯𝘆..🌸**")
        await nexio.delete()

        sticker_message = await message.reply_sticker(sticker=random.choice(STICKERS))
        asyncio.create_task(delete_sticker_after_delay(sticker_message, 2))
        await message.reply_photo(photo=random.choice(NEXIO),
        caption=_["start_2"].format(message.from_user.mention),
        )

        await message.reply_text(text=_["start_3"].format(app.mention),
        reply_markup=InlineKeyboardMarkup(out),
        )

        if await is_on_off(2):
            return await app.send_message(chat_id=config.LOGGER_ID, text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(photo=random.choice(NEXIO),
    caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
    reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)

@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_5"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_6"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(photo=random.choice(NEXIO),
                    caption=_["start_4"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
