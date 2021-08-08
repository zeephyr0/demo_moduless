#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoSWMod(loader.Module): 
    """Кто прочитал тот лох""" 
    strings = {"name": "AutoSW"}

    async def watcher(self, message):
        if message.sender_id == 227859379:
            if "Ты очень голоден." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '/use_101');
