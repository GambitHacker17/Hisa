# meta developer: @MartyyyK

from .. import loader, utils
from telethon.tl.types import Message
import urllib.parse

@loader.tds
class SearchPic(loader.Module):
    """Модуль для поиска изображений"""
    strings = {"name": "SearchPic"}

    @loader.unrestricted
    async def spiccmd(self, message: Message):
        """Поиск изображения\nИспользование: .spic <запрос>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "❌ Укажите поисковый запрос")
            return

        try:
            query = urllib.parse.quote_plus(args)
            image_url = f"https://yandex.uz/images/touch/search/?text={query}"
            
            await message.delete()
            await self.inline.form(
                message=message,
                text = f"🎑 Изображение найдено\n✍ Запрос: {args}",
                photo=image_url,
                reply_markup=None
            )

        except Exception as e:
            await utils.answer(message, f"⚠️ Ошибка: {str(e)}")