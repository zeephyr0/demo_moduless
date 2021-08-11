
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoCWMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoCW"}

    async def watcher(self, message):
        if message.sender_id == 577009581:
