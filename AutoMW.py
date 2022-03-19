#и хули ты тут забыл

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoMWMod(loader.Module): 
    strings = {"name": "AutoMW"}

    async def watcher(self, message):
        if message.sender_id == 1745526034:
            if "Ты полноценно отдохнул!" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Главная площадь');
                await sleep(20);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Туннель');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Лубянка [👾1-2🔮13-14]🔋20');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
                await sleep(60);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Лубянка');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
                await sleep(60);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Лубянка');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
                await sleep(60);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Лубянка');
            if "На вас нападают:" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '⚔️ Драться');
            if "Шаг: 1" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@metro_wars_bot', '♻️ Автобой');
            if "«Лубянка» - еще один центр торговли Московского метро. В основном тут живут семьи торговцев и бакалейщиков. В служебных помещениях находятся склады, а на платформе - огромное количество торговых палаток. Найти тут можно все, что угодно: от патронов до противогаза. Периодически на станцию совершают нападки мутанты из Детского мира, но беспокоиться не стоит — гермоворота охраняют бойцы с самым мощным вооружением." in message.raw_text:
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '⚖️ Торговец');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🔘 Продать ненужное');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '✅ Подтвердить');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Главная площадь');
                await sleep(20);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Туннель');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Чистые пруды [👾1-2🔮13-14]🔋20');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Чистые пруды');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Чистые пруды');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Чистые пруды');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '⛑ Медпункт');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '❤️‍🩹 Восстановить здоровье');


