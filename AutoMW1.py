#и хули ты тут забыл

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoMWMod(loader.Module): 
    strings = {"name": "AutoMW"}

    async def watcher(self, message):
        if message.sender_id == 1745526034:
            time = [5, 15, 30]
            if "Шаг: 1" in message.raw_text:
                await sleep(random.choice(time));
                await message.client.send_message('@metro_wars_bot', '♻️ Автобой');

