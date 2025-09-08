#meta developer: @MartyyyK

import os
import re
import sys
import logging
import asyncio
import requests

from telethon.tl.types import Message
from .. import loader, utils
from ..inline.types import InlineCall, InlineQuery

logger = logging.getLogger(__name__)

async def bash_exec(command: str):
    a = await asyncio.create_subprocess_shell(
        command.strip(),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    out = await a.stdout.read(-1)
    if not out:
        try:
            return (await a.stderr.read(-1)).decode()
        except UnicodeDecodeError:
            return f"Ошибка декодирования Unicode: {(await a.stderr.read(-1))}"
    else:
        try:
            return out.decode()
        except UnicodeDecodeError:
            return f"Ошибка декодирования Unicode: {out}"


def get_tree(directory, level=0):
    tree = ""
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)

        if item == "__pycache__" or item == "debug_modules":
            tree += "|   " * level + "|-- " + item + "/\n"
            continue

        if os.path.isdir(item_path):
            tree += "|   " * level + "|-- " + item + "/\n"
            tree += get_tree(item_path, level + 1)
        else:
            if item.endswith(".py") or item in ["__init__.py", "__main__.py"]:
                tree += "|   " * level + "|-- " + f"{item}\n"
    return tree

@loader.tds
class HisaFrameworkMod(loader.Module):
    """Модуль для кастомизации Hisa Userbot"""

    strings = {
        "name": "HisaFramework",

        "main.info.text": (
            "<b>Hisa Framework</b> - лучший <code>мультитул</code> для вашего Hisa Userbot.\n"
            "Подходит как для обычного <b>пользователя</b>, так и для <b>продвинутого пользователя</b>.\n"
            "Имеет множество функций для помощи в <b>кастомизации</b> и <b>модификации</b> вашего Hisa.\n"
            "Открывает <b>портал новых возможностей</b> для разработки."
        ),

        "config.pip_install": "Команда установки PIP.",
        "config.pip_uninstall": "Команда удаления PIP.",
        "config.version_check": "Проверка доступной версии Hisa.",

        "menu.title": "<b>Выберите действие</b>",
        "menu.button.files": "📂 Дерево файлов Hisa",
        "menu.button.database": "🖊️ Редактор базы данных",
        "menu.button.editors": "📝 Простые редакторы",
        "menu.button.pip_manager": "⛩️ Менеджер PIP пакетов",
        "menu.button.info": "🚀 ИНФО",

        "database.title": "🖊️ <b>Настройка базы данных вашего Hisa.</b>",
        "database.button.enter_value": "🖊️ Ввести значение",
        "database.value_description": "🖊️ Введите новое значение базы данных",

        "editors.title": "📝 <b>Простое редактирование значений</b>",
        "editors.button.device": "💻 Изменить устройство",
        "editors.button.device.description": "🖊️ Напишите ваше устройство",
        "editors.button.startup": "⌛ Изменить время запуска",
        "editors.button.startup.description": "🖊️ Напишите ваше UNIX время",

        "pip_manager.button.add": "➕ добавить",
        "pip_manager.button.remove": "➖ удалить",
        "pip_manager.button.add.description": "➕ Напишите название пакета из PyPi",
        "pip_manager.button.remove.description": "➖ Напишите название пакета из freeze"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "pip_install",
                "pip install --upgrade --disable-pip-version-check --no-warn-script-location",
                doc=lambda: self.strings("config.pip_install")
            ),
            loader.ConfigValue(
                "pip_uninstall",
                "pip uninstall",
                doc=lambda: self.strings("config.pip_uninstall")
            ),
            loader.ConfigValue(
                "version_check",
                True,
                doc=lambda: self.strings("config.version_check"),
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self, client, db):
        self.db = db
        if "HisaFramework" not in db.keys():
            db["HisaFramework"] = {}
            db.save()


    @loader.inline_handler()
    async def framework(self, query: InlineQuery):
        """- открывает меню через inline бота"""

        return {
            "title": "Hisa Framework",
            "description": "Открыть меню Hisa framework",
            "message": self.strings("menu.title"),
            "reply_markup": [
                [
                    {
                        "text": self.strings("menu.button.files"),
                        "callback": self.test_files,
                    },
                ],
                [
                    {
                        "text": self.strings("menu.button.database"),
                        "callback": self.database,
                    },
                    {
                        "text": self.strings("menu.button.editors"),
                        "callback": self.editors,
                    },
                ],
                [
                    {
                        "text": self.strings("menu.button.pip_manager"),
                        "callback": self.pip_manager,
                    },
                ],
                [
                    {
                        "text": self.strings("menu.button.info"),
                        "callback": self.info
                    }
                ]
            ]
        }

    @loader.command()
    async def frameworkcmd(self, message: Message):
        """- открывает меню через команду"""
        await self.inline.form(
            self.strings("menu.title"),
            reply_markup=[
                [
                    {
                        "text": self.strings("menu.button.files"),
                        "callback": self.test_files,
                    },
                ],
                [
                    {
                        "text": self.strings("menu.button.database"),
                        "callback": self.database,
                    },
                    {
                        "text": self.strings("menu.button.editors"),
                        "callback": self.editors,
                    },
                ],
                [
                    {
                        "text": self.strings("menu.button.pip_manager"),
                        "callback": self.pip_manager,
                    },
                ],
                [
                    {
                        "text": self.strings("menu.button.info"),
                        "callback": self.info
                    }
                ],
            ],
            message=message,
        )

    async def pip_manager_add(self, call: InlineCall, query: str, inline_message_id: str):
        command = self.config["pip_install"]
        stdout = await bash_exec(f"{sys.executable} -m {command} {query}")

        output = (
            stdout
            if len(stdout) <= 2000
            else stdout[:-1000]
        )

        text = (
            "➕ <b>Установлено!</b>\n"
            f"<code>{output}</code>"
        )

        await call.edit(text)

    async def pip_manager_remove(self, call: InlineCall, query: str, inline_message_id: str):
        command = self.config["pip_uninstall"]
        stdout = await bash_exec(f"{sys.executable} -m {command} {query}")

        output = (
            stdout
            if len(stdout) <= 2000
            else stdout[:-1000]
        )

        text = (
            "➖ <b>Удалено!</b>\n"
            f"<code>{output}</code>"
        )

        await call.edit(text)

    async def pip_manager(self, call: InlineCall):

        output = await bash_exec(f"{sys.executable} -m pip freeze")

        await call.edit(
            f"<code>{output}</code>",
            reply_markup=[
                {
                    "text": self.strings("pip_manager.button.add"),
                    "input": self.strings("pip_manager.button.add.description"),
                    "handler": self.pip_manager_add,
                    "args": (call.inline_message_id,),
                },
                {
                    "text": self.strings("pip_manager.button.remove"),
                    "input": self.strings("pip_manager.button.remove.description"),
                    "handler": self.pip_manager_remove,
                    "args": (call.inline_message_id,),
                },
            ]
        )

    async def info(self, call: InlineCall):
        await call.edit(self.strings("main.info.text"))

    async def device(self, call: InlineCall, query: str, inline_message_id: str):
        """Изменяет настройку устройства."""
        utils.get_named_platform = lambda: query
        await call.edit(f"🖊️ <b>Изменено на {query}!</b>", inline_message_id=inline_message_id)

    async def startup(self, call: InlineCall, query: str, inline_message_id: str):
        """Изменяет настройку времени запуска."""
        utils.init_ts = int(query)
        await call.edit(f"🖊️ <b>Изменено на {query}!</b>", inline_message_id=inline_message_id)

    async def editors(self, call: InlineCall):
        """Открывает меню простого редактирования значений."""
        await call.edit(
            self.strings("editors.title"),
            reply_markup=[
                {
                    "text": self.strings("editors.button.device"),
                    "input": self.strings("editors.button.device.description"),
                    "handler": self.device,
                    "args": (call.inline_message_id,),
                },
                {
                    "text": self.strings("editors.button.startup"),
                    "input": self.strings("editors.button.startup.description"),
                    "handler": self.startup,
                    "args": (call.inline_message_id,),
                },
            ]
        )

    async def change_value(self, call: InlineCall, query: str, inline_message_id: str, keys: list):
        """Изменяет значение в базе данных"""
        db = self.db
        for key in keys[:-1]:
            db = db[key]

        db[keys[-1]] = query
        self.db.save()

        await call.edit(
            f"🖊️ <b>Изменено на</b> <code>{query}</code>",
            inline_message_id=inline_message_id
        )

    async def database_edit(self, call: InlineCall, keys: list):
        """Редактирует значения базы данных"""
        value = self.db
        for key in keys:
            value = value[key]

        if isinstance(value, dict):
            await call.edit(
                f"<code>{value}</code>",
                reply_markup=[
                    *[
                        {
                            "text": key,
                            "callback": self.database_edit,
                            "args": (keys + [key],),
                        }
                        for key in value.keys()
                    ]
                ]
            )
        else:
            await call.edit(
                f"<code>{value}</code>",
                reply_markup=[
                    {
                        "text": self.strings("database.button.enter_value"),
                        "input": self.strings("database.value_description"),
                        "handler": self.change_value,
                        "args": (call.inline_message_id, keys,),
                    }
                ]
            )

    async def database(self, call: InlineCall):
        """Редактор базы данных"""
        keys = list(self.db.keys())

        button_rows = []
        for i in range(0, len(keys), 5):
            row = [
                {
                    "text": key,
                    "callback": self.database_edit,
                    "args": ([key],),
                }
                for key in keys[i:i + 5]
            ]
            button_rows.append(row)

        button_rows.insert(0, [
            {
                "text": "📌 HisaFramework",
                "callback": self.database_edit,
                "args": (["HisaFramework"],),
            },
        ])

        await call.edit(
            self.strings["database.title"],
            reply_markup=button_rows
        )

    async def test_files(self, call: InlineCall):
        """Дерево файлов"""
        tree = get_tree("hisa")
        await call.edit(f"<code>{tree}</code>")