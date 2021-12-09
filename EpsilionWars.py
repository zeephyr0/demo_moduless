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
        defense = ['Ноги, голова, грудь', 'Пояс, ноги, голова', 'Живот, пояс, ноги', 'Голову, грудь, живот', 'Грудь, живот, пояс']
        if message.sender_id == 776510403:
            if "Куда будешь бить?" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', random.choice(attack));   
            if "Ход" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', random.choice(attack));   
            if "Что будешь блокировать?" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', random.choice(defense));   
            if "📍 Ты победил своего врага" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', '✅ Забрать нaграду');
            if "🔸 уровень, твое ❤️ здоровье полностью восстановлено" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', '⚔️ Найти врагов');
            if "💖 Ваше здоровье полностью восстановлено" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', '⚔️ Найти врагов');
            if "Ты был отправлен восстанавливаться в город" in message.raw_text:
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', '🗺 Карта');
                await sleep(random.choice(time))
                await message.client.send_message('@EpsilionWarBot', '🏜 Пустошь');
