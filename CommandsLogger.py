# meta developer: @MartyyyK

import logging

from telethon.tl.functions.channels import InviteToChannelRequest
from hisatl.tl.types import PeerUser, PeerChannel, PeerChat, Channel, User

from .. import loader
from .. import utils

logger = logging.getLogger(__name__)


@loader.tds
class HisaCommandsLoggerMod(loader.Module):
    '''Hisa Commands Logger'''

    strings = {
        "name": "CommandsLogger",
        "log-groups": (
            "<b>#GROUP\n\n"
            "┌ Command:\n├ « <code>{}</code> »\n"
            "├ From --> {}\n"
            "├ Chat --> {}\n"
            "└ Message Link --> <a href='https://t.me/c/{}/{}'>CLICK</a></b>"
        ),
        "log-pm": (
            "<b>#PM\n\n"
            "┌ Command:\n├ « <code>{}</code> »\n"
            "├ From --> {}\n"
            "├ Chat with --> {}\n"
            "└ Message Link --> <a href='tg://openmessage?user_id={}&message_id={}'>CLICK</a></b>"
        ),
        "log-channels": (
            "<b>#CHANNEL\n\n"
            "┌ Command:\n├ « <code>{}</code> »\n"
            "├ From --> {}\n"
            "├ Channel --> {}\n"
            "└ Message Link --> <a href='https://t.me/c/{}/{}'>CLICK</a></b>"
        ),
    }

    async def client_ready(self, client, _):
        self.chat_l, _ = await utils.asset_channel(
            client,
            "hisa-commands-logs",
            "💬 Chat for Hisa commands logger",
            silent=True,
            avatar="",
        )

        self.chat_logs = f"-100{self.chat_l.id}"

        logger.warning("[MartyyyK::HisaCommandsLogger] Commands logger started.")

    @loader.watcher(only_commands=True)
    async def watcher(self, message):
        is_pm = isinstance(message.peer_id, PeerUser)
        sender = await message.get_sender()
        is_channel = message.post or isinstance(sender, Channel)
        chat_id = (
            message.peer_id.user_id
            if is_pm
            else message.peer_id.chat_id
            if isinstance(message.peer_id, PeerChat)
            else message.peer_id.channel_id
            if isinstance(message.peer_id, PeerChannel)
            else self.hisa_me.id
        )

        chat = await self._client.get_entity(chat_id)
        chat_username = getattr(chat, "username", None)

        user_link = (
            f"<a href='https://t.me/{sender.username}'>{sender.first_name if not is_channel else sender.title}</a>"
            if sender.username
            else f"<a href=tg://user?id={sender.id}>{sender.first_name if not is_channel else sender.title}</a>"
        )
        chat_link = (
            f"<a href='https://t.me/{chat_username}'>{chat.title}</a>"
            if chat_username
            else chat.title
        ) if not is_pm else (
            f"<a href='https://t.me/{chat.username}'>{chat.first_name}</a>"
            if chat.username
            else f"<a href='tg://user?id={chat.id}'>{chat.first_name}</a>"
        )

        async def send():
            await self.inline.bot.send_message(
                self.chat_logs,
                self.strings(
                    "log-pm"
                    if is_pm
                    else "log-channels"
                    if message.post
                    else "log-groups"
                ).format(
                    utils.escape_html(message.raw_text),
                    user_link,
                    chat_link,
                    chat.id,
                    message.id,
                ),
                disable_web_page_preview=True,
                parse_mode="HTML",
            )

        try:
            await send()
        except Exception:
            await utils.invite_inline_bot(self.client, self.chat_l)
            await send()