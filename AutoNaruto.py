import random
import asyncio
from .. import loader
from hikkatl.types import Message
from hikkatl.types import KeyboardButton

@loader.tds
class NarutoAdventureMod(loader.Module):
    """Авто рейды нахуй"""

    strings = {"name": "NarutoAdventure"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id == 6745912139: 
            if "🗺 Уровень отдаленности от деревни:" in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        # Получаем текст первой кнопки и отправляем его
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(2, 7))
                        await self.client.send_message(message.sender_id, button_text)
          
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
                       if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) >= 4:  # Проверяем, что есть минимум 4 кнопки
                # Получаем текст четвёртой кнопки и отправляем его
                           button_text = message.reply_markup.rows[0].buttons[3].text  # Индекс 3 для четвёртой кнопки
                           await asyncio.sleep(random.uniform(2, 7))
                           await self.client.send_message(message.sender_id, button_text)

            if "В одном из городов, где вы остановились, вы нашли онсэн. Абонемент стоит 2 млн рё." in message.raw_text:
               if message.reply_markup:
                   if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                       if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) >= 2:  # Проверяем, что есть минимум 4 кнопки
                # Получаем текст четвёртой кнопки и отправляем его
                           button_text = message.reply_markup.rows[0].buttons[1].text  # Индекс 3 для четвёртой кнопки
                           await asyncio.sleep(random.uniform(2, 7))
                           await self.client.send_message(message.sender_id, button_text)



                 
