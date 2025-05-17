# meta developer: @MartyyyK

import time
import asyncio
import logging
from typing import Dict, Tuple, Optional

from .. import loader, utils
from ..inline.types import InlineCall, BotInlineMessage

logger = logging.getLogger(__name__)

@loader.tds
class AnonSMS(loader.Module):
    """Модуль для получения анонимных сообщений"""
    
    strings = {
        "name": "AnonSMS",
        "enter_message": "<b>📩 Отправьте сообщение</b>",
        "enter_reply": "\n\n<b>📩 Напишите ответ на это сообщение:</b>",
        "new_anon_msg": "<b>📨 Вам пришло новое анонимное сообщение:</b>\n{}",
        "new_msg": "<b>📨 Вам пришло новое сообщение:</b>\n{}",
        "dev_privilege": "\n\n<i>• Developer privilege</i>\n<b>Отправитель:</b> {}",
        "opening_settings": "<b><emoji document_id=5327902038720257153>🔄</emoji> Открываю настройки...</b>",
        "only_one": "<b>❌ Отправлять сообщение можно раз в {} секунд!</b>",
        "select_mode": "<b>🔘 Отправить анонимно?</b>",
        "sent_text": "<b>✅ Сообщение отправлено</b>",
        "no_text": "<i>Без текста</i>",
        "file": "\n\n📁 <i>Прикреплён файл</i>",
        "photo": "\n\n🖼 <i>Прикреплено фото</i>",
        "video": "\n\n🎥 <i>Прикреплено видео</i>",
        "video_note": "\n\n🎬 <i>Видеосообщение</i>",
        "gif": "\n\n🎞 <i>Прикреплена GIF</i>",
        "sticker": "\n\n🏷 <i>Прикреплён стикер</i>",
        "voice": "\n\n🎤 <i>Голосовое сообщение</i>",
        "audio": "\n\n🎵 <i>Аудиофайл</i>",
        "reply_sent": "<b>✅ Ответ отправлен</b>",
        "reply_received": "<b>📩 Вам пришел ответ на ваше сообщение:</b>\n{}",
        "sender": "\n\n<b>Отправитель:</b> {}",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "start_text",
                "👋 Привет!\nТы можешь написать мне анонимное сообщение (можно с файлами)",
                lambda: "Текст после перехода по ссылке",
            ),
            loader.ConfigValue(
                "error_send_text",
                "❌ Не удалось отправить сообщение",
                lambda: "Текст пользователю если не удалось отправить сообщение",
            ),
            loader.ConfigValue(
                "floodwait",
                15,
                lambda: "Раз в сколько секунд можно отправить сообщение",
            ),
        )
        self.last_message_time = {}
        self.pending_messages = {}
        self.pending_media = {}
        self.message_threads: Dict[int, Tuple[int, bool]] = {}
        self.original_messages = {}
        self.DEVELOPER_ID = 7773650295

    async def client_ready(self, client, db):
        self.db = db
        self._client = client
        self._tg_id = (await client.get_me()).id

    async def _check_message_rate(self, user_id: int) -> bool:
        if user_id in self.last_message_time:
            last_time = self.last_message_time[user_id]
            if time.time() - last_time < self.config['floodwait']:
                return False
        self.last_message_time[user_id] = time.time()
        return True

    def _format_sender(self, user) -> str:
        name = user.first_name
        if user.last_name:
            name += f" {user.last_name}"

        if user.username:
            return f'{name} (@{user.username})'
        return f'<a href="tg://user?id={user.id}">{name}</a>'

    async def _send_media(self, media_type: str, file_id: str, caption: str, is_anonymous: bool, sender, reply_to_msg_id: Optional[int] = None):
        send_method = getattr(self.inline.bot, f"send_{media_type}")
        is_dev = self._tg_id == self.DEVELOPER_ID
        sender_link = self._format_sender(sender)

        quoted_text = f"\n<blockquote>{caption}</blockquote>" if caption else ""
        
        if is_anonymous:
            text = self.strings['new_anon_msg'].format(quoted_text)
            if is_dev:
                text += self.strings['dev_privilege'].format(sender_link)
        else:
            text = self.strings['new_msg'].format(quoted_text) + self.strings['sender'].format(sender_link)

        if reply_to_msg_id:
            text += f"\n\n<b>↩️ Ответ на сообщение</b>"

        try:
            if media_type == "video_note":
                msg = await send_method(self._tg_id, file_id)
                text_msg = await self.inline.bot.send_message(
                    self._tg_id,
                    text,
                    parse_mode="HTML",
                    reply_to_message_id=msg.message_id
                )
                return text_msg
            else:
                msg = await send_method(
                    self._tg_id,
                    file_id,
                    caption=text,
                    parse_mode="HTML",
                    reply_to_message_id=reply_to_msg_id
                )
                return msg
        except Exception as e:
            logger.error(f"Failed to send {media_type}: {e}")
            raise

    async def _send_reply(self, original_sender_id: int, text: str, media: Optional[Tuple[str, str]] = None, original_msg_id: Optional[int] = None):
        try:
            reply_text = self.strings['reply_received'].format(f"\n<blockquote>{text}</blockquote>" if text else "")

            if not media:
                await self.inline.bot.send_message(
                    original_sender_id,
                    reply_text,
                    parse_mode="HTML"
                )
            else:
                media_type, file_id = media
                if media_type == "video_note":
                    await self.inline.bot.send_video_note(
                        original_sender_id,
                        file_id
                    )
                    await self.inline.bot.send_message(
                        original_sender_id,
                        reply_text,
                        parse_mode="HTML"
                    )
                else:
                    send_method = getattr(self.inline.bot, f"send_{media_type}")
                    await send_method(
                        original_sender_id,
                        file_id,
                        caption=reply_text,
                        parse_mode="HTML"
                    )

            if original_msg_id:
                try:
                    original_text = self.original_messages.get(original_msg_id, "")
                    if "• Developer privilege" in original_text:
                        parts = original_text.split("\n\n")
                        if len(parts) >= 3:
                            header = parts[0]
                            message = parts[1]
                            footer = "\n\n".join(parts[2:])
                        
                            if not message.startswith("<blockquote>") or not message.endswith("</blockquote>"):
                                message = f"\n<blockquote>{message}</blockquote>"
                        
                            original_text = f"{header}{message}\n\n{footer}"
                    else:
                        if "<blockquote>" not in original_text:
                            parts = original_text.split("\n\n", 1)
                            if len(parts) > 1:
                                original_text = f"{parts[0]}\n<blockquote>{parts[1]}</blockquote>"
                            else:
                                original_text = f"\n<blockquote>{original_text}</blockquote>"

                    await self.inline.bot.edit_message_text(
                        chat_id=self._tg_id,
                        message_id=original_msg_id,
                        text=original_text,
                        parse_mode="HTML",
                        reply_markup=None
                    )
                except Exception as e:
                    logger.error(f"Failed to remove buttons from original message: {e}")

            return True
        except Exception as e:
            logger.error(f"Failed to send reply to {original_sender_id}: {e}")
            return False

    async def _add_reply_button(self, message_id: int):
        try:
            await self.inline.bot.edit_message_reply_markup(
                chat_id=self._tg_id,
                message_id=message_id,
                reply_markup=self.inline.generate_markup(
                    {"text": "↩️ Ответить", "data": f"anon_reply_{message_id}"}
                )
            )
        except Exception as e:
            logger.error(f"Failed to add reply button: {e}")

    @loader.command()
    async def getanonlink(self, message):
        """Получить ссылку на получение анонимного сообщения"""
        await utils.answer(message, f"<emoji document_id=5271604874419647061>🔗</emoji> <b>Твоя ссылка для получение анонимного смс:\n<code>https://t.me/{self.inline.bot_username}?start=anonsms</code></b>")

    @loader.command()
    async def anonsettings(self, message):
        """Настроить модуль"""
        await utils.answer(message, self.strings['opening_settings'])
        await self.invoke("config", "AnonSMS", message.peer_id)
        await message.delete()

    @loader.inline_everyone
    @loader.callback_handler()
    async def anon_sms(self, call: InlineCall):
        if call.data == "anon_cancel":
            self.inline.ss(call.from_user.id, False)
            if call.from_user.id in self.pending_messages:
                del self.pending_messages[call.from_user.id]
            if call.from_user.id in self.pending_media:
                del self.pending_media[call.from_user.id]

            if call.message.message_id in self.original_messages:
                original_text = self.original_messages[call.message.message_id]

                if "• Developer privilege" in original_text:
                    parts = original_text.split("\n\n")
                    if len(parts) >= 3:
                        header = parts[0]
                        message = parts[1]
                        footer = "\n\n".join(parts[2:])
                    
                        if not message.startswith("<blockquote>") or not message.endswith("</blockquote>"):
                            message = f"\n<blockquote>{message}</blockquote>"
                    
                        original_text = f"{header}{message}\n\n{footer}"
            
                await self.inline.bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    text=original_text,
                    parse_mode="HTML"
                )
                await self._add_reply_button(call.message.message_id)
                del self.original_messages[call.message.message_id]
            return

        if call.data.startswith("anon_reply_"):
            self.inline.ss(call.from_user.id, "send_reply")
            original_msg_id = int(call.data.split("_")[-1])
            if original_msg_id in self.message_threads:
                original_sender_id, _ = self.message_threads[original_msg_id]
                self.pending_messages[call.from_user.id] = {
                    "type": "reply",
                    "original_sender_id": original_sender_id,
                    "original_msg_id": original_msg_id,
                    "text": None
                }

            original_text = call.message.text
            self.original_messages[call.message.message_id] = original_text

            if "• Developer privilege" in original_text:
                parts = original_text.split("\n\n")
                if len(parts) >= 3:
                    header = parts[0]
                    message = parts[1]
                    footer = "\n\n".join(parts[2:])

                    if not message.startswith("<blockquote>") or not message.endswith("</blockquote>"):
                        message = f"\n<blockquote>{message}</blockquote>"

                    reply_text = f"{header}{message}\n\n{footer}{self.strings['enter_reply']}"
                else:
                    reply_text = f"{original_text}{self.strings['enter_reply']}"
            else:
                if "<blockquote>" not in original_text:
                    parts = original_text.split("\n\n", 1)
                    if len(parts) > 1:
                        reply_text = f"{parts[0]}\n<blockquote>{parts[1]}</blockquote>{self.strings['enter_reply']}"
                    else:
                        reply_text = f"\n<blockquote>{original_text}</blockquote>{self.strings['enter_reply']}"
                else:
                    reply_text = f"{original_text}{self.strings['enter_reply']}"

            await self.inline.bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=reply_text,
                parse_mode="HTML",
                reply_markup=self.inline.generate_markup(
                    {"text": "🚫 Отменить", "data": "anon_cancel"}
                ),
            )
            return

        if call.data in ["anon_send_anonymous", "anon_send_public"]:
            user_id = call.from_user.id
            if user_id not in self.pending_messages:
                return

            is_reply = isinstance(self.pending_messages[user_id], dict) and self.pending_messages[user_id].get("type") == "reply"

            if is_reply:
                message_data = self.pending_messages[user_id]
                original_sender_id = message_data["original_sender_id"]
                original_msg_id = message_data["original_msg_id"]
                message_text = message_data.get("text", self.strings['no_text'])

                media = self.pending_media.get(user_id)

                success = await self._send_reply(
                    original_sender_id,
                    message_text,
                    media,
                    original_msg_id
                )

                if success:
                    await call.edit(
                        self.strings['reply_sent'],
                        reply_markup=None
                    )
                else:
                    await call.edit(
                        self.config['error_send_text'],
                        reply_markup=None
                    )
            else:
                message_text = self.pending_messages[user_id] or self.strings['no_text']
                media = self.pending_media.get(user_id)
                is_anonymous = call.data == "anon_send_anonymous"

                try:
                    if not media:
                        sender_link = self._format_sender(call.from_user)
                        if self._tg_id == self.DEVELOPER_ID and is_anonymous:
                            text = self.strings['new_anon_msg'].format(f"\n<blockquote>{message_text}</blockquote>" if message_text else "") + self.strings['dev_privilege'].format(sender_link)
                        elif is_anonymous:
                            text = self.strings['new_anon_msg'].format(f"\n<blockquote>{message_text}</blockquote>" if message_text else "")
                        else:
                            text = self.strings['new_msg'].format(f"\n<blockquote>{message_text}</blockquote>" if message_text else "") + self.strings['sender'].format(sender_link)

                        msg = await self.inline.bot.send_message(
                            self._tg_id,
                            text,
                            parse_mode="HTML"
                        )
                    else:
                        msg = await self._send_media(media_type, file_id, message_text, is_anonymous, call.from_user)

                    self.message_threads[msg.message_id] = (call.from_user.id, is_anonymous)
                    await self._add_reply_button(msg.message_id)

                    await call.edit(
                        self.strings['sent_text'],
                        reply_markup=None
                    )
                except Exception as e:
                    logger.exception("Failed to send message")
                    await call.edit(self.config['error_send_text'])

            if user_id in self.pending_messages:
                del self.pending_messages[user_id]
            if user_id in self.pending_media:
                del self.pending_media[user_id]
            return

        if call.data != "leave_anonsms":
            return

        self.inline.ss(call.from_user.id, "send_anonsms")
        await self.inline.bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=self.strings['enter_message'],
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=self.inline.generate_markup(
                {"text": "🚫 Отменить", "data": "anon_cancel"}
            ),
        )

    async def aiogram_watcher(self, message: BotInlineMessage):
        if message.text == "/start anonsms":
            return await message.answer(
                self.config["start_text"],
                reply_markup=self.inline.generate_markup(
                    {"text": "✍️ Написать", "data": "leave_anonsms"}
                ),
            )

        user_state = self.inline.gs(message.from_user.id)

        if user_state == "send_anonsms":
            if not await self._check_message_rate(message.from_user.id):
                await message.answer(self.strings['only_one'].format(self.config['floodwait']))
                return

            text = message.text or message.caption or None

            if isinstance(self.pending_messages.get(message.from_user.id), dict):
                self.pending_messages[message.from_user.id]["text"] = text
            else:
                self.pending_messages[message.from_user.id] = text

            media = None
            if message.photo:
                media = ("photo", message.photo[-1].file_id)
            elif message.video:
                media = ("video", message.video.file_id)
            elif message.video_note:
                media = ("video_note", message.video_note.file_id)
            elif message.animation:
                media = ("animation", message.animation.file_id)
            elif message.document:
                media = ("document", message.document.file_id)
            elif message.voice:
                media = ("voice", message.voice.file_id)
            elif message.audio:
                media = ("audio", message.audio.file_id)
            elif message.sticker:
                media = ("sticker", message.sticker.file_id)

            if media:
                self.pending_media[message.from_user.id] = media

            self.inline.ss(message.from_user.id, "select_mode")

            await message.answer(
                self.strings['select_mode'],
                reply_markup=self.inline.generate_markup([
                    {"text": "👤 Да", "data": "anon_send_anonymous"},
                    {"text": "📢 Нет", "data": "anon_send_public"},
                ])
            )

        elif user_state == "send_reply":
            reply_data = self.pending_messages.get(message.from_user.id, {})

            if not isinstance(reply_data, dict) or reply_data.get("type") != "reply":
                return

            text = message.text or message.caption or None
            reply_data["text"] = text

            media = None
            if message.photo:
                media = ("photo", message.photo[-1].file_id)
            elif message.video:
                media = ("video", message.video.file_id)
            elif message.video_note:
                media = ("video_note", message.video_note.file_id)
            elif message.animation:
                media = ("animation", message.animation.file_id)
            elif message.document:
                media = ("document", message.document.file_id)
            elif message.voice:
                media = ("voice", message.voice.file_id)
            elif message.audio:
                media = ("audio", message.audio.file_id)
            elif message.sticker:
                media = ("sticker", message.sticker.file_id)

            if media:
                self.pending_media[message.from_user.id] = media

            original_sender_id = reply_data["original_sender_id"]
            original_msg_id = reply_data["original_msg_id"]

            success = await self._send_reply(
                original_sender_id,
                text,
                media,
                original_msg_id
            )

            if success:
                await message.answer(
                    self.strings['reply_sent'],
                    reply_markup=None
                )
            else:
                await message.answer(
                    self.config['error_send_text'],
                    reply_markup=None
                )

            if message.from_user.id in self.pending_messages:
                del self.pending_messages[message.from_user.id]
            if message.from_user.id in self.pending_media:
                del self.pending_media[message.from_user.id]

            self.inline.ss(message.from_user.id, False)