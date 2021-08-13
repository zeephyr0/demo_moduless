
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoWODMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoWOD"}

    async def watcher(self, message):
        if message.sender_id == 913530224:
            if "В этой битве тебе не было равных, это безупречная победа!" in message.raw_text:
                await sleep(3);
