# meta developer: @MartyyyK
# meta

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
    }

    def __init__(self):
        self.name = self.strings["name"]
        self._me = None
        self.__author__ = "@MartyyyK"
        self.__version__ = "1.0.0"
        self.commands = ["p", "c", "s", "configp"]
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


    @loader.command(
        ru_doc="Анимированный эффект печатания.",
        eng_doc="Animated typing effect."
    )
    async def p(self, message):
        try:
            text = utils.get_args_raw(message)
            if not text:
                return await utils.answer(message, "<b>Укажите текст для печатания!</b>", parse_mode="html")
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
                return await utils.answer(message, "<b>Укажите новый символ курсора!</b>", parse_mode="html")
            self.typing_cursor = new_cursor
            self.async_set("typing_cursor", self.typing_cursor)
            await utils.answer(message, f"<b>Курсор изменен на</b> {self.typing_cursor}", parse_mode="html")
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
                  return await utils.answer(message, "<b>Укажите задержку</b>", parse_mode="html")
             try:
                  new_delay = float(new_delay)
             except ValueError:
                  return await utils.answer(message, "<b>Задержка должна быть числом</b>", parse_mode="html")
             self.typing_delay = new_delay
             self.async_set("typing_delay", self.typing_delay)
             await utils.answer(message, f"<b>Задержка изменена на</b> {self.typing_delay}", parse_mode="html")

        except Exception as e:
             await utils.answer(message, self.strings["error"])
             log.error(str(e))

    def async_set(self, key, value):  
        self.set(key, value)

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
                f"<b><code>.configp</code> Вся информация\n<code>.p</code> Анимированный эффект печатания\n<code>.s</code> Изменяет тайминг\n<code>.c</code> Изменяет курсор\n\n</b>"
                f"<b>Создатель модуля @MartyyyK</b>"

            )

            await utils.answer(message, config_text, parse_mode="html")
        except Exception as e:
            await utils.answer(message, self.strings["error"])
            log.error(str(e))

    def async_set(self, key, value):
         self.set(key, value)