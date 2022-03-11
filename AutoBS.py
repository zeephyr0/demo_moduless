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
            if "Территория: 1," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 2," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 3," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 4," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 5," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 6," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 6," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 7," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 8," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 9," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 10," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 11," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 12," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 13," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 14," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Территория: 15," in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(4);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            elif "Цель:" in message.raw_text:
                await sleep(2);
                await message.click(1);
            elif "🗺 Разведка" in message.raw_text:
                await sleep(2);
                await message.click();
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '🗺 Разведка');
            if "Всего раундов:" in message.raw_text:
                await sleep(2);
                await message.forward_to(666473433);
            if "Копать еще:" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@BSv2Bot', '/dig');
