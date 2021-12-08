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
                await message.client.send_message('@EpsilionWarBot', 'В ноги');
            if "📍 Ты победил своего врага" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', '✅ Забрать нaграду');
            elif "Ход" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', 'В ноги');
            if "Что будешь блокировать?" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', 'Ноги, голова');
            if "💖 Ваше здоровье полностью восстановлено" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', '⚔️ Найти врагов');
            if "Ты был отправлен восстанавливаться в город" in message.raw_text:
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', '🗺 Карта');
                await sleep(3)
                await message.client.send_message('@EpsilionWarBot', '🏞 Устье реки');
