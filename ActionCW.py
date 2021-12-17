#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class ActionsCWMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "ActionsCW"}

    async def watcher(self, message):
        sleep = [4, 120]
        buttons = [0, 1, 2]
        time = [2, 4, 6]
        if message.sender_id == 1399565278:
            if "👮 Ты отдохнул" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '👮 Патрулируем');
            elif "👮 На улицах" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '👮 Патрулируем');
            if "🚑 Cостоянию здоровья" in message.raw_text:
                await sleep(15);                
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "🚑 К сожалению, тебе не хватило умения, чтобы вылечить" in message.raw_text:
                await sleep(245);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "🚑 Ты отдохнул" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "#лечка" in message.raw_text:
                await sleep(245);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "Пришлось отдать 💵" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '🏪 Грабим');
            elif "#ограбление" in message.raw_text:
                await sleep(10)
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '🏪 Грабим');
            if "Глава твоей банды запускает атаку на" in message.raw_text:
                await sleep(random.choice(time));
                await message.click();
            if "Готов ли ты отбиваться? У тебя есть минута на ответ..." in message.raw_text:
                await sleep(random.choise(sleep))
                await message.click()
            if "Куда будешь стрелять?" in message.raw_text:
                await message.click(random.choice(buttons));
                await sleep(5);
                await message.click(random.choice(buttons));
