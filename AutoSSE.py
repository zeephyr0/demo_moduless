#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoSEMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoSE"}

    async def watcher(self, message):
        time1 = [4, 120]
        buttons = [0, 1, 2]
        time2 = [2, 4, 6]
        if message.sender_id == 605298957:
            if "📡Ты вернулся с поиска обломков. " in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '⌨️');
            if "👁‍🗨Ты в космосе" and "🔋30" in message.raw_text:
                await sleep(1);
                await message.click();
            elif "👁‍🗨Ты в космосе" in message.raw_text:
                await sleep(1);
                await message.click(3);
            if "📡Ты можешь отправиться на поиски обломков, в которых иногда можно найти ценные ресурсы." in message.raw_text:
                await sleep(1);
                await message.click();
