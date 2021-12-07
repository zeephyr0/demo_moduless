#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class EspillionWarsMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "EspillionWars"}

    async def watcher(self, message):
        if message.sender_id == 776510403:
            if "Вот ты и встретил своего врага." in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Что будешь блокировать?" in message.raw_text:
                await sleep(4)
                await message.client.send_message('@EpsilionWarBot', 'Ноги, голова');
