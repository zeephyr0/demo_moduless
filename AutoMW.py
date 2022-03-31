#и хули ты тут забыл

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoMWMod(loader.Module): 
    strings = {"name": "AutoMW"}

    async def watcher(self, message):
        time = [5, 10, 15]
        if message.sender_id == 1745526034:
            if "Ты полноценно отдохнул!" in message.raw_text:
                await sleep(30);
                await message.client.send_message('@metro_wars_bot', '/g');
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '🏜 Тверская [👾1-4🔮35-36]🔋25');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Тверская');
            if "Активирован" in message.raw_text:
                await sleep(2);
                await message.click();
            if "Деактивирован" in message.raw_text:
                await sleep(2);
                await message.click();
            if "На вас нападают:" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '⚔️ Драться');
            if "Шаг: 1" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '🌀 Умения');
                await sleep(7);
                await message.client.send_message('@metro_wars_bot', '🖲 Ловушка');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↕️ По направлению');
                await sleep(4);
                await message.client.send_message('@metro_wars_bot', '↖');
                await sleep(4);
                await message.client.send_message('@metro_wars_bot', '✅ Подтвердить');
                await sleep(8);
                await message.client.send_message('@metro_wars_bot', '📜 Карта боя');
            if "Шаг: 2" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '♻️ Автобой');
            if "Бой выигран" in message.raw_text:
                await sleep(7);
                await message.client.send_message('@metro_wars_bot', '⬅️ Назад на Маяковская');
            if "Вы подошли к выходу на поверхность Маяковская." in message.raw_text:
                await sleep(4);
                await message.client.send_message('@metro_wars_bot', '/g');



