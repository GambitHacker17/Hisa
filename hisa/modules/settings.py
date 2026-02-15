import hisatl
import typing
import time
import os
import contextlib
import logging
from hisatl.extensions.html import CUSTOM_EMOJIS
from hisatl.tl.types import Message

from .. import loader, main, utils, version
from ..compat.dragon import DRAGON_EMOJI
from ..inline.types import InlineCall
from .._internal import restart

@loader.tds
class CoreMod(loader.Module):

    strings = {"name": "Settings"}

    async def _canceled_restart(self, call: InlineCall):
        await call.edit(self.strings("restartcancel"), reply_markup=None)

    async def blacklistcommon(self, message: Message):
        args = utils.get_args(message)

        if len(args) > 2:
            await utils.answer(message, self.strings("too_many_args"))
            return

        chatid = None
        module = None

        if args:
            try:
                chatid = int(args[0])
            except ValueError:
                module = args[0]

        if len(args) == 2:
            module = args[1]

        if chatid is None:
            chatid = utils.get_chat_id(message)

        module = self.allmodules.get_classname(module)
        return f"{str(chatid)}.{module}" if module else chatid

    @loader.command()
    async def hisacmd(self, message: Message):
        await utils.answer_file(
            message,
            "https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/Hisa_cmd.png",
            self.strings("hisa").format(
                (
                    "🌘 <b>Hisa userbot</b>"
                ),
                *version.__version__,
                "release",
                f"{hisatl.__version__} #{hisatl.tl.alltlobjects.LAYER}",
            )
            + (
                ""
                if version.branch == "master"
                else self.strings("unstable").format(version.branch)
            ),
        )

    @loader.command()
    async def blacklist(self, message: Message):
        chatid = await self.blacklistcommon(message)

        self._db.set(
            main.__name__,
            "blacklist_chats",
            self._db.get(main.__name__, "blacklist_chats", []) + [chatid],
        )

        await utils.answer(message, self.strings("blacklisted").format(chatid))

    @loader.command()
    async def unblacklist(self, message: Message):
        chatid = await self.blacklistcommon(message)

        self._db.set(
            main.__name__,
            "blacklist_chats",
            list(set(self._db.get(main.__name__, "blacklist_chats", [])) - {chatid}),
        )

        await utils.answer(message, self.strings("unblacklisted").format(chatid))

    async def getuser(self, message: Message):
        try:
            return int(utils.get_args(message)[0])
        except (ValueError, IndexError):
            if reply := await message.get_reply_message():
                return reply.sender_id

            return message.to_id.user_id if message.is_private else False

    @loader.command()
    async def blacklistuser(self, message: Message):
        if not (user := await self.getuser(message)):
            await utils.answer(message, self.strings("who_to_blacklist"))
            return

        self._db.set(
            main.__name__,
            "blacklist_users",
            self._db.get(main.__name__, "blacklist_users", []) + [user],
        )

        await utils.answer(message, self.strings("user_blacklisted").format(user))

    @loader.command()
    async def unblacklistuser(self, message: Message):
        if not (user := await self.getuser(message)):
            await utils.answer(message, self.strings("who_to_unblacklist"))
            return

        self._db.set(
            main.__name__,
            "blacklist_users",
            list(set(self._db.get(main.__name__, "blacklist_users", [])) - {user}),
        )

        await utils.answer(
            message,
            self.strings("user_unblacklisted").format(user),
        )

    @loader.command()
    async def setprefix(self, message: Message):
        if not (args := utils.get_args_raw(message)):
            await utils.answer(message, self.strings("what_prefix"))
            return

        if len(args.split()) == 2 and args.split()[0] == "dragon":
            args = args.split()[1]
            is_dragon = True
        else:
            is_dragon = False

        if len(args) != 1:
            await utils.answer(message, self.strings("prefix_incorrect"))
            return

        if args == "s":
            await utils.answer(message, self.strings("prefix_incorrect"))
            return

        if (
            not is_dragon
            and args[0] == self._db.get("dragon.prefix", "command_prefix", ",")
            or is_dragon
            and args[0] == self._db.get(main.__name__, "command_prefix", ".")
        ):
            await utils.answer(message, self.strings("prefix_collision"))
            return

        oldprefix = (
            f"dragon {utils.escape_html(self.get_prefix('dragon'))}"
            if is_dragon
            else utils.escape_html(self.get_prefix())
        )
        self._db.set(
            "dragon.prefix" if is_dragon else main.__name__,
            "command_prefix",
            args,
        )
        await utils.answer(
            message,
            self.strings("prefix_set").format(
                (
                    DRAGON_EMOJI
                    if is_dragon
                    else "<emoji document_id=5197474765387864959>👍</emoji>"
                ),
                newprefix=utils.escape_html(
                    self.get_prefix() if is_dragon else args[0]
                ),
                oldprefix=utils.escape_html(oldprefix),
            ),
        )

    @loader.command()
    async def aliases(self, message: Message):
        await utils.answer(
            message,
            self.strings("aliases")
            + "\n".join(
                [
                    f"▫️ <code>{i}</code> &lt;- {y}"
                    for i, y in self.allmodules.aliases.items()
                ]
            ),
        )

    @loader.command()
    async def addalias(self, message: Message):
        if len(args := utils.get_args(message)) != 2:
            await utils.answer(message, self.strings("alias_args"))
            return

        alias, cmd = args
        if self.allmodules.add_alias(alias, cmd):
            self.set(
                "aliases",
                {
                    **self.get("aliases", {}),
                    alias: cmd,
                },
            )
            await utils.answer(
                message,
                self.strings("alias_created").format(utils.escape_html(alias)),
            )
        else:
            await utils.answer(
                message,
                self.strings("no_command").format(utils.escape_html(cmd)),
            )

    @loader.command()
    async def delalias(self, message: Message):
        args = utils.get_args(message)

        if len(args) != 1:
            await utils.answer(message, self.strings("delalias_args"))
            return

        alias = args[0]

        if not self.allmodules.remove_alias(alias):
            await utils.answer(
                message,
                self.strings("no_alias").format(utils.escape_html(alias)),
            )
            return

        current = self.get("aliases", {})
        del current[alias]
        self.set("aliases", current)
        await utils.answer(
            message,
            self.strings("alias_removed").format(utils.escape_html(alias)),
        )

    @loader.command(
        ru_doc="Перезагрузить юзербота",
        en_doc="Restart the userbot"
    )
    async def restart(self, message: Message):
        args = utils.get_args_raw(message)
        secure_boot = any(trigger in args for trigger in {"--secure-boot", "-sb"})
        try:
            if (
                "-f" in args
                or not self.inline.init_complete
                or not await self.inline.form(
                    message=message,
                    text=self.strings(
                        "secure_boot_confirm" if secure_boot else "restart_confirm"
                    ),
                    reply_markup=[
                        {
                            "text": self.strings("btn_restart"),
                            "callback": self.inline_restart,
                            "args": (secure_boot,),
                        },
                        {"text": self.strings("cancel"), "action": "close",},
                    ],
                )
            ):
                raise
        except Exception:
            await self.restart_common(message, secure_boot)

    async def process_restart_message(self, msg_obj: typing.Union[InlineCall, Message]):
        self.set(
            "selfupdatemsg",
            (
                msg_obj.inline_message_id
                if hasattr(msg_obj, "inline_message_id")
                else f"{utils.get_chat_id(msg_obj)}:{msg_obj.id}"
            ),
        )

    async def inline_restart(self, call: InlineCall, secure_boot: bool = False):
        await self.restart_common(call, secure_boot=secure_boot)

    async def restart_common(
        self,
        msg_obj: typing.Union[InlineCall, Message],
        secure_boot: bool = False,
    ):
        if (
            hasattr(msg_obj, "form")
            and isinstance(msg_obj.form, dict)
            and "uid" in msg_obj.form
            and msg_obj.form["uid"] in self.inline._units
            and "message" in self.inline._units[msg_obj.form["uid"]]
        ):
            message = self.inline._units[msg_obj.form["uid"]]["message"]
        else:
            message = msg_obj

        if secure_boot:
            self._db.set(loader.__name__, "secure_boot", True)

        msg_obj = await utils.answer(
            msg_obj,
            self.strings("restarting_caption").format(
                "Hisa"
            ),
        )

        await self.process_restart_message(msg_obj)

        self.set("restart_ts", time.time())

        await self._db.remote_force_save()

        if "LAVHOST" in os.environ:
            os.system("lavhost restart")
            return

        with contextlib.suppress(Exception):
            await main.hisa.web.stop()

        handler = logging.getLogger().handlers[0]
        handler.setLevel(logging.CRITICAL)

        for client in self.allclients:
            if client is not message.client:
                await client.disconnect()

        await message.client.disconnect()
        restart()

    @loader.command()
    async def cleardb(self, message: Message):
        await self.inline.form(
            self.strings("confirm_cleardb"),
            message,
            reply_markup=[
                {
                    "text": self.strings("cleardb_confirm"),
                    "callback": self._inline__cleardb,
                },
                {
                    "text": self.strings("cancel"),
                    "action": "close",
                },
            ],
        )

    async def _inline__cleardb(self, call: InlineCall):
        self._db.clear()
        self._db.save()
        await utils.answer(call, self.strings("db_cleared"))
