import re
import random 
from .. import loader, utils 
from asyncio import sleep 

@loader.tds 
class TwinCaseSenderMod(loader.Module): 
 """<b>Модуль для твинов</b>/n<i>Coded By EboDem</i>"""
 strings = {
  'name': 'TwinCaseSender',
  'cases': 'кейсы',
  'thx': 'thx',
  'nothing': '❌ На аккаунте нет кейсов',
  'kt': 'передать ZEPHYR_god кт 1',
  'rkt': 'передать ZEPHYR_god ркт 1',
  'k': 'передать ZEPHYR_god к 1',
  'rk': 'передать ZEPHYR_god рк 1',
  'mif': 'передать ZEPHYR_god миф 1',
  'kr': 'передать ZEPHYR_god кр 1',
  'zv': 'передать ZEPHYR_god зв 1'
  } 

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.mine = 5522271758
  self.chat = -1001870697043
 
 async def watcher(self, message):
  #тайм слип
  time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  if message.sender_id == 5522271758:
   #отправка кейсов на основу
   if "✉ Ты нашел(ла) конверт." in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.mine, self.strings['kt']);
   if "🧧 Ты нашел(ла) редкий конверт." in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.mine, self.strings['rkt']);
   if "📦 Ты нашел(ла) Кейс!" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.mine, self.strings['k']);
   if "🗳 Ты нашел(ла) Редкий Кейс!" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.mine, self.strings['rk']);
   if "🕋 Ты нашел(ла) Мифический Кейс!" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.mine, self.strings['mif']);
   if "💎 Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.mine, self.strings['kr']);
   if "📦 Кейсы игрока" and "✉ |  Конверт" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['kt']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "🧧 |  Редкий Конверт" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['rkt']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "📦 |  Кейс" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['k']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "🗳 |  Редкий Кейс" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['rk']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "🕋 |  Мифический Кейс" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['mif']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "💎 |  Кристальный Кейс" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['kr']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "🌌 |  Звёздный Кейс" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['zv']);
    await sleep(random.choice(time));
    await self.client.send_message(self.mine, self.strings['cases']);
   elif "📦 Кейсы игрока" and "Пусто." in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['nothing']);

  if message.chat_id == -1001870697043 and message.sender_id == 920762514:
   #чекер кейсов на твинах
   if "ткейсы" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['cases']);
   #отправка "thx" в чат твинов
   if "тнх" in message.raw_text:
    await sleep(random.choice(time));
    await self.client.send_message(self.chat, self.strings['thx']);
   #ручной сбор промо
   if "промо" in message.raw_text:
    await sleep(random.choice(time));
    regex = r"промо\s([A-Za-z0-9]+)"
    result = re.search(regex, message.raw_text)
    await self.client.send_message(self.chat, f'Промо {result.group(1)}');
  #авто-сбор промо
  if message.chat_id == -1001892345917 and "Этот промокод был сгенерирован ботом" in message.raw_text:
    await sleep(random.choice(time))
    regex = r"Промо\s([A-Za-z0-9]+)"
    result = re.search(regex, message.raw_text)
    await self.client.send_message(self.chat, f'Промо {result.group(1)}')

