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
        self.limit_active = False
        await self.client.send_message(message.sender_id, "Статус лимита отключен.")

    async def send_button_text(self, message, button_index):
        if (message.reply_markup and 
            len(message.reply_markup.rows) > button_index and 
            message.reply_markup.rows[button_index].buttons):
            button_text = message.reply_markup.rows[button_index].buttons[0].text
            await asyncio.sleep(random.uniform(2, 4))
            await self.client.send_message(message.sender_id, button_text)

    async def check_message(self, message, patterns):
        for pattern, button_index in patterns.items():
            if re.search(pattern, message.raw_text) and not self.limit_active:
                await self.send_button_text(message, button_index)
                return

    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id != 6745912139:
            return
        
        patterns = {
            r"🗺 Уровень отдаленности от деревни: 16": 1,
            r"❔ Выберите еду": 0,
            r"🍜 Перед вылазкой, вы можете взять еду с собой.": 0,
            r"🏚 Выберите на каком уровне отдаленности вы хотите начать": 1,
            r"В одном из городов, где вы остановились, вы нашли онсэн. Абонемент стоит 2 млн рё.": 1,
            r"На окраине деревни вы заметили старый колодец, увитый глициниями.": 0,
            r"Похоже, это была самая популярная подобная точка в стране.": 0,
            r"Во время короткого отдыха в тени дерева вы замечаете в траве какой-то блеск.": 0,
            r"Дождь безжалостно хлещет ваше лицо.": 0,
            r"Утром наступает.*": 0,
            r"Усилием воли вы разбираете.": 0,
            r"Вы находите обломок маски.": 0,
            r"По дороге вы замечаете лежащего на обочине человека.": 2
        }

        await self.check_message(message, patterns)

        hunger_match = re.search(r"🍜 Ваша сытость: (\d+)", message.raw_text)
        if hunger_match:
            hunger_value = int(hunger_match.group(1))
            button_index = 0 if hunger_value > 8 else 1
            await self.send_button_text(message, button_index)

        if "❔ Вы хотите вернуться в деревню?" in message.raw_text:
            await self.send_button_text(message, 0)
            await asyncio.sleep(random.uniform(2, 4))
            await self.client.send_message(message.sender_id, "🍜 Квартал ресторанов")

        if "❌ У ресторана закончились продукты, заходите позже!" in message.raw_text:
            self.limit_active = True

        if "❌ Вы уже сыты!" in message.raw_text:
            await asyncio.sleep(random.uniform(2, 7))
            await self.client.send_message(message.sender_id, "/raid")
