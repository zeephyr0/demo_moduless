#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoWWraidMod(loader.Module): 
    """Кто прочитал тот лох""" 
    strings = {"name": "AutoWW Raid"}

    async def watcher(self, message):
        if message.sender_id == 430930191:
            if "Эта вылазка могла бы стать последней для тебя. Ты лежал на земле, жадно глотая воздух..." in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WastelandWarsBot', '⛺️Лагерь');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🛠Верстак');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛑Аптечка');
            elif "Ты можешь попробовать вступить с ним в битву, или же попытаться убежать." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⚔️Дать отпор');
            elif "Ты можешь купить у него редкие вещи." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/buy_5i')
                await sleep(10);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "🐐TestGoat 🤘" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "🐐 FǁȺǁggǁØǁAT 🤘" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Ты можешь попытаться воспользоваться элементом неожиданности и напасть на него, или же аккуратно идти дальше." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🔪Напасть');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/eq_1002');
            elif "Получено: Человечина" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/eq_480');
            elif "18 👣20км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/voevat_suda');    
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/eq_1002');
            elif "Ты занял позицию для 👊Рейда и приготовился к групповому сражению козлов." in message.raw_text:
                await sleep(2);
                await message.forward_to(963853904);
            elif "18 👣23км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛺️Вернуться');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Вернуться в лагерь');  
            elif "Ты отправился в лагерь. Как ни странно, время летит гораздо быстрее, когда ты идешь в обратную сторону." in message.raw_text:
                await sleep(300);
                await message.client.send_message('@WastelandWarsBot', '🛠Верстак');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛑Аптечка');          
            elif "👁Осмотреться" in message.raw_text:
                await sleep(18);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Ты одержал победу!" in message.raw_text:
                await sleep(18);
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
                await message.client.send_message('@WastelandWarsBot', '👓Инженер');
            if "Если у тебя есть материалы и много нужных деталей, то этот парень сможет соорудить тебе очень неплохую экипировку." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛑Аптечка');
            if "Эти технологические приблуды дороги, но они могут выручить тебя прямо во время вылазки." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💉 Мед-Х');
            if "Ты можешь носить только два таких шприца с собой." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💌 Медпак');
            elif "Инженер достал из ящика стола маленький шприц с зеленоватой жидкостью. Вытащив иглу из своей руки, он швырнул все мне на стол." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💉 Мед-Х');
            if "👝Сумка под медпаки вмещает максимум 3 шт." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💰Ломбард');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Обменять все');
            elif "Получено:💌Медпак" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💌 Медпак');
            if "Ты продал" in message.raw_text:
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
                await message.client.send_message('@WastelandWarsBot', '🎓Обучение');
            elif "Ты объелся и чувствуешь себя нехорошо." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⬅️Назад');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🎓Обучение');
            elif "Ты съел Булочка." in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WastelandWarsBot', '/eat2');
            if "🚫 Недостаточно ресурсов!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '👣Пустошь');
            elif "Теперь ты стал немного опытнее." in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WastelandWarsBot', '💪Сила');
            elif "Мудрый старец готов обучить тебя необходимым навыкам. Не бесплатно, разумеется. Крышечки тут всегда в ходу." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💪Сила');
