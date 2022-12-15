from .. import loader
from asyncio import sleep

@loader.tds 
class AutoGRMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoGR"}

    async def watcher(self, message):
        if message.sender_id == 5788046441:
            if "Вы убили босса - Гарри Поттер" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@valyutaTG_bot', '🔮 Хогвартс');
            if "Хогвартс" in message.raw_text:
                await sleep(1); 
                await message.click();
            if "Выбери боса для битвы" in message.raw_text:
                await sleep(1); 
                await message.click();
            if "Босс - Гарри Поттер" in message.raw_text:
                await sleep(1); 
                await message.click();
            if "Вы начали бить - Гарри Поттер" in message.raw_text:
                await sleep(1); 
                await message.click();
