from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoBSClWMod(loader.Module): 
    strings = {"name": "AutoBSClW"}

    async def watcher(self, message):
        time1 = [5, 10, 15]
        time2 = [30, 50, 70] 
        if message.sender_id == 2063668248:
            if "🎊Приключение «Кража люков» успешно завершено!" in message.raw_text:
                await sleep(random.choice(time1));
                await message.client.send_message('@BSv2Bot', '⬆️ Наверх');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⚔️ Гарнизон');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "🚓Приключение провалено!" in message.raw_text:
                await sleep(random.choice(time1));
                await message.client.send_message('@BSv2Bot', '⬆️ Наверх');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⚔️ Гарнизон');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            if "🏦🔥Банк ограблен!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
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
            if "[🐉🤺]ZEPHYR" in message.raw_text:
                await sleep(2);
                await message.forward_to(-1001494500538);
            elif "Территория: 1," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 2," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 3," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 4," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 5," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 6," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 6," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 7," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 8," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 9," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 10," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 11," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 12," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 13," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 14," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 15," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Территория: 16," in message.raw_text:
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            elif "Цель:" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⚔️ Атаковать');
            elif "🗺 Разведка" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🔍 Иcкaть');
            if "Всего раундов:" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');
                await sleep(random.choice(time1));
                await message.forward_to(666473433);
            if "Копать еще:" in message.raw_text:
                await sleep(random.choice(time2));
                await message.client.send_message('@BSv2Bot', '/dig');
            if "🕑 Дозор окончен." in message.raw_text:
                await sleep(random.choice(time2));
                await message.client.send_message('@BSv2Bot', '⬆️ Наверх');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⚔️ Гарнизон');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🕑 Дозор');
            if "🕑 Чтобы отправить дозорных необходимо" in message.raw_text:
                await sleep(2);
                await message.click();
