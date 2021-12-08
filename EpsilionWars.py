#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class EpsillionWarsMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "EpsillionWars"}

    async def watcher(self, message):
        time = [2, 5, 8]
        attack = ['В ноги', 'В пояс', 'В живот', 'В грудь', 'В голову']
        defense = ['Ноги, голова', 'Пояс, ноги', 'Живот, пояс', 'Грудь, живот', 'Голова, грудь']
        if message.sender_id == 776510403:
            if "Куда будешь бить?" in message.raw_text:
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', random.choise(attack));   
            if "Ход" in message.raw_text:
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', random.choise(attack));   
            if "Что будешь блокировать?" in message.raw_text:
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', random.choise(defense));   
            if "📍 Ты победил своего врага" in message.raw_text:
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', '✅ Забрать нaграду');
            if "💖 Ваше здоровье полностью восстановлено" in message.raw_text:
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', '⚔️ Найти врагов');
            if "Ты был отправлен восстанавливаться в город" in message.raw_text:
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', '🗺 Карта');
                await sleep(random.choise(time))
                await message.client.send_message('@EpsilionWarBot', '🏕 Дом в лесу');
