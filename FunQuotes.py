__version__ = (1, 0, 0)

# meta developer: @MartyyyK

from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class InlineFunMod(loader.Module):
    """Create Fun quotes"""

    strings = {
        "name": "FunQuotes",
        "where_text": "<emoji document_id='6041914500272098262'>🚫</emoji> <b>Provide a text to create sticker with</b>",
        "processing": (
            "<emoji document_id='6318766236746384900'>🕔</emoji> <b>Processing...</b>"
        ),
    }

    strings_ru = {
        "where_text": "<emoji document_id='6041914500272098262'>🚫</emoji> <b>Укажи текст для создания стикера</b>",
        "processing": (
            "<emoji document_id='6318766236746384900'>🕔</emoji> <b>Обработка...</b>"
        ),
    }

    async def twitcmd(self, message: Message):
        """<text> - Create Twitter message quote"""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit(self.strings("where_text"))
            return

        await message.edit(self.strings("processing"))

        try:
            query = await self._client.inline_query("@TwitterStatusBot", text)
            await message.respond(file=query[0].document)
        except Exception as e:
            await utils.answer(message, str(e))
            return

        if message.out:
            await message.delete()

    async def frogcmd(self, message: Message):
        """<text> - Create Frog text quote"""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit(self.strings("where_text"))
            return

        await message.edit(self.strings("processing"))

        try:
            query = await self._client.inline_query("@honka_says_bot", text + ".")
            await message.respond(file=query[0].document)
        except Exception as e:
            await utils.answer(message, str(e))
            return

        if message.out:
            await message.delete()         