import random
import asyncio
import re  # Импортируем регулярные выражения
from .. import loader
from hikkatl.types import Message

@loader.tds
class NarutoAdventureMod(loader.Module):
    """Авто рейды нахуй"""

    strings = {"name": "NarutoAdventure"}

    def __init__(self):
        self.limit_active = False  # Изначально статус лимита не активен
    
    async def client_ready(self, client, db):
        self.client = client

    async def limitoffcmd(self, message: Message):
        """Команда для деактивации статуса лимита"""
        self.limit_active = False
        await self.client.send_message(message.sender_id, "Статус лимита отключен.")


    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id == 6745912139:
            # Проверка на уровень отдаленности от деревни
            if "🗺 Уровень отдаленности от деревни: 16" in message.raw_text:
                # Если уровень отдаленности 16, отправляем текст с первой кнопки второй строки
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                        button_text = message.reply_markup.rows[1].buttons[0].text  # Текст с первой кнопки второй строки
                        await asyncio.sleep(random.uniform(4, 9))
                        await self.client.send_message(message.sender_id, button_text)
                return  # Не продолжать проверку, если выполнено условие для отдаленности

            # Проверка на сытость
            hunger_match = re.search(r"🍜 Ваша сытость: (\d+)", message.raw_text)
            if hunger_match:
                # Извлекаем значение сытости
                hunger_value = int(hunger_match.group(1))
                
                if hunger_value > 8:
                    # Если сытость больше 8, отправляем текст с первой кнопки первой строки
                    if message.reply_markup and message.reply_markup.rows:
                        if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                            button_text = message.reply_markup.rows[0].buttons[0].text
                            await asyncio.sleep(random.uniform(1, 7))
                            await self.client.send_message(message.sender_id, button_text)
                else:
                    # Если сытость 8 или меньше, отправляем текст с первой кнопки второй строки
                    if message.reply_markup and message.reply_markup.rows:
                        if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                            button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс кнопки во второй строке
                            await asyncio.sleep(random.uniform(1, 7))
                            await self.client.send_message(message.sender_id, button_text)
                            
            # Проверка на сообщение "❔ Вы хотите вернуться в деревню?"
            if "❔ Вы хотите вернуться в деревню?" in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(4, 9))
                        await self.client.send_message(message.sender_id, button_text)
                        await asyncio.sleep(random.uniform(10, 30))
                        await self.client.send_message(message.sender_id, "🍜 Квартал ресторанов")

            if "❌ У ресторана закончились продукты, заходите позже!" in message.raw_text:
                self.limit_active = True
                
            # Проверка состояния лимита перед обработкой выбора еды
            if "❔ Выберите еду" in message.raw_text:
                if self.limit_active:
                    return  # Не выполняем дальнейшие действия, если лимит активен

                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 1:
                        button_text = message.reply_markup.rows[0].buttons[1].text  # Текст со второй кнопки первой строки
                        delay = random.uniform(2, 7)
                        await asyncio.sleep(delay)
                        await self.client.send_message(message.sender_id, button_text)
                        
            if "❌ Вы уже сыты!" in message.raw_text:
                delay = random.uniform(2, 7) 
                await asyncio.sleep(delay) 
                await self.client.send_message(message.sender_id, "/raid")
        
            if "🍜 Перед вылазкой, вы можете взять еду с собой. Она восстанавливает сытость и позволяет пройти дальше." in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        # Получаем текст первой кнопки и отправляем его
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)
                      
            if "🏚 Выберите на каком уровне отдаленности вы хотите начать" in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:  # Проверяем, что во второй строке есть хотя бы 1 кнопка
                         # Получаем текст первой кнопки второй строки и отправляем его
                            button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс [1][0] для первой кнопки
                            await asyncio.sleep(random.uniform(1, 7))
                            await self.client.send_message(message.sender_id, button_text)
                
            if "В одном из городов, где вы остановились, вы нашли онсэн. Абонемент стоит 2 млн рё." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:  # Проверяем наличие reply_markup и его строк
        # Проверяем, что в второго строки есть минимум 1 кнопка
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс [1][0] для второй строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "На окраине деревни вы заметили старый колодец, увитый глициниями. Местные жители рассказали вам, что если загадать желание и бросить монетку, то судьба обязательно сведет вас с тем, кого вы желаете встретить." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:  # Проверяем наличие reply_markup и его строк
        # Проверяем, что в второго строки есть минимум 1 кнопка
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Индекс [0][0] для второй строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Похоже, это была самая популярная подобная точка в стране." in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        # Получаем текст первой кнопки и отправляем его
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время короткого отдыха в тени дерева вы замечаете в траве какой-то блеск." in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Вы находите обломок маски они, наполовину ушедший в мягкий речной ил. Белая глина потрескалась и потемнела от времени, но на внутренней стороне еще видны бурые пятна, похожие на засохшую кровь. " in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "По дороге вы замечаете лежащего на обочине человека. Приблизившись, вы видите, что он ранен и без сознания." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    # Проверяем наличие кнопок на третьей строке
                    if len(message.reply_markup.rows) > 2 and len(message.reply_markup.rows[2].buttons) > 0:
                        button_text = message.reply_markup.rows[2].buttons[0].text  # Текст первой кнопки третьей строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Ночной ветер доносит до вас странный аромат - сладковатый и тяжелый, он напоминает благовония, которыми жрецы окуривают мертвецов перед погребением." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение о дожде
            if "Дождь безжалостно хлещет ваше лицо, тело пробивает озноб. Вы дрожите, но продолжаете идти, стараясь не обращать внимания на горячку с её кислотными видениями." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение о утре
            if "Утром наступает... утро, и это довольно необычно, если смириться со своей участью. Вы в богатой комнате, пахнущей свежими татами, рисовой водой и зеленым чаем." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение о усилии воли
            if "Усилием воли вы разбираете очертания и комнаты, и девушки." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)
                 
