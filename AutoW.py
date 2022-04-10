from .. import loader
from asyncio import sleep

@loader.tds 
class VikingsMod(loader.Module): 
    strings = {"name": "Vikings"}

    async def farmvcmd(self, message):
        await message.edit('<b>Отпрвляем письку в бой..</b>');
        await sleep(1);
        await message.edit('<b>Писька отправлена фармить!</b>');
        await sleep(1);
        await message.client.send_message('@vikinggame_bot', '💠Режимы');

    async def watcher(self, message):
        if message.sender_id == 960603914:
            if "Выбери, куда отправишься" in message.raw_text:
                await sleep(1);
                await message.click(1);
            if "Ты вернулся из леса:" in message.raw_text:
               await sleep(1);
               await message.client.send_message('@vikinggame_bot', '💠Режимы');
            if "Ты восстановил силы и готов к новым приключениям" in message.raw_text:
               await sleep(1);
               await message.client.send_message('@vikinggame_bot', '💠Режимы');
