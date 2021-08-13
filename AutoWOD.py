
#и хули ты тут забыл?

from .. import loader
from asyncio import sleep

@loader.tds 
class AutoWODMod(loader.Module): 
    """Нахуя тебе это?""" 
    strings = {"name": "AutoWOD"}

    async def watcher(self, message):
        if message.sender_id == 913530224:
            if "В этой битве тебе не было равных, это безупречная победа!" in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WorldDogs_bot', '⚔️ Авто-Арена');
            if "Ты проиграл эту битву, но достойно сражался!" in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WorldDogs_bot', '⚔️ Авто-Арена');
            if "Ты у городских ворот. Приключения ждут!" in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WorldDogs_bot', '⚔️ PvP Арены');
            if "⚔️ PVP Арены - это отличная возможность для каждого пса продемонстрировать свою силу, доблесть и отвагу. Сражайтесь с другими собаками в режимах 1х1, 3х3, принимайте участие в регулярных PvP турнирах и просто расслабляйтесь в авто-боях!" in message.raw_text:
                await sleep(3);
                await message.client.send_message('@WorldDogs_bot', '⚔️ Авто-Арена');
            if "Плата за участие:" in message.raw_text:
                await sleep(1);
                await message.click(1);
            if "Начать поиск соперника?" in message.raw_text:
                await sleep(3);
                await message.click();

