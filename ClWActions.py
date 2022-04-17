#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0

from .. import loader
from asyncio import sleep

@loader.tds 
class ClWActionsMod(loader.Module): 
    strings = {"name": "ClWActions"}

    async def watcher(self, message):
        if message.group_id and message.sender_id == 920762514:
            if "" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '');
