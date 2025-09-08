# meta developer: @MartyyyK
# requires: python-barcode

import barcode
from barcode.writer import ImageWriter
from .. import loader, utils
import uuid
import os
import re

async def generate_barcode(data, filename):
    options = {
        'write_text': False,
        'quiet_zone': 2,
        'module_height': 15.0
    }
    code128 = barcode.get('code128', data, writer=ImageWriter())
    code128.save(filename, options)

@loader.tds
class BarcodeGeneratorMod(loader.Module):
    """Генерирует штрих-код"""

    strings = {
        "name": "BarcodeGenerator",
    }

    @loader.command()
    async def barcodecmd(self, message):
        """<числовые данные>"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, "Пожалуйста, введите данные для генерации")
            return

        if not re.match("^[0-9]+$", args):
            await utils.answer(message, "Ошибка: штрих-код может содержать только цифры")
            return

        try:
            randuuid = str(uuid.uuid4())
            filename = f"{randuuid}.png"
            await generate_barcode(args, randuuid)
            await utils.answer_file(message, filename, caption=args)
            os.remove(filename)
        except Exception as e:
            await utils.answer(message, f"Ошибка: {str(e)}")