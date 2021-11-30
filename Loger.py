from .. import loader, utils

class TestMod(loader.Module):
 strings = {"name": "LoaderMod"}

 async def client_ready(self, client, db):
  self.db = db
  self.db.set("LoaderMod", "status", True)

 async def chatcmd(self, message):
  chat = str(message.chat_id)
  await message.respond(f"Айди чата: <code>{chat}</code>")

 async def logcmd(self, message):
  if utils.get_args_raw(message):
   self.args = int(utils.get_args_raw(message))
  else:
   self.args = "me"
  self.chat = message.chat_id
  status = self.db.get("LoaderMod", "status")
  if status is not False:
   self.db.set("LoaderMod", "status", False)
   await message.edit("<b>Логгер для этого чата включен!</b>")
  else:
   self.db.set("LoaderMod", "status", True)
   await message.edit("<b>Логгер для этого чата выключен!</b>")
  await message.delete()
        
 async def watcher(self, message):
  status = self.db.get("LoaderMod", "status")
  if self.chat != message.chat_id:
   return
  sender = await message.get_sender()
  await message.client.send_message(self.args, f"<a href=tg://user?id={sender.id}>{sender.first_name}</a>: {message.text}")
