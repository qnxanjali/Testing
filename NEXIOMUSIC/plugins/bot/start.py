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
"CAACAgUAAxkBAAEBTOxm3z37FlWf1kxXsV3BTowp31kdqgACxgQAAhy8-VUcAzVlizY3bB4E",
"CAACAgUAAxkBAAEBTO1m3z38AAFqwtrZQybObkNiTfRb3IgAAvcEAAKluvlVe9FSpTsDTXMeBA",
"CAACAgUAAxkBAAEBTO5m3z38742obNe0uQpIAbHlhxubiwACLgYAAv1CAAFWaHyQYOHYA0geBA",
"CAACAgUAAxkBAAEBTO9m3z39CV0yJ3u4O0l4R8eDRK4M-AACShEAApTU-VX95QwdgdktKR4E",
"CAACAgUAAxkBAAEBTPBm3z4C4enyLY9lJUTj1LeDpm8jagACcQcAAguP-FWtU33QgpGchx4E",
"CAACAgUAAxkBAAEBTPFm3z4HAAHLkU9ZwkbJrVN072TRmmgAAggFAAIVDflVr8X_uhL47dMeBA",
"CAACAgUAAxkBAAEBTPJm3z4HQ0JG8Sp7yX13bC7pP65zUQACQAUAAm6c-VWHUk18jds0QR4E",
"CAACAgUAAxkBAAEBTPNm3z4IOTYffxmCBGC2F1KdGgysEQACbwYAAsrM-FUeMFwEto3Wwh4E",
"CAACAgUAAxkBAAEBTPRm3z4I0uUliFjaCzSMaL74s6slMAACCQkAAsYl8FUAAYs5T97AnKoeBA",
"CAACAgUAAxkBAAEBTPVm3z4KIEt8kc0LbVCxYl70NFbzqAACgAYAAuho-FUeIpkQA5omrR4E",
"CAACAgUAAxkBAAEBTPZm3z4LcC1GihptHNJgG0Ik49DIsgACLSEAAjZx8FU1CkmZEPSvSh4E",
"CAACAgUAAxkBAAEBTPdm3z4OmiYnWUcbosNOjeJuuhzIbQACKwUAAu04-VVzp21EypPZER4E",
"CAACAgUAAxkBAAEBTPhm3z4OwdJUijX2XPDpBuawUH8mbQACqQkAAhfo-VXKa23jh5-Pgx4E",
"CAACAgUAAxkBAAEBTPlm3z4S_6wltRVt74t6MbSLPjsUwQACQQQAApTxOFSDZapEqAiD7h4E",
"CAACAgUAAxkBAAEBTPpm3z4TwyB9m-37IBZx74XUUmNJTQACmQUAAus_OVQKiSsa_Xi9dB4E",
"CAACAgUAAxkBAAEBTPtm3z4U0QMZtnT-p9R_jVwItVAAAXEAAjsGAAIzEzlUoEWZn974SpseBA",
]

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                random.choice(NEXIO),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>❍ ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>❍ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
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
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>❍ ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>❍ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        await message.reply_sticker(
        random.choice(HIMANSHI),)
        return await message.reply_photo(
            random.choice(NEXIO),
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"❖ {message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>❍ ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>❍ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
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
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
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
