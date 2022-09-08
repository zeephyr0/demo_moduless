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
   if "Рулетка" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, 'повторить');
    await sleep(12);
    await message.client.send_message(self.owl_group, 'го');






#ты лох, ахахахах

#хуита
