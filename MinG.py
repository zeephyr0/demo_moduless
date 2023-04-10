import random 
from .. import loader, utils 
from asyncio import sleep 

@loader.tds 
class MinGMod(loader.Module): 
 strings = {
  'name': 'MinG',
  'st1': 'Кубик 1 10Ii',
  'st2': 'Кубик 1 20Ii',
  'st3': 'Кубик 1 40Ii',
  'st4': 'Кубик 1 80Ii',
  'st5': 'Кубик 1 160Ii',
  'st6': 'Кубик 1 320Ii',
  'st7': 'Кубик 1 640Ii',
  'st8': 'Кубик 1 1280Ii',
  'st9': 'Кубик 1 2560Ii',
  'st10': 'Кубик 1 5120Ii',
  'st11': 'Кубик 1 10240Ii',
  'st12': 'Кубик 1 20480Ii',
  'st13': 'Кубик 1 40960Ii',
  'st14': 'Кубик 1 81920Ii',
  'st15': 'Кубик 1 163840Ii',
  'st16': 'Кубик 1 327680Ii',
  'st17': 'Кубик 1 655360Ii',
  'st18': 'Кубик 1 1310720Ii',
  'st19': 'Кубик 1 2621440Ii',
  'st20': 'Кубик 1 5621440Ii',
  'st21': 'Кубик 1 10621440Ii',
  'st22': 'Кубик 1 20621440Ii'
  } 

 async def client_ready(self, client, db): 
  self.client = client 
  self.db = db 
  self.myid = (await client.get_me()).id 
  self.mine = 5522271758
 
 async def watcher(self, message):
  if message.sender_id == 5522271758:
   if "ZEPHYR_god  проиграл(а) -10Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st2']);
   if "ZEPHYR_god  проиграл(а) -20Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st3']);
   if "ZEPHYR_god  проиграл(а) -40Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st4']);
   if "ZEPHYR_god  проиграл(а) -80Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st5']);
   if "ZEPHYR_god  проиграл(а) -160Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st6']);
   if "ZEPHYR_god  проиграл(а) -320Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st7']);
   if "ZEPHYR_god  проиграл(а) -640Ii$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st8']);
   if "ZEPHYR_god  проиграл(а) -1.28Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st9']);
   if "ZEPHYR_god  проиграл(а) -2.56Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st10']);
   if "ZEPHYR_god  проиграл(а) -5.12Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st11']);
   if "ZEPHYR_god  проиграл(а) -10.24Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st12']);
   if "ZEPHYR_god  проиграл(а) -20.48Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st13']);
   if "ZEPHYR_god  проиграл(а) -40.96Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st14']);
   if "ZEPHYR_god  проиграл(а) -81.92Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st15']);
   if "ZEPHYR_god  проиграл(а) -163.84Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st16']);
   if "ZEPHYR_god  проиграл(а) -327.68Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st17']);
   if "ZEPHYR_god  проиграл(а) -655.36Jj$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st18']);
   if "ZEPHYR_god  проиграл(а) -1.31Kk$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st19']);
   if "ZEPHYR_god  проиграл(а) -2.62Kk$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st20']);
   if "ZEPHYR_god  проиграл(а) -5.62Kk$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st21']);
   if "ZEPHYR_god  проиграл(а) -10.62Kk$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st22']);
   if "ZEPHYR_god  проиграл(а) -20.62Kk$" in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st1']);
   if "❗ZEPHYR_god, в кубик можно играть каждые 5 секунд!" in message.raw_text:
    await sleep(5);
    await self.client.send_message(self.mine, self.strings['st1']);
   if "😄 Выпало 1! Выигрыш ×4!." in message.raw_text:
    await sleep(2);
    await self.client.send_message(self.mine, self.strings['st1']);
