import random
import random
import asyncio
import re  # Импортируем регулярные выражения
from .. import loader
from hikkatl.types import Message

@loader.tds
class NarutoAdventureFoodMod(loader.Module):
    """Авто рейды нахуй"""

    strings = {"name": "NarutoAdventureFood"}

    def init(self):
        self.status_one_active = True  # Изначально первый статус активен
        self.status_two_active = False  # Изначально второй статус не активен
        self.status_three_active = False  # Изначально третий статус не активен
        self.limit_active = False  # Изначально статус лимита не активен

    async def client_ready(self, client, db):
        self.client = client

    async def statusonecmd(self, message: Message):
        """Активирует первый статус и деактивирует второй и третий"""
        self.status_one_active = True
        self.status_two_active = False
        self.status_three_active = False
        self.limit_active = False  # Деактивируем статус лимита
        await self.client.send_message(message.sender_id, "Первый статус активирован. Второй и третий статус отключены.")
        await asyncio.sleep(random.uniform(1, 5))  # Случайная задержка от 1 до 5 секунд
        await self.client.send_message("@KirinGameBot", "/raid")  # Отправляем команду

    async def statustwocmd(self, message: Message):
        """Активирует второй статус и деактивирует первый и третий"""
        self.status_one_active = False
        self.status_two_active = True
        self.status_three_active = False
        self.limit_active = False  # Деактивируем статус лимита
        await self.client.send_message(message.sender_id, "Второй статус активирован. Первый и третий статус отключены.")
        await asyncio.sleep(random.uniform(1, 5))  # Случайная задержка от 1 до 5 секунд
        await self.client.send_message("@KirinGameBot", "/raid")  # Отправляем команду

    async def statusthreecmd(self, message: Message):
        """Активирует третий статус и деактивирует первый и второй"""
        self.status_one_active = False
        self.status_two_active = False
        self.status_three_active = True
        self.limit_active = False  # Деактивируем статус лимита
        await self.client.send_message(message.sender_id, "Третий статус активирован. Первый и второй статус отключены.")
        await asyncio.sleep(random.uniform(1, 5))  # Случайная задержка от 1 до 5 секунд
        await self.client.send_message("@KirinGameBot", "/raid")  # Отправляем команду
        
    @loader.watcher()
    async def watcher(self, message):
        if message.sender_id == 6745912139:
            # Проверяем уровень отдаленности
            if "🗺 Уровень отдаленности от деревни:" in message.raw_text:
                level_match = re.search(r"🗺 Уровень отдаленности от деревни: (\d+)", message.raw_text)
                if level_match:
                    distance_level = int(level_match.group(1))

                    # Если уровень отдаленности равен 16 или 466
                    if distance_level in {16, 833}:
                        if message.reply_markup and message.reply_markup.rows:
                            if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                                button_text = message.reply_markup.rows[1].buttons[0].text
                                await asyncio.sleep(random.uniform(4, 9))
                                await self.client.send_message(message.sender_id, button_text)
                        return  # Не продолжать проверку, если выполнено условие для отдаленности

            if "🏚 Выберите на каком уровне отдаленности вы хотите начать" in message.raw_text:
                if self.status_one_active and message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Индекс [0][0] для первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 3))
                        await self.client.send_message(message.sender_id, button_text)

                elif self.status_two_active and message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                        button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс [1][0] для первой кнопки второй строки
                        await asyncio.sleep(random.uniform(1, 3))
                        await self.client.send_message(message.sender_id, button_text)

                elif self.status_three_active:
                    await asyncio.sleep(random.uniform(1, 3))  # Добавляем задержку
                    await self.client.send_message(message.sender_id, "733")  # Отправляем "499"
                
            hunger_match = re.search(r"🍜 Ваша сытость: (\d+)", message.raw_text)
            if hunger_match:
                # Извлекаем значение сытости
                hunger_value = int(hunger_match.group(1))

                # Если сытость больше 8
                if hunger_value > 8:
                    # Отправляем текст с первой кнопки первой строки
                    if message.reply_markup and message.reply_markup.rows:
                        if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                            button_text = message.reply_markup.rows[0].buttons[0].text
                            await asyncio.sleep(random.uniform(1, 7))
                            await self.client.send_message(message.sender_id, button_text)
                else:
                    # Если сытость 8 или меньше, проверяем на наличие текста "Восстановить сытость"
                    if "Восстановить сытость" in message.raw_text:
                        await asyncio.sleep(random.uniform(1, 3))
                        await self.client.send_message(message.sender_id, "/food1")
                    else:
                        # Если сытость 8 или меньше и нет дополнительного текста, отправляем текст с первой кнопки второй строки
                        if message.reply_markup and message.reply_markup.rows:
                            if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                                button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс кнопки во второй строке
                                await asyncio.sleep(random.uniform(1, 7))
                                await self.client.send_message(message.sender_id, button_text)

            
            # Проверяем наличие текста с запросом на количество еды
            quantity_match = re.search(r"Сколько еды этого типа вы хотите взять\? \(у вас есть (\d+)\)", message.raw_text)
            
            if quantity_match:
                # Извлекаем количество
                available_quantity = int(quantity_match.group(1))

                # Отправляем 10 если доступное количество больше 10, иначе отправляем доступное количество
                quantity_to_send = min(available_quantity, 10)

                await asyncio.sleep(random.uniform(1, 7))
                await self.client.send_message(message.sender_id, str(quantity_to_send))
                
            # Проверка на сообщение "❔ Вы хотите вернуться в деревню?"
            if "❔ Вы хотите вернуться в деревню?" in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(4, 9))
                        await self.client.send_message(message.sender_id, button_text)
                        await asyncio.sleep(random.uniform(5, 30))
                        await self.client.send_message(message.sender_id, "/raid")

            if "❌ У ресторана закончились продукты, заходите позже!" in message.raw_text:
                self.limit_active = True
                
            # Проверка состояния лимита перед обработкой выбора еды
            if "❔ Выберите еду" in message.raw_text:
                if self.limit_active:
                    return  # Не выполняем дальнейшие действия, если лимит активен

                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 1:
                        button_text = message.reply_markup.rows[0].buttons[1].text  # Текст со второй кнопки первой строки
                        delay = random.uniform(2, 7)
                        await asyncio.sleep(delay)
                        await self.client.send_message(message.sender_id, button_text)
                        
            if "❌ Вы уже сыты!" in message.raw_text:
                delay = random.uniform(2, 7) 
                await asyncio.sleep(delay) 
                await self.client.send_message(message.sender_id, "/raid")
        
            food_match = re.search(r"🍥 Вы можете взять с собой до 10 ед. еды, вы взяли (\d+).", message.raw_text)
            
            if food_match:
                # Извлекаем количество еды
                food_value = int(food_match.group(1))

                # Если количество еды равно нулю, отправляем текст с первой кнопки второй строки
                if food_value == 0:
                    if message.reply_markup and message.reply_markup.rows:
                        if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                            button_text = message.reply_markup.rows[1].buttons[0].text
                            await asyncio.sleep(random.uniform(1, 4))
                            await self.client.send_message(message.sender_id, button_text)
                # Если количество еды больше нуля, отправляем текст с первой кнопки первой строки
                else:
                    if message.reply_markup and message.reply_markup.rows:
                        if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                            button_text = message.reply_markup.rows[0].buttons[0].text
                            await asyncio.sleep(random.uniform(1, 7))
                            await self.client.send_message(message.sender_id, button_text)

            
            if "В одном из городов, где вы остановились, вы нашли онсэн. Абонемент стоит 2 млн рё." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:  # Проверяем наличие reply_markup и его строк
        # Проверяем, что в второго строки есть минимум 1 кнопка
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[1].buttons[0].text  # Индекс [1][0] для второй строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "На окраине деревни вы заметили старый колодец, увитый глициниями. Местные жители рассказали вам, что если загадать желание и бросить монетку, то судьба обязательно сведет вас с тем, кого вы желаете встретить." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:  # Проверяем наличие reply_markup и его строк
        # Проверяем, что в второго строки есть минимум 1 кнопка
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Индекс [0][0] для второй строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Похоже, это была самая популярная подобная точка в стране." in message.raw_text:
                if message.reply_markup:
                    if message.reply_markup.rows:  # Проверяем, есть ли строки кнопок
                        # Получаем текст первой кнопки и отправляем его
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время короткого отдыха в тени дерева вы замечаете в траве какой-то блеск." in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Вы находите обломок маски они, наполовину ушедший в мягкий речной ил. Белая глина потрескалась и потемнела от времени, но на внутренней стороне еще видны бурые пятна, похожие на засохшую кровь. " in message.raw_text:
                # Проверяем наличие кнопок в первой строке
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "По дороге вы замечаете лежащего на обочине человека. Приблизившись, вы видите, что он ранен и без сознания." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    # Проверяем наличие кнопок на третьей строке
                    if len(message.reply_markup.rows) > 2 and len(message.reply_markup.rows[2].buttons) > 0:
                        button_text = message.reply_markup.rows[2].buttons[0].text  # Текст первой кнопки третьей строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Ночной ветер доносит до вас странный аромат - сладковатый и тяжелый, он напоминает благовония, которыми жрецы окуривают мертвецов перед погребением." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение о дожде
            if "Дождь безжалостно хлещет ваше лицо, тело пробивает озноб. Вы дрожите, но продолжаете идти, стараясь не обращать внимания на горячку с её кислотными видениями." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение о утре
            if "Утром наступает... утро, и это довольно необычно, если смириться со своей участью. Вы в богатой комнате, пахнущей свежими татами, рисовой водой и зеленым чаем." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверка на сообщение о усилии воли
            if "Усилием воли вы разбираете очертания и комнаты, и девушки." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text  # Текст первой кнопки первой строки
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Вы проходите мимо прекрасного сада сакуры в полном цвету." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if message.reply_markup.rows and message.reply_markup.rows[0].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время перехода через реку вы замечаете странное существо, наполовину скрытое в воде." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if message.reply_markup.rows and message.reply_markup.rows[0].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Проходя через небольшую деревню, вы натыкаетесь на уличного игрока в кости." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[1].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время вашего путешествия вы натыкаетесь на скрытый горячий источник." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if message.reply_markup.rows and message.reply_markup.rows[0].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)


            if "На лесной тропинке вы встречаете плачущего ребенка." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[1].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Вы приходите в небольшую деревню, где сегодня проходит рыночный день." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if message.reply_markup.rows and message.reply_markup.rows[0].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время привала вы замечаете поляну с разнообразными травами." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if message.reply_markup.rows and message.reply_markup.rows[0].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "Во время путешествия вы натыкаетесь на передвижную раменную." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if message.reply_markup.rows and message.reply_markup.rows[0].buttons:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            if "На дороге вы встречаете странствующего музыканта." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 1 and message.reply_markup.rows[1].buttons:
                        button_text = message.reply_markup.rows[1].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверяем наличие текста о фестивале Танабата
            if "Вы прибываете в небольшую деревню как раз в день фестиваля Танабата." in message.raw_text:
                # Отправляем текст с первой кнопки первой строки
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)

            # Проверяем текст "На привале в лесу вы встречаете загадочную незнакомку в маске, которая называет себя Юи."
            if "На привале в лесу вы встречаете загадочную незнакомку в маске, которая называет себя Юи." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)
                return  # Не продолжать, если выполнено условие для Юи

            # Проверяем сообщение "Вы решаете принять предложение Юки и сыграть в кости, положившись на удачу."
            if "Вы решаете принять предложение Юки и сыграть в кости, положившись на удачу." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 0 and len(message.reply_markup.rows[0].buttons) > 0:
                        button_text = message.reply_markup.rows[0].buttons[0].text
                        await asyncio.sleep(random.uniform(1, 7))
                        await self.client.send_message(message.sender_id, button_text)
                return  # Не продолжать, если выполнено условие для Юки

            # Проверяем сообщение "👣 Вы нашли переход на следующую локацию."
            if "👣 Вы нашли переход на следующую локацию." in message.raw_text:
                if message.reply_markup and message.reply_markup.rows:
                    if len(message.reply_markup.rows) > 1 and len(message.reply_markup.rows[1].buttons) > 0:
                        button_text = message.reply_markup.rows[1].buttons[0].text
                        await asyncio.sleep(random.uniform(4, 9))
                        await self.client.send_message(message.sender_id, button_text)
                return  # Не продолжать, если выполнено условие для перехода на следующую локацию
