# meta developer: @MartyyyK

from telethon.tl.types import Message

from .. import loader, utils

FRAMES = [
    "🌘🌗🌖🌕🌔🌓🌒\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💓❤️💓💓❤️\n❤️💓💓💓💓💓❤️\n🌙❤️💓💓💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌘🌗🌖🌕🌔🌓🌒",
    "🌗🌖🌕🌔🌓🌒🌘\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💓❤️💓💓❤️\n❤️💓💓💗💓💓❤️\n🌙❤️💓💓💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌗🌖🌕🌔🌓🌒🌘",
    "🌖🌕🌔🌓🌒🌘🌗\n🌙❤️❤️🌙❤️❤️🌙\n❤️💓💗❤️💗💓❤️\n❤️💓💗💗💗💓❤️\n🌙❤️💓💗💓❤️🌙\n🌙🌙❤️💓❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌖🌕🌔🌓🌒🌘🌗",
    "🌕🌔🌓🌒🌘🌗🌖\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💗❤️💗💗❤️\n❤️💗💗💗💗💗❤️\n🌙❤️💗💗💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌕🌔🌓🌒🌘🌗🌖",
    "🌔🌓🌒🌘🌗🌖🌕\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💗❤️💗💗❤️\n❤️💗💗💖💗💗❤️\n🌙❤️💗💗💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌔🌓🌒🌘🌗🌖🌕",
    "🌓🌒🌘🌗🌖🌕🌔\n🌙❤️❤️🌙❤️❤️🌙\n❤️💗💖❤️💖💗❤️\n❤️💗💖💖💖💗❤️\n🌙❤️💗💖💗❤️🌙\n🌙🌙❤️💗❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌓🌒🌘🌗🌖🌕🌔",
    "🌒🌘🌗🌖🌕🌔🌓\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💖❤️💖💖❤️\n❤️💖💖💖💖💖❤️\n🌙❤️💖💖💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌒🌘🌗🌖🌕🌔🌓",
    "🌘🌗🌖🌕🌔🌓🌒\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💖❤️💖💖❤️\n❤️💖💖💓💖💖❤️\n🌙❤️💖💖💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌘🌗🌖🌕🌔🌓🌒",
    "🌗🌖🌕🌔🌓🌒🌘\n🌙❤️❤️🌙❤️❤️🌙\n❤️💖💓❤️💓💖❤️\n❤️💖💓💓💓💖❤️\n🌙❤️💖💓💖❤️🌙\n🌙🌙❤️💖❤️🌙🌙\n🌙🌙🌙❤️🌙🌙🌙\n🌗🌖🌕🌔🌓🌒🌘",
] * 3 + [
    "💓",
    "💗",
    "💖",
]

@loader.tds
class MoonLoveMod(loader.Module):

    strings = {"name": "MoonLove"}
    strings_ru = {
        "_cls_doc": "Анимация с лунами и сердечками",
        "_cmd_doc_moonlove": "<текст> - люблю тебя невообразимо",
        "_cmd_doc_moonlovei": "<текст> - люблю тебя невообразимо (инлайн)",
    }

    async def moonlovecmd(self, message: Message):
        m = await self.animate(
            message,
            FRAMES,
            interval=0.3,
            inline=False,
        )
        await m.edit(utils.get_args_raw(message) or "❤️")

    async def moonloveicmd(self, message: Message):
        m = await self.animate(
            message,
            FRAMES,
            interval=0.3,
            inline=True,
        )
        await m.edit(utils.get_args_raw(message) or "❤️")