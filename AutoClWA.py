#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoClWMod(loader.Module): 
    strings = {"name": "AutoClW"}

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "Сразитесь против других игроков из враждующих кланов!" in message.raw_text:
                await sleep(1);
                await message.click();
