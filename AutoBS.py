from .. import loader
from asyncio import sleep

@loader.tds 
class AutoBSMod(loader.Module): 
    strings = {"name": "AutoBS"}

    async def watcher(self, message):
        if message.sender_id == 2063668248:
            if "🏦🔥Банк ограблен!" in message.raw_text:
                await sleep(2);
                await message.client.send_message('@clan_warsbot', '🏦 Ограбление банка (1 час)');
