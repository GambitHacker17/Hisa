# meta developer: @MartyyyK

import asyncio
import telethon as tl
from .. import loader, utils

@loader.tds
class Dep(loader.Module):
    """Депни всё что хочешь"""

    strings = {
        "name": "dep",
    }

    @loader.command()
    async def депаю(self, message):
        """ - то, что депнешь"""
        stavka = utils.get_args_raw(message)
        if not stavka:
            return await utils.answer(message, f"А что депать то?")
        await utils.answer(message, f"<b>Вы поставили: {stavka}</b>\nНу чтож, начинаем😈")
        await asyncio.sleep(2)
        cas = await utils.answer_file(message, tl.types.InputMediaDice('🎰'))
        await asyncio.sleep(3.1)
        await message.respond(f"<b>Вы выиграли X2 {stavka}</b>\nНа этот раз тебе повезло", reply_to=cas.id) if cas.dice.value in [64, 1, 43, 22] else await message.respond(f"<b>Вы проиграли {stavka}</b>\nДелай додеп", reply_to=cas.id)