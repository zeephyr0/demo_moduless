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
                await message.client.send_message('@WastelandWarsBot', '/use_101');
            if "⚠️ACHTUNG!⚠️" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "🐐TestGoat 🤘TеstBand1" in message.raw_text:
                await message.client.send_message('@WasterlandWarsBot', '👣Идти дaльше');
            elif "Эта вылазка могла бы стать последней для тебя. Ты лежал на земле, жадно глотая воздух..." in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WastelandWarsBot', '⛺️Лагерь');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🛠Верстак');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛑Аптечка');
            elif "Уйти отсюда без боя он тебе точно не даст." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Ты можешь попробовать вступить с ним в битву, или же попытаться убежать." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⚔️Дать отпор');
            elif "Ты можешь купить у него редкие вещи." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/buy_5i')
                await sleep(10);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "👣22км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🚷В Темную зону');
            elif "👣45км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🌁Высокий Хротгар');
            elif "👣46км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛺️Вернуться');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Вернуться в лагерь');
                await sleep(300);
                await message.client.send_message('@WastelandWarsBot', '🛠Верстак');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛑Аптечка');
            elif "Ты услышал неподалеку какой-то шум. Ты можешь отправиться дальше, либо не обращать внимания на подозрительные звуки." in message.raw_text:
                await sleep(15);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Противник выглядит устрашающе, победить будет нелегко. Лучше отступи." in message.raw_text:
                await sleep(15);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Ты можешь попытаться воспользоваться элементом неожиданности и напасть на него, или же аккуратно идти дальше." in message.raw_text:
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '🔪Напасть');
                await sleep(25);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '/medpack');
            elif "👁Осмотреться" in message.raw_text:
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Ты одержал победу!" in message.raw_text:
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            if "Использован 💉++ Суперстим." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛺️Лагерь');
                await sleep(5);
                await message.client.send_message('@WastelandWarsBot', '⬅️Назад');
                await sleep(3);
                await message.client.send_message('@WastelandWarsBot', '🏘В Нью-Рино');
            elif "Эти предметы помогут тебе продержаться еще один день в Пустоши." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💉++ Суперстим');
            if "Около бара лежит мертвый бомж." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💰Ломбард');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Обменять все');
            if "Ты продал" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🎓Обучение');
            if "🚫 Недостаточно ресурсов!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🍺Бар');
            elif "Мудрый старец готов обучить тебя необходимым навыкам. Не бесплатно, разумеется. Крышечки тут всегда в ходу." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '❤️Живучесть');
            elif "Теперь ты стал немного опытнее." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '❤️Живучесть');
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
