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
 retur
 async def watcher(self, message): 
  if message.chat_id == -1001163341690 and message.sender_id == 5143234239:
   if "💰🏪 Найм рабочих/Постройки/Акции" in message.raw_text:
    await sleep(2);
    await message.client.send_message('@idle_city_bot', 'Построить Электростанцию 🏗⚡️');
