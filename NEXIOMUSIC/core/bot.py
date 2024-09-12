from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class SACHIN(Client):
    def __init__(self):
        LOGGER(__name__).info(f"❖ STARTING BOT 🖤")
        super().__init__(
            name="NEXIOMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>❖ {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ </b><u>\n\n❍ ɪᴅ ➠ <code>{self.id}</code>\n❍ ɴᴀᴍᴇ ➠ {self.name}\n❍ ᴜsᴇʀɴᴀᴍᴇ ➠ @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "❖ BOT HAS FAILED TO ACCESS THE LOG GROUP|CHANNEL MAKE SURE THAT YOU HAVE ADDED YOUR BOT TO YOUR LOG GROUP|CHANNEL 💙 "
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"❖ BOT HAS FAILED TO ACCESS THE LOG GROUP|CHANNEL ❍ REASON ➠ {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "PLEASE PROMOTE YOUR BOT AS AN ADMIN IN YOUR LOG GROUP|CHANNEL 💙"
            )
            exit()
        LOGGER(__name__).info(f"❖ MUSIC BOT STARTED AS {self.name} 💛")

    async def stop(self):
        await super().stop()
