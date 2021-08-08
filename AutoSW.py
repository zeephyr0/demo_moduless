#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoSWMod(loader.Module): 
    """Кто прочитал тот лох""" 
    strings = {"name": "AutoSW"}

    async def watcher(self, message):
        if message.chat_id == 1573616342 and message.sender_id == 376592453 and message.sender_id == 1806724130:
            if "⚔В атаку на" in message.raw_text:
                await sleep(300);
                await message.click();
            if "🛡Все в защиту" in message.raw_text:
                await sleep(300);
                await message.click();
            if "⚔️Готовы к битве:⚔️" in message.raw_text:
                await sleep(300);
                await message.click();
        if message.sender_id == 227859379:
            if "Продолжить 💻Работать" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '/job');
            if "Тебе не хватает Мотивации." in message.raw_text:
                await sleep(3601);
                await message.client.send_message('@StartupWarsBot', '/job');
            if "Поздравляю! Твоя 🔥Мотивация полностью восстановлена" in message.raw_text:
            if "Ты достиг нового уровня." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '/levelup');
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '+1 🔨Практика')
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '+1 🐿Хитрость')            
