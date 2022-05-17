#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class ActionsCWMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "ActionsCW"}

    async def watcher(self, message):
        time1 = [4, 120]
        buttons = [0, 1, 2]
        time2 = [2, 4, 6]
        if message.sender_id == 1399565278:
            if "👮 Ты отдохнул" in message.raw_text:
                await sleep(random.choise(time2));
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@CityWars2_bot', '👮 Патрулируем');
            elif "👮 На улицах" in message.raw_text:
                await sleep(random.choise(time2));
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@CityWars2_bot', '👮 Патрулируем');
            if "🚑 Cостоянию здоровья" in message.raw_text:
                await sleep(random.choise(time2));
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@CityWars2_bot', '🚑 Лечим');
            if "🚑 Ты отдохнул" in message.raw_text:
                await sleep(random.choise(time2));
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@CityWars2_bot', '🚑 Лечим');
        if message.sender_id == 1159155249:
            if "У меня для вас есть несколько 🎁 Подарков!" in message.raw_text:
                await sleep(random.choise(time2)
                await message.click(random.choise(time2));
