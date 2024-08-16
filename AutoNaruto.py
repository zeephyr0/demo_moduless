import random
import asyncio
from .. import loader
from hikkatl.types import Message
from hikkatl.types import KeyboardButton

@loader.tds
class NarutoAdventureMod(loader.Module):
    """Авто рейды нахуй"""

    strings = {"name": "NarutoAdventure"}

    def __init__(self):
        self.is_hungry = False  # Изначально статус голода False

    async def client_ready(self, client, db):
        self.client = client

    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id == 6745912139:
            if "🍜 Вы голодны, поэтому не можете идти дальше" in message.raw_text:
                self.is_hungry = True  # Устанавливаем статус голода
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[0].buttons) > 0:
                            # Получаем текст первой кнопки во второй строке и отправляем его
                            button_text = message.reply_markup.rows[1].buttons[0].text
                            await asyncio.sleep(random.uniform(2, 4))
                            await self.client.send_message(message.sender_id, button_text)
                            
            if "🗺 Уровень отдаленности от деревни:" in message.raw_text:
                if not self.is_hungry:  # Если не голоден, отправляем сообщение
                    if message.reply_markup:
                        if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                            # Получаем текст первой кнопки и отправляем его
                            button_text = message.reply_markup.rows[0].buttons[0].text
                            await asyncio.sleep(random.uniform(2, 7))
                            await self.client.send_message(message.sender_id, button_text)
                else:
                    pass
          
            if "❔ Выберите еду" in message.raw_text:
                delay = random.uniform(2, 7) 
                await asyncio.sleep(delay) 
                await self.client.send_message(message.sender_id, "🍡 Данго (17 энергии, 40к рё)")

            if "❌ Вы уже сыты!" in message.raw_text:
                self.is_hungry = False  # Сбрасываем статус голода
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
                        

                 
