#и хули ты тут забыл?
#создано в развлекательных и ознакомительных целях
#by ZEPHYR0

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoClWMod(loader.Module): 
    """Модуль для частичной автоматизации игры @clan_warsbot\n\nОсобенности модуля:\n• Автоматически ходить в приключение "Кража люков"\n• Возможность отправить в путешествие "Кража люков" командой adv\n• Возможность отменить путешествие командой stopadv\n\nОстальное будет добавляться постепенно по ходу освоения игры автором\n\n❗Модуль создан в ознакомительных целях и может работать нестабильно""" 
    strings = {"name": "AutoClW"}

    async def attack1(self, message):
      #атака на РЖД🚂
        await sleep(2);
        await message.client.send_message('@clan_warsbot', 'РЖД🚂');

    async def attack2(self, message):
      #атака на Аэропорт🛩
        await sleep(2);
        await message.client.send_message('@clan_warsbot', 'Аэропорт🛩');

    async def attack3(self, message):
      #атака на Таксопарк🚕
        await sleep(2);
        await message.client.send_message('@clan_warsbot', 'Таксопарк🚕');

    async def attack4(self, message):
      #атака на Заправочную станцию⛽️
        await sleep(2);
        await message.client.send_message('@clan_warsbot', 'Заправочная станция⛽️');

    async def attack5(self, message):
      #атака на Порт🚢
        await sleep(2);
        await message.client.send_message('@clan_warsbot', 'Порт🚢');

    async def adv(self, message):
      #начать приключение
        await sleep(2);
        await message.client.send_message('@clan_warsbot', '🗺Приключения');

    async def stopadv(self, message):
      #закончить приключение
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
