#by @ZEPHYR0 
#www

import random 
from asyncio import sleep
from .. import loader, utils

@loader.tds 
class ByOwlMod(loader.Module): 
 """Кто прочитал тот лох""" 
 strings = {"name": "ByOwl"}

 colors = ['10000 к', '10000 ч']
 async def watcher(self, message): 
  if message.sender_id == 5505560402:
   if 
