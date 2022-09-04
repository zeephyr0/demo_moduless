#by @ZEPHYR0 
#www

import random 
from asyncio import sleep
from .. import loader, utils 
from telethon import functions 
from telethon.tl.types import Message

@loader.tds 
class ByOwlMod(loader.Module): 
 """Кто прочитал тот лох""" 
 strings = {
  'name': 'ByOwl',
  'red': '100 к',
  'black': '100 ч',
  'repeat': 'повторить', 
  'double': 'удвоить',
  'owlon': 'Авторулетка включена',
  'owlon_already': 'Авторулетка уже включена',
  'owloff': 'Авторулетка выключена'

 }

 def __init__(self): 
  self.name = self.strings['name']

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.owl = 5143234239
  self.owl_group = -1001163341690

 async def cwoncmd(self, message): 
  """Включить автоматизацию""" 
  status1 = self.db.get(self.name, "status", False);
  if status1: return await message.edit(self.strings['owlon_already']);
  self.db.set(self.name, "status", True);
  await message.edit(self.strings['owlon']);

 async def cwoffcmd(self, message): 
  """Выключить автоматизацию, лол"""
  self.db.set(self.name, 'status', False);
  await message.edit(self.strings['owloff']);


 async def watcher(self, message): 
  if message.chat_id == -1001163341690 and message.sender_id == 5143234239:
   if "HDR ставка 100 выиграл 200 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 200 выиграл 400 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 400 выиграл 800 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 1600 выиграл 3200 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 3200 выиграл 6400 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 6400 выиграл 12800 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 12800 выиграл 23600 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 23600 выиграл 45200 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 45200 выиграл 90400 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 90400 выиграл 180800 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 180800 выиграл 361600 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 361600 выиграл 723200 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 723200 выиграл 1446400 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 1446400 выиграл 2892800 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "HDR ставка 2892800 выиграл 5785600 на красное" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['red']);
   elif "Рулетка" and "⚫️" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['repeat']);
    await sleep(1);
    await message.client.send_message(self.owl_group, self.strings['double']);






#ты лох, ахахахах

#хуита
