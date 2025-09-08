# meta developer: @MartyyyK

import contextlib
import logging
import time
from typing import Optional

from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest, ReportSpamRequest
from telethon.tl.types import Message, PeerUser, User
from telethon.utils import get_display_name, get_peer_id

from .. import loader, utils

logger = logging.getLogger(__name__)

def format_(state: Optional[bool]) -> str:
    if state is None:
        return "❔"

    return "🫡" if state else "🙅‍♂️ Not"

@loader.tds
class PMBLMod(loader.Module):

    strings = {
        "name": "PMBL",
        "state": (
            "<emoji document_id=5314803591058301611>🛡</emoji> <b>PM->BL is now"
            " {}</b>\n<i>Report spam? - {}\nDelete dialog? - {}</i>"
        ),
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Usage example:"
            " </b><code>.pmblsett 0 0</code>"
        ),
        "args_pmban": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Usage example:"
            " </b><code>.pmbanlast 5</code>"
        ),
        "banned": (
            "😃 <b>Hey there"
            " •ᴗ•</b>\n<b>Unit «SIGMA»<b> - the <b>guardian</b> of this account. You are"
            " <b>not approved</b>!"
            "\n<b>I need to ban you in terms of security.</b>"
        ),
        "removing": (
            "<emoji document_id=5456529570431770384>🚮</emoji> <b>Removing {} last"
            " dialogs...</b>"
        ),
        "removed": (
            "<emoji document_id=5456529570431770384>🚮</emoji> <b>Removed {} last"
            " dialogs!</b>"
        ),
        "user_not_specified": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>You haven't specified"
            " user</b>"
        ),
        "approved": (
            "<emoji document_id=5461129450341014019>✋</emoji> <b><a"
            ' href="tg://user?id={}">{}</a> approved in pm</b>'
        ),
        "banned_log": (
            '👮 <b>I banned <a href="tg://user?id={}">{}</a>.</b>\n\n<b>{} Reported'
            " spam</b>\n<b>{} Deleted dialog</b>\n\n<b>"
            " 📝 Message</b>\n<code>{}</code>"
        ),
        "hello": (
            "🔏 <b>Unit «SIGMA»</b> protects your personal messages from intrusions. It"
            " will block everyone, who's trying to invade you.\n\nUse"
            " <code>pmbl</code> to enable protection, <code>pmblsett</code> to"
            " configure it and <code>pmbanlast</code> if you've already been"
            " pm-raided."
        ),
    }

    strings_ru = {
        "state": (
            "<emoji document_id=5314803591058301611>🛡</emoji> <b>Текущее состояние"
            " PM->BL: {}</b>\n<i>Сообщать о спаме? - {}\nУдалять диалог? - {}</i>"
        ),
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Пример:"
            " </b><code>.pmblsett 0 0</code>"
        ),
        "args_pmban": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Пример:"
            " </b><code>.pmbanlast 5</code>"
        ),
        "banned": (
            "😃 <b>Добрый день"
            " •ᴗ•</b>\n<b>Юнит «SIGMA»<b> - <b>защитник</b> этого аккаунта. Вы <b>не"
            " потверждены</b>!"
            "\n<b>Я вынужден заблокировать вас из соображений"
            " безопасности.</b>"
        ),
        "hello": (
            "🔏 <b>Юнит «SIGMA»</b> защищает твои личные сообщения от неизвестных"
            " пользователей. Он будет блокировать всех, кто не соответствует"
            " настройкам.\n\nВведи <code>pmbl</code> для активации защиты,"
            " <code>pmblsett</code> для ее настройки и <code>pmbanlast</code> если"
            " нужно очистить уже прошедший рейд на личные сообщения."
        ),
        "removing": (
            "<emoji document_id=5456529570431770384>🚮</emoji> <b>Удаляю {} последних"
            " диалогов...</b>"
        ),
        "removed": (
            "<emoji document_id=5456529570431770384>🚮</emoji> <b>Удалил {} последних"
            " диалогов!</b>"
        ),
        "user_not_specified": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Укажи"
            " пользователя</b>"
        ),
        "_cmd_doc_pmbl": "- вкл/выкл защиту",
        "_cmd_doc_pmbanlast": (
            "<количество> - забанить и удалить n последних диалогов с пользователями"
        ),
        "_cmd_doc_allowpm": "<пользователь> - разрешить пользователю писать тебе в ЛС",
        "_cls_doc": "Блокирует и репортит входящие сообщения от незнакомцев",
        "approved": (
            "<emoji document_id=5461129450341014019>✋</emoji> <b><a"
            ' href="tg://user?id={}">{}</a> одобрен в лс</b>'
        ),
        "banned_log": (
            '👮 <b>Я заблокировал <a href="tg://user?id={}">{}</a>.</b>\n\n<b>{}'
            " Сообщил"
            " о спаме</b>\n<b>{} Удалил диалог</b>\n\n<b>📝"
            " Сообщение</b>\n<code>{}</code>"
        ),
    }

    def __init__(self):
        self._queue = []
        self._ban_queue = []
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "ignore_contacts",
                True,
                lambda: "Ignore contacts?",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "ignore_active",
                True,
                lambda: "Ignore peers, where you participated?",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "active_threshold",
                5,
                lambda: "What number of your messages is required to trust peer",
                validator=loader.validators.Integer(minimum=1),
            ),
            loader.ConfigValue(
                "custom_message",
                doc=lambda: "Custom message to notify untrusted peers. Leave empty for default one",
            ),
            loader.ConfigValue(
                "photo",
                "https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/unit_sigma.png",
                lambda: "Photo, which is sent along with banned notification",
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "report_spam",
                False,
                lambda: "Report spam?",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "delete_dialog",
                False,
                lambda: "Delete dialog?",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "silent",
                False,
                lambda: "Do not send anything to banned user",
                validator=loader.validators.Boolean(),
            ),
        )

    async def client_ready(self):
        self._whitelist = self.get("whitelist", [])
        self._ratelimit = []
        self._ratelimit_timeout = 5 * 60
        self._ratelimit_threshold = 10
        if not self.get("ignore_hello", False):
            await self.inline.bot.send_photo(
                self._tg_id,
                photo=(
                    r"https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/unit_sigma.png"
                ),
                caption=self.strings("hello"),
                parse_mode="HTML",
            )

            self.set("ignore_hello", True)

    async def pmblcmd(self, message: Message):
        current = self.get("state", False)
        new = not current
        self.set("state", new)
        await utils.answer(
            message,
            self.strings("state").format(
                "on" if new else "off",
                "yes" if self.config["report_spam"] else "no",
                "yes" if self.config["delete_dialog"] else "no",
            ),
        )

    async def pmbanlastcmd(self, message: Message):
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

    def _approve(self, user: int, reason: str = "unknown"):
        self._whitelist += [user]
        self._whitelist = list(set(self._whitelist))
        self.set("whitelist", self._whitelist)
        logger.debug(f"User approved in pm {user}, filter: {reason}")
        return

    async def allowpmcmd(self, message: Message):
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        user = None

        try:
            user = await self._client.get_entity(args)
        except Exception:
            with contextlib.suppress(Exception):
                user = await self._client.get_entity(reply.sender_id) if reply else None

        if not user:
            chat = await message.get_chat()
            if not isinstance(chat, User):
                await utils.answer(message, self.strings("user_not_specified"))
                return

            user = chat

        self._approve(user.id, "manual_approve")
        await utils.answer(
            message, self.strings("approved").format(user.id, get_display_name(user))
        )

    async def watcher(self, message: Message):
        if (
            getattr(message, "out", False)
            or not isinstance(message, Message)
            or not isinstance(message.peer_id, PeerUser)
            or not self.get("state", False)
            or utils.get_chat_id(message)
            in {
                1271266957,
                777000,
                self._tg_id,
            }
        ):
            return

        self._queue += [message]

    @loader.loop(interval=0.05, autostart=True)
    async def ban_loop(self):
        if not self._ban_queue:
            return

        message = self._ban_queue.pop(0)
        self._ratelimit = list(
            filter(
                lambda x: x + self._ratelimit_timeout < time.time(),
                self._ratelimit,
            )
        )

        dialog = None

        if len(self._ratelimit) < self._ratelimit_threshold:
            if not self.config["silent"]:
                try:
                    await self._client.send_file(
                        message.peer_id,
                        self.config["photo"],
                        caption=self.config["custom_message"] or self.strings("banned"),
                    )
                except Exception:
                    await utils.answer(
                        message,
                        self.config["custom_message"] or self.strings("banned"),
                    )

                self._ratelimit += [round(time.time())]

            try:
                dialog = await self._client.get_entity(message.peer_id)
            except ValueError:
                pass

        await self.inline.bot.send_message(
            self._client.tg_id,
            self.strings("banned_log").format(
                dialog.id if dialog is not None else message.sender_id,
                (
                    utils.escape_html(dialog.first_name)
                    if dialog is not None
                    else (
                        getattr(getattr(message, "sender", None), "username", None)
                        or message.sender_id
                    )
                ),
                format_(self.config["report_spam"]),
                format_(self.config["delete_dialog"]),
                utils.escape_html(
                    "<sticker"
                    if message.sticker
                    else (
                        "<photo>"
                        if message.photo
                        else (
                            "<video>"
                            if message.video
                            else (
                                "<file>"
                                if message.document
                                else message.raw_text[:3000]
                            )
                        )
                    )
                ),
            ),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )

        await self._client(BlockRequest(id=message.sender_id))

        if self.config["report_spam"]:
            await self._client(ReportSpamRequest(peer=message.sender_id))

        if self.config["delete_dialog"]:
            await self._client(
                DeleteHistoryRequest(peer=message.sender_id, just_clear=True, max_id=0)
            )

        self._approve(message.sender_id, "banned")

        logger.warning(f"Intruder punished: {message.sender_id}")

    @loader.loop(interval=0.01, autostart=True)
    async def queue_processor(self):
        if not self._queue:
            return

        message = self._queue.pop(0)

        cid = utils.get_chat_id(message)
        if cid in self._whitelist:
            return

        peer = (
            getattr(getattr(message, "sender", None), "username", None)
            or message.peer_id
        )

        with contextlib.suppress(ValueError):
            entity = await self._client.get_entity(peer)

            if entity.bot:
                return self._approve(cid, "bot")

            if self.config["ignore_contacts"]:
                if entity.contact:
                    return self._approve(cid, "ignore_contacts")

        first_message = (
            await self._client.get_messages(
                peer,
                limit=1,
                reverse=True,
            )
        )[0]

        if (
            getattr(message, "raw_text", False)
            and first_message.sender_id == self._tg_id
        ):
            return self._approve(cid, "started_by_you")

        if self.config["ignore_active"]:
            q = 0

            async for msg in self._client.iter_messages(peer, limit=200):
                if msg.sender_id == self._tg_id:
                    q += 1

                if q >= self.config["active_threshold"]:
                    return self._approve(cid, "active_threshold")

        self._ban_queue += [message]

    @loader.debug_method(name="unwhitelist")
    async def denypm(self, message: Message):
        user = (await message.get_reply_message()).sender_id
        self.set("whitelist", list(set(self.get("whitelist", [])) - {user}))
        return f"User unwhitelisted: {user}"