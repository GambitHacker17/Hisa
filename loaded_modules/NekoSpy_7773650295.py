# meta developer: @MartyyyK
# requires: python-magic
import contextlib
import io
import logging
import time
import typing
import asyncio
import json
import zlib
import os
import mimetypes
import magic
import re
import datetime
from pathlib import Path
from abc import ABC, abstractmethod

from telethon.tl.types import (
    DocumentAttributeFilename,
    Message,
    PeerChat,
    UpdateDeleteChannelMessages,
    UpdateDeleteMessages,
    UpdateEditChannelMessage,
    UpdateEditMessage,
    InputDocumentFileLocation,
    InputPhotoFileLocation,
)
from telethon.utils import get_display_name

from .. import loader, utils

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_size(path: Path) -> int:
    return sum(f.stat().st_size for f in path.glob("**/*") if f.is_file())

def sizeof_fmt(num: int, suffix: str = "B") -> str:
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

class RecentsItem(typing.NamedTuple):
    timestamp: int
    chat_id: int
    message_id: int
    action: str

    @classmethod
    def from_edit(cls, message: Message) -> "RecentsItem":
        return cls(
            timestamp=int(time.time()),
            chat_id=utils.get_chat_id(message),
            message_id=message.id,
            action="edit",
        )

    @classmethod
    def from_delete(
        cls,
        message_id: int,
        chat_id: typing.Optional[int] = None,
    ) -> "RecentsItem":
        return cls(
            timestamp=int(time.time()),
            chat_id=chat_id,
            message_id=message_id,
            action="del",
        )

class CacheManager(ABC):
    @abstractmethod
    def purge(self):
        pass

    @abstractmethod
    def stats(self) -> tuple:
        pass

    @abstractmethod
    def gc(self, max_age: int, max_size: int) -> None:
        pass

    @abstractmethod
    async def store_message(
        self,
        message: Message,
        no_repeat: bool = False,
    ) -> typing.Union[bool, typing.Dict[str, typing.Any]]:
        pass

    @abstractmethod
    async def fetch_message(
        self,
        chat_id: typing.Optional[int],
        message_id: int,
    ) -> typing.Optional[dict]:
        pass

