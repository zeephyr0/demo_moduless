#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoWWMod(loader.Module): 
    """Кто прочитал тот лох""" 
    strings = {"name": "AutoWW"}

    async def watcher(self, message):
        if message.sender_id == 430930191:
            if "Ты очень голоден." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/myfood');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/use_101 ');
            if "Ты можешь попробовать вступить с ним в битву, или же попытаться убежать." in message.raw_text:
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '⚔️Дать отпор');
            elif "👣22км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🚷В Темную зону');
            elif "👣45км" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@WastelandWarsBot', '⛺️Вернуться');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Вернуться в лагерь');
                await sleep(200);
                await message.client.send_message('@WastelandWarsBot', '⬅️Назад');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘В Нью-Рино');
            elif "👁Осмотреться" in message.raw_text:
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Ты одержал победу!" in message.raw_text:
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            if "Около бара лежит мертвый бомж." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🍺Бар');
            if "🥖Взять булочку: 🕳80" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@WastelandWarsBot', '/eat2');
            if "Ты сыт. Осторожнее с перееданием, здоровяк." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⬅️Назад');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '👣Пустошь');
            elif "Ты съел Булочка." in message.raw_text:
                await sleep(10);
                await message.client.send_message('@WastelandWarsBot', '/eat2');
            if "Ты можешь купить у него редкие вещи." in message.raw_text:
                await sleep(4);
                await message.client.send_message('@WastelandWarsBot', '/buy_5i')
