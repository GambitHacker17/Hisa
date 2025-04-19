# meta developer: @MartyyyK
# meta

import asyncio
from datetime import datetime, timedelta
from .. import loader, utils
import logging

log = logging.getLogger(__name__)

@loader.tds
class AnimatedTypingMod(loader.Module):
    strings = {
        "name": "Animated Typing",
        "usage": "Используйте .p <текст> для анимации печатания.\nИспользуйте .c <новый курсор>\nИспользуйте .s <задержка>",
        "error": "<b>Произошла ошибка во время выполнения команды.</b>",
           "loaded": (
        "▫️ .c Изменяет символ курсора.\n"
        "▫️ .configp Показывает текущие настройки и время по МСК.\n"
        "▫️ .p Анимированный эффект печатания.\n"
        "▫️ .s Изменяет задержку печатания.\n\n"
        "updated": "Модуль <bold>Animated Typing</bold> был успешно обновлен!",
        "spam_usage": "Используйте: .sp <текст> <количество> <задержка>",
        "no_text": "<b>Укажите текст для печатания!</b>",
        "no_cursor": "<b>Укажите новый символ курсора!</b>",
        "no_delay": "<b>Укажите задержку!</b>",
        "invalid_delay": "<b>Задержка должна быть числом!</b>",
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self.__author__ = "@MartyyyK"
        self.__version__ = "1.0.0"
        self.commands = ["p", "c", "s", "configp", "sp"]
        self.typing_delay = 0.08
        self.typing_cursor = "▮"

    async def client_ready(self, client, db):
        self._me = await client.get_me()
        try:
            cursor = self.get("typing_cursor", default="█")
            if cursor is not None:
                self.typing_cursor = cursor

            delay = self.get("typing_delay", default=0.08)
            if delay is not None:
                self.typing_delay = float(delay)
        except Exception as e:
            log.error(f"Ошибка при загрузке настроек: {e}")

    async def p(self, message):
        try:
            text = utils.get_args_raw(message)
            if not text:
                return await utils.answer(message, self.strings["no_text"])
            
            await message.edit(self.typing_cursor)
            typed_text = ""
            for char in text:
                typed_text += char
                await message.edit(typed_text + self.typing_cursor)
                await asyncio.sleep(self.typing_delay)

            await message.edit(typed_text)

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e), exc_info=True)

    async def c(self, message):
        try:
            new_cursor = utils.get_args_raw(message)
            if not new_cursor:
                return await utils.answer(message, self.strings["no_cursor"])
            
            self.typing_cursor = new_cursor
            self.async_set("typing_cursor", self.typing_cursor)
            await utils.answer(message, f"<b>Курсор изменен на</b> {self.typing_cursor}")

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e), exc_info=True)

    async def s(self, message):
        try:
            new_delay = utils.get_args_raw(message)
            if not new_delay:
                return await utils.answer(message, self.strings["no_delay"])
            
            try:
                new_delay = float(new_delay)
            except ValueError:
                return await utils.answer(message, self.strings["invalid_delay"])
            
            self.typing_delay = new_delay
            self.async_set("typing_delay", self.typing_delay)
            await utils.answer(message, f"<b>Задержка изменена на</b> {self.typing_delay}")

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e), exc_info=True)

    async def configp(self, message):
        try:
            utc_time = datetime.utcnow()
            moscow_timezone = timedelta(hours=3)
            moscow_time = utc_time + moscow_timezone
            formatted_moscow_time = moscow_time.strftime("%H:%M:%S %d.%m.%Y")
            
            config_text = (
                "<b>Текущие настройки:</b>\n"
                f"<b>Курсор:</b> {self.typing_cursor}\n"
                f"<b>Задержка:</b> <code>{self.typing_delay}</code>\n"
                f"<b>Время по Москве:</b> {formatted_moscow_time}\n\n"
                f"<b>Команды:</b>\n"
                f"<code>.configp</code> - Показать настройки\n"
                f"<code>.p</code> - Анимированный ввод текста\n"
                f"<code>.s</code> - Изменить задержку\n"
                f"<code>.c</code> - Изменить курсор\n"
                f"<code>.sp</code> - Спам (текст кол-во задержка)\n\n"
                f"<b>Автор:</b> @MartyyyK\n"
                f"<b>Версия:</b> {self.__version__}"
            )
            
            await utils.answer(message, config_text)

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e), exc_info=True)

    async def sp(self, message):
        try:
            args = utils.get_args_raw(message)
            if not args:
                return await utils.answer(message, self.strings["spam_usage"])
            
            parts = []
            current = []
            in_quotes = False
            
            for char in args:
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ' ' and not in_quotes:
                    if current:
                        parts.append(''.join(current))
                        current = []
                else:
                    current.append(char)
            
            if current:
                parts.append(''.join(current))
            
            if len(parts) < 2:
                return await utils.answer(message, self.strings["spam_usage"])
            
            text = parts[0]
            count = 1
            delay = 0.5
            
            try:
                if len(parts) > 1:
                    count = int(parts[1])
                if len(parts) > 2:
                    delay = float(parts[2])
            except ValueError:
                return await utils.answer(message, self.strings["invalid_delay"])
            
            await message.delete()
            
            for _ in range(count):
                await message.respond(text)
                if delay > 0:
                    await asyncio.sleep(delay)
                    
        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e), exc_info=True)

    def async_set(self, key, value):
        self.set(key, value)
