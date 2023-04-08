import random 
from .. import loader, utils 
from asyncio import sleep 

@loader.tds 
class TwinCaseSenderMod(loader.Module): 
 strings = {
  'name': 'TwinCaseSender',
  'kt': 'передать ZEPHYR_god кт 1',
  'rkt': 'передать ZEPHYR_god ркт 1',
  'k': 'передать ZEPHYR_god к 1',
  'rk': 'передать ZEPHYR_god рк 1',
  'mif': 'передать ZEPHYR_god миф 1',
  'kr': 'передать ZEPHYR_god кр 1'
  } 

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.mine = 5522271758
 
 async def watcher(self, message):

  if message.sender_id == 5522271758:
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

  if message.group_id == -1001870697043 and message.sender_id == 920762514:
   if "промо" in message.raw_text:
    await message.client.send_message(-1001870697043), message, reply_to=await message.get_reply_message() or message)
