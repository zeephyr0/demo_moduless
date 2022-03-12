#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0
#v1.5.1

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoClWMod(loader.Module): 
    """Модуль для частичной автоматизации игры @clan_warsbot\n\nОсобенности модуля:\n• Автоматически ходить в приключение "Кража люков"\nОстальное будет добавляться постепенно по ходу освоения игры автором\n\n❗Модуль создан в ознакомительных целях и может работать нестабильно\nv1.3.0""" 
    strings = {"name": "AutoClW"}

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "🏦🔥Банк ограблен!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🏦 Ограбление банка (1 час)');
            if "🚓Кто-то из вас оказался крысой и слил ваши планы полиции!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
            if "🎫Осталось билетов: 1" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🔍Найти подельников');
            elif "🎫Осталось билетов: 2" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🔍Найти подельников');
            elif "🎫Осталось билетов: 3" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🔍Найти подельников');
            if "Отправиться в приключение💎" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');
        if message.chat_id == -1001649471126 and message.sender_id == 2063668248:
            if "🎭Результаты войны кланов за предприятия" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
        if message.sender_id == 764095451:
            if "Всего раундов:" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');



