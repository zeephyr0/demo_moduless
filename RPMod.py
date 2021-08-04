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
        await message.edit("<b>Список доступных РП команд:</b>\n\n• <code>Поцеловать</code>\n• <code>Поцеловать в щёчку</code>\n• <code>Поцеловать в губы</code>\n• <code>Поцеловать в носик</code>\n• <code>Поцеловать в лобик</code>\n• <code>Поцеловать в лоб\n</code\n• <code>Поцеловать в шею</code>\n• <code>Чмокнуть</code>\n• <code>Чмок</code>\n• <code>Притянуть</code>\n• <code>Обнять</code>\n• <code>Обнять за талию</code>\n• <code>Взять за руку</code>\n• <code>Взять за талию</code>\n• <code>Взять за шею</code>\n• <code>Взять за горло</code>\n• <code>Взять за попу</code>\n• <code>Схватить</code>\n• <code>Поймать</code>\n• <code>Прижать</code>\n• <code>Погладить</code>\n• <code>Погладить по голове</code>\n• <code>Укусить</code>\n• <code>Укусить за руку</code>\n• <code>Укусить в шею</code>\n• <code>Укусить за губу</code>\n• <code>Оставить засос на шее</code>\n• <code>Оставить засос на ключице</code>\n• <code>Шлепнуть</code>\n• <code>Залапать</code>\n• <code>Отдаться</code>\n• <code>Выебать</code>\n• <code>Чпокнуть</code>\n• <code>Трахнуть</code>\n• <code>Изнасиловать</code>\n• <code>Связать</code>\n• <code>Связать руки</code>\n• <code>Связь ноги</code>\n• <code>Ударить</code>\n• <code>Уебать</code>\n• <code>Убить</code>\n• <code>Утопить</code>\n• <code>Сбить на камазе</code>\n• <code>Сбить на автобусе</code>\n• <code>Отсосать</code>\n• <code>Отлизать</code>\n• <code>Лизнуть</code>\n• <code>Придушить</code>\n• <code>Задушить</code>\n• <code>Украсть</code>\n• <code>Отпороть</code>\n• <code>Наебать</code>\n• <code>Обмануть</code>\n• <code>Накурить</code>\n• <code>Набухать</code>\n• <code>Расстрелять</code>\n• <code>Понюхат</code>ь\n• <code>Накормить</code>\n• <code>Напоить</code>\n• <code>Кастрировать</code>\n• <code>Стерилизовать</code>\n• <code>Пнуть</code>\n• <code>Пожелать спокойной ночи</code>\n• <code>Пожелать доброго утра</code>\n• <code>Послать нахуй</code>\n• <code>Ущипнуть</code>\n• <code>Дать пощечину</code>\n• <code>Дать подзатыльник</code>\n• <code>Полюбить</code>\n• <code>Признаться в любви</code>")

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                    if message.text.lower() == "чмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> чмокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
        except: pass
