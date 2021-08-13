#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoWWMod(loader.Module): 
    """Кто прочитал тот лох""" 
    strings = {"name": "AutoWW"}

    async def watcher(self, message):
        if message.sender_id == 430930191:
            if "Казалось, что этой шахте нет конца." in message.raw_text:
                await sleep(2);
                await message.forward_to(963853904);
            elif "Как оказалось, даже в канализации ты умудрился найти что-то полезное." in message.raw_text:
                await sleep(2);
                await message.forward_to(963853904);
            elif "Стоп... Это что, конец? Всё? Вот она, ебучая вершина горы?" in message.raw_text:
                await sleep(2);
                await message.forward_to(963853904);
            if "Сражение с" in message.raw_text:
                await sleep(2);
                await message.forward_to(1073120406);
            if "Раньше эту шахту активно бурили. Кажется, из глубины доносятся какие-то звуки." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Враги в канализации? Сомнительно, братан. Но воняет неприятно." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "⚠️ACHTUNG!⚠️" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            if "Ты очень голоден." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/use_101');
            if "Эта вылазка могла бы стать последней для тебя. Ты лежал на земле, жадно глотая воздух..." in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WastelandWarsBot', '⛺️Лагерь');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🛠Верстак');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛑Аптечка');
            elif "Сражение с 👁Мутант (Голодный)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 👁Мутант (❗️Огромный)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🐲Трог (❗️Огромный)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🐲Трог (💙Леонардо)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🐲Трог (💛Микеланджело)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🐲Трог (💜Донателло)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🐲Трог (❤️Рафаэль)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Они все мертвы." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🦀Краб (Грязевой)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🌞Атронах (🔥Огненный)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с ㊙️Дремора (🔥Даэдра)" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Двигаться дальше');
            elif "Сражение с 🐲Алдуин (🔥Пожиратель Мира)" in message.raw_text:
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
            elif "❤️-" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⚔️Атаковать')
            elif "Твое местоположение: Возле гиганта" in message.raw_text:
                await sleep(150);
                await message.client.send_message('@WastelandWarsBot', '📟Пип-бой');
                await sleep(150);
                await message.client.send_message('@WastelandWarsBot', '🔎Дeйствие');
            elif "Если тебе есть что терять, то лучше отступи в лагерь." in message.raw_text:
                await sleep(150);
                await message.client.send_message('@WastelandWarsBot', '📟Пип-бой');
                await sleep(150);
                await message.client.send_message('@WastelandWarsBot', '🔎Дeйствие');
            elif "Ты услышал неподалеку какой-то шум. Ты можешь отправиться дальше, либо не обращать внимания на подозрительные звуки." in message.raw_text:
                await sleep(5);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "Противник выглядит устрашающе, победить будет нелегко. Лучше отступи." in message.raw_text:
                await sleep(15);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "🐐TestGoat 🤘TestBand1" in message.raw_text:
                await message.client.send_message('@WasterlandWarsBot', '👣Идти дaльше');
            elif "🐐TestGoat 🤘TеstBand1" in message.raw_text:
                await message.client.send_message('@WasterlandWarsBot', '👣Идти дaльше');
            elif "Ты можешь попытаться воспользоваться элементом неожиданности и напасть на него, или же аккуратно идти дальше." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🔪Напасть');
                await sleep(75);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
                await sleep(20);
                await message.client.send_message('@WastelandWarsBot', '/medpack');
            elif "18 👣11км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Старая шахта');
            elif "18 👣22км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🚷В Темную зону');
            elif "18 👣23км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🚽Сточная труба');
            elif "18 👣24км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/goboss');
                await sleep(10);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "18 👣28км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '/goboss');
                await sleep(10);
                await message.client.send_message('@WastelandWarsBot', '👣Идти дaльше');
            elif "18 👣45км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🌁Высокий Хротгар');
            elif "18 👣52км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🚷В Темную зону');
            elif "18 👣58км" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⛺️Вернуться');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', 'Вернуться в лагерь');
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
                await message.client.send_message('@WastelandWarsBot', '🍺Бар');
            elif "Получено:💌Медпак" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💌 Медпак');
            if "🥖Взять булочку: 🕳80" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@WastelandWarsBot', '/eat2');
            if "Ты объелся и чувствуешь себя нехорошо." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🏘Нью-Рино');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '⬅️Назад');
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '🎓Обучение');
            elif "Ты сыт. Осторожнее с перееданием, здоровяк." in message.raw_text:
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
            elif "Мудрый старец готов обучить тебя необходимым навыкам. Не бесплатно, разумеется. Крышечки тут всегда в ходу." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💪Сила');
            elif "Теперь ты стал немного опытнее." in message.raw_text:
                await sleep(2);
                await message.client.send_message('@WastelandWarsBot', '💪Сила');

