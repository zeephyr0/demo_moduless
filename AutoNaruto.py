import random
import asyncio
import re
from .. import loader
from hikkatl.types import Message

@loader.tds
class NarutoAdventureMod(loader.Module):
    """Авто рейды нахуй"""

    strings = {"name": "NarutoAdventure"}

    def init(self):
        self.limit_active = False

    async def client_ready(self, client, db):
        self.client = client

    async def limitoffcmd(self, message: Message):
        """Команда для деактивации статуса лимита"""
        self.limit_active = False
        await self.client.send_message(message.sender_id, "Статус лимита отключен.")

    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id == 6745912139:

            # Обработка других сообщений
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
