#by @ZEPHYR0 
#www

import random 
from asyncio import sleep
from .. import loader, utils 
from telethon import functions 
from telethon.tl.types import Message

@loader.tds 
class RdnoMod(loader.Module): 
 """Кто прочитал тот лох""" 
 strings = {'name': 'Rdno'}

 def __init__(self): 
  self.name = self.strings['name']

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.owl = 1014481227
  self.owl_group = -1001163341690

 async def watcher(self, message): 
  if message.sender_id == 1014481227:
   if "twist выиграл" in message.raw_text:
    await sleep(2);
    await message.client.send_message(1014481227, 'рулетка');
    await sleep(2);
    await message.client.send_message(1014481227, '5 к');
    await sleep(2);
    await message.client.send_message(1014481227, 'го');
   elif "Рулетка" in message.raw_text:
    await sleep(2);
    await message.client.send_message(1014481227, 'рулетка');
    await sleep(2);
    await message.client.send_message(1014481227, 'повторить');
    await sleep(2);
    await message.client.send_message(1014481227, 'удвоить');
    await sleep(2);
    await message.client.send_message(1014481227, 'го');

