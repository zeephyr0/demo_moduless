 .. import loader
from asyncio import sleep

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
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '☠ Локации');
            if "Пора в бой!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🐣1-10 Окрестности Ген. штаба');
            if "На пути у вас встретился" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@rf_telegram_bot', '🔪 Атаковать');
