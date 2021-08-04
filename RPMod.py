from .. import loader, utils

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""
    strings = {'name': 'RPMod'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status is not False:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP Режим <b>выключен</b></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP Режим <b>включен</b></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        await message.edit()
    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a>  <a href=tg://user?id={user.id}>{user.first_name}</a>")
