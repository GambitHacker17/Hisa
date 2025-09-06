# meta developer: @MartyyyK

import asyncio
import contextlib
import logging
import time
import re
from typing import Union

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest, ReportSpamRequest
from telethon.tl.types import Channel, Message, PeerUser, User
from telethon.utils import get_display_name, get_peer_id

from .. import loader, utils

logger = logging.getLogger(__name__)

def format_(state: Union[bool, None]) -> str:
    if state is None:
        return "❔"

    return "✅" if state else "🚫 Not"

@loader.tds
class DND(loader.Module):
    """
    Prevents people sending you unsolicited private messages
    """

    strings = {
        "name": "DND",
        "_cfg_active_threshold": (
            "What number of your messages is required to trust peer."
        ),
        "_cfg_custom_msg": (
            "Custom message to notify untrusted peers. Leave empty for default one."
        ),
        "_cfg_delete_dialog": "If set to true, dialog will be deleted after banning.",
        "_cfg_ignore_active": "If set to true, ignore peers, where you participated.",
        "_cfg_ignore_contacts": "If set to true, ignore contacts.",
        "_cfg_photo": "Photo, which is sent along with banned notification.",
        "_cfg_dnd": "If set to true, DND is active.",
        "_cfg_report_spam": "If set to true, user will be reported after banning.",
        "_log_msg_approved": "User approved in pm {}, filter: {}",
        "_log_msg_punished": "Intruder punished: {}",
        "_log_msg_unapproved": "User unapproved in pm {}.",
        "approved": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> approved in pm.</b>',
        "args_incorrect": "<b>🚫 Args are incorrect.</b>",
        "args_pmban": "ℹ️ <b>Example usage: </b><code>.pmbanlast 5</code>",
        "banned": (
            " <b>Hello •ᴗ•</b>\n<b>Unit «SIGMA»<b> – <b>guardian</b> of this"
            " account.\nYou <b>not approved</b>!"
            " \n<b>I need to ban you in terms of security.</b>" 
        ),
        "banned_log": (
            "👮 <b>I banned {}.</b>\n\n<b>{} Contact</b>\n<b>{} Started by"
            " you</b>\n<b>{} Active conversation</b>\n\n<b>✊"
            " Actions</b>\n\n<b>{} Reported spam</b>\n<b>{} Deleted"
            " dialog</b>\n<b>{} Blocked</b>\n\n<b>ℹ️"
            " Message</b>\n<code>{}</code>"
        ),
        "blocked": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> blocked.</b>',
        "hello": (
            "🔏 <b>Unit «SIGMA»</b> protects your personal messages from"
            " intrusions. It will block everyone, who's trying to invade"
            " you.\n\nUse <code>.pmbanlast</code> if you've already been"
            " pm-raided."
        ),
        "no_pchat": "<b>This command is only available in private chats.</b>",
        "no_reply": "ℹ️ <b>Reply to a message to block the user.</b>",
        "pm_reported": "⚠️ <b>You just got reported to spam !</b>",
        "removed": "😶‍🌫️ <b>Removed {} last dialogs!</b>",
        "removing": "😶‍🌫️ <b>Removing {} last dialogs...</b>",
        "unapproved": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> unapproved in pm.</b>',
        "unblocked": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> unblocked.</b>',
        "user_not_specified": "🚫 <b>You haven't specified user.</b>",
    }

    strings_ru = {
        "_cfg_active_threshold": (
            "Какое количество Ваших сообщений необходимо, чтобы доверять пользователю."
        ),
        "_cfg_custom_msg": (
            "Кастомное оповещение неодобренных пользователей. Оставьте пустым,"
            " чтобы оставить по умолчанию."
        ),
        "_cfg_delete_dialog": (
            "Если установлено true, диалог будет удалён после блокировки."
        ),
        "_cfg_ignore_active": (
            "Если установлено true, игнорирует диалоги, где вы участвовали."
        ),
        "_cfg_ignore_contacts": "Если установлено true, игнорирует контакты.",
        "_cfg_photo": "Фото, которое отправляется вместе с уведомлением о блокировке",
        "_cfg_dnd": "Если установлено true, DND активирован.",
        "_cfg_report_spam": (
            "Если установлено true, после блокировки на пользователя будет"
            " отправлена жалоба о спаме."
        ),
        "_cls_doc": (
            "Запрещает пользователям отправлять вам личные сообщения"
        ),
        "_cmd_doc_allowpm": (
            "<ответ или username> - разрешает пользователю писать вам в ЛС"
        ),
        "_cmd_doc_block": "<ответ> - блокирует этого пользователя без предупреждения",
        "_cmd_doc_cdnd": "откроет конфиг для модуля.",
        "_cmd_doc_denypm": (
            "<ответ или username> - запрещает пользователю писать вам в ЛС"
        ),
        "_cmd_doc_pmbanlast": (
            "<число> - Блокирует и удаляет диалоги с N количеством новых"
            " пользователей"
        ),
        "_cmd_doc_reportpm": (
            "<ответ> - отправляет жалобу на пользователя на СПАМ"
        ),
        "_cmd_doc_unblock": "<ответ> - разблокировать этого пользователя",
        "_log_msg_approved": "Пользователь {} допущен в ЛС, фильтр: {}",
        "_log_msg_punished": "Нарушитель наказан: {}",
        "_log_msg_unapproved": "Пользователь {} не допущен к ЛС.",
        "approved": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> допущен к ЛС.</b>',
        "args_incorrect": "<b>🚫 Аргументы некорректны.</b>",
        "args_pmban": "ℹ️ <b>Пример использования: </b><code>.pmbanlast 5</code>",
        "banned": (
            " <b>Привет •ᴗ•</b>\n<b>Юнит «SIGMA»<b> – <b>защитник</b> этого"
            " аккаунта.\nВы <b>не подтверждены!</b>"
            " \n<b>Я должен заблокировать Вас из соображений безопасности.</b>"
        ),
        "banned_log": (
            "👮 <b>Я заблокировал {}.</b>\n\n<b>{} Контакт</b>\n<b>{} Начатый"
            " тобой</b>\n<b>{} Активный диалог</b>\n\n<b>✊"
            " Действия</b>\n\n<b>{} Сообщить о спаме</b>\n<b>{} Удалить"
            " диалог</b>\n<b>{} Заблокировать</b>\n\n<b>ℹ️"
            " Сообщение</b>\n<code>{}</code>"
        ),
        "blocked": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> заблокирован.</b>',
        "hello": (
            "🔏 <b>Юнит «SIGMA»</b> защищает ваши личные сообщения от нежелательного"
            " контакта. Это будет блокировать всех, кто попытается связаться с"
            " Вами..\n\nИспользуй <code>.pmbanlast</code> если уже были попытки"
            " нежелательного вторжения."
        ),
        "no_pchat": "<b>Эта команда работает только в ЛС.</b>",
        "no_reply": (
            "ℹ️ <b>Ответьте на сообщение, чтобы заблокировать пользователя.</b>"
        ),
        "pm_reported": "⚠️ <b>Отправил жалобу на спам!</b>",
        "removed": "😶‍🌫️ <b>Удалил {} последних диалогов!</b>",
        "removing": "😶‍🌫️ <b>Удаляю {} последних диалогов...</b>",
        "unapproved": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> не допущен к ЛС.</b>',
        "unblocked": '😶‍🌫️ <b><a href="tg://user?id={}">{}</a> разблокирован.</b>',
        "user_not_specified": "🚫 <b>Вы не указали пользователя.</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "DND_Active",
                True,
                doc=lambda: self.strings("_cfg_dnd"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "active_threshold",
                5,
                doc=lambda: self.strings("_cfg_active_threshold"),
                validator=loader.validators.Integer(minimum=1),
            ),
            loader.ConfigValue(
                "custom_message",
                doc=lambda: self.strings("_cfg_custom_msg"),
            ),
            loader.ConfigValue(
                "delete_dialog",
                False,
                doc=lambda: self.strings("_cfg_delete_dialog"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "ignore_active",
                True,
                doc=lambda: self.strings("_cfg_ignore_active"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "ignore_contacts",
                True,
                doc=lambda: self.strings("_cfg_ignore_contacts"),
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "photo",
                "https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/unit_sigma.png",
                doc=lambda: self.strings("_cfg_photo"),
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "report_spam",
                False,
                doc=lambda: self.strings("_cfg_report_spam"),
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self):
        self._ratelimit_dnd = []
        self._ratelimit_dnd_threshold = 10
        self._ratelimit_dnd_timeout = 5 * 60
        self._whitelist = self.get("whitelist", [])
        if not self.get("ignore_hello", False):
            await self.inline.bot.send_photo(
                self.tg_id,
                photo="https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/unit_sigma.png",
                caption=self.strings("hello"),
                parse_mode="HTML",
            )
            self.set("ignore_hello", True)

    def _approve(self, user: int, reason: str = "unknown"):
        self._whitelist += [user]
        self._whitelist = list(set(self._whitelist))
        self.set("whitelist", self._whitelist)
        if reason != "blocked":
            logger.info(self.strings("_log_msg_approved").format(user, reason))

    def _unapprove(self, user: int):
        self._whitelist = list(set(self._whitelist))
        self._whitelist = list(filter(lambda x: x != user, self._whitelist))
        self.set("whitelist", self._whitelist)
        logger.info(self.strings("_log_msg_unapproved").format(user))

    async def _send_dnd_message(
        self, message, peer, contact, started_by_you, active_peer, self_id
    ):
        if len(self._ratelimit_dnd) < self._ratelimit_dnd_threshold:
            try:
                await self._client.send_file(
                    peer,
                    self.config["photo"],
                    caption=self.config["custom_message"] or self.strings("banned"),
                )
            except Exception:
                await utils.answer(
                    message,
                    self.config["custom_message"] or self.strings("banned"),
                )

            self._ratelimit_dnd += [round(time.time())]

            try:
                peer = await self._client.get_entity(peer)
            except ValueError:
                await asyncio.sleep(1)
                peer = await self._client.get_entity(peer)

            await self.inline.bot.send_message(
                self_id,
                self.strings("banned_log").format(
                    await self._get_tag(peer, True),
                    format_(contact),
                    format_(started_by_you),
                    format_(active_peer),
                    format_(self.config["report_spam"]),
                    format_(self.config["delete_dialog"]),
                    format_(True),
                    self._raw_text(message)[:3000],
                ),
                parse_mode="HTML",
                disable_web_page_preview=True,
            )

    async def _active_peer(self, cid, peer):
        if self.config["ignore_active"]:
            q = 0

            async for msg in self._client.iter_messages(peer, limit=200):
                if msg.sender_id == self.tg_id:
                    q += 1

                if q >= self.config["active_threshold"]:
                    self._approve(cid, "active_threshold")
                    return True
        return False

    async def _punish_handler(self, cid):
        await self._client(BlockRequest(id=cid))
        if self.config["report_spam"]:
            await self._client(ReportSpamRequest(peer=cid))

        if self.config["delete_dialog"]:
            await self._client(
                DeleteHistoryRequest(peer=cid, just_clear=True, max_id=0)
            )

    async def cdndcmd(self, message: Message):
        """
        open config for this module
        """
        name = self.strings("name")
        await self.allmodules.commands["config"](
            await utils.answer(message, f"{self.get_prefix()}config {name}")
        )

    async def pmbanlastcmd(self, message: Message):
        """
        <number> - ban and delete dialogs with N most new users
        """
        n = utils.get_args_raw(message)
        if not n or not n.isdigit():
            await utils.answer(message, self.strings("args_pmban"))
            return

        n = int(n)

        await utils.answer(message, self.strings("removing").format(n))

        dialogs = []
        async for dialog in self._client.iter_dialogs(ignore_pinned=True):
            try:
                if not isinstance(dialog.message.peer_id, PeerUser):
                    continue
            except AttributeError:
                continue

            m = (
                await self._client.get_messages(
                    dialog.message.peer_id,
                    limit=1,
                    reverse=True,
                )
            )[0]

            dialogs += [
                (
                    get_peer_id(dialog.message.peer_id),
                    int(time.mktime(m.date.timetuple())),
                )
            ]

        dialogs.sort(key=lambda x: x[1])
        to_ban = [d for d, _ in dialogs[::-1][:n]]

        for d in to_ban:
            await self._client(BlockRequest(id=d))

            await self._client(DeleteHistoryRequest(peer=d, just_clear=True, max_id=0))

        await utils.answer(message, self.strings("removed").format(n))

    async def allowpmcmd(self, message: Message):
        """
        <reply or user> - allow user to pm you
        """
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        user = None

        try:
            user = await self._client.get_entity(args)
        except Exception:
            with contextlib.suppress(Exception):
                user = await reply.get_sender() if reply else None

        if not user:
            chat = await message.get_chat()
            if not isinstance(chat, User):
                await utils.answer(message, self.strings("user_not_specified"))
                return

            user = chat

        self._approve(user.id, "manual_approve")
        await utils.answer(
            message,
            self.strings("approved").format(user.id, get_display_name(user)),
        )

    async def denypmcmd(self, message: Message):
        """
        <reply or user> - deny user to pm you
        """
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        user = None

        try:
            user = await self._client.get_entity(int(args))
            if not isinstance(user, User):
                user = None
        except Exception:
            with contextlib.suppress(Exception):
                user = await reply.get_sender() if reply else None

        if not user:
            chat = await message.get_chat()
            if not isinstance(chat, User):
                await utils.answer(message, self.strings("user_not_specified"))
                return

            user = chat

        self._unapprove(user.id)
        await utils.answer(
            message,
            self.strings("unapproved").format(user.id, get_display_name(user)),
        )

    async def reportpmcmd(self, message: Message):
        """
        <reply> - report the user to spam
        """
        if not message.is_private:
            await utils.answer(message, self.strings("no_pchat"))
            return
        user = await message.get_chat()
        await message.client(ReportSpamRequest(peer=user.id))
        await utils.answer(message, self.strings("pm_reported"))

    async def blockcmd(self, message: Message):
        """
        <reply> - block this user without being warned
        """
        user = await utils.get_target(message)
        user = await self._client.get_entity(user)
        if not user:
            await utils.answer(message, self.strings("no_reply"))
            return
        await message.client(BlockRequest(user.id))
        await utils.answer(
            message,
            self.strings("blocked").format(user.id, get_display_name(user)),
        )

    async def unblockcmd(self, message: Message):
        """
        <reply> - unblock this user
        """
        user = await utils.get_target(message)
        user = await self._client.get_entity(user)
        if not user:
            await utils.answer(message, self.strings("no_reply"))
            return
        await message.client(UnblockRequest(user.id))
        await utils.answer(
            message,
            self.strings("unblocked").format(user.id, get_display_name(user)),
        )

    @loader.watcher("only_messages", "in")
    async def watcher(self, message: Message):
        chat_id = utils.get_chat_id(message)
        if chat_id in {
            1271266957,
            777000,
            self.tg_id,
        }:
            return
        try:
            if (
                self.config["DND_Active"]
                and message.is_private
                and not isinstance(message, Channel)
                and isinstance(message.peer_id, PeerUser)
            ):
                peer = (
                    getattr(getattr(message, "sender", None), "username", None)
                    or message.peer_id
                )
                await self.p__dnd(peer, message)
            return
        except ValueError as exc:
            logger.debug(exc)

    async def p__dnd(
        self,
        peer,
        message: Union[None, Message] = None,
    ) -> bool:
        cid = utils.get_chat_id(message)
        if cid in self._whitelist:
            return

        contact, started_by_you, active_peer = None, None, None

        with contextlib.suppress(ValueError):
            entity = await message.get_sender()
            if entity.bot:
                return self._approve(cid, "bot")

            if self.config["ignore_contacts"]:
                if entity.contact:
                    return self._approve(cid, "ignore_contacts")
                contact = False

        first_message = (
            await self._client.get_messages(
                peer,
                limit=1,
                reverse=True,
            )
        )[0]

        if (
            getattr(message, "raw_text", False)
            and first_message.sender_id == self.tg_id
        ):
            return self._approve(cid, "started_by_you")
        started_by_you = False

        active_peer = await self._active_peer(cid, peer)
        if active_peer:
            return

        self._ratelimit_dnd = list(
            filter(
                lambda x: x + self._ratelimit_dnd_timeout < time.time(),
                self._ratelimit_dnd,
            )
        )

        await self._send_dnd_message(
            message, peer, contact, started_by_you, active_peer, self.tg_id
        )
        await self._punish_handler(cid)

        self._approve(cid, "blocked")
        logger.warning(self.strings("_log_msg_punished").format(cid))
        return True

    def _raw_text(self, message: Message, keep_custom_emoji: bool = False) -> str:
        return self._remove_html(message.text, keep_emoji_tag=keep_custom_emoji)

    def _remove_html(self, text: str, escape: bool = False, keep_emoji_tag: bool = False) -> str:
        html_regex = (
            r"(<\/?a.*?>|<\/?b>|<\/?i>|<\/?u>|<\/?strong>|<\/?em>|<\/?code>|<\/?strike>|<\/?del>|<\/?pre.*?>|<\/?br>)"
            if keep_emoji_tag
            else r"(<\/?a.*?>|<\/?b>|<\/?i>|<\/?u>|<\/?strong>|<\/?em>|<\/?code>|<\/?strike>|<\/?del>|<\/?pre.*?>|<\/?br>|<\/?emoji.*?>)"
        )
        return (self._escape_html if escape else self._unescape_html)(
            re.sub(html_regex, "", text)
        )

    @staticmethod
    def _unescape_html(text: str) -> str:
        import html
        return html.unescape(text)

    @staticmethod
    def _escape_html(text: str) -> str:
        import html
        return html.escape(text)

    async def _get_tag(self, user, WithID: bool = False) -> str:
        from telethon.utils import get_display_name
        user = await self._client.get_entity(user) if isinstance(user, int) else user
        if isinstance(user, Channel):
            if WithID:
                return (
                    f"<a href='tg://resolve?domain={user.username}'>{user.title}</a>"
                    f" (<code>{str(user.id)}</code>)"
                    if user.username
                    else f"{user.title}(<code>{str(user.id)}</code>)"
                )
            return (
                f"<a href='tg://resolve?domain={user.username}'>{user.title}</a>"
                if user.username
                else f"{user.title}"
            )
        if WithID:
            return (
                f"<a href='tg://resolve?domain={user.username}'>{get_display_name(user)}</a>"
                f" (<code>{str(user.id)}</code>)"
                if user.username
                else (
                    f"<a href='tg://user?id={str(user.id)}'>{get_display_name(user)}</a>"
                    f" (<code>{str(user.id)}</code>)"
                )
            )
        return (
            f"<a href='tg://resolve?domain={user.username}'>{get_display_name(user)}</a>"
            if user.username
            else f"<a href='tg://user?id={str(user.id)}'>{get_display_name(user)}</a>"
        )