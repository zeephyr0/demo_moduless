#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoSWMod(loader.Module): 
    """Кто прочитал тот лох""" 
    strings = {"name": "AutoSW"}

    async def watcher(self, message):
        if message.sender_id == 227859379:
            if "Продолжить 💻Работать" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '/job');
            elif "Тебе не хватает Мотивации." in message.raw_text:
                await sleep(3601);
                await message.client.send_message('@StartupWarsBot', '/job');
            elif "Поздравляю! Твоя 🔥Мотивация полностью восстановлена" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '/job');
            elif "Ты достиг нового уровня." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '/levelup');
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '+1 🎓Теория')
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '+1 🐢Мудрость')            
        if message.chat_id == -1573616342 and message.sender_id == 376592453:
            if "⚔В атаку на" in message.raw_text:
                await sleep(300);
                await message.click();
            if "🛡Все в защиту" in message.raw_text:
                await sleep(300);
                await message.click();
        if message.sender_id == 1806724130:
            if "⚔️Готовы к битве:⚔️" in message.raw_text:
                await sleep(300);
                await message.click()
        if message.chat_id == -1001222463353 and message.sender_id == 701686415:
            if "🎖MVP битвы:" in message.raw_text:
                await sleep(180);
                await message.client.send_message('@StartupWarsBot', '/battle');
                await sleep(18);
                await message.client.send_message('@StartupWarsBot', '/to_eat');
                await sleep(2);
                await message.client.send_message('@StartupWarsBot', '🍴Есть');

