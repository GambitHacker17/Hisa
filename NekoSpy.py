__version__ = (1, 0, 0)

# meta developer: MartyyyK
# scope: hisa_only
# scope: hisa_min 0.0.1

import contextlib
import io
import logging
import time
import typing

from telethon.tl.types import (
    DocumentAttributeFilename,
    Message,
    PeerChat,
    UpdateDeleteChannelMessages,
    UpdateDeleteMessages,
    UpdateEditChannelMessage,
    UpdateEditMessage,
)
from telethon.utils import get_display_name

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class NekoSpy(loader.Module):

    rei = "<emoji document_id=5409143295039252230>👩‍🎤</emoji>"
    groups = "<emoji document_id=6037355667365300960>👥</emoji>"
    pm = "<emoji document_id=6048540195995782913>👤</emoji>"

    strings = {
        "name": "NekoSpy",
        "state": f"{rei} <b>Spy mode is now {{}}</b>",
        "spybl": f"{rei} <b>Current chat added to blacklist for spying</b>",
        "spybl_removed": f"{rei} <b>Current chat removed from blacklist for spying</b>",
        "spybl_clear": f"{rei} <b>Ignore list for spying cleared</b>",
        "spywl": f"{rei} <b>Current chat added to whitelist for spying</b>",
        "spywl_removed": f"{rei} <b>Current chat removed from whitelist for spying</b>",
        "spywl_clear": f"{rei} <b>Include list for spying cleared</b>",
        "whitelist": f"\n{rei} <b>Tracking only messages from:</b>\n{{}}",
        "always_track": f"\n{rei} <b>Always tracking messages from:</b>\n{{}}",
        "blacklist": f"\n{rei} <b>Ignoring messages from:</b>\n{{}}",
        "chat": f"{groups} <b>Tracking messages in groups</b>\n",
        "pm": f"{pm} <b>Tracking messages in personal messages</b>\n",
        "mode_off": f"{pm} <b>Not tracking messages </b><code>{{}}spymode</code>\n",
        "deleted_pm": (
            '<b><a href="{}">{}</a>{} удалил(а) сообщение:</b>\n\n<blockquote>{}</blockquote>'
        ),
        "deleted_chat": (
            '<b><a href="{}">{}</a>{} удалил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n<blockquote>{}</blockquote>'
        ),
        "edited_pm": (
            '<b><a href="{}">{}</a>{} изменил(а) сообщение:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote><a href="{message_url}">{}</a></blockquote>'
        ),
        "edited_chat": (
            '<b><a href="{}">{}</a>{} изменил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote><a href="{message_url}">{}</a></blockquote>'
        ),
        "on": "on",
        "off": "off",
        "cfg_enable_pm": "Enable spy mode in Personal messages",
        "cfg_enable_groups": "Enable spy mode in Groups",
        "cfg_whitelist": "List of chats to include messages from",
        "cfg_blacklist": "List of chats to exclude messages from",
        "cfg_always_track": "List of chats to always track messages from, no matter what",
        "cfg_log_edits": "Log information about messages being edited",
        "cfg_ignore_inline": "Ignore inline messages (sent using @via bots)",
        "cfg_fw_protect": "Interval of messages sending to prevent floodwait",
        "sd_media": "🔥 <b><a href='tg://user?id={}'>{}</a> sent you a self-destructing media</b>",
        "save_sd": "<emoji document_id=5420315771991497307>🔥</emoji> <b>Saving self-destructing media</b>\n",
        "cfg_save_sd": "Save self-destructing media",
    }

    strings_ru = {
        "on": "включен",
        "off": "выключен",
        "state": f"{rei} <b>Режим слежения теперь {{}}</b>",
        "spybl": f"{rei} <b>Текущий чат добавлен в черный список для слежения</b>",
        "spybl_removed": f"{rei} <b>Текущий чат удален из черного списка для слежения</b>",
        "spybl_clear": f"{rei} <b>Черный список для слежения очищен</b>",
        "spywl": f"{rei} <b>Текущий чат добавлен в белый список для слежения</b>",
        "spywl_removed": f"{rei} <b>Текущий чат удален из белого списка для слежения</b>",
        "spywl_clear": f"{rei} <b>Белый список для слежения очищен</b>",
        "whitelist": f"\n{rei} <b>Слежу только за сообщениями от пользователей/групп:</b>\n{{}}",
        "always_track": f"\n{rei} <b>Всегда слежу за сообщениями от пользователей/групп:</b>\n{{}}",
        "blacklist": f"\n{rei} <b>Игнорирую сообщения от пользователей/групп:</b>\n{{}}",
        "chat": f"{groups} <b>Слежу за сообщениями в группах</b>\n",
        "pm": f"{pm} <b>Слежу за сообщениями в личных сообщениях</b>\n",
        "deleted_pm": (
            '<b><a href="{}">{}</a>{} удалил(а) сообщение:</b>\n\n<blockquote>{}</blockquote>'
        ),
        "deleted_chat": (
            '<b><a href="{}">{}</a>{} удалил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n<blockquote>{}</blockquote>'
        ),
        "edited_pm": (
            '<b><a href="{}">{}</a>{} изменил(а) сообщение:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote><a href="{message_url}">{}</a></blockquote>'
        ),
        "edited_chat": (
            '<b><a href="{}">{}</a>{} изменил(а) сообщение в чате <a href="{}">{}</a>:</b>\n\n'
            '<b>Старое:</b>\n<blockquote>{}</blockquote>\n\n'
            '<b>Новое:</b>\n<blockquote><a href="{message_url}">{}</a></blockquote>'
        ),
        "mode_off": f"{pm} <b>Не отслеживаю сообщения </b><code>{{}}spymode</code>\n",
        "cfg_enable_pm": "Включить режим шпиона в личных сообщениях",
        "cfg_enable_groups": "Включить режим шпиона в группах",
        "cfg_whitelist": "Список чатов, от которых нужно сохранять сообщения",
        "cfg_blacklist": "Список чатов, от которых нужно игнорировать сообщения",
        "cfg_always_track": "Список чатов, от которых всегда следует отслеживать сообщения, несмотря ни на что",
        "cfg_log_edits": "Сохранять отредактированные сообщения",
        "cfg_ignore_inline": "Игнорировать сообщения из инлайн-режима",
        "cfg_fw_protect": "Защита от флудвейтов при пересылке",
        "sd_media": "🔥 <b><a href='tg://user?id={}'>{}</a> отправил вам самоуничтожающееся медиа</b>",
        "save_sd": "<emoji document_id=5420315771991497307>🔥</emoji> <b>Сохраняю самоуничтожающиеся медиа</b>\n",
        "cfg_save_sd": "Сохранять самоуничтожающееся медиа",
    }

    def __init__(self):
        self._tl_channel = None
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
        )

        self._queue = []
        self._cache = {}
        self._next = 0
        self._threshold = 10
        self._flood_protect_sample = 60

    @loader.loop(interval=0.1, autostart=True)
    async def sender(self):
        if not self._queue or self._next > time.time():
            return

        item = self._queue.pop(0)
        await item
        self._next = int(time.time()) + self.config["fw_protect"]

    @staticmethod
    def _int(value: typing.Union[str, int], /) -> typing.Union[str, int]:
        return int(value) if str(value).isdigit() else value

    @property
    def blacklist(self):
        return list(
            map(
                self._int,
                self.config["blacklist"]
                + [777000, self._client.tg_id, self._tl_channel, self.inline.bot_id],
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
        return list(map(self._int, self.config["whitelist"]))

    @whitelist.setter
    def whitelist(self, value: list):
        self.config["whitelist"] = value

    @property
    def always_track(self):
        return list(map(self._int, self.config["always_track"]))

    async def client_ready(self):
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

    @loader.command(
        ru_doc="Включить/выключить шпиона",
    )
    async def spymode(self, message: Message):
        await utils.answer(
            message,
            self.strings("state").format(
                self.strings("off" if self.get("state", False) else "on")
            ),
        )
        self.set("state", not self.get("state", False))

    @loader.command(
        ru_doc="Добавить/удалить чат из списка игнора",
    )
    async def spybl(self, message: Message):
        chat = utils.get_chat_id(message)
        if chat in self.blacklist:
            self.blacklist = list(set(self.blacklist) - {chat})
            await utils.answer(message, self.strings("spybl_removed"))
        else:
            self.blacklist = list(set(self.blacklist) | {chat})
            await utils.answer(message, self.strings("spybl"))

    @loader.command(
        ru_doc="Очистить черный список",
    )
    async def spyblclear(self, message: Message):
        self.blacklist = []
        await utils.answer(message, self.strings("spybl_clear"))

    @loader.command(
        ru_doc="Добавить/удалить чат из белого списка",
    )
    async def spywl(self, message: Message):
        chat = utils.get_chat_id(message)
        if chat in self.whitelist:
            self.whitelist = list(set(self.whitelist) - {chat})
            await utils.answer(message, self.strings("spywl_removed"))
        else:
            self.whitelist = list(set(self.whitelist) | {chat})
            await utils.answer(message, self.strings("spywl"))

    @loader.command(
        ru_doc="Очистить белый список",
    )
    async def spywlclear(self, message: Message):
        self.whitelist = []
        await utils.answer(message, self.strings("spywl_clear"))

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

    @loader.command(
        ru_doc="Показать текущую конфигурацию спай-мода",
    )
    async def spyinfo(self, message: Message):
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

        if self.config["enable_pm"]:
            info += self.strings("pm")

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

    async def _message_deleted(self, msg_obj: Message, caption: str):
        caption = self.inline.sanitise_text(caption)

        if not msg_obj.photo and not msg_obj.video and not msg_obj.document:
            self._queue += [
                self.inline.bot.send_message(
                    self._channel,
                    caption,
                    disable_web_page_preview=True,
                )
            ]
            return

        if msg_obj.sticker:
            self._queue += [
                self.inline.bot.send_message(
                    self._channel,
                    caption + "\n\n&lt;sticker&gt;",
                    disable_web_page_preview=True,
                )
            ]
            return

        file = io.BytesIO(await self._client.download_media(msg_obj, bytes))
        args = (self._channel, file)
        kwargs = {"caption": caption}
        if msg_obj.photo:
            file.name = "photo.jpg"
            self._queue += [self.inline.bot.send_photo(*args, **kwargs)]
        elif msg_obj.video:
            file.name = "video.mp4"
            self._queue += [self.inline.bot.send_video(*args, **kwargs)]
        elif msg_obj.voice:
            file.name = "audio.ogg"
            self._queue += [self.inline.bot.send_voice(*args, **kwargs)]
        elif msg_obj.document:
            file.name = next(
                attr.file_name
                for attr in msg_obj.document.attributes
                if isinstance(attr, DocumentAttributeFilename)
            )
            self._queue += [self.inline.bot.send_document(*args, **kwargs)]

    async def _message_edited(self, caption: str, msg_obj: Message):
        args = (
            self._channel,
            await self._client.download_media(msg_obj, bytes),
        )
        kwargs = {"caption": self.inline.sanitise_text(caption)}
        if msg_obj.photo:
            self._queue += [self.inline.bot.send_photo(*args, **kwargs)]
        elif msg_obj.video:
            self._queue += [self.inline.bot.send_video(*args, **kwargs)]
        elif msg_obj.voice:
            self._queue += [self.inline.bot.send_voice(*args, **kwargs)]
        elif msg_obj.document:
            self._queue += [self.inline.bot.send_document(*args, **kwargs)]
        else:
            self._queue += [
                self.inline.bot.send_message(
                    self._channel,
                    self.inline.sanitise_text(caption),
                    disable_web_page_preview=True,
                )
            ]

    @loader.raw_handler(UpdateEditChannelMessage)
    async def channel_edit_handler(self, update: UpdateEditChannelMessage):
        if (
            not self.get("state", False)
            or update.message.out
            or (self.config["ignore_inline"] and update.message.via_bot_id)
        ):
            return

        key = f"{utils.get_chat_id(update.message)}/{update.message.id}"
        if key in self._cache and (
            utils.get_chat_id(update.message) in self.always_track
            or self._cache[key].sender_id in self.always_track
            or (
                self.config["log_edits"]
                and self.config["enable_groups"]
                and utils.get_chat_id(update.message) not in self.blacklist
                and (
                    not self.whitelist
                    or utils.get_chat_id(update.message) in self.whitelist
                )
            )
        ):
            msg_obj = self._cache[key]
            if not msg_obj.sender.bot and update.message.raw_text != msg_obj.raw_text:
                sender = await self._client.get_entity(msg_obj.sender_id, exp=0)
                username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""
                await self._message_edited(
                    self.strings("edited_chat").format(
                        utils.get_entity_url(sender),
                        utils.escape_html(get_display_name(sender)),
                        username,
                        utils.get_entity_url(msg_obj.chat),
                        utils.escape_html(get_display_name(msg_obj.chat)),
                        msg_obj.text,
                        update.message.text,
                        message_url=await utils.get_message_link(msg_obj),
                    ),
                    msg_obj,
                )

        self._cache[key] = update.message

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

    @loader.raw_handler(UpdateEditMessage)
    async def pm_edit_handler(self, update: UpdateEditMessage):
        if (
            not self.get("state", False)
            or update.message.out
            or (self.config["ignore_inline"] and update.message.via_bot_id)
        ):
            return

        key = update.message.id
        msg_obj = self._cache.get(key)
        if (
            key in self._cache
            and (
                self._cache[key].sender_id in self.always_track
                or (utils.get_chat_id(self._cache[key]) in self.always_track)
                or (
                    self.config["log_edits"]
                    and self._should_capture(
                        self._cache[key].sender_id,
                        utils.get_chat_id(self._cache[key]),
                    )
                )
                and (
                    (
                        self.config["enable_pm"]
                        and not isinstance(msg_obj.peer_id, PeerChat)
                        or self.config["enable_groups"]
                        and isinstance(msg_obj.peer_id, PeerChat)
                    )
                )
            )
            and update.message.raw_text != msg_obj.raw_text
        ):
            sender = await self._client.get_entity(msg_obj.sender_id, exp=0)
            if not sender.bot:
                username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""
                chat = (
                    await self._client.get_entity(
                        msg_obj.peer_id.chat_id,
                        exp=0,
                    )
                    if isinstance(msg_obj.peer_id, PeerChat)
                    else None
                )
                await self._message_edited(
                    (
                        self.strings("edited_chat").format(
                            utils.get_entity_url(sender),
                            utils.escape_html(get_display_name(sender)),
                            username,
                            utils.get_entity_url(chat),
                            utils.escape_html(get_display_name(chat)),
                            msg_obj.text,
                            update.message.text,
                            message_url=await utils.get_message_link(msg_obj),
                        )
                        if isinstance(msg_obj.peer_id, PeerChat)
                        else self.strings("edited_pm").format(
                            utils.get_entity_url(sender),
                            utils.escape_html(get_display_name(sender)),
                            username,
                            msg_obj.text,
                            update.message.text,
                            message_url=await utils.get_message_link(msg_obj),
                        )
                    ),
                    msg_obj,
                )

        self._cache[update.message.id] = update.message

    @loader.raw_handler(UpdateDeleteMessages)
    async def pm_delete_handler(self, update: UpdateDeleteMessages):
        if not self.get("state", False):
            return

        for message in update.messages:
            if message not in self._cache:
                continue

            msg_obj = self._cache.pop(message)

            if (
                msg_obj.sender_id not in self.always_track
                and utils.get_chat_id(msg_obj) not in self.always_track
                and (
                    not self._should_capture(
                        msg_obj.sender_id, utils.get_chat_id(msg_obj)
                    )
                    or (self.config["ignore_inline"] and msg_obj.via_bot_id)
                    or (
                        not self.config["enable_groups"]
                        and isinstance(msg_obj.peer_id, PeerChat)
                    )
                    or (
                        not self.config["enable_pm"]
                        and not isinstance(msg_obj.peer_id, PeerChat)
                    )
                )
            ):
                continue

            sender = await self._client.get_entity(msg_obj.sender_id, exp=0)

            if sender.bot:
                continue

            username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""
            chat = (
                await self._client.get_entity(msg_obj.peer_id.chat_id, exp=0)
                if isinstance(msg_obj.peer_id, PeerChat)
                else None
            )

            await self._message_deleted(
                msg_obj,
                (
                    self.strings("deleted_chat").format(
                        utils.get_entity_url(sender),
                        utils.escape_html(get_display_name(sender)),
                        username,
                        utils.get_entity_url(chat),
                        utils.escape_html(get_display_name(chat)),
                        msg_obj.text,
                    )
                    if isinstance(msg_obj.peer_id, PeerChat)
                    else self.strings("deleted_pm").format(
                        utils.get_entity_url(sender),
                        utils.escape_html(get_display_name(sender)),
                        username,
                        msg_obj.text,
                    )
                ),
            )

    @loader.raw_handler(UpdateDeleteChannelMessages)
    async def channel_delete_handler(self, update: UpdateDeleteChannelMessages):
        if not self.get("state", False):
            return

        for message in update.messages:
            key = f"{update.channel_id}/{message}"
            if key not in self._cache:
                continue

            msg_obj = self._cache.pop(key)

            if (
                msg_obj.sender_id in self.always_track
                or utils.get_chat_id(msg_obj) in self.always_track
                or self.config["enable_groups"]
                and (
                    self._should_capture(
                        msg_obj.sender_id,
                        utils.get_chat_id(msg_obj),
                    )
                    and (not self.config["ignore_inline"] or not msg_obj.via_bot_id)
                    and not msg_obj.sender.bot
                )
            ):
                sender = await self._client.get_entity(msg_obj.sender_id, exp=0)
                username = f" (@{sender.username})" if getattr(sender, 'username', None) else ""
                await self._message_deleted(
                    msg_obj,
                    self.strings("deleted_chat").format(
                        utils.get_entity_url(sender),
                        utils.escape_html(get_display_name(sender)),
                        username,
                        utils.get_entity_url(msg_obj.chat),
                        utils.escape_html(get_display_name(msg_obj.chat)),
                        msg_obj.text,
                    ),
                )

    @loader.watcher("in")
    async def watcher(self, message: Message):
        if (
            self.config["save_sd"]
            and getattr(message, "media", False)
            and getattr(message.media, "ttl_seconds", False)
        ):
            media = io.BytesIO(await self.client.download_media(message.media, bytes))
            media.name = "sd.jpg" if message.photo else "sd.mp4"
            sender = await self.client.get_entity(message.sender_id, exp=0)
            await (
                self.inline.bot.send_photo
                if message.photo
                else self.inline.bot.send_video
            )(
                self._channel,
                media,
                caption=self.strings("sd_media").format(
                    utils.get_entity_url(sender),
                    utils.escape_html(get_display_name(sender)),
                ),
            )

        with contextlib.suppress(AttributeError):
            self._cache[
                (
                    message.id
                    if message.is_private or isinstance(message.peer_id, PeerChat)
                    else f"{utils.get_chat_id(message)}/{message.id}"
                )
            ] = message