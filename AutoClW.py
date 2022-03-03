#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoClWMod(loader.Module): 
    """<b>Модуль для частичной автоматизации игры</b> @clan_warsbot\n\n<b>Особенности модуля:</b>\n<code>• Ходить в приключения</code>\nОстальное будет добавляться постепенно по ходу освоения игры автором\n\n<b>❗Модуль создан в ознакомительных целях и может работать нестабильно</b>""" 
    strings = {"name": "AutoClW"}

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "🎊Приключение «Кража люков» успешно завершено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');
            if "🚓Приключение провалено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🗺Приключения');
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '👻 Кража люков (15 минут)');

