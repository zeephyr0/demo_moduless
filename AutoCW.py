
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoCWMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoCW"}

    async def watcher(self, message):
        if message.chat_id == -1001222463353 and message.sender_id == 701686415:
            if "Забирайте свой бонус🧚‍♀💛" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '/daily');
            if "✅ На битве" in message.raw_text:
                await sleep(2)
                await message.client.send_message('@citywars2_bot', '/buy_set_1');
                await sleep(3);
                await message.client.send_message('@citywars2_bot', '/war');
                await sleep(300);
                await message.click();
        if message.sender_id == 1399565278:
            if "@CityWars2Reports" in message.raw_text:
                await sleep(2);
                await message.forward_to(1222463353);
            if "#патруль" in message.raw_text:
                await sleep(10);
                await message.forward_to(-1001222463353);
            if "#лечка" in message.raw_text:
                await sleep(40);
                await message.forward_to(701686415);
            if "#ограбление" in message.raw_text:
                await sleep(10)
                await message.forward_to(701686415);
            if "🎈 У тебя есть неполученный бонус!" in message.raw_text:
                await sleep(5);
                await message.click();