class CacheManagerDisc(CacheManager):
    def __init__(self, client, db):
        self._client = client
        self._db = db
        self._cache_dir = Path.home().joinpath(".nekospy")
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def purge(self):
        for _file in self._cache_dir.iterdir():
            if _file.is_dir():
                for _child in _file.iterdir():
                    _child.unlink()
                _file.rmdir()
            else:
                _file.unlink()

    def stats(self) -> tuple:
        try:
            dirsize = sizeof_fmt(get_size(self._cache_dir))
            messages_count = len(list(self._cache_dir.glob("**/*")))
            oldest = min(
                (f.stat().st_mtime for f in self._cache_dir.glob("**/*") if f.is_file()),
                default=time.time()
            )
            oldest_message = datetime.datetime.fromtimestamp(oldest).strftime("%Y-%m-%d %H:%M:%S")
            return dirsize, messages_count, oldest_message
        except Exception as e:
            logger.error(f"Stats error: {e}")
            return "0B", 0, "n/a"

    def gc(self, max_age: int, max_size: int) -> None:
        try:
            current_time = time.time()
            for _file in self._cache_dir.glob("**/*"):
                if _file.is_file() and _file.stat().st_mtime < current_time - max_age:
                    _file.unlink()

            while get_size(self._cache_dir) > max_size:
                oldest = min(
                    self._cache_dir.glob("**/*"),
                    key=lambda x: x.stat().st_mtime,
                    default=None
                )
                if oldest:
                    oldest.unlink()
                else:
                    break
        except Exception as e:
            logger.error(f"GC error: {e}")

    async def store_message(
        self,
        message: Message,
        no_repeat: bool = False,
    ) -> typing.Union[bool, typing.Dict[str, typing.Any]]:
        try:
            if not hasattr(message, "id"):
                return False

            chat_id = utils.get_chat_id(message)
            _dir = self._cache_dir.joinpath(str(chat_id))
            _dir.mkdir(parents=True, exist_ok=True)
            _file = _dir.joinpath(str(message.id))

            sender = None
            try:
                if message.sender_id is not None:
                    try:
                        sender = await self._client.get_entity(message.sender_id, exp=0)
                    except Exception:
                        sender = await message.get_sender()

                try:
                    chat = await self._client.get_entity(chat_id, exp=0)
                except Exception:
                    chat = await message.get_chat()

                if message.sender_id is None:
                    sender = chat
            except ValueError:
                if no_repeat:
                    return False
                await asyncio.sleep(5)
                return await self.store_message(message, True)

            is_chat = message.is_group or message.is_channel
            text = getattr(message, "text", getattr(message, "raw_text", ""))

            message_data = {
                "url": await utils.get_message_link(message),
                "text": text,
                "sender_id": sender.id if sender else None,
                "sender_bot": bool(getattr(sender, "bot", False)),
                "sender_name": utils.escape_html(get_display_name(sender)),
                "sender_url": utils.get_entity_url(sender),
                "chat_id": chat.id,
                "is_chat": is_chat,
                "via_bot_id": bool(message.via_bot_id),
                "assets": await self._extract_assets(message),
            }

            if is_chat:
                message_data.update({
                    "chat_name": utils.escape_html(get_display_name(chat)),
                    "chat_url": utils.get_entity_url(chat),
                })

            if hasattr(message, "to_dict"):
                try:
                    raw_msg = message.to_dict()
                    for k, v in raw_msg.items():
                        if isinstance(v, datetime.datetime):
                            raw_msg[k] = v.isoformat()
                    message_data["raw_message"] = raw_msg
                except Exception:
                    pass

            _file.write_bytes(zlib.compress(json.dumps(message_data, default=str).encode("utf-8")))
            return message_data
        except Exception as e:
            logger.error(f"Store message error: {e}")
            return False

    async def fetch_message(
        self,
        chat_id: typing.Optional[int],
        message_id: int,
    ) -> typing.Optional[dict]:
        try:
            if chat_id:
                _file = self._cache_dir.joinpath(str(chat_id), str(message_id))
                if _file.exists():
                    data = json.loads(zlib.decompress(_file.read_bytes()).decode("utf-8"))
                    data["chat_id"] = data.get("chat_id", chat_id)
                    return data
            else:
                for _dir in self._cache_dir.iterdir():
                    _file = _dir.joinpath(str(message_id))
                    if _file.exists():
                        data = json.loads(zlib.decompress(_file.read_bytes()).decode("utf-8"))
                        data["chat_id"] = data.get("chat_id", int(_dir.name))
                        return data
        except Exception as e:
            logger.error(f"Fetch message error: {e}")
        return None

    async def _extract_assets(self, message: Message) -> typing.Dict[str, dict]:
        assets = {}
        for attr in ["photo", "audio", "document", "sticker", "video", "voice", "video_note", "gif"]:
            media = getattr(message, attr, None)
            if media:
                try:
                    asset_data = {
                        "id": media.id,
                        "access_hash": media.access_hash,
                        "file_reference": bytearray(media.file_reference).hex(),
                    }

                    if hasattr(media, "sizes") and media.sizes:
                        asset_data["thumb_size"] = media.sizes[-1].type

                    if hasattr(media, "attributes"):
                        attributes = []
                        for attr_obj in media.attributes:
                            if hasattr(attr_obj, "file_name"):
                                asset_data["file_name"] = attr_obj.file_name
                            elif hasattr(attr_obj, "duration"):
                                asset_data["duration"] = attr_obj.duration
                            elif hasattr(attr_obj, "width") and hasattr(attr_obj, "height"):
                                asset_data["width"] = attr_obj.width
                                asset_data["height"] = attr_obj.height

                    assets[attr] = asset_data
                except Exception as e:
                    logger.error(f"Failed to extract {attr}: {e}")
        return assets

