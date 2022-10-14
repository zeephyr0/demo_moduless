#и хули ты тут забыл?

from .. import loader
from asyncio import sleep
import random

@loader.tds 
class AutoSEMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoSE"}

    async def watcher(self, message):
        war_buttons = [0, 1, 2]
        time1 = [4, 120]
        buttons = [0, 1, 2]
        time2 = [2, 4, 6]
        if message.sender_id == 605298957:
            if "📡Ты вернулся с поиска обломков." and "К сожалению ты ничего не нашел, может повезет в следующий раз." in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '⌨️');
            elif "📡Ты вернулся с поиска обломков." and "Ты нашел 🛢контейнер, нужно будет открыть и посмотреть что там!" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '📦');
            if "📦 Грузовой карго отсек" and "🛢Контейнеры:" in message.raw_text:
                await sleep(1);
                await message.click(3);
                await message.client.send_message('@SpaceExplorerBot', '📦');
            if "⚠️Бортовой компьютер недоступен." in message.raw_text:
                await sleep(300);
                await message.client.send_message('@SpaceExplorerBot', '📦');
            if "👁‍🗨Ты в космосе возле ☠️Пиратская станция" and "🔋13" in message.raw_text:
                await sleep(1);
                await message.click(1);
            elif "👁‍🗨Ты в космосе возле ☠️Пиратская станция" in message.raw_text:
                await sleep(1);
                await message.click(4);
            if "📡Ты можешь отправиться на поиски обломков, в которых иногда можно найти ценные ресурсы." in message.raw_text:
                await sleep(1);
                await message.click();
            if "Недостаточно 🔋топлива" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '⌨️');
            if "👁‍🗨Ты на корабле. ☠️Пиратская станция" and "🔋357" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '/buy_max_fuel');
            elif "👁‍🗨Ты на корабле. ☠️Пиратская станция" and "🔋314" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '/buy_max_fuel');
            elif "👁‍🗨Ты на корабле. ☠️Пиратская станция" and "🔋271" in message.raw_text:
                await sleep(1);
                await message.client.send_message('@SpaceExplorerBot', '/buy_max_fuel');
            elif "👁‍🗨Ты на корабле. ☠️Пиратская станция" and "🔋400" in message.raw_text:
                await sleep(1);
                await message.click(3);
