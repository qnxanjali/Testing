import asyncio
from random import choice
from telethon import events
from telethon import events, functions, types
from NEXIOMUSIC import app
from NEXIOMUSIC.misc import SUDOERS
from NEXIOMUSIC.module.data import RAID
from config import OWNER_ID
from config import SANATANITECH






@app.on_message(filters.command(["raid"]) & filters.group & SUDOERS)
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in SANATANITECH:
                await e.reply("❖ ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀᴜᴛʜᴏʀ ʙᴏᴛ ᴏᴡɴᴇʀ ")
            elif uid == OWNER_ID:
                await e.reply("❖ ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ")
            elif uid in SUDO_USERS:
                await e.reply("❖ ɴᴏᴘᴇ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
