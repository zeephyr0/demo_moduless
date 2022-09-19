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
 strings = {'name': 'ByOwl'}

 def __init__(self): 
  self.name = self.strings['name']

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.owl = 5143234239
  self.owl_group = -1001163341690

 async def watcher(self, message): 
  if message.chat_id == -1001163341690 and message.sender_id == 5143234239:
   if "Рулетка" in message.raw_text:
    await sleep(2);
    await message.client.send_message(-1001163341690, 'повторить');
    await sleep(2);
    await message.client.send_message(-1001163341690, 'удвоить');
    await sleep(3);
    await message.client.send_message(-1001163341690, 'го');
   if "HDR ставка" in message.raw_text:
    await sleep(2);
    await message.client.send_message(-1001163341690, '500 1 2 4 5 7 8 10 11');
    await sleep(2);
    await message.client.send_message(-1001163341690, 'го');


