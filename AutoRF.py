
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoRFMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoRF"}

    async def watcher(self, message):
        if message.sender_id == 577009581:
            if "+1 к энергии" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            elif "На пути у вас встретился" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            elif "Ты наткнулся на" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            if "нанес удар 💔" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🏛 В ген. штаб');
            elif "Ты нанес удар 💥" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🐺 Любой');
            if "Ты дошел до локации." in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '💖 Пополнить здоровье');
            if "Здоровье пополнено" in message.raw_text:
                await sleep (3);
                await message.client.send_message('@rf_telegram_bot', '☠ Локации');
            if "Пора в бой!" in message.raw_text:
                await sleep (3);
                await message.client.send_message('@rf_telegram_bot', '🐥 11-20 Аванпост');

