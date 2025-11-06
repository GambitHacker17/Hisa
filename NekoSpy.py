# meta developer: @MartyyyK
# requires: python-magic libmagic

import subprocess

try:
    import magic
except ImportError:
    try:
        subprocess.run(["pkg", "install", "-y", "file", "libmagic"], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка: {e}")
    except FileNotFoundError:
        logger.error(f"pkg не найден")
    try:
        subprocess.check_call(["pip", "install", "python-magic"])
        import magic
    except:
        logger.error(f"Ошибка установки python-magic")

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
import re
import datetime
from pathlib import Path
from abc import ABC, abstractmethod
from collections import defaultdict

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
    DocumentAttributeSticker,
    DocumentAttributeVideo,
    DocumentAttributeAudio,
    User
)
from telethon.utils import get_display_name
from telethon import events
from telethon.errors import FileReferenceExpiredError

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
        self._media_dir = self._cache_dir.joinpath("media")
        self._media_dir.mkdir(parents=True, exist_ok=True)

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

            media_path = None
            if message.media and not message.web_preview:
                try:
                    media_data = await self._client.download_media(message, bytes)
                    if media_data:
                        media_ext = await self._get_media_extension(message)
                        media_filename = f"{chat_id}_{message.id}_{int(time.time())}{media_ext}"
                        media_path = self._media_dir.joinpath(media_filename)
                        media_path.write_bytes(media_data)
                except Exception as e:
                    logger.error(f"Failed to download media: {e}")

            if isinstance(sender, User):
                sender_url = f"tg://user?id={sender.id}"
            else:
                sender_url = utils.get_entity_url(sender)

            message_data = {
                "url": await utils.get_message_link(message),
                "text": text,
                "sender_id": sender.id if sender else None,
                "sender_bot": bool(getattr(sender, "bot", False)),
                "sender_name": utils.escape_html(get_display_name(sender)),
                "sender_url": sender_url,
                "chat_id": chat.id,
                "is_chat": is_chat,
                "via_bot_id": bool(message.via_bot_id),
                "assets": await self._extract_assets(message),
                "media_type": await self._get_media_type(message),
                "message_id": message.id,
                "media_path": str(media_path) if media_path else None,
            }

            if is_chat:
                message_data.update({
                    "chat_name": utils.escape_html(get_display_name(chat)) if chat else "Unknown Chat",
                    "chat_url": utils.get_entity_url(chat) if chat else "",
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

    async def _get_media_extension(self, message: Message) -> str:
        if message.photo:
            return ".jpg"
        elif message.video:
            return ".mp4"
        elif message.voice:
            return ".ogg"
        elif message.video_note:
            return ".mp4"
        elif message.sticker:
            if hasattr(message.sticker, 'mime_type'):
                if message.sticker.mime_type == "application/x-tgsticker":
                    return ".tgs"
                elif message.sticker.mime_type == "video/webm":
                    return ".webm"
            return ".webp"
        elif message.gif:
            return ".mp4"
        elif message.document:
            if hasattr(message.document, 'attributes'):
                for attr in message.document.attributes:
                    if isinstance(attr, DocumentAttributeFilename) and hasattr(attr, 'file_name'):
                        return os.path.splitext(attr.file_name)[1]
            return ".bin"
        elif message.audio:
            return ".mp3"
        else:
            return ".bin"

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
        media_attrs = ["photo", "audio", "document", "sticker", "video", "voice", "video_note", "gif"]

        for attr in media_attrs:
            media = getattr(message, attr, None)
            if media:
                try:
                    try:
                        await self._client.get_messages(message.peer_id, ids=message.id)
                        media = getattr(message, attr, None)
                    except:
                        pass

                    asset_data = {
                        "id": media.id,
                        "access_hash": media.access_hash,
                        "file_reference": bytearray(media.file_reference).hex() if media.file_reference else "",
                    }

                    if hasattr(media, "sizes") and media.sizes:
                        asset_data["thumb_size"] = media.sizes[-1].type

                    if hasattr(media, "attributes"):
                        attributes = []
                        for attr_obj in media.attributes:
                            if hasattr(attr_obj, 'file_name'):
                                asset_data["file_name"] = attr_obj.file_name
                            elif hasattr(attr_obj, 'duration'):
                                asset_data["duration"] = attr_obj.duration
                            elif hasattr(attr_obj, 'width') and hasattr(attr_obj, 'height'):
                                asset_data["width"] = attr_obj.width
                                asset_data["height"] = attr_obj.height

                    assets[attr] = asset_data
                except Exception as e:
                    logger.error(f"Failed to extract {attr}: {e}")
        return assets

    async def _get_media_type(self, message: Message) -> str:
        if message.photo:
            return "photo"
        elif message.video:
            if hasattr(message.video, 'attributes'):
                for attr in message.video.attributes:
                    if isinstance(attr, DocumentAttributeVideo) and hasattr(attr, 'round_message') and attr.round_message:
                        return "video_note"
            return "video"
        elif message.voice:
            return "voice"
        elif message.video_note:
            return "video_note"
        elif message.sticker:
            if hasattr(message.sticker, 'mime_type'):
                if message.sticker.mime_type in ["application/x-tgsticker", "video/webm"]:
                    return "animated_sticker"
            return "sticker"
        elif message.gif:
            return "gif"
        elif message.document:
            if hasattr(message.document, 'attributes'):
                for attr in message.document.attributes:
                    if isinstance(attr, DocumentAttributeSticker):
                        if hasattr(message.document, 'mime_type') and message.document.mime_type in ["application/x-tgsticker", "video/webm"]:
                            return "animated_sticker"
                        return "sticker"
                    elif isinstance(attr, DocumentAttributeVideo):
                        if hasattr(attr, 'round_message') and attr.round_message:
                            return "video_note"
                        return "video"
                    elif isinstance(attr, DocumentAttributeAudio):
                        if hasattr(attr, 'voice') and attr.voice:
                            return "voice"
                        return "audio"
            return "document"
        elif message.audio:
            return "audio"
        else:
            return "text"

    def _get_plural_form(self, n: int) -> str:
        if n % 10 == 1 and n % 100 != 11:
            return "сообщение"
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            return "сообщения"
        else:
            return "сообщений"

@loader.tds
class NekoSpy(loader.Module):
    """Сохраняет удаленные/измененные сообщения"""

    rei = "<emoji document_id=5409143295039252230>👩‍🎤</emoji>"
    groups = "<emoji document_id=6037355667365300960>👥</emoji>"
    pm = "<emoji document_id=6048540195995782913>👤</emoji>"

    strings = {
        "name": "NekoSpy",
        "state": f"{rei} <b>Spy mode is now {{}}</b>",
        "nswl": f"{rei} <b>Current chat added to whitelist for spying</b>",
        "nswl_removed": f"{rei} <b>Current chat removed from whitelist for spying</b>",
        "nswl_clear": f"{rei} <b>Include list for spying cleared</b>",
        "whitelist": f"\n{rei} <b>Tracking only messages from:</b>\n{{}}",
        "always_track": f"\n{rei} <b>Always tracking messages from:</b>\n{{}}",
        "chat": f"{groups} <b>Tracking messages in groups</b>\n",
        "pm": f"{pm} <b>Tracking messages in personal messages</b>\n",
        "mode_off": f"{pm} <b>Not tracking messages </b><code>{{}}nsmode</code>\n",
        "saved_pm": (
            '<b>Сохранённое сообщение от</b> <a href="{}">{}</a>{}:\n\n{}'
        ),
        "saved_chat": (
            '<b>Сохранённое сообщение от</b> <a href="{}">{}</a>{} в чате <a href="{}">{}</a>:\n\n{}'
        ),
        "deleted_pm": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение:</b>\n\n<blockquote>{}</blockquote>'
        ),
        "deleted_pm_no_text": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение</b>'
        ),
        "deleted_chat": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n{}'
        ),
        "deleted_chat_no_text": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение в чате <a href="{}">{}</a></b>'
        ),
        "edited_pm": (
            '<a href="{}">{}</a>{} <b>изменил(а) сообщение:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote>{}</blockquote>'
        ),
        "edited_chat": (
            '<a href="{}">{}</a>{} <b>изменил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote>{}</blockquote>'
        ),
        "on": "on",
        "off": "off",
        "cfg_enable_pm": "Enable spy mode in Personal messages",
        "cfg_enable_groups": "Enable spy mode in Groups",
        "cfg_whitelist": "List of chats to include messages from",
        "cfg_always_track": "List of chats to always track messages from, no matter what",
        "cfg_log_edits": "Log information about messages being edited",
        "cfg_ignore_inline": "Ignore inline messages (sent using @via bots)",
        "cfg_fw_protect": "Interval of messages sending to prevent floodwait",
        "save_sd": "<emoji document_id=5420315771991497307>🔥</emoji> <b>Saving self-destructing media</b>\n",
        "cfg_save_sd": "Save self-destructing media",
        "nspm": f"{rei} <b>Режим ЛС {{}}</b>",
        "media_photo": "фото",
        "media_video": "видео",
        "media_voice": "голосовое сообщение",
        "media_video_note": "видеосообщение",
        "media_sticker": "стикер",
        "media_animated_sticker": "анимированный стикер",
        "media_gif": "GIF",
        "media_document": "документ",
        "media_audio": "аудио",
        "media_text": "сообщение",
        "media": "медиа",
        "multiple_messages": "{} {}",
        "file_reference_expired": " (файл недоступен)",
        "stats": "<b>Статистика кэша:</b>\n<b>Размер:</b> {}\n<b>Сообщений:</b> {}\n<b>Самое старое:</b> {}",
        "purged_cache": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Кэш сообщений очищен</b>",
        "saved": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Сообщения сохранены</b>",
        "invalid_time": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Указано неверное время</b>",
        "restoring": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Восстанавливаю сообщения...</b>",
        "restored": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Сообщения восстановлены</b>",
        "ignore_channels": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Игнорирование каналов теперь {}</b>",
        "cfg_ignore_channels": "Игнорировать сообщения из каналов",
        "channel_create_failed": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Не удалось создать канал для логов!</b>",
        "cfg_ignore_bots": "Игнорировать сообщения от ботов",
        "ignore_bots": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Игнорирование ботов теперь {}</b>",
        "cfg_download_media": "Скачивать медиафайлы сразу при сохранении",
        "downloading_media": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Скачиваю медиафайлы...</b>",
        "cfg_track_self": "Отслеживать свои действия (удаление и редактирование)",
        "self_edited": "Вы <b>изменили сообщение:</b>\n\n<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n<b>Новое:</b>\n<blockquote>{}</blockquote>",
        "self_deleted_single": "Вы <b>удалили сообщение:</b>\n\n<blockquote>{}</blockquote>",
        "self_deleted_multiple": "Вы <b>удалили {} {}:</b>\n\n{}",
    }

    strings_ru = {
        "on": "включен",
        "off": "выключен",
        "state": f"{rei} <b>Режим слежения теперь {{}}</b>",
        "nswl": f"{rei} <b>Текущий чат добавлен в белый список для слежения</b>",
        "nswl_removed": f"{rei} <b>Текущий чат удален из белого списка для слежения</b>",
        "nswl_clear": f"{rei} <b>Белый список для слежения очищен</b>",
        "whitelist": f"\n{rei} <b>Слежу только за сообщениями от пользователей/групп:</b>\n{{}}",
        "always_track": f"\n{rei} <b>Всегда слежу за сообщениями от пользователей/групп:</b>\n{{}}",
        "chat": f"{groups} <b>Слежу за сообщениями в группах</b>\n",
        "pm": f"{pm} <b>Слежу за сообщениями в личных сообщениях</b>\n",
        "saved_pm": (
            '<b>Сохранённое сообщение от</b> <a href="{}">{}</a>{}:\n\n{}'
        ),
        "saved_chat": (
            '<b>Сохранённое сообщение от</b> <a href="{}">{}</a>{} в чате <a href="{}">{}</a>:\n\n{}'
        ),
        "deleted_pm": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение:</b>\n\n<blockquote>{}</blockquote>'
        ),
        "deleted_pm_no_text": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение</b>'
        ),
        "deleted_chat": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n{}'
        ),
        "deleted_chat_no_text": (
            '<a href="{}">{}</a>{} <b>удалил(а) сообщение в чате <a href="{}">{}</a></b>'
        ),
        "edited_pm": (
            '<a href="{}">{}</a>{} <b>изменил(а) сообщение:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote>{}</blockquote>'
        ),
        "edited_chat": (
            '<a href="{}">{}</a>{} <b>изменил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote>{}</blockquote>'
        ),
        "mode_off": f"{pm} <b>Не отслеживаю сообщения </b><code>{{}}nsmode</code>\n",
        "cfg_enable_pm": "Включить режим шпиона в личных сообщениях",
        "cfg_enable_groups": "Включить режим шпиона в группах",
        "cfg_whitelist": "Список чатов, от которых нужно сохранять сообщения",
        "cfg_always_track": "Список чатов, от которых всегда следует отслеживать сообщения, несмотря ни на что",
        "cfg_log_edits": "Сохранять отредактированные сообщения",
        "cfg_ignore_inline": "Игнорировать сообщения из инлайн-режима",
        "cfg_fw_protect": "Защита от флудвейтов при пересылке",
        "save_sd": "<emoji document_id=5420315771991497307>🔥</emoji> <b>Сохраняю самоуничтожающиеся медиа</b>\n",
        "cfg_save_sd": "Сохранять самоуничтожающееся медиа",
        "nspm": f"{rei} <b>Режим ЛС {{}}</b>",
        "media_photo": "фото",
        "media_video": "видео",
        "media_voice": "голосовое сообщение",
        "media_video_note": "видеосообщение",
        "media_sticker": "стикер",
        "media_animated_sticker": "анимированный стикер",
        "media_gif": "GIF",
        "media_document": "документ",
        "media_audio": "аудио",
        "media_text": "сообщение",
        "media": "медиа",
        "multiple_messages": "{} {}",
        "file_reference_expired": " (файл недоступен)",
        "stats": "<b>Статистика кэша:</b>\n<b>Размер:</b> {}\n<b>Сообщений:</b> {}\n<b>Самое старое:</b> {}",
        "purged_cache": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Кэш сообщений очищен</b>",
        "saved": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Сообщения сохранены</b>",
        "invalid_time": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Указано неверное время</b>",
        "restoring": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Восстанавливаю сообщения...</b>",
        "restored": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Сообщения восстановлены</b>",
        "ignore_channels": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Игнорирование каналов теперь {}</b>",
        "cfg_ignore_channels": "Игнорировать сообщения из каналов",
        "channel_create_failed": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Не удалось создать канал для логов!</b>",
        "cfg_ignore_bots": "Игнорировать сообщения от ботов",
        "ignore_bots": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Игнорирование ботов теперь {}</b>",
        "cfg_download_media": "Скачивать медиафайлы сразу при сохранении",
        "downloading_media": "<emoji document_id=5409143295039252230>👩‍🎤</emoji> <b>Скачиваю медиафайлы...</b>",
        "cfg_track_self": "Отслеживать свои действия (удаление и редактирование)",
        "self_edited": "Вы <b>изменили сообщение:</b>\n\n<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n<b>Новое:</b>\n<blockquote>{}</blockquote>",
        "self_deleted_single": "Вы <b>удалили сообщение:</b>\n\n<blockquote>{}</blockquote>",
        "self_deleted_multiple": "Вы <b>удалили {} {}:</b>\n\n{}",
    }

    def __init__(self):
        self._tl_channel = None
        self._channel = None
        self._queue = []
        self._cache = {}
        self._next = 0
        self._threshold = 10
        self._flood_protect_sample = 60
        self._ignore_cache = []
        self._cacher = None
        self.METHOD_MAP = None
        self._recent = []
        self._delete_queue = defaultdict(set)
        self._delete_timers = {}
        self._processed_messages = set()
        self._media_cache = {}
        self._last_processed = {}
        self._pending_messages = set()

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
                "ignore_channels",
                True,
                lambda: self.strings("cfg_ignore_channels"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "all_pm",
                True,
                lambda: "Отслеживать все личные сообщения",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "group_deletes_timeout",
                1.0,
                lambda: "Таймаут группировки удаленных сообщений",
                validator=loader.validators.Float(minimum=0.1, maximum=10.0),
            ),
            loader.ConfigValue(
                "ignore_bots",
                True,
                lambda: self.strings("cfg_ignore_bots"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "download_media",
                True,
                lambda: self.strings("cfg_download_media"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "track_self",
                False,
                lambda: self.strings("cfg_track_self"),
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
                "Deleted and edited messages will appear there",
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

                self._processed_messages = set()
                self._media_cache = {}

                for key in list(self._last_processed.keys()):
                    if self._last_processed[key] < current_time - 3600:
                        del self._last_processed[key]
            except Exception as e:
                logger.error(f"GC error: {e}")

    @loader.loop(interval=0.1, autostart=True)
    async def sender(self):
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

    def _get_media_type_string(self, media_type: str) -> str:
        return self.strings.get(f"media_{media_type}", self.strings("media_text"))

    def _get_message_deep_link(self, msg_obj: dict) -> str:
        if msg_obj.get("is_chat"):
            return f"tg://openmessage?chat_id={msg_obj['chat_id']}&message_id={msg_obj['message_id']}"
        else:
            return f"tg://openmessage?user_id={msg_obj['sender_id']}&message_id={msg_obj['message_id']}"

    def _format_text_with_link(self, text: str, msg_obj: dict) -> str:
        message_link = self._get_message_deep_link(msg_obj)
        return f'<a href="{message_link}">{text}</a>'

    async def _message_deleted(self, msg_obj: dict, caption: str):
        caption = self.inline.sanitise_text(caption)
        media_path = msg_obj.get("media_path")
        if media_path and Path(media_path).exists():
            try:
                file = io.BytesIO(Path(media_path).read_bytes())
                media_type = msg_obj.get("media_type")

                if media_type == "photo":
                    file.name = "photo.jpg"
                    self._queue.append(self.inline.bot.send_photo(self._channel, file, caption=caption))
                elif media_type == "video":
                    file.name = "video.mp4"
                    self._queue.append(self.inline.bot.send_video(self._channel, file, caption=caption))
                elif media_type == "voice":
                    file.name = "audio.ogg"
                    self._queue.append(self.inline.bot.send_voice(self._channel, file, caption=caption))
                elif media_type == "video_note":
                    file.name = "video_note.mp4"
                    await self._send_text(caption)
                    self._queue.append(self.inline.bot.send_video_note(self._channel, file))
                    await self._send_text(">------------------>")
                    return
                elif media_type == "document":
                    file.name = msg_obj.get("assets", {}).get("document", {}).get("file_name", "document.bin")
                    self._queue.append(self.inline.bot.send_document(self._channel, file, caption=caption))
                elif media_type == "audio":
                    file.name = "audio.mp3"
                    self._queue.append(self.inline.bot.send_audio(self._channel, file, caption=caption))
                elif media_type in ["sticker", "animated_sticker"]:
                    await self._send_text(caption)
                    file.name = "sticker.webp"
                    self._queue.append(self.inline.bot.send_sticker(self._channel, file))
                return
            except Exception as e:
                logger.error(f"Failed to send downloaded media: {e}")

        assets = msg_obj.get("assets", {})
        file = next((x for x in assets.values() if x), None)

        if not file:
            await self._send_text(caption)
            return

        media_type = msg_obj.get("media_type")
        if media_type in ["sticker", "animated_sticker"]:
            await self._send_text(caption)
            try:
                await self._send_sticker(file, media_type)
            except FileReferenceExpiredError:
                await self._send_text(caption + self.strings("file_reference_expired"))
            return

        if media_type == "video_note":
            await self._send_text(caption)
            try:
                await self._send_video_note(file)
            except FileReferenceExpiredError:
                await self._send_text(caption + self.strings("file_reference_expired"))
            return

        try:
            await self._send_media(file, assets, caption, media_type)
        except FileReferenceExpiredError:
            await self._send_text(caption + self.strings("file_reference_expired"))

    async def _send_sticker(self, file: dict, media_type: str):
        try:
            if not file.get("file_reference"):
                raise FileReferenceExpiredError("No file reference")

            file["file_reference"] = bytes.fromhex(file["file_reference"])
            file["thumb_size"] = file.get("thumb_size", "")

            file_key = f"{file['id']}_{file['access_hash']}"
            if file_key in self._media_cache:
                file_data = self._media_cache[file_key]
            else:
                try:
                    file_data = await self._client.download_file(
                        InputDocumentFileLocation(
                            id=file["id"],
                            access_hash=file["access_hash"],
                            file_reference=file["file_reference"],
                            thumb_size=file["thumb_size"],
                        ),
                        bytes,
                    )
                    if self.config["download_media"]:
                        self._media_cache[file_key] = file_data
                except FileReferenceExpiredError:
                    logger.error("File reference expired, cannot download sticker")
                    raise

            if not file_data:
                raise ValueError("Empty file data")

            mime = magic.from_buffer(file_data, mime=True)
            if mime == "application/x-tgsticker" or media_type == "animated_sticker":

                file_io = io.BytesIO(file_data)
                file_io.name = "sticker.tgs"
                await self.inline.bot.send_sticker(self._channel, file_io)
            elif mime == "video/webm":
                file_io = io.BytesIO(file_data)
                file_io.name = "sticker.webm"
                await self.inline.bot.send_video(self._channel, file_io)
            else:
                file_io = io.BytesIO(file_data)
                file_io.name = "sticker.webp"
                await self.inline.bot.send_sticker(self._channel, file_io)
        except Exception as e:
            logger.error(f"Failed to send sticker: {e}")
            raise

    async def _send_video_note(self, file: dict):
        try:
            if not file.get("file_reference"):
                raise FileReferenceExpiredError("No file reference")

            file["file_reference"] = bytes.fromhex(file["file_reference"])
            file["thumb_size"] = file.get("thumb_size", "")

            file_key = f"{file['id']}_{file['access_hash']}"
            if file_key in self._media_cache:
                file_data = self._media_cache[file_key]
            else:
                try:
                    file_data = await self._client.download_file(
                        InputDocumentFileLocation(
                            id=file["id"],
                            access_hash=file["access_hash"],
                            file_reference=file["file_reference"],
                            thumb_size=file["thumb_size"],
                        ),
                        bytes,
                    )
                    if self.config["download_media"]:
                        self._media_cache[file_key] = file_data
                except FileReferenceExpiredError:
                    logger.error("File reference expired, cannot download video note")
                    raise

            if not file_data:
                raise ValueError("Empty file data")

            file_io = io.BytesIO(file_data)
            file_io.name = "video_note.mp4"
            await self.inline.bot.send_video_note(self._channel, file_io)
        except Exception as e:
            logger.error(f"Failed to send video note: {e}")
            raise

    async def _send_media(self, file: dict, assets: dict, caption: str, media_type: str):
        try:
            if not file.get("file_reference"):
                raise FileReferenceExpiredError("No file reference")
                
            file["file_reference"] = bytes.fromhex(file["file_reference"])
            file["thumb_size"] = file.get("thumb_size", "")

            file_key = f"{file['id']}_{file['access_hash']}"
            if file_key in self._media_cache:
                file_data = self._media_cache[file_key]
            else:
                try:
                    file_data = await self._client.download_file(
                        InputDocumentFileLocation(
                            id=file["id"],
                            access_hash=file["access_hash"],
                            file_reference=file["file_reference"],
                            thumb_size=file["thumb_size"],
                        ),
                        bytes,
                    )
                    if self.config["download_media"]:
                        self._media_cache[file_key] = file_data
                except FileReferenceExpiredError:
                    logger.error("File reference expired, cannot download media")
                    raise

            if not file_data:
                raise ValueError("Empty file data")

            mime = magic.from_buffer(file_data, mime=True)
            ext = mimetypes.guess_extension(mime) or ".bin"
            file_io = io.BytesIO(file_data)

            if mime == "video/webm":
                media_type = "video"
                ext = ".webm"

            if media_type == "photo":
                file_io.name = f"photo{ext}"
                await self.inline.bot.send_photo(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif media_type == "video":
                file_io.name = f"video{ext}"
                await self.inline.bot.send_video(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif media_type == "voice":
                file_io.name = f"voice{ext}"
                await self.inline.bot.send_voice(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif media_type == "document":
                filename = assets.get("document", {}).get("file_name", f"document{ext}")
                file_io.name = filename
                await self.inline.bot.send_document(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
            elif media_type == "audio":
                file_io.name = f"audio{ext}"
                await self.inline.bot.send_audio(
                    self._channel, 
                    file_io, 
                    caption=caption
                )
        except Exception as e:
            logger.error(f"Failed to send media {media_type}: {e}")
            raise

    async def _process_deleted_messages(self, chat_id: int, message_ids: set):
        try:
            messages_data = []
            for message_id in message_ids:
                message_key = f"{chat_id}_{message_id}"
                if message_key in self._processed_messages:
                    continue

                self._processed_messages.add(message_key)
                msg_obj = await self._cacher.fetch_message(chat_id, message_id)
                if msg_obj:
                    if self.config["ignore_bots"] and msg_obj.get("sender_bot"):
                        continue
                    messages_data.append(msg_obj)

            if not messages_data:
                return

            sender_groups = defaultdict(list)
            for msg_obj in messages_data:
                sender_id = msg_obj["sender_id"]
                sender_groups[sender_id].append(msg_obj)

            for sender_id, msgs in sender_groups.items():
                if len(msgs) > 1:
                    await self._notify_multiple_messages(msgs)
                else:
                    await self._notify_single_message(msgs[0])
        except Exception as e:
            logger.error(f"Error processing deleted messages: {e}")

    async def _notify_multiple_messages(self, msgs: list):
        if not msgs:
            return

        msgs.sort(key=lambda x: x['message_id'])
        first_msg = msgs[0]
        try:
            sender = await self._client.get_entity(first_msg["sender_id"], exp=0)
            username = f" (@{sender.username})" if getattr(sender, 'username', None) else f" ( tg://user?id={sender.id} )"
            count = len(msgs)
            plural_form = self._cacher._get_plural_form(count)
            message_texts = []
            for msg in msgs:
                if msg.get("text"):
                    text_content = self._format_text_with_link(msg["text"], msg)
                    message_texts.append(f"<blockquote>{text_content}</blockquote>")
                else:
                    media_type = self._get_media_type_string(msg.get("media_type", "media"))
                    message_texts.append(f"<blockquote>{media_type}</blockquote>")

            combined_text = "\n".join(message_texts)

            if self.config["track_self"] and first_msg["sender_id"] == self._client.tg_id:
                text = self.strings("self_deleted_multiple").format(
                    count,
                    plural_form,
                    combined_text
                )
            else:
                if first_msg.get("is_chat"):
                    text = (
                        f'<b><a href="{first_msg["sender_url"]}">{first_msg["sender_name"]}</a>'
                        f'{username} удалил(а) {count} {plural_form} в чате '
                        f'<a href="{first_msg["chat_url"]}">{first_msg["chat_name"]}</a>:</b>\n\n'
                        f'{combined_text}'
                    )
                else:
                    text = (
                        f'<b><a href="{first_msg["sender_url"]}">{first_msg["sender_name"]}</a>'
                        f'{username} удалил(а) {count} {plural_form}:</b>\n\n'
                        f'{combined_text}'
                    )

            await self._send_text(text)

            for msg in msgs:
                if not msg.get("text"):
                    await self._message_deleted(msg, "")

        except Exception as e:
            logger.error(f"Error in _notify_multiple_messages: {e}")

    async def _notify_single_message(self, msg_obj: dict):
        try:
            sender = await self._client.get_entity(msg_obj["sender_id"], exp=0)
            username = f" (@{sender.username})" if getattr(sender, 'username', None) else f" ( tg://user?id={sender.id} )"
            sender_name = f'<a href="{msg_obj["sender_url"]}">{msg_obj["sender_name"]}</a>'

            if msg_obj.get("text"):
                text_content = self._format_text_with_link(msg_obj["text"], msg_obj)

                if self.config["track_self"] and msg_obj["sender_id"] == self._client.tg_id:
                    text = self.strings("self_deleted_single").format(text_content)
                else:
                    if msg_obj.get("is_chat"):
                        text = (
                            f'{sender_name}{username} <b>удалил(а) сообщение в чате '
                            f'<a href="{msg_obj["chat_url"]}">{msg_obj["chat_name"]}</a>:</b>\n\n'
                            f'<blockquote>{text_content}</blockquote>'
                        )
                    else:
                        text = (
                            f'{sender_name}{username} <b>удалил(а) сообщение:</b>\n\n'
                            f'<blockquote>{text_content}</blockquote>'
                        )
            else:
                if self.config["track_self"] and msg_obj["sender_id"] == self._client.tg_id:
                    text = self.strings("self_deleted_single").format(
                        self._get_media_type_string(msg_obj.get("media_type", "media"))
                    )
                else:
                    if msg_obj.get("is_chat"):
                        text = (
                            f'{sender_name}{username} <b>удалил(а) сообщение в чате '
                            f'<a href="{msg_obj["chat_url"]}">{msg_obj["chat_name"]}</a></b>'
                        )
                    else:
                        text = f'{sender_name}{username} <b>удалил(а) сообщение</b>'

            await self._message_deleted(msg_obj, text)
        except Exception as e:
            logger.error(f"Error in _notify_single_message: {e}")

    @loader.raw_handler(UpdateEditMessage)
    async def pm_edit_handler(self, update: UpdateEditMessage):
        if (
            not self.get("state", False)
            or update.message.out
            or (self.config["ignore_inline"] and update.message.via_bot_id)
        ):
            return

        if self.config["ignore_bots"]:
            try:
                sender = await update.message.get_sender()
                if isinstance(sender, User) and sender.bot:
                    return
            except Exception as e:
                logger.error(f"Error getting sender in edit handler: {e}")
                return

        chat_id = utils.get_chat_id(update.message)

        is_pm = not (update.message.is_group or update.message.is_channel)
        should_track = (
            (is_pm and (self.config["all_pm"] or chat_id in self.whitelist or chat_id in self.always_track)) or 
            (not is_pm and (chat_id in self.whitelist or chat_id in self.always_track))
        )

        if not should_track:
            return

        message_key = f"edit_{chat_id}_{update.message.id}"
        current_time = time.time()
        if message_key in self._last_processed and current_time - self._last_processed[message_key] < 5:
            return

        self._last_processed[message_key] = current_time
        self._recent.append(RecentsItem.from_edit(update.message))
        msg_obj = await self._cacher.fetch_message(chat_id, update.message.id)

        if not msg_obj:
            await self._cacher.store_message(update.message)
            return

        sender_id = int(msg_obj["sender_id"])
        is_chat = msg_obj["is_chat"]

        if (self.config["log_edits"] and
            update.message.raw_text != utils.remove_html(msg_obj["text"]) and
            not msg_obj["sender_bot"]):

            if self.config["track_self"] and msg_obj["sender_id"] == self._client.tg_id:
                old_text = utils.escape_html(msg_obj["text"])
                new_text = self._format_text_with_link(update.message.text, msg_obj)

                await self._send_text(
                    self.strings("self_edited").format(old_text, new_text)
                )
            else:
                sender = await self._client.get_entity(sender_id, exp=0)
                username = f" (@{sender.username})" if getattr(sender, 'username', None) else f" ( tg://user?id={sender.id} )"

                old_text = utils.escape_html(msg_obj["text"])
                new_text = self._format_text_with_link(update.message.text, msg_obj)

                await self._send_text(
                    (
                        self.strings("edited_chat").format(
                            msg_obj["sender_url"],
                            msg_obj["sender_name"],
                            username,
                            msg_obj["chat_url"] if "chat_url" in msg_obj else "",
                            msg_obj["chat_name"] if "chat_name" in msg_obj else "",
                            old_text,
                            new_text
                        )
                        if is_chat
                        else self.strings("edited_pm").format(
                            msg_obj["sender_url"],
                            msg_obj["sender_name"],
                            username,
                            old_text,
                            new_text
                        )
                    ),
                )

        await self._cacher.store_message(update.message)

    @loader.raw_handler(UpdateDeleteMessages)
    async def pm_delete_handler(self, update: UpdateDeleteMessages):
        if not self.get("state", False):
            return

        current_time = time.time()
        for message_id in update.messages:
            message_key = f"del_None_{message_id}"
            if message_key in self._last_processed and current_time - self._last_processed[message_key] < 5:
                continue

            self._last_processed[message_key] = current_time
            self._recent.append(RecentsItem.from_delete(message_id))
            self._delete_queue[None].add(message_id)

        if None not in self._delete_timers and self._delete_queue[None]:
            self._delete_timers[None] = asyncio.create_task(
                self._process_delete_queue(None)
            )

    @loader.raw_handler(UpdateDeleteChannelMessages)
    async def channel_delete_handler(self, update: UpdateDeleteChannelMessages):
        if self.config["ignore_channels"] or not self.get("state", False):
            return

        current_time = time.time()
        for message_id in update.messages:
            message_key = f"del_{update.channel_id}_{message_id}"
            if message_key in self._last_processed and current_time - self._last_processed[message_key] < 5:
                continue

            self._last_processed[message_key] = current_time
            self._recent.append(RecentsItem.from_delete(message_id, update.channel_id))
            self._delete_queue[update.channel_id].add(message_id)

        if update.channel_id not in self._delete_timers and self._delete_queue[update.channel_id]:
            self._delete_timers[update.channel_id] = asyncio.create_task(
                self._process_delete_queue(update.channel_id)
            )

    async def _process_delete_queue(self, chat_id: typing.Optional[int]):
        await asyncio.sleep(self.config["group_deletes_timeout"])

        if chat_id not in self._delete_queue:
            return

        message_ids = self._delete_queue[chat_id].copy()

        self._delete_queue[chat_id] = set()
        del self._delete_timers[chat_id]

        await self._process_deleted_messages(chat_id, message_ids)

    @loader.command()
    async def nspm(self, message: Message):
        """- вкл/выкл сохранение всех ЛС"""
        self.config["all_pm"] = not self.config["all_pm"]
        await utils.answer(
            message,
            self.strings("nspm").format(
                self.strings("on" if self.config["nspm"] else "off")
            ),
        )

    @loader.command()
    async def nsmode(self, message: Message):
        """- вкл/выкл модуль"""
        await utils.answer(
            message,
            self.strings("state").format(
                self.strings("off" if self.get("state", False) else "on")
            ),
        )
        self.set("state", not self.get("state", False))

    @loader.command()
    async def nswl(self, message: Message):
        """- добавить/удалить чат из белого списка"""
        chat = utils.get_chat_id(message)
        if chat in self.whitelist:
            self.whitelist = list(set(self.whitelist) - {chat})
            await utils.answer(message, self.strings("nswl_removed"))
        else:
            self.whitelist = list(set(self.whitelist) | {chat})
            await utils.answer(message, self.strings("nswl"))

    @loader.command()
    async def nswlclear(self, message: Message):
        """- очистить белый список"""
        self.whitelist = []
        await utils.answer(message, self.strings("nswl_clear"))

    async def _get_entities_list(self, entities: list) -> str:
        return "\n".join(
            [
                "\u0020\u2800\u0020\u2800<emoji document_id=4971987363145188045>▫️</emoji> <b><a href=\"{}\">{}</a></b>"
                .format(
                    utils.get_entity_url(await self._client.get_entity(x, exp=0)),
                    utils.escape_html(
                        get_display_name(await self._client.get_entity(x, exp=0))
                    ),
                )
                for x in entities
            ]
        )

    @loader.command()
    async def nsinfo(self, message: Message):
        """- показать текущую конфигурацию"""
        if not self.get("state"):
            await utils.answer(
                message, self.strings("mode_off").format(self.get_prefix())
            )
            return

        info = ""

        if self.config["save_sd"]:
            info += self.strings("save_sd")

        if self.config["enable_groups"]:
            info += self.strings("chat")

        if self.config["all_pm"]:
            info += f"{self.rei} <b>Режим ЛС</b>\n"

        if self.whitelist:
            info += self.strings("whitelist").format(
                await self._get_entities_list(self.whitelist)
            )

        if self.always_track:
            info += self.strings("always_track").format(
                await self._get_entities_list(self.always_track)
            )

        if self.config["track_self"]:
            info += f"{self.rei} <b>Отслеживание своих действий</b>\n"

        await utils.answer(message, info)

    @loader.command()
    async def nsstat(self, message: Message):
        """- показать статистику кэша"""
        if not self._cacher:
            await utils.answer(message, "Кэш не инициализирован")
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
    async def nscache(self, message: Message):
        """- очистить кэш сообщений"""
        if not self._cacher:
            await utils.answer(message, "Кэш не инициализирован")
            return

        self._cacher.purge()
        self._recent = []
        self._processed_messages = set()
        self._media_cache = {}
        self._last_processed = {}
        await utils.answer(message, self.strings("purged_cache"))

    @loader.command()
    async def nssave(self, message: Message):
        """- сохранить ответное сообщение"""
        async def _save(_reply: Message):
            msg_obj = await self._cacher.store_message(_reply)
            if not msg_obj:
                return

            try:
                sender = await self._client.get_entity(msg_obj["sender_id"], exp=0)
            except Exception:
                sender = None

            username = f" (@{sender.username})" if getattr(sender, 'username', None) else f" ( tg://user?id={sender.id} )"

            if msg_obj.get("is_chat"):
                caption = self.strings("saved_chat").format(
                    msg_obj["sender_url"],
                    msg_obj["sender_name"],
                    username,
                    msg_obj["chat_url"],
                    msg_obj["chat_name"],
                    utils.escape_html(msg_obj["text"]),
                )
            else:
                caption = self.strings("saved_pm").format(
                    msg_obj["sender_url"],
                    msg_obj["sender_name"],
                    username,
                    utils.escape_html(msg_obj["text"]),
                )

            if msg_obj.get("media_path") or msg_obj.get("assets"):
                await self._message_deleted(msg_obj, caption)
            else:
                await self._send_text(caption)

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
    async def nsrest(self, message: Message):
        """- восстановить сообщения за период времени"""
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

            if self.config["ignore_bots"] and msg_obj.get("sender_bot"):
                continue

            try:
                sender = await self._client.get_entity(msg_obj["sender_id"], exp=0)
            except Exception:
                sender = None

            username = f" (@{sender.username})" if getattr(sender, 'username', None) else f" ( tg://user?id={sender.id} )"

            if msg_obj.get("text"):
                text_content = self._format_text_with_link(msg_obj["text"], msg_obj)
            else:
                text_content = self._format_text_with_link(self.strings("media"), msg_obj)

            if msg_obj.get("is_chat"):
                await self._send_text(
                    self.strings(
                        "deleted_chat" if recent.action == "del" else "edited_chat"
                    ).format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        msg_obj["chat_url"] if "chat_url" in msg_obj else "",
                        msg_obj["chat_name"] if "chat_name" in msg_obj else "",
                        text_content,
                        text_content if recent.action == "del" else "",
                    )
                )
            else:
                await self._send_text(
                    self.strings(
                        "deleted_pm" if recent.action == "del" else "edited_pm"
                    ).format(
                        msg_obj["sender_url"],
                        msg_obj["sender_name"],
                        username,
                        text_content,
                        text_content if recent.action == "del" else "",
                    )
                )
            restored += 1
            await asyncio.sleep(0.1)

        await utils.answer(
            message,
            self.strings("restored") + f"\n<b>Восстановлено сообщений:</b> {restored}"
        )

    @loader.watcher(only_messages=True)
    async def watcher(self, message: Message):
        try:
            if not hasattr(message, "sender_id"):
                return

            if message.out and not self.config["track_self"]:
                return

            if self.config["ignore_bots"]:
                try:
                    sender = await message.get_sender()
                    if isinstance(sender, User) and sender.bot:
                        return
                except Exception as e:
                    logger.error(f"Error checking ignore_bots: {e}")
                    return

            chat_id = utils.get_chat_id(message)

            is_pm = message.is_private
            should_track = (
                (is_pm and (self.config["all_pm"] or chat_id in self.whitelist or chat_id in self.always_track)) or 
                (not is_pm and (chat_id in self.whitelist or chat_id in self.always_track))
            )

            if not should_track:
                return

            if (self.config["save_sd"] and
                getattr(message, "media", None) and
                getattr(message.media, "ttl_seconds", None)):

                try:
                    try:
                        sender = await self.client.get_entity(message.sender_id)
                        sender_name = utils.escape_html(get_display_name(sender))
                        if hasattr(sender, 'username') and sender.username:
                            username_part = f"(@{sender.username})"
                        else:
                            username_part = f"( tg://user?id={sender.id} )"
                        caption = f'🔥 <a href="tg://user?id={sender.id}">{sender_name}</a> {username_part} отправил(а) вам самоуничтожающееся медиа'
                    except Exception as e:
                        logger.error(f"Error getting sender for self-destructing media: {e}")
                        sender_name = "Unknown user"
                        caption = f'🔥 <a href="tg://user?id={message.sender_id}">Unknown user</a> ( tg://user?id={message.sender_id} ) отправил(а) вам самоуничтожающееся медиа'

                    media = io.BytesIO(await self.client.download_media(message.media, bytes))
                    media.name = "sd.jpg" if message.photo else "sd.mp4"

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

            msg_obj = await self._cacher.store_message(message)
            if not msg_obj:
                return

        except Exception as e:
            logger.error(f"Watcher error: {e}")

    @property
    def whitelist(self):
        return list(map(self._int, self.config["whitelist"]))

    @whitelist.setter
    def whitelist(self, value: list):
        self.config["whitelist"] = value

    @property
    def always_track(self):
        return list(map(self._int, self.config["always_track"]))

    @staticmethod
    def _int(value: typing.Union[str, int], /) -> typing.Union[str, int]:
        return int(value) if str(value).isdigit() else value