#и хули ты тут забыл

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoMWMod(loader.Module): 
    strings = {"name": "AutoMW"}

    async def watcher(self, message):
        if message.sender_id == 1745526034:
            if "«Чистые пруды» — это жилая станция, в то же время она играет роль торгового перевалочного пункта и склада. Причиной тому стало ее расположение на торговых путях между «Лубянкой» и «Комсомольской». На платформе расположены жилые палатки, гостиница и медпункт. В гостинице останавливаются не только челноки и торговцы, но и Путешественники, держащие путь к «Красным воротам» и выходу на поверхность. В медпункте они оказываются на обратном пути. Во всяком случае чаще всего" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '⛑ Медпункт');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '❤️‍🩹 Восстановить здоровье');
                await sleep(10)
                await message.client.send_message('@metro_wars_bot', '🔘 Продать ненужное');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '✅ Подтвердить');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Главная площадь');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🚥 Переход');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', 'Сретенский бульвар');
            if "Ты полноценно отдохнул!" in message.raw_text:
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Туннель');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Чкаловская [👾1-3🔮19-20]🔋25');
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
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🚥 Переход');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '⛑ Курская (синяя)');
            if "Помешанность «Курской» на чистоте – притча во языцех. Костры здесь не разводят из соображений безопасности, поэтому нет ни копоти, ни сажи, полы чисто подметены, никакого мусора и беспорядка. Именно здесь располагается один из крупнейших медпунктов в метро. Кстати, ты не забыл прикрепиться к одному из них? Наружный вестибюль станции находится на Земляном Валу, а там всегда есть, чем поживиться" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '⛑ Медпункт');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '❤️‍🩹 Восстановить здоровье');
                await sleep(10)
                await message.client.send_message('@metro_wars_bot', '🔘 Продать ненужное');
                await sleep(900);
                await message.client.send_message('@metro_wars_bot', '✅ Подтвердить');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Главная площадь');
                await sleep(20);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🚥 Переход');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', 'Чкаловская');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Туннель');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🍙 Сретенский бульвар [👾1-3🔮19-20]🔋25');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
                await sleep(60);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Сретенский бульвар');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
                await sleep(60);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Сретенский бульвар');
                await sleep(9);
                await message.client.send_message('@metro_wars_bot', '👾 Поиск монстров');
                await sleep(60);
                await message.client.send_message('@metro_wars_bot', '➡️ Вперёд на Сретенский бульвар');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🏃 Покинуть станцию');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '🚥 Переход');
                await sleep(10);
                await message.client.send_message('@metro_wars_bot', '⛑ Чистые пруды');
            if "На вас нападают:" in message.raw_text:
                await sleep(5);
                await message.client.send_message('@metro_wars_bot', '⚔️ Драться');
            if "Шаг: 1" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@metro_wars_bot', '♻️ Автобой');



