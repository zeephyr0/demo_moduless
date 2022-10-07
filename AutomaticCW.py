#by @ZEPHYR0 
#www

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
  'report': 'war',
  'stats': 'Статистика выполненных действий:\n\n',
  'stat_heal_s': '✅Успешных лечек: %heal_s%\n',
  'stat_heal_f': '❌Неудачных лечек: %heal_f%\n',
  'stat_heal_h': '💤Тишина: %heal_h%\n\n',
  'stat_heal_t': 'Всего лечек: %heal_t%'
 } 

 def __init__(self): 
  self.name = self.strings['name'] 
   
 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.city = 5505560402
  self.test_group = -1001578033582

 async def cwoncmd(self, message): 
  """Включить автоматизацию""" 
  status1 = self.db.get(self.name, "status", False);
  if status1: return await message.edit(self.strings['cwon_already']);
  self.db.set(self.name, "status", True);
  await message.edit(self.strings['cwon']);

 async def cwoffcmd(self, message): 
  """Выключить автоматизацию, лол"""
  self.db.set(self.name, 'status', False);
  await message.edit(self.strings['cwoff']);

 async def healcmd(self, message):
  """Отправить лечить лол"""
  status1 = self.db.get(self.name, "status", False);
  status2 = self.db.get(self.name, "status", True);
  if status1:
   await sleep(1);
   await self.client.send_message(self.city, self.strings['actions']);
   await sleep(1);
   await message.edit(self.strings['sending']);
   await sleep(1);
   await self.client.send_message(self.city, self.strings['heal']);
   await sleep(1);
   await message.edit(self.strings['sended']);

 async def statscmd(self, message):
  """Выводит статистику"""
  await message.delete()
  await sleep(1);
  await self.client.send_message(self.strings['stats']) 
  await sleep(1);
  await self.client.send_message(self.strings['stat_heal_s'].replace("%heal_s%", str(heal_s)), \nself.strings['stat_heal_f'].replace("%heal_f%", str(heal_f)));

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
   elif "🚑 Ура! Тебе удалось вылечить" in message.raw_text:
    await self.client.send_message(self.city, "/heal", schedule=timedelta(minutes=random.randint(6, 7)))
   elif "🚑 К сожалению, тебе не хватило умения, чтобы вылечить" in message.raw_text:
    await self.client.send_message(self.city, "/heal", schedule=timedelta(minutes=random.randint(6, 7)))
   elif "🚑 Cостоянию здоровья" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.city, self.strings['actions']);
    await sleep(1);
    await self.client.send_message(self.city, self.strings['heal']);
   if "@RestoredReports" in message.raw_text:
    await sleep(1);
    await message.forward_to(1660857021);
  if message.chat_id == -1001642762193 and message.sender_id == 1660857021:
   if "⚔️В атаку на" in message.raw_text:
    await sleep(180);
    await message.click();
    await sleep(1);
    await self.client.send_message(self.city, self.strings['actions']);
    await sleep(1);
    await self.client.send_message(self.city, self.strings['heal']);
    await sleep(3);
    await self.client.send_message(self.city, self.strings['report']);  
  if message.chat_id == -1001528018515 and message.sender_id == 5553546657:
   if "У меня для вас есть несколько 🎁 Подарков!" in message.raw_text:
    await message.click()
