#и хули ты тут забыл

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoMWMod(loader.Module): 
    strings = {"name": "AutoMW"}

    async def watcher(self, message):
        if message.sender_id == 1745526034:
            if "Шаг: 1" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@metro_wars_bot', '♻️ Автобой');

