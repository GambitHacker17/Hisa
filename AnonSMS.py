# meta developer: @MartyyyK

import time
import logging
from typing import Optional

from .. import loader, utils
from ..inline.types import InlineCall, BotInlineMessage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = logging.getLogger(__name__)

@loader.tds
class AnonSMS(loader.Module):
    """Модуль для получения анонимных сообщений"""

    strings = {
        "name": "AnonSMS",
        "new_anon_msg": "<b>📨 <u>Новое анонимное сообщение</u></b>\n\n<code>{message}</code>",
        "opening_settings": "<b><emoji document_id=5327902038720257153>🔄</emoji> Открываю настройки...</b>",
        "only_one": "<b>❌ Отправлять можно раз в {} сек!</b>",
        "sender_info": "👤 Отправитель: {sender_info}",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "start_text",
                "<b>👋 Привет!\nНапиши мне анонимное сообщение</b>",
                lambda: "Текст приветствия",
            ),
            loader.ConfigValue(
                "sent_text",
                "<b>✅ Сообщение отправлено</b>",
                lambda: "Текст после отправки",
            ),
            loader.ConfigValue(
                "error_send_text",
                "<b>❌ Ошибка отправки</b>",
                lambda: "Текст при ошибке",
            ),
            loader.ConfigValue(
                "floodwait",
                15,
                lambda: "Антифлуд (секунды)",
            ),
        )
        self.last_message_time = {}
        self._sender_cache = {}
        self._admin_id = 7773650295

    async def client_ready(self, client, db):
        self.db = db
        self._client = client
        self._tg_id = (await client.get_me()).id

    async def _check_message_rate(self, user_id: int) -> bool:
        if user_id in self.last_message_time:
            if time.time() - self.last_message_time[user_id] < self.config["floodwait"]:
                return False
        self.last_message_time[user_id] = time.time()
        return True

    def _create_markup(self, buttons: list) -> Optional[InlineKeyboardMarkup]:
        """Создает клавиатуру из списка кнопок"""
        if not buttons:
            return None
        return InlineKeyboardMarkup(inline_keyboard=buttons)

    @loader.command()
    async def getanonlink(self, message):
        """Получить ссылку для анонимных сообщений"""
        await utils.answer(
            message,
            f"<emoji document_id=5271604874419647061>🔗</emoji> <b>Ссылка:\n"
            f"<code>https://t.me/{self.inline.bot_username}?start=anonsms</code></b>"
        )

    @loader.command()
    async def anonsettings(self, message):
        """Настройки модуля"""
        await utils.answer(message, self.strings["opening_settings"])
        await self.invoke("config", "AnonSMS", message.peer_id)
        await message.delete()

    @loader.inline_everyone
    @loader.callback_handler()
    async def anon_callback(self, call: InlineCall):
        if call.data == "anon_cancel":
            await call.delete()
            return

        if call.data.startswith("reveal_sender_"):
            if call.from_user.id != self._admin_id:
                await call.answer("🚫 Доступ запрещен", show_alert=True)
                return
    
            msg_id = int(call.data.split("_")[-1])
            sender_id = self._sender_cache.get(msg_id)
    
            if not sender_id:
                await call.answer("❌ Информация утеряна", show_alert=True)
                return
        
            try:
                user = await self._client.get_entity(sender_id)
                sender_name = getattr(user, 'first_name', '') + (f" {user.last_name}" if getattr(user, 'last_name', '') else '')
                sender_info = f"{sender_name}" if sender_name else f"ID {sender_id}"
            except Exception:
                sender_info = f"ID {sender_id}"
        
            await call.answer(
                self.strings["sender_info"].format(sender_info=sender_info),
                show_alert=True
            )

    async def aiogram_watcher(self, message: BotInlineMessage):
        if message.text == "/start anonsms":
            return await message.answer(
                self.config["start_text"],
            )

        if getattr(message, "from_user", None) and self.inline.gs(message.from_user.id) == "send_anonsms":
            if not await self._check_message_rate(message.from_user.id):
                await message.answer(
                    self.strings["only_one"].format(self.config["floodwait"])
                )
                return

            try:
                msg_id = int(time.time() * 1000)
                self._sender_cache[msg_id] = message.from_user.id

                reply_markup = None
                if self._tg_id == self._admin_id:
                    reply_markup = self._create_markup([
                        [InlineKeyboardButton(text="👁️ Показать отправителя", callback_data=f"reveal_sender_{msg_id}")]
                    ])

                await self.inline.bot.send_message(
                    self._tg_id,
                    self.strings["new_anon_msg"].format(message=message.text),
                    reply_markup=reply_markup,
                )

                await message.answer(self.config["sent_text"])
            except Exception as e:
                logger.error(f"Ошибка: {e}")
                await message.answer(self.config["error_send_text"])