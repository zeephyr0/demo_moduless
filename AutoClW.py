#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoClWMod(loader.Module): 
    strings = {"name": "AutoClW"}

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "🎊Приключение «Кража люков» успешно завершено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');
            if "🎊Приключение «Бриллиантовая афера» успешно завершено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '💎 Бриллиантовая афера (3 часа)');
            elif "🚓Приключение провалено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');
            if "🏦🔥Банк ограблен!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🏦 Ограбление банка (1 час)');
            if "🚓Кто-то из вас оказался крысой и слил ваши планы полиции!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🏦 Ограбление банка (1 час)');
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
            if "Вы победили!" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@clan_warsbot', '⚔️Арена');
            if "Вы проиграли!" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@clan_warsbot', '⚔️Арена');
            if "Сразитесь против других игроков из враждующих кланов!" in message.raw_text:
                await sleep(1);
                await message.click();
        if message.chat_id == -1001649471126 and message.sender_id == 2063668248:
            if "🎭Результаты войны кланов за предприятия" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');

