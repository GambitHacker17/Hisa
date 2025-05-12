# meta developer: @MartyyyK

import asyncio
import random
import os
import time
from datetime import datetime, timedelta
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from .. import loader, utils
import logging


log = logging.getLogger(__name__)

@loader.tds
class AnimatedTypingMod(loader.Module):
    strings = {
        "name": "Animated Typing",
        "usage": "Используйте .p <текст> для анимации печатания.\nИспользуйте .c <новый курсор>\nИспользуйте .s <задержка>",
        "error": "<b>Произошла ошибка во время выполнения команды.</b>",
        "loaded": "Модуль <bold>Animated Typing</bold> был успешно загружен!",
        "updated": "Модуль <bold>Animated Typing</bold> был успешно обновлен!",
        "spam_usage": "<b>Использование:</b> .sp <текст> <количество> <задержка>",
        "invalid_delay": "<b>Задержка и количество должны быть числами.</b>",
        "missing_text": "<b>Укажите текст для печатания!</b>",
        "missing_cursor": "<b>Укажите новый символ курсора!</b>",
        "missing_delay": "<b>Укажите задержку</b>",
        "invalid_number": "<b>Задержка должна быть числом</b>",
        "positive_number": "<b>Значение должно быть положительным числом.</b>",
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
        self.typing_cursor = self.get("typing_cursor", "█")
        self.typing_delay = float(self.get("typing_delay", 0.08))

    @loader.command(
        ru_doc="Анимированный эффект печатания.",
        eng_doc="Animated typing effect."
    )
    async def p(self, message):
        try:
            text = utils.get_args_raw(message)
            if not text:
                return await utils.answer(message, self.strings["missing_text"])
            
            await message.edit(self.typing_cursor)
            typed_text = ""
            
            for char in text:
                typed_text += char
                await message.edit(typed_text + self.typing_cursor)
                await asyncio.sleep(self.typing_delay)

            await message.edit(typed_text)

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e))

    @loader.command(
        ru_doc="Изменяет символ курсора.",
        eng_doc="Changes the cursor symbol."
    )
    async def c(self, message):
        try:
            new_cursor = utils.get_args_raw(message)
            if not new_cursor:
                return await utils.answer(message, self.strings["missing_cursor"])
            
            self.typing_cursor = new_cursor
            self.async_set("typing_cursor", self.typing_cursor)
            await utils.answer(message, f"<b>Курсор изменен на</b> {self.typing_cursor}")
        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e))

    @loader.command(
        ru_doc="Изменяет задержку печатания.",
        eng_doc="Changes the typing delay."
    )
    async def s(self, message):
        try:
            new_delay = utils.get_args_raw(message)
            if not new_delay:
                return await utils.answer(message, self.strings["missing_delay"])
            
            try:
                new_delay = float(new_delay)
                if new_delay <= 0:
                    return await utils.answer(message, self.strings["positive_number"])
            except ValueError:
                return await utils.answer(message, self.strings["invalid_number"])
            
            self.typing_delay = new_delay
            self.async_set("typing_delay", self.typing_delay)
            await utils.answer(message, f"<b>Задержка изменена на</b> {self.typing_delay}")

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e))

    @loader.command(
        ru_doc="Спам. Использование: .sp <текст> <количество> <задержка>",
        eng_doc="Spam. Usage: .sp <text> <amount> <delay>"
    )
    async def sp(self, message):
        try:
            args = utils.get_args(message)
            if len(args) < 1:
                return await utils.answer(message, self.strings["spam_usage"])
            
            text = args[0]
            count = 1
            delay = 0.5
            
            if len(args) > 1:
                try:
                    count = int(args[1])
                    if count <= 0:
                        return await utils.answer(message, self.strings["positive_number"])
                except ValueError:
                    return await utils.answer(message, self.strings["invalid_delay"])
            
            if len(args) > 2:
                try:
                    delay = float(args[2])
                    if delay < 0:
                        return await utils.answer(message, self.strings["positive_number"])
                except ValueError:
                    return await utils.answer(message, self.strings["invalid_delay"])
            
            await message.delete()
            
            for _ in range(count):
                await message.respond(text)
                if delay > 0:
                    await asyncio.sleep(delay)

        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e))

    @loader.command(
        ru_doc="Показывает текущие настройки и время по МСК.",
        eng_doc="Shows current settings and time in Moscow"
    )
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
                f"<b><code>.configp</code> Вся информация\n"
                f"<code>.p</code> Анимированный эффект печатания\n"
                f"<code>.s</code> Изменяет тайминг\n"
                f"<code>.c</code> Изменяет курсор\n"
                f"<code>.sp</code> Спамит сообщениями. <текст> <количество> <задержка>\n\n</b>"
                f"<b>Создатель модуля @MartyyyK</b>"
            )

            await utils.answer(message, config_text)
        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e))

    def async_set(self, key, value):
        self.set(key, value)
