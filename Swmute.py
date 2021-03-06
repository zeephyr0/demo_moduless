from .. import loader, utils  
 
@loader.tds 
class MuteMod(loader.Module): 
    """Мут.""" 
    strings = {'name': 'Mute'} 
 
    async def client_ready(self, client, db): 
        self.db = db 
 
    async def swmutecmd(self, message): 
        """Включить/выключить мут. Используй: .swmute <@ или реплай>.""" 
        if message.chat: 
            chat = await message.get_chat() 
            if not chat.admin_rights and not chat.creator: 
                return await message.edit("<b>Я не админ здесь.</b>") 
            else: 
                if chat.admin_rights.delete_messages == False: 
                    return await message.edit("<b>У меня нет нужных прав.</b>") 
 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        chatid = str(message.chat_id) 
        mutes = self.db.get("Mute", "mutes", {}) 
 
        if not args and not reply: 
            entityid = str(message.chat_id) 
        else: 
            if args:  
                entity = await message.client.get_entity(int(args) if args.isnumeric() else args) 
            else: 
                entity = await message.client.get_entity(reply.sender_id) 
            entityid = str(entity.id)  
 
        if chatid not in mutes: 
            mutes.setdefault(chatid, []) 
 
        if entityid not in mutes[chatid]: 
            mutes[chatid].append(entityid) 
            self.db.set("Mute", "mutes", mutes) 
            if entityid == chatid: 
                return await message.edit("<b>Чат, ты в муте.</b>") 
            return await message.edit("<b>Чел, ты в муте.</b>") 
        else: 
            mutes[chatid].remove(entityid) 
            if len(mutes[chatid]) == 0: 
                mutes.pop(chatid) 
            self.db.set("Mute", "mutes", mutes) 
            if entityid == chatid: 
                return await message.edit("<b>Чат, ты не в муте.</b>") 
            return await message.edit("<b>Чел, ты не в муте.</b>") 
 
    async def setmutecmd(self, message): 
        """Настройки мута. Используй: .setmute <clear/clearall (по желанию)>.""" 
        try: 
            args = utils.get_args_raw(message) 
            mutes = self.db.get("Mute", "mutes", {}) 
            chatid = str(message.chat_id) 
            ls = mutes[chatid] 
            ll = len(ls) 
            users = "" 
            if args == "clear": 
                mutes.pop(chatid) 
                self.db.set("Mute", "mutes", mutes) 
                return await message.edit("<b>Мут-список очищен.</b>") 
            if args == "clearall": 
                self.db.set("Mute", "mutes", {}) 
                return await message.edit("<b>Мут-список очищен во всех чатах.</b>") 
            for _ in ls: 
                if _ == chatid: 
                    users += "Этот чат" 
                try: 
                    user = await message.client.get_entity(int(_)) 
                    users += f"• <a href=\"tg://user?id={int(_)}\">{user.first_name}</a> <b>| [</b><code>{_}</code><b>]</b>\n" 
                except: 
                    ls.remove(_) 
                    self.db.set("Mute", "mutes", mutes) 
            await message.edit(f"<b>В этом чате в муте: {ll}</b>\n\n{users}") 
        except KeyError: return await message.edit("<b>Мут-список чист.</b>") 
 
    async def watcher(self, message): 
        try: 
            if message.sender_id == (await message.client.get_me()).id: return 
            mutes = self.db.get("Mute", "mutes", {}) 
            chatid = str(message.chat_id) 
            if chatid not in mutes: return 
            if chatid in mutes[chatid]: 
                await message.client.delete_messages(int(chatid), message.id) 
            if str(message.sender_id) in mutes[chatid]: 
                await message.client.delete_messages(int(chatid), message.id) 
        except: pass
