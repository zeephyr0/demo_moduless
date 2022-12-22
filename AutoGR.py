#by @ZEPHYR0 
#www

import random 
from asyncio import sleep
from .. import loader, utils 
from telethon import functions 
from telethon.tl.types import Message 
 
@loader.tds 
class AutoGRMod(loader.Module): 
 """ты лох""" 
 strings = { 
  'name': 'AutoGR', 
  'gron': '<code>✅ Автоматизация ZephyrGram включена</code>', 
  'gron_already': '<i>Уже запущено</i>', 
  'groff': '<code> Автоматизация ZephyrGram выключена.</code>\n<b>Ты лох</b>',
  'groff_already': '<i>Модуль выключен</i>',
  'sending': 'Отправляем...',
  'sended': '✅ Отправлен!',
  'hog': '🔮 Хогвартс',
  'duel': 'Дуэль',
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
  self.gram = 5788046441
  self.test_group = -1001893681024                

 async def groncmd(self, message): 
  """Включить автоматизацию""" 
  status1 = self.db.get(self.name, "status", False);
  if status1: return await message.edit(self.strings['gron_already']);
  self.db.set(self.name, "status", True);
  await message.edit(self.strings['gron']);

 async def cwoffcmd(self, message): 
  """Выключить автоматизацию, лол"""
  self.db.set(self.name, 'status', False);
  await message.edit(self.strings['groff']);

 async def statscmd(self, message):
  """Выводит статистику"""
  await message.delete()
  await sleep(1);
  await self.client.send_message('Не сделал я пока нихуя тут') 

 async def watcher(self, message): 
  if message.sender_id == 5788046441:
   if "Вы убили босса - Гарри Поттер" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.gram, self.strings['hog']);
   if "Ви вбили боса - Гаррі Поттер" in message.raw_text:
    await sleep(1);
    await self.client.send_message(self.gram, self.strings['hog']);
   if "Хогвартс" in message.raw_text:
    await sleep(1); 
    await message.click();
   if "Выбери боса для битвы" in message.raw_text:
    await sleep(1); 
    await message.click();
   if "Босс - Гарри Поттер" in message.raw_text:
    await sleep(1); 
    await message.click();
   if "Вы начали бить - Гарри Поттер" in message.raw_text:
    await sleep(1); 
    await message.click();
  if message.chat_id == -1001528018515 and message.sender_id == 5788046441:
   if "Ваши характеристики" in message.raw_text:
    await message.click();
   if "Вы победили" in message.raw_text:
    await self.client.send_message(self.city, self.strings['duel']);  
if "Следующая дуэль через" in message.raw_text:
    await sleep (20);
    await self.client.send_message(self.city, self.strings['duel']);  
