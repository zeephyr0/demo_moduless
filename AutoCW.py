
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoCWMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoCW"}

    async def watcher(self, message):
        if message.chat_id == -1001222463353 and message.sender_id == 701686415:
            if "Забирайте свой бонус🧚‍♀💛" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '/daily');
            elif "Атакуем" in message.raw_text:
                await sleep(300);
                await message.client.send_message('@citywars2_bot', '/buy_set_1');
            elif "Встаём в" in message.raw_text:
                await sleep(300);
                await message.client.send_message('@citywars2_bot', '/buy_set_1');
            if "✅ На битве" in message.raw_text:
                await sleep(300);
                await message.click();
            elif "🎖MVP битвы:" in message.raw_text:
                await sleep(180);
                await message.client.send_message('@citywars2_bot', '/war');
                await sleep(280);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
        if message.sender_id == 1399565278:
            if "@CityWars2Reports" in message.raw_text:
                await sleep(20);
                await message.forward_to(701686415);
            if "👮 На улицах" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '👮 Патрулируем');
            if "#патруль" in message.raw_text:
                await sleep(40);
                await message.forward_to(-1001222463353);
                await sleep(570);
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
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "#лечка" in message.raw_text:
                await sleep(40);
                await message.forward_to(701686415);
                await sleep(205);
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
                await message.forward_to(701686415);
            if "🎈 У тебя есть неполученный бонус!" in message.raw_text:
                await sleep(50);
                await message.click();
