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
 'double': 'удвоить'}

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.owl = 5143234239
  self.owl_group = -1001163341690


 async def watcher(self, message): 
  if message.chat_id == -1001163341690 and message.sender_id == 5143234239:
   if "Рулетка" in message.raw_text:
    await sleep(1);
    await message.client.send_message(self.owl_group, 'Построить Электростанцию 🏗⚡️');
