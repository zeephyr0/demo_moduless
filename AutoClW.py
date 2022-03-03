#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoClWMod(loader.Module): 
    """Модуль для частичной автоматизации игры @clan_warsbot\n\nОсобенности модуля:\n• Ходить в приключения\nОстальное будет добавляться постепенно по ходу освоения игры автором\n\n❗Модуль создан в ознакомительных целях и может работать нестабильно""" 
    strings = {"name": "AutoClW"}

    async def adv(self, message):
        await sleep(2);
        await message.client.send_message('@clan_warsbot', '🗺Приключения');

    async def stopadv(self, message):
        await sleep(2);
        await message.client.send_message('@clan_warsbot', 'Отменить приключение❌');

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "🎊Приключение «Кража люков» успешно завершено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
            if "🚓Приключение провалено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
            if "Отправиться в приключение💎" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');
