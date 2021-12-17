            if "👮 Ты отдохнул" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '👮 Патрулируем');
            elif "👮 На улицах" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '👮 Патрулируем');
            if "🚑 Cостоянию здоровья" in message.raw_text:
                await sleep(15);                
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "🚑 К сожалению, тебе не хватило умения, чтобы вылечить" in message.raw_text:
                await sleep(245);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "#лечка" in message.raw_text:
                await sleep(245);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(1);
                await message.client.send_message('@citywars2_bot', '🚑 Лечим');
            if "Пришлось отдать 💵" in message.raw_text:
                await sleep(10);
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '🏪 Грабим');
            elif "#ограбление" in message.raw_text:
                await sleep(10)
                await message.client.send_message('@citywars2_bot', '🕹 Действия');
                await sleep(2);
                await message.client.send_message('@citywars2_bot', '🏪 Грабим');
