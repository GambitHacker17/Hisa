#meta developer: @MartyyyK

import logging
import requests
from hisa import loader, utils
import time

logger=logging.getLogger(__name__)

class GitClone(loader.Module):
    """Cloning codes from GitHub using raw links"""
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "file_name",
                "clone.py",
                lambda:
                self.strings("cfg_file"),
            ),
        )

    strings={
        "name": "GitClone",
        "no_args": "<emoji document_id=5321074831720982832>⚠️</emoji> Don't have any args",
        "invalid_url": "<emoji document_id=5305724700209454594>❎</emoji> Invalid link format.",
        "cloning": "<emoji document_id=5303382121967001310>💻</emoji> Cloning code..",
        "success": "<emoji document_id=5305417687357203905>✅</emoji> <b>The code was successfully cloned into the file</b>",
        "cfg_file": "Choose a file name with format.\nExample:  file.js, file.py, file.java etc.",
    }

    strings_ru={
        "no_args": "<emoji document_id=5321074831720982832>⚠️</emoji> Недостаточно аргументов",
        "invalid_url": "<emoji document_id=5305724700209454594>❎</emoji> Неверный формат ссылки.",
        "cloning": "<emoji document_id=5303382121967001310>💻</emoji> Клонирую код..",
        "success": "<emoji document_id=5305417687357203905>✅</emoji> <b>Код успешно клонирован в файл</b>",
        "cfg_file": "Укажи название и расширение для своего файла\nНапример: file.js, main.py, clone.java и т.д.",
    }
    
    @loader.command(ru_doc="-> клонировать код из репозитория, используя raw ссылку")
    async def gitclcmd(self, message):
        """-> Clone code from repository using raw link"""
        args=utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_args"))
        else:
            response=requests.get(args)
            name=self.config["file_name"]
            if response.status_code==200:
                await utils.answer(message, self.strings("cloning"))
                time.sleep(1)
                with open(name, 'wb') as file:
                    file.write(response.content)
                await utils.answer_file(message, name, self.strings("success"))
            else:
                await utils.answer(message, self.strings("invalid_url"))