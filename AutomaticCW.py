#by @ZEPHYR0 (просто спиздил модуль)
#спиздил во благо

import random 
from asyncio import sleep
from .. import loader, utils 
from telethon import functions 
from telethon.tl.types import Message 
 
@loader.tds 
class AutoCWMod(loader.Module): 
 """ты лох""" 
 strings = { 
  'name': 'AutoCW', 
  'cwon': '<code>✅ Автоматизация CityWars включена</code>', 
  'cwon_already': '<i>Уже запущено</i>', 
  'cwoff': '<code> Автоматизация CityWars выключена.</code>\n<b>Ты лох</b>',
  'cwoff_already': '<i>Модуль выключен</i>',
  'sending': 'Отправляем...',
  'sended': '✅ Отправлен!',
  'actions': '🕹 Действия',
  'heal': '🚑 Лечим',
  'patrol': '👮 Патрулируем',
  'rob': '🏪 Грабим',
  'report': 'war'
 } 

 def __init__(self): 
  self.name = self.strings['name'] 
   
 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.city = 5505560402

 async def cwoncmd(self, message): 
  """Включить автоматизацию""" 
  status = self.db.get(self.name, "status", False);
  if status: return await message.edit(self.strings['cwon_already']);
  self.db.set(self.name, "status", True);
  await message.edit(self.strings['cwon']);

 async def cwoffcmd(self, message): 
  """Выключить автоматизацию, лол""" 
  self.db.set(self.name, 'status', False);
  await message.edit(self.strings['cwoff']);

 async def healcmd(self, message):
    """Отправить лечить лол"""
   await sleep(1);
   await self.client.send_message(self.city, self.strings['actions']);
   await sleep(1);
   await message.edit(self.strings['sending']);
   await sleep(1);
   await self.client.send_message(self.city, self.strings['heal']);
   await sleep(1);
   await message.edit(self.strings['sended']);

 async def watcher(self, message): 
  if message.sender_id == 5505560402:
   if "👮 Ты отдохнул" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.city, self.strings['actions']);
    await sleep(1);
    await self.client.send_message(self.city, self.strings['patrol']);
   elif "👮 На улицах" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.city, self.strings['actions']);
    await sleep(1);
    await self.client.send_message(self.city, self.strings['patrol']);
   if "🚑 Ты отдохнул" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.city, self.strings['actions']);
    await sleep(1);
    await self.client.send_message(self.city, self.strings['heal']);
   elif "🚑 Cостоянию здоровья" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.city, self.strings['actions']);
    await sleep(1);
    await self.client.send_message(self.city, self.strings['heal']);
   if "@RestoredReports" in message.raw_text:
    await sleep(1);
    await message.forward_to(1710320396);
  if message.chat_id == -1001710320396 and message.sender_id == 1660857021:
   if "⚔️В атаку на" in message.raw_text:
    await message.click();
  if message.chat_id == -1001528018515 and message.sender_id == 5553546657:
   if "У меня для вас есть несколько 🎁 Подарков!" in message.raw_text:
    await message.click()
