import random 
from .. import loader, utils 
from datetime import timedelta 
from telethon import functions 
from telethon.tl.types import Message 
 
@loader.tds 
class AutoCWMod(loader.Module): 
 """"" 
 strings = { 
  'name': 'AutoCW', 
  'cwmon': '<code>✅ Автоматизация CityWars включена</code>', 
  'cwon_already': '<i>Уже запущено</i>', 
  'cwoff': '<code> Автоматизация CityWars выключена.</code>\n<b>Собрано %money% </b>', 
  'balance': '<i>Собрано:</i> <b>%money% </b>', 
 } 

 def __init__(self): 
  self.name = self.strings['name'] 
   
 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.city = 5505560402

 async def cwoncmd(self, message): 
  """""" 
  status = self.db.get(self.name, "status", False) 
  if status: return await message.edit(self.strings['cwon_already']) 
  self.db.set(self.name, "status", True) 
  await self.client.send_message(self.iris, "Фарма", schedule=timedelta(seconds=20)) 
  await message.edit(self.strings['cwon'])

 async def cwoffcmd(self, message): 
  """""" 
  self.db.set(self.name, 'status', False) 
  money = self.db.get(self.name, 'money', 0) 
  if money: self.db.set(self.name, 'money', 0) 
  await message.edit(self.strings['cwoff'].replace("%money%", str(money)))

 async def balancecmd(self, message): 
  """""" 
  money = self.db.get(self.name, "money", 0) 
  await message.edit(self.strings['balance'].replace("%money%", str(money))) 

 async def watcher(self, event): 
  if not isinstance(event, Message): return 
  chat = utils.get_chat_id(event) 
  if chat != self.city: return 
  status = self.db.get(self.name, 'status', False) 
  if not status: return 
  if "Ты заработал" in event.raw_text: 
   args = event.raw_text.split() 
   for x in args: 
    if x[0] == '+':  
     return self.db.set(self.name, 'money', self.db.get(self.name, 'money', 0) + int(x[1:]))
