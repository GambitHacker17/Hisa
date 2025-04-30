#meta developer: @MartyyyK

import asyncio
from datetime import datetime
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class Stats(loader.Module):
    """Показать статистику аккаунта"""

    strings = {
        "name": "Stats",
        "loading_stats": "<b><emoji document_id=5326015457155620929>🔄</emoji> Загрузка статистики...</b>",
    }

    @loader.command()
    async def stats(self, message):
        """Получить статистику"""

        await utils.answer(message, self.strings['loading_stats'])
        u_chat = 0
        b_chat = 0
        c_chat = 0
        ch_chat = 0
        all_chats = 0

        async for dialog in self._client.iter_dialogs():
            all_chats += 1
            if dialog.is_user:
                if dialog.entity.bot:
                    b_chat += 1
                elif not dialog.entity.bot:
                    u_chat += 1
            elif dialog.is_group:
                c_chat += 1
            elif dialog.is_channel:
                if dialog.entity.megagroup or dialog.entity.gigagroup:
                    if dialog.entity.megagroup:
                        c_chat += 1
                    elif dialog.entity.gigagroup:
                        c_chat += 1
                elif not dialog.entity.megagroup and not dialog.entity.gigagroup:
                    ch_chat += 1
        await utils.answer(message,
f"""<b><emoji document_id=5431577498364158238>📊</emoji> Твоя статистика

<emoji document_id=5884510167986343350>💬</emoji> Всего чатов: <code>{all_chats}</code>

<emoji document_id=5258011929993026890>👤</emoji> <code>{u_chat}</code> личных чатов
<emoji document_id=5258513401784573443>👥</emoji> <code>{c_chat}</code> групп
<emoji document_id=5260268501515377807>📢</emoji> <code>{ch_chat}</code> каналов
<emoji document_id=5258093637450866522>🤖</emoji> <code>{b_chat}</code> ботов</b>""")