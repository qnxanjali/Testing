import asyncio
import random
import time
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from NEXIOMUSIC import app
from NEXIOMUSIC.misc import _boot_
from NEXIOMUSIC.plugins.sudo.sudoers import sudoers_list
from NEXIOMUSIC.utils import bot_sys_stats
from NEXIOMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    get_served_chats,
    get_served_users,
    is_banned_user,
    is_on_off,
)
from NEXIOMUSIC.utils.decorators.language import LanguageStart
from NEXIOMUSIC.utils.formatters import get_readable_time
from NEXIOMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS,
from strings import get_string

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

HIMANSHI = [
"CAACAgEAAxkBAAEBSBVm2-xs1zE1YL6BL6PdhdjYN8qQNAAC0gQAAlEpDTl8h9NLLim0sh4E",
"CAACAgUAAxkBAAEBSBhm2-xwD_ILrcipRibV4PXrAtvIZgACPgMAAkR6UVX0GucO3bwEER4E",
"CAACAgUAAxkBAAEBSBxm2-x7jA1zKd7p5hOt6lWQj1nxMAACvAMAAgiyyFUwH8IluWirUx4E",
"CAACAgUAAxkBAAEBSB1m2-x8LL3lv8NL0sFLLBv8s7LPpwACvQIAAnviWFV3YB3thOJgUh4E",
"CAACAgQAAxkBAAEBSB5m2-yP-X6dHUnigPmqUYomPQ7brgACJRkAAtqjlSyPFI6KfBy2gh4E",
"CAACAgUAAxkBAAEBSB9m2-ycrtvTDdX0ep720ybH-359tgACyAcAAhHnoVS2I8LDJbNSgh4E",
"CAACAgUAAxkBAAEBSCBm2-ye2q3ZKo5p9dbIPruYhAv0cgACEBAAAmVM8VTGX670G3pB_R4E",
"CAACAgUAAxkBAAEBSCFm2-yfc4RNmZW5oOgqOB49JVxzCgACgQ0AAhGP-VTcRaf7f3Md3h4E",
"CAACAgUAAxkBAAEBSCJm2-ywwTxJ4a9YbJ9AJbB40Zt1bQACjg0AAin6-VQZLhrqJspmlx4E",
"CAACAgUAAxkBAAEBSCNm2-y6BZ0Wng7DTyKNZ0Wq22F7KAACxgQAAhy8-VUcAzVlizY3bB4E",
"CAACAgUAAxkBAAEBSCRm2-y-hL2Y3XHDu4Ykv_K8gh1AEgACQAUAAm6c-VWHUk18jds0QR4E",
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
            asyncio.create_task(delete_sticker_after_delay(sticker_message, 2))  # Delete sticker after 2 seconds
            await message.reply_sticker(
            random.choice(HIMANSHI),)
            return await message.reply_photo(
            random.choice(NEXIO),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        elif name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>❍ sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>❍ ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n<b>❖ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
                )
        elif name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = str(name).replace("info_", "", 1)
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
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_video(
                chat_id=message.chat.id,
                video=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>❍ ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>\n\n<b>❍ ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n<b>❍ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        sticker_message = await message.reply_sticker(sticker=random.choice(STICKERS))
        asyncio.create_task(delete_sticker_after_delay(sticker_message, 2))  # Delete sticker after 2 seconds
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await message.reply_sticker(
        random.choice(HIMANSHI),)
        return await message.reply_photo(
        random.choice(NEXIO),
        caption=_["start_2"]..format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM, served_users, served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>❍ ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>\n<b>❖ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}",
            )

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_sticker(
        random.choice(HIMANSHI),)
        return await message.reply_photo(
        random.choice(NEXIO),
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
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_sticker(
                random.choice(HIMANSHI),)
                return await message.reply_photo(
                random.choice(NEXIO),
                caption=_["start_1"].
                caption=_["start_3"].format(
                message.from_user.mention,
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
