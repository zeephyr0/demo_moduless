
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoRFMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoRF"}

    async def watcher(self, message):
        if message.sender_id == 577009581:
            if "[недостаточно энергии]" in message.raw_text:
                await sleep(725);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            if "+1 к энергии" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            if "На пути у вас встретился" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            elif "Ты наткнулся на" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            if "нанес удар 💔" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🏛 В ген. штаб');
                await sleep (125);
                await message.client.send_message('@rf_telegram_bot', '💖 Пополнить здоровье');
                await sleep (3);
                await message.client.send_message('@rf_telegram_bot', '☠ Локации');
                await sleep (3);
                await message.client.send_message('@rf_telegram_bot', '🐣1-10 Окрестности Ген. штаба');
            elif "Ты нанес удар 💥" in message.raw_text:
                await sleep (2);
                await message.client.send_message('@rf_telegram_bot', '🐺 Любой');