@loader.tds
class NekoSpy(loader.Module):
    """Сохраняет удаленные/измененные сообщения"""

    strings = {
        "name": "NekoSpy",
        "state": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Режим слежения теперь {}</b>",
        "spybl": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Текущий чат добавлен в черный список для слежения</b>",
        "spybl_removed": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Текущий чат удален из черного списка для слежения</b>",
        "spybl_clear": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Черный список для слежения очищен</b>",
        "spywl": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Текущий чат добавлен в белый список для слежения</b>",
        "spywl_removed": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Текущий чат удален из белого списка для слежения</b>",
        "spywl_clear": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Белый список для слежения очищен</b>",
        "whitelist": "\n<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Слежу только за сообщениями от:</b>\n{}",
        "always_track": "\n<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Всегда слежу за сообщениями от:</b>\n{}",
        "blacklist": "\n<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Игнорирую сообщения от:</b>\n{}",
        "chat": "<emoji document_id=6037355667365300960>👥</emoji> <b>Слежу за сообщениями в группах</b>\n",
        "pm": "<emoji document_id=6048540195995782913>👤</emoji> <b>Слежу за сообщениями в личных сообщениях</b>\n",
        "deleted_pm": '<b><a href="{}">{}</a>{} удалил(а) сообщение:</b>\n\n<blockquote>{}</blockquote>',
        "deleted_chat": '<b><a href="{}">{}</a>{} удалил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n<blockquote>{}</blockquote>',
        "edited_pm": '<b><a href="{}">{}</a>{} изменил(а) сообщение:</b>\n\n<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n<b>Новое:</b>\n<blockquote><a href="{message_url}">{}</a></blockquote>',
        "edited_chat": '<b><a href="{}">{}</a>{} изменил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n<b>Новое:</b>\n<blockquote><a href="{message_url}">{}</a></blockquote>',
        "mode_off": "<emoji document_id=6048540195995782913>👤</emoji> <b>Не отслеживаю сообщения </b><code>{}spymode</code>\n",
        "cfg_enable_pm": "Включить режим шпиона в личных сообщениях",
        "cfg_enable_groups": "Включить режим шпиона в группах",
        "cfg_whitelist": "Список чатов, от которых нужно сохранять сообщения",
        "cfg_blacklist": "Список чатов, от которых нужно игнорировать сообщения",
        "cfg_always_track": "Список чатов, от которых всегда следует отслеживать сообщения",
        "cfg_log_edits": "Сохранять отредактированные сообщения",
        "cfg_ignore_inline": "Игнорировать сообщения из инлайн-режима",
        "cfg_fw_protect": "Защита от флудвейтов при пересылке",
        "sd_media": "🔥 <b><a href='tg://user?id={}'>{}</a> отправил вам самоуничтожающееся медиа</b>",
        "save_sd": "<emoji document_id=5420315771991497307>🔥</emoji> <b>Сохраняю самоуничтожающиеся медиа</b>\n",
        "cfg_save_sd": "Сохранять самоуничтожающееся медиа",
        "spyall": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Режим слежения в личных чатах теперь {}</b>",
        "stats": "<b>Статистика кэша:</b>\n<b>Размер:</b> {}\n<b>Сообщений:</b> {}\n<b>Самое старое:</b> {}",
        "purged_cache": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Кэш сообщений очищен</b>",
        "saved": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Сообщения сохранены</b>",
        "invalid_time": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Указано неверное время</b>",
        "restoring": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Восстанавливаю сообщения...</b>",
        "restored": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Сообщения восстановлены</b>",
        "on": "включен",
        "off": "выключен",
        "ignore_channels": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Игнорирование каналов теперь {}</b>",
        "cfg_ignore_channels": "Игнорировать сообщения из каналов",
        "channel_create_failed": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Не удалось создать канал для логов!</b>",
    }

    def __init__(self):
        self._channel = None
        self._tl_channel = None
        self._queue = []
        self._next = 0
        self._ignore_cache = []
        self._cacher = None
        self.METHOD_MAP = None
        self._recent = []

        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "enable_pm",
                True,
                lambda: self.strings("cfg_enable_pm"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "enable_groups",
                False,
                lambda: self.strings("cfg_enable_groups"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "whitelist",
                [],
                lambda: self.strings("cfg_whitelist"),
                validator=loader.validators.Series(),
            ),
            loader.ConfigValue(
                "blacklist",
                [],
                lambda: self.strings("cfg_blacklist"),
                validator=loader.validators.Series(),
            ),
            loader.ConfigValue(
                "always_track",
                [],
                lambda: self.strings("cfg_always_track"),
                validator=loader.validators.Series(),
            ),
            loader.ConfigValue(
                "log_edits",
                True,
                lambda: self.strings("cfg_log_edits"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "ignore_inline",
                True,
                lambda: self.strings("cfg_ignore_inline"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "fw_protect",
                3.0,
                lambda: self.strings("cfg_fw_protect"),
                validator=loader.validators.Float(minimum=0.0),
            ),
            loader.ConfigValue(
                "save_sd",
                True,
                lambda: self.strings("cfg_save_sd"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "max_cache_size",
                1024 * 1024 * 1024,
                lambda: "Максимальный размер кэша",
                validator=loader.validators.Integer(minimum=0),
            ),
            loader.ConfigValue(
                "max_cache_age",
                7 * 24 * 60 * 60,
                lambda: "Максимальное время хранения в кэше",
                validator=loader.validators.Integer(minimum=0),
            ),
            loader.ConfigValue(
                "recent_maximum",
                60 * 60,
                lambda: "Максимальное время хранения недавних сообщений",
                validator=loader.validators.Integer(minimum=0),
            ),
            loader.ConfigValue(
                "nocache_big_chats",
                True,
                lambda: "Не кэшировать большие чаты",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "nocache_chats",
                [],
                lambda: "Чаты, которые не нужно кэшировать",
                validator=loader.validators.Series(),
            ),
            loader.ConfigValue(
                "ecospace_mode",
                False,
                lambda: "Режим экономии места",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "very_important",
                [],
                "Очень важные чаты",
                validator=loader.validators.Series(),
            ),
            loader.ConfigValue(
                "ignore_channels",
                False,
                lambda: self.strings("cfg_ignore_channels"),
                validator=loader.validators.Boolean(),
            ),
                loader.ConfigValue(
                "spyall",
                False,
                lambda: "Отслеживать все личные сообщения",
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

        try:
            channel, _ = await utils.asset_channel(
                self._client,
                "hisa-nekospy",
                "Deleted and edited messages will appear here",
                silent=True,
                invite_bot=True,
                avatar="https://pm1.narvii.com/6733/0e0380ca5cd7595de53f48c0ce541d3e2f2effc4v2_hq.jpg",
                _folder="hisa",
            )

            self._channel = int(f"-100{channel.id}")
            self._tl_channel = channel.id
            logger.debug(f"Log channel created: {self._channel}")

            self._cacher = CacheManagerDisc(self._client, self._db)

            self.METHOD_MAP = {
                "photo": self.inline.bot.send_photo,
                "video": self.inline.bot.send_video,
                "voice": self.inline.bot.send_voice,
                "document": self.inline.bot.send_document,
                "sticker": self.inline.bot.send_sticker,
            }

            self._recent = []

            self._gc.start()
            
        except Exception as e:
            logger.error(f"Failed to initialize NekoSpy: {e}")
            await self._client.send_message(
                "me",
                self.strings("channel_create_failed") + f"\nError: {str(e)}"
            )

    @loader.loop(interval=3600)
    async def _gc(self):
        if self._cacher:
            try:
                self._cacher.gc(self.config["max_cache_age"], self.config["max_cache_size"])
                current_time = time.time()
                self._recent = [
                    item for item in self._recent 
                    if item.timestamp + self.config["recent_maximum"] >= current_time
                ]
            except Exception as e:
                logger.error(f"GC error: {e}")

    @loader.loop(interval=0.1, autostart=True)
    async def _sender(self):
        if not self._queue or self._next > time.time():
            return

        try:
            task = self._queue.pop(0)
            try:
                if asyncio.iscoroutine(task):
                    await task
                elif callable(task):
                    task()
            except Exception as e:
                logger.error(f"Failed to process task: {e}")
        except Exception as e:
            logger.error(f"Sender error: {e}")
        finally:
            self._next = time.time() + self.config["fw_protect"]

    async def _send_text(self, caption: str):
        future = asyncio.Future()

        async def _send():
            try:
                msg = await self.inline.bot.send_message(
                    self._channel,
                    caption,
                    disable_web_page_preview=True,
                )
                future.set_result(msg)
            except Exception as e:
                future.set_exception(e)

        self._queue.append(_send())
        return await future

    async def _notify(self, msg_obj: dict, caption: str):
        try:
            caption = self.inline.sanitise_text(caption)

            for username in set(
                [username.username for username in (self._client.hisa_me.usernames or [])]
                + [self._client.hisa_me.username]
            ):
                caption = caption.replace(f"@{username}", f"@{username}")

            assets = msg_obj.get("assets", {})
            file = next((x for x in assets.values() if x), None)

            if not file:
                await self._send_text(caption)
                return

            if assets.get("sticker"):
                try:
                    msg = await self._send_text(caption + "\n&lt;sticker&gt;")
                    await self._send_sticker(file, reply_to=msg.message_id)
                except Exception as e:
                    logger.error(f"Failed to send sticker notification: {e}")
                    await self._send_text(caption + "\n&lt;sticker (failed to restore)&gt;")
                return

            await self._send_media(file, assets, caption)
        except Exception as e:
            logger.error(f"Notify error: {e}")

    async def _send_sticker(self, file: dict, caption: str = None, reply_to: int = None):
        try:
            file["file_reference"] = bytes.fromhex(file["file_reference"])
            file["thumb_size"] = file.get("thumb_size", "")

            file_data = await self._client.download_file(
                InputDocumentFileLocation(
                    id=file["id"],
                    access_hash=file["access_hash"],
                    file_reference=file["file_reference"],
                    thumb_size=file["thumb_size"],
                ),
                bytes,
            )

            if not file_data:
                raise ValueError("Empty file data")

            ext = mimetypes.guess_extension(magic.from_buffer(file_data, mime=True)) or ".bin"
            if ext == ".gz":
                ext = ".tgs"

            file_io = io.BytesIO(file_data)
            file_io.name = f"sticker{ext}"

            if ext in [".webm", ".tgs"]:
                return await self.inline.bot.send_video(
                    self._channel, 
                    file_io,
                    caption=caption,
                    reply_to_message_id=reply_to,
                )
            else:
                return await self.inline.bot.send_sticker(
                    self._channel,
                    file_io,
                    reply_to_message_id=reply_to,
                )
        except Exception as e:
            logger.error(f"Failed to send sticker: {e}")
            if caption:
                await self._send_text(caption + "\n&lt;sticker (failed to restore)&gt;")

    async def _send_media(self, file: dict, assets: dict, caption: str):
        try:
            file["file_reference"] = bytes.fromhex(file["file_reference"])
            file["thumb_size"] = file.get("thumb_size", "")

            file_data = await self._client.download_file(
                InputDocumentFileLocation(
                    id=file["id"],
                    access_hash=file["access_hash"],
                    file_reference=file["file_reference"],
                    thumb_size=file["thumb_size"],
                ),
                bytes,
            )

            if not file_data:
                raise ValueError("Empty file data")

            mime = magic.from_buffer(file_data, mime=True)
            ext = mimetypes.guess_extension(mime) or ".bin"
            file_io = io.BytesIO(file_data)

            if assets.get("document"):
                filename = assets["document"].get("file_name", f"document{ext}")
                file_io.name = filename
            else:
                file_io.name = f"media{ext}"

            if assets.get("photo"):
                await self.inline.bot.send_photo(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif assets.get("video"):
                await self.inline.bot.send_video(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif assets.get("voice"):
                await self.inline.bot.send_voice(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif assets.get("document"):
                await self.inline.bot.send_document(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
        except Exception as e:
            logger.error(f"Failed to send media: {e}")
            await self._send_text(caption + "\n&lt;media (failed to restore)&gt;")

    @loader.command()
    async def spymode(self, message: Message):
        """Toggle spymode"""
        new_state = not self.get("state", False)
        self.set("state", new_state)
        await utils.answer(
            message,
            self.strings("state").format(
                self.strings("on" if new_state else "off")
            ),
        )

    @loader.command()
    async def spybl(self, message: Message):
        """Add/remove chat from blacklist"""
        chat = utils.get_chat_id(message)
        if chat in self.blacklist:
            self.blacklist = list(set(self.blacklist) - {chat})
            await utils.answer(message, self.strings("spybl_removed"))
        else:
            self.blacklist = list(set(self.blacklist) | {chat})
            await utils.answer(message, self.strings("spybl"))

    @loader.command()
    async def spyblclear(self, message: Message):
        """Clear blacklist"""
        self.blacklist = []
        await utils.answer(message, self.strings("spybl_clear"))

    @loader.command()
    async def spywl(self, message: Message):
        """Add/remove chat from whitelist"""
        chat = utils.get_chat_id(message)
        if chat in self.whitelist:
            self.whitelist = list(set(self.whitelist) - {chat})
            await utils.answer(message, self.strings("spywl_removed"))
        else:
            self.whitelist = list(set(self.whitelist) | {chat})
            await utils.answer(message, self.strings("spywl"))

    @loader.command()
    async def spywlclear(self, message: Message):
        """Clear whitelist"""
        self.whitelist = []
        await utils.answer(message, self.strings("spywl_clear"))

    @loader.command()
    async def spyall(self, message: Message):
        """Toggle spyall mode (track all PMs)"""
        new_state = not self.config["spyall"]
        self.config["spyall"] = new_state
        await utils.answer(
            message,
            self.strings("spyall").format(
                self.strings("on" if new_state else "off")
            ),
        )

    @loader.command()
    async def spych(self, message: Message):
        """Toggle channels ignore mode"""
        self.config["ignore_channels"] = not self.config["ignore_channels"]
        await utils.answer(
            message,
            self.strings("ignore_channels").format(
                self.strings("on" if self.config["ignore_channels"] else "off")
            ),
        )

    async def _get_entities_list(self, entities: list) -> str:
        result = []
        for x in entities:
            try:
                try:
                    entity = await self._client.get_entity(x, exp=0)
                    name = utils.escape_html(get_display_name(entity))
                    url = utils.get_entity_url(entity)
                except Exception:
                    name = f"Unknown ({x})"
                    url = f"tg://user?id={x}"

                result.append(
                    "\u0020\u2800\u0020\u2800<emoji document_id=4971987363145188045>▫️</emoji> "
                    f"<b><a href='{url}'>{name}</a></b>"
                )
            except Exception as e:
                logger.error(f"Failed to get entity {x}: {e}")
        return "\n".join(result)

    @loader.command()
    async def spyinfo(self, message: Message):
        """Show current spy mode configuration"""
        if not self.get("state"):
            await utils.answer(
                message,
                self.strings("mode_off").format(self.get_prefix())
            )
            return

        info = ""

        if self.config["save_sd"]:
            info += self.strings("save_sd")

        if self.config["enable_groups"]:
            info += self.strings("chat")

        if self.config["enable_pm"]:
            info += self.strings("pm")

        if self.config["spyall"]:
            info += self.strings("spyall").format(self.strings("on" if self.config["spyall"] else "off")) + "\n"

        if self.whitelist:
            info += self.strings("whitelist").format(
                await self._get_entities_list(self.whitelist)
            )

        if self.config["blacklist"]:
            info += self.strings("blacklist").format(
                await self._get_entities_list(self.config["blacklist"])
            )

        if self.always_track:
            info += self.strings("always_track").format(
                await self._get_entities_list(self.always_track)
            )

        await utils.answer(message, info)

    @loader.command()
    async def stat(self, message: Message):
        """Show cache stats"""
        if not self._cacher:
            await utils.answer(message, "Cache not initialized")
            return
            
        dirsize, messages_count, oldest_message = self._cacher.stats()
        await utils.answer(
            message,
            self.strings("stats").format(
                dirsize,
                messages_count,
                oldest_message,
            ),
        )

    @loader.command()
    async def purgecache(self, message: Message):
        """Purge message cache"""
        if not self._cacher:
            await utils.answer(message, "Cache not initialized")
            return

        self._cacher.purge()
        self._recent = []
        await utils.answer(message, self.strings("purged_cache"))

    @loader.command()
    async def nssave(self, message: Message):
        """Save replied message to channel"""
        async def _save(_reply: Message):
            msg_obj = await self._cacher.store_message(_reply)
            if not msg_obj:
                return

            sender = await self._client.get_entity(msg_obj["sender_id"], exp=0)
            username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""

            if msg_obj.get("is_chat"):
                await self._notify(
                    msg_obj,
                    self.strings("deleted_chat").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["chat_url"],
                        msg_obj["chat_name"],
                        msg_obj["text"],
                    ),
                )
            else:
                await self._notify(
                    msg_obj,
                    self.strings("deleted_pm").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["text"],
                    ),
                )

        if reply := await message.get_reply_message():
            await _save(reply)

        args = utils.get_args_raw(message)
        links = re.findall(r"(https://t.me[^\s]+)", args)

        for link in links:
            peer, msg = link.split("/")[-2:]
            msg = int(msg)
            if re.match(r"https://t.me/c/\d+/\d+", link):
                peer = int(peer)

            try:
                msg = (await self.client.get_messages(peer, ids=[msg]))[0]
                if not msg:
                    raise RuntimeError
                await _save(msg)
            except Exception as e:
                logger.error(f"Can't save message from link {link}: {e}")

        await utils.answer(message, self.strings("saved"))

    @loader.command()
    async def rest(self, message: Message):
        """Restore messages from time period"""
        args = utils.get_args_raw(message) or "5m"

        if "-current" in args:
            args = args.replace("-current", "").strip()
            from_chat = utils.get_chat_id(message)
        else:
            from_chat = None

        if args[-1].isdigit():
            args += "s"

        if args[-1] == "m":
            args = int(args[:-1]) * 60
        elif args[-1] == "s":
            args = int(args[:-1])
        elif args[-1] == "h":
            args = int(args[:-1]) * 60 * 60
        else:
            await utils.answer(message, self.strings("invalid_time"))
            return

        if args < 1:
            await utils.answer(message, self.strings("invalid_time"))
            return

        message = await utils.answer(message, self.strings("restoring"))

        restored = 0
        for recent in self._recent:
            if time.time() - recent.timestamp > args:
                continue

            if not (msg_obj := await self._cacher.fetch_message(recent.chat_id, recent.message_id)):
                continue

            if from_chat and msg_obj.get("chat_id") != from_chat:
                continue

            sender = await self._client.get_entity(msg_obj["sender_id"], exp=0)
            username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""

            if msg_obj.get("is_chat"):
                await self._notify(
                    msg_obj,
                    self.strings(
                        "deleted_chat" if recent.action == "del" else "edited_chat"
                    ).format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["chat_url"],
                        msg_obj["chat_name"],
                        msg_obj["text"],
                        msg_obj["text"] if recent.action == "del" else "",
                        message_url=msg_obj["url"],
                    ),
                )
            else:
                await self._notify(
                    msg_obj,
                    self.strings(
                        "deleted_pm" if recent.action == "del" else "edited_pm"
                    ).format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["text"],
                        msg_obj["text"] if recent.action == "del" else "",
                        message_url=msg_obj["url"],
                    ),
                )
            restored += 1
            await asyncio.sleep(0.5)

        await utils.answer(
            message,
            self.strings("restored") + f"\n<b>Восстановлено сообщений:</b> {restored}"
        )

    @loader.raw_handler(UpdateEditMessage)
    async def pm_edit_handler(self, update: UpdateEditMessage):
        if (
            not self.get("state", False)
            or update.message.out
            or (self.config["ignore_inline"] and update.message.via_bot_id)
        ):
            return

        self._recent.append(RecentsItem.from_edit(update.message))
        msg_obj = await self._cacher.fetch_message(
            utils.get_chat_id(update.message), update.message.id
        )

        if not msg_obj:
            await self._cacher.store_message(update.message)
            return

        sender_id = int(msg_obj["sender_id"])
        chat_id = int(msg_obj["chat_id"])
        is_chat = msg_obj["is_chat"]

        if (
            (
                sender_id in self.always_track
                or chat_id in self.always_track
                or (
                    self.config["log_edits"]
                    and self._should_capture(sender_id, chat_id)
                )
            )
            and (
                ((self.config["enable_pm"] or self._spyall) and not is_chat)
                or (self.config["enable_groups"] and is_chat)
            )
            and update.message.raw_text != utils.remove_html(msg_obj["text"])
            and not msg_obj["sender_bot"]
        ):
            sender = await self._client.get_entity(sender_id, exp=0)
            username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""

            await self._notify(
                msg_obj,
                (
                    self.strings("edited_chat").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["chat_url"],
                        msg_obj["chat_name"],
                        msg_obj["text"],
                        update.message.text,
                        message_url=msg_obj["url"],
                    )
                    if is_chat
                    else self.strings("edited_pm").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["text"],
                        update.message.text,
                        message_url=msg_obj["url"],
                    )
                ),
            )

        await self._cacher.store_message(update.message)

    @loader.raw_handler(UpdateDeleteMessages)
    async def pm_delete_handler(self, update: UpdateDeleteMessages):
        if not self.get("state", False):
            return

        for message in update.messages:
            self._recent.append(RecentsItem.from_delete(message))
            msg_obj = await self._cacher.fetch_message(None, message)

            if not msg_obj:
                continue

            sender_id, chat_id, is_chat = (
                int(msg_obj["sender_id"]),
                int(msg_obj["chat_id"]),
                msg_obj["is_chat"],
            )

            if ((sender_id in self.always_track or chat_id in self.always_track or
                (self._should_track_pm(sender_id) or self._should_capture(sender_id, chat_id))) and
                not (self.config["ignore_inline"] and msg_obj["via_bot_id"]) and
                ((self.config["enable_pm"] or self._spyall) and not is_chat or
                 self.config["enable_groups"] and is_chat) and
                not msg_obj["sender_bot"]):

                sender = await self._client.get_entity(sender_id, exp=0)
                username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""

                await self._notify(
                    msg_obj,
                    (self.strings("deleted_chat").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["chat_url"],
                        msg_obj["chat_name"],
                        msg_obj["text"],
                    ) if is_chat else self.strings("deleted_pm").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["text"],
                    )),
                )

    @loader.raw_handler(UpdateDeleteChannelMessages)
    async def channel_delete_handler(self, update: UpdateDeleteChannelMessages):
        if self.config["ignore_channels"] or not self.get("state", False):
            return

        for message in update.messages:
            self._recent.append(RecentsItem.from_delete(message, update.channel_id))
            msg_obj = await self._cacher.fetch_message(update.channel_id, message)

            if not msg_obj:
                continue

            sender_id, chat_id = (
                int(msg_obj["sender_id"]),
                int(msg_obj["chat_id"]),
            )

            if (self._is_always_track(sender_id, chat_id) or
                (self.config["enable_groups"] and
                 self._should_capture(sender_id, chat_id) and
                 not (self.config["ignore_inline"] and msg_obj["via_bot_id"]) and
                 not msg_obj["sender_bot"])):

                sender = await self._client.get_entity(sender_id, exp=0)
                username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""

                await self._notify(
                    msg_obj,
                    self.strings("deleted_chat").format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["chat_url"],
                        msg_obj["chat_name"],
                        msg_obj["text"],
                    ),
                )

    @loader.watcher("in", only_messages=True)
    async def watcher(self, message: Message):
        try:
            if not hasattr(message, "sender_id"):
                return

            chat_id = utils.get_chat_id(message)
            if chat_id in self._ignore_cache:
                return

            if (self.config["save_sd"] and
                getattr(message, "media", None) and
                getattr(message.media, "ttl_seconds", None) and
                (self.config["spyall"] or
                 self._should_capture(message.sender_id, chat_id) or
                 message.sender_id in self.always_track or
                 chat_id in self.always_track)):

                try:
                    try:
                        sender = await self.client.get_entity(message.sender_id)
                        sender_name = utils.escape_html(get_display_name(sender))
                        sender_url = utils.get_entity_url(sender)
                    except Exception:
                        sender_name = "Unknown user"
                        sender_url = f"{message.sender_id}"

                    media = io.BytesIO(await self.client.download_media(message.media, bytes))
                    media.name = "sd.jpg" if message.photo else "sd.mp4"

                    caption = self.strings("sd_media").format(
                        sender_url,
                        sender_name,
                    )

                    if message.photo:
                        await self.inline.bot.send_photo(
                            self._channel,
                            media,
                            caption=caption,
                        )
                    else:
                        await self.inline.bot.send_video(
                            self._channel,
                            media,
                            caption=caption,
                        )
                except Exception as e:
                    logger.error(f"Failed to save self-destructing media: {e}")
                    await self._send_text(
                        f"🔥 <b>Не удалось сохранить самоуничтожающееся медиа от {sender_name}</b>\n"
                        f"Ошибка: {str(e)}"
                    )

            for chat in self.config["nocache_chats"]:
                try:
                    if (await self._client.get_entity(chat, exp=0)).id == chat_id:
                        self._ignore_cache.append(chat_id)
                        return
                except Exception:
                    continue

            if (message.is_group and 
                self.config["nocache_big_chats"] and 
                (await self._client.get_participants(chat_id, limit=1)).total > 500):
                self._ignore_cache.append(chat_id)
                return

            msg_obj = await self._cacher.store_message(message)
            if not msg_obj:
                return

            for chat in self.very_important:
                try:
                    if (message.sender_id in self.very_important or
                        (await self._client.get_entity(chat, exp=0)).id == chat_id):

                        sender = await self._client.get_entity(message.sender_id, exp=0)
                        username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""

                        if msg_obj.get("is_chat"):
                            await self._notify(
                                msg_obj,
                                self.strings("deleted_chat").format(
                                    msg_obj["sender_url"],
                                    msg_obj["sender_name"],
                                    username,
                                    msg_obj["chat_url"],
                                    msg_obj["chat_name"],
                                    msg_obj["text"],
                                ),
                            )
                        else:
                            await self._notify(
                                msg_obj,
                                self.strings("deleted_pm").format(
                                    msg_obj["sender_url"],
                                    msg_obj["sender_name"],
                                    username,
                                    msg_obj["text"],
                                ),
                            )
                        break
                except Exception:
                    continue
        except Exception as e:
            logger.error(f"Watcher error: {e}")

    def _should_capture(self, user_id: int, chat_id: int) -> bool:
        return (
            chat_id not in self.blacklist
            and user_id not in self.blacklist
            and (
                not self.whitelist
                or chat_id in self.whitelist
                or user_id in self.whitelist
            )
        )

    def _should_track_pm(self, user_id: int) -> bool:
        return (
            (self.config["spyall"] or user_id in self.always_track)
            and user_id not in self.blacklist
            and not self.config["ignore_inline"]
        )

    def _is_always_track(self, user_id: int, chat_id: int) -> bool:
        return chat_id in self.always_track or user_id in self.always_track

    @property
    def blacklist(self):
        return list(
            set(
                int(x) if str(x).isdigit() else x
                for x in self.config["blacklist"]
                + [777000, self._client.tg_id, self._tl_channel, self.inline.bot_id]
            )
        )

    @blacklist.setter
    def blacklist(self, value: list):
        self.config["blacklist"] = list(
            set(value)
            - {777000, self._client.tg_id, self._tl_channel, self.inline.bot_id}
        )

    @property
    def whitelist(self):
        return [int(x) if str(x).isdigit() else x for x in self.config["whitelist"]]

    @whitelist.setter
    def whitelist(self, value: list):
        self.config["whitelist"] = value

    @property
    def always_track(self):
        return [int(x) if str(x).isdigit() else x for x in self.config["always_track"]]

    @property
    def very_important(self):
        return [int(x) if str(x).isdigit() else x for x in self.config["very_important"]]