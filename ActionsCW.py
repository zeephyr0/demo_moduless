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
                await sleep(10);
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@CityWars2_bot', '👮 Патрулируем');
            elif "👮 На улицах" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@CityWars2_bot', '👮 Патрулируем');
            if "#патруль" in message.raw_text:
                await sleep(40);
                await message.forward_to(-1001222463353);
            if "🚑 Cостоянию здоровья" in message.raw_text:
                await sleep(15);
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@CityWars2_bot', '🚑 Лечим');
            if "🚑 Ты отдохнул" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@CityWars2_bot', '🚑 Лечим');
            if "Пришлось отдать 💵" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@CityWars2_bot', '🏪 Грабим');
            elif "#ограбление" in message.raw_text:
                await sleep(10)
                await message.client.send_message('@CityWars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@CityWars2_bot', '🏪 Грабим');
                await message.forward_to(701686415);
            if "Глава твоей банды запускает атаку на" in message.raw_text:
                await sleep(random.choice(time2));
                await message.click();
            if "Готов ли ты отбиваться? У тебя есть минута на ответ..." in message.raw_text:
                await sleep(random.choise(time1))
                await message.click()
            if "Куда будешь стрелять?" in message.raw_text:
                await message.click(random.choice(buttons));
                await sleep(5);
                await message.click(random.choice(buttons));
