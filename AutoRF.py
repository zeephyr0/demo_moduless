from .. import loader
from asyncio import sleep
import random


@loader.tds 
class AutoRFMod(loader.Module): 
    strings = {"name": "AutoRF"}

    async def watcher(self, message):
        if message.sender_id == 577009581:
            if "Ты одержал победу!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🏛 В ген. штаб');
            if "Ты дошел до локации." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '💖 Пополнить здоровье');
            if "Ты снова жив👼" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '☠ Локации');
            if "Пора в бой!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🐥 11-20 Аванпост');
            if "+1 к энергии 🔋5/5" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '☠ Локации');
            if "Ты наткнулся на Змееголов" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            elif "Ты наткнулся" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🐺 Любой');
            if "На пути у вас встретился Змееголов" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
            elif "На пути у вас встретился" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🐺 Любой');



           
