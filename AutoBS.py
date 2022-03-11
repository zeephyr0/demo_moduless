from .. import loader
from asyncio import sleep

@loader.tds 
class AutoBSMod(loader.Module): 
    strings = {"name": "AutoBS"}

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "🎊Приключение «Кража люков» успешно завершено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⬆️ Наверх');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⚔️ Гарнизон');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "🚓Приключение провалено!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⬆️ Наверх');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '⚔️ Гарнизон');
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
        if message.sender_id == 764095451:
            if "🗺 Разведка" in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(2);
                await message.click(1);
            if "🏦🔥Банк ограблен!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🏦 Ограбление банка (1 час)');
