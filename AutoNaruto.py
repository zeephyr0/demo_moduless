import random
import asyncio
import re  # Импортируем регулярные выражения
from .. import loader
from hikkatl.types import Message

@loader.tds
class NarutoAdventureMod(loader.Module):
    """Авто рейды нахуй"""

    strings = {"name": "NarutoAdventure"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id == 6745912139:
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
                            await asyncio.sleep(random.uniform(2, 4))
                            await self.client.send_message(message.sender_id, button_text)
                else:
                    # Если сытость 8 или меньше, отправляем текст с первой кнопки второй строки
                    if message.reply_markup and message.reply_markup.rows:
                        if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                            button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс кнопки во второй строке
                            await asyncio.sleep(random.uniform(2, 4))
                            await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение "❔ Вы хотите вернуться в деревню?"
            if "❔ Вы хотите вернуться в деревню?" in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(2, 4))
                        await self.client.send_message(message.sender_id, button_text)
                        await asyncio.sleep(random.uniform(2, 4))
                        await self.client.send_message(message.sender_id, "🍜 Квартал ресторанов")

            # Обработка других сообщений
            if "❔ Выберите еду" in message.raw_text:
                delay = random.uniform(2, 7)
                await asyncio.sleep(delay)
                await self.client.send_message(message.sender_id, "🍡 Данго (17 энергии, 40к рё)")

            if "❌ Вы уже сыты!" in message.raw_text:
                delay = random.uniform(2, 7) 
                await asyncio.sleep(delay) 
                await self.client.send_message(message.sender_id, "/raid")
        
            if "🍜 Перед вылазкой, вы можете взять еду с собой. Она восстанавливает сытость и позволяет пройти дальше." in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        # Получаем текст первой кнопки и отправляем его
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(2, 7))
                        await self.client.send_message(message.sender_id, button_text)
                      
            if "🏚 Выберите на каком уровне отдаленности вы хотите начать" in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 1:  # Проверяем, что во второй строке есть минимум 2 кнопки
                            # Получаем текст четвёртой кнопки и отправляем его
                            button_text = message.reply_markup.rows[1].buttons[1].text  # Индекс [1][1] для четвёртой кнопки
                            await asyncio.sleep(random.uniform(2, 7))
                            await self.client.send_message(message.sender_id, button_text)

            if "В одном из городов, где вы остановились, вы нашли онсэн. Абонемент стоит 2 млн рё." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:  # Проверяем наличие reply_markup и его строк
        # Проверяем, что в второго строки есть минимум 1 кнопка
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс [1][0] для второй строки
                        await asyncio.sleep(random.uniform(2, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "На окраине деревни вы заметили старый колодец, увитый глициниями. Местные жители рассказали вам, что если загадать желание и бросить монетку, то судьба обязательно сведет вас с тем, кого вы желаете встретить." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:  # Проверяем наличие reply_markup и его строк
        # Проверяем, что в второго строки есть минимум 1 кнопка
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Индекс [0][0] для второй строки
                        await asyncio.sleep(random.uniform(2, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Похоже, это была самая популярная подобная точка в стране." in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        # Получаем текст первой кнопки и отправляем его
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(2, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время короткого отдыха в тени дерева вы замечаете в траве какой-то блеск." in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(2, 4))
                        await self.client.send_message(message.sender_id, button_text)

            if "Вы находите обломок маски они, наполовину ушедший в мягкий речной ил. Белая глина потрескалась и потемнела от времени, но на внутренней стороне еще видны бурые пятна, похожие на засохшую кровь. " in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(2, 4))
                        await self.client.send_message(message.sender_id, button_text)

                 
