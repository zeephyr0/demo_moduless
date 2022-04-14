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
                await sleep(15);
                await message.client.send_message('@metro_wars_bot', '/g');
                await sleep(7);
                await message.client.send_message('@metro_wars_bot', '🏜 Трубная [👾1-4🔮37-38]🔋30');
            if "Активирован" in message.raw_text:
                await sleep(1);
                await message.click();
            if "Деактивирован" in message.raw_text:
                await sleep(1);
                await message.click();
            if "🔋145/150" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Трубная');
            elif "Станция отправления" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
            if "Монстров нет" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '⬅️ Назад на Тверская');
            if "На вас нападают:" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@metro_wars_bot', '⚔️ Драться');
                await sleep(7);
                await message.client.send_message('@metro_wars_bot', '🏃 Движение');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↕️ По направлению');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↖');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '🌀 Умения');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '🖲 Ловушка');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↕️ По направлению');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↖');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '✅ Подтвердить');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '📜 Карта боя');
            if "Вы нападаете на" in message.raw_text:
                await sleep(7);
                await message.client.send_message('@metro_wars_bot', '🏃 Движение');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↕️ По направлению');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↘');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '🌀 Умения');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '🖲 Ловушка');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↕️ По направлению');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '↘');
                await sleep(6);
                await message.client.send_message('@metro_wars_bot', '✅ Подтвердить');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '📜 Карта боя');
            if "Шаг: 3" in message.raw_text:
                await sleep(3);
                await message.client.send_message('@metro_wars_bot', '♻️ Автобой');



