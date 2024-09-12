from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("❖ CONNECTING TO YOUR MONGO DATABASE 💚")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("❖ CONNECTED TO YOUR MONGO DATABASE 💜")
except:
    LOGGER(__name__).error("❖ FAILED TO CONNECT TO YOUR MONGO DATABASE 💛")
    exit()
