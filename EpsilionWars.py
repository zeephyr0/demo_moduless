#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class EpsillionWarsMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "EpsillionWars"}

    async def watcher(self, message):
        if message.sender_id == 776510403:
            if "Куда будешь бить?" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Ход 1" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Ход 2" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Ход 3" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Ход 4" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Ход 5" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Ход 6" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarsBot', 'В ноги');
            if "Что будешь блокировать?" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', 'Ноги, голова');
            if "💖 Ваше здоровье полностью восстановлено" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', '⚔️ Найти врагов');
