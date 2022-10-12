#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoSEMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoSE"}

    async def watcher(self, message):
        war_buttons = [0, 1, 2]
        time1 = [4, 120]
        buttons = [0, 1, 2]
        time2 = [2, 4, 6]
        if message.sender_id == 605298957:
            if "📡Ты вернулся с поиска обломков. " in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '⌨️');
            if "👁‍🗨Ты в космосе" and "🔋13" in message.raw_text:
                await sleep(1);
                await message.click();
            elif "👁‍🗨Ты в космосе возле ☠️Пиратская станция" in message.raw_text:
                await sleep(1);
                await message.click(0);
            elif "👁‍🗨Ты в космосе" in message.raw_text:
                await sleep(1);
                await message.click(3);
            if "📡Ты можешь отправиться на поиски обломков, в которых иногда можно найти ценные ресурсы." in message.raw_text:
                await sleep(1);
                await message.click();
            if "Недостаточно 🔋топлива" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '⌨️');
            if "👁‍🗨Ты на корабле." and "🔋13" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '/buy_max_fuel');
            if "👁‍🗨Ты на корабле." and "🔋400" in message.raw_text:
                await sleep(1);
                await message.click(2);
            if "☠️На радаре появились подходящие отметки!" in message.raw_text:
                await sleep(1);
                await message.click(0);
            if "🎯Куда прикажешь выстрелить?" in message.raw_text:
                await sleep(1);
                await message.click(random.choice(war_buttons));
            if "🔰Перед чем поднять щиты?" in message.raw_text:
                await sleep(1);
                await message.click(random.choice(war_buttons));
