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

 async def roulettecmd(message):
 nums = ['20 1', '20 2', '20 3', '20 4', '20 5', '20 6', '20 7', '20 8', '20 9', '20 10', '20 11', '20 12',]
 await message.delete();
 for i in range(10000):
  await message.respond("руелетка")
  await sleep(5);
  await message.respond(random.randint(nums))
  await sleep(2);
  await message.respond(random.randint(nums))
  await sleep(2);
message.respond(random.randint(nums))
  await sleep(2);
message.respond(random.randint(nums))
  await sleep(2);
message.respond(random.randint(nums))
  await sleep(2);
  await message.respond('го')


