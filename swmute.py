import logging 
from .. import loader 
from telethon.tl.types import Message 
#ты пидор
 
@loader.tds 
class swmuteMod(loader.Module): 
 """Используй команду <code>.cwmute</code> для того чтобы вырубить собеседника""" 
 strings = {"name": "swmute"} 
 
 async def watcher(self, message): 
  if isinstance(message, Message): 
   if message.sender_id == (await message.client.get_me()).id: 
    await message.delete()
