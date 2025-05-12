# meta developer: @MartyyyK

import asyncio
import io
import logging
import typing
import requests

from telethon.errors.rpcerrorlist import BotResponseTimeoutError
from telethon.events import MessageEdited, StopPropagation
from telethon.tl.types import Document, Message

from .. import loader, utils


@loader.tds
class MusicDLMod(loader.Module):
    strings = {
        "name": "MusicDL",
        "args": "🚫 <b>Arguments not specified</b>",
        "loading": "🔍 <b>Loading...</b>",
        "404": "🚫 <b>Music </b><code>{}</code><b> not found</b>",
    }

    strings_ru = {
        "args": "🚫 <b>Не указаны аргументы</b>",
        "loading": "🔍 <b>Загрузка...</b>",
        "404": "🚫 <b>Песня </b><code>{}</code><b> не найдена</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "timeout", 40, "Timeout for downloading", validator=loader.validators.Integer(minimum=5)
            ),
            loader.ConfigValue(
                "retries", 3, "Number of retries for downloading", validator=loader.validators.Integer(minimum=0)
            ),
            loader.ConfigValue(
                "lossless_priority", False, "If True, lossless music will be downloaded first", validator=loader.validators.Boolean()
            ),
        )

    async def client_ready(self, client, db):
        self._client = client

    @loader.command(ru_doc="<название> - Скачать песню")
    async def mdl(self, message: Message):
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("args"))
            return

        msg = await utils.answer(message, self.strings("loading"))
        result = await self.dl(args, only_document=True)

        if not result:
            await utils.answer(msg, self.strings("404").format(args))
            return

        await self._client.send_file(
            message.peer_id,
            result,
            caption=f"🎧 {utils.ascii_face()}",
            reply_to=getattr(message, "reply_to_msg_id", None),
        )
        if msg.out:
            await msg.delete()

    async def _dl(self, bot: str, full_name: str):
        try:
            return (await self._client.inline_query(bot, full_name))[0].document
        except Exception:
            return None

    async def _legacy(self, full_name: str):
        document = await self._dl("@vkm4bot", full_name)
        document = await self._dl("@spotifysavebot", full_name) if not document else document
        document = await self._dl("@lybot", full_name) if not document else document
        return document

    async def dl(self, full_name: str, only_document: bool = False, retries: int = 0) -> typing.Union[Document, str, None]:
        try:
            document = None
            if not self.config["lossless_priority"]:
                document = await self._legacy(full_name)

            if self.config["lossless_priority"] or not document:
                try:
                    q = await self._client.inline_query("@losslessrobot", full_name)
                except BotResponseTimeoutError:
                    if retries >= self.config["retries"]:
                        raise Exception("Failed to download")
                    await asyncio.sleep(3)
                    return await self.dl(full_name, only_document, retries + 1)

                result = q.result.results[0]
                if not getattr(getattr(result, "send_message", None), "reply_markup", None):
                    document = result.document
                    if text := getattr(getattr(result, "send_message", None), "message", None):
                        if "FLAC" in text:
                            document.is_flac = True
                else:
                    m = await q[0].click("me")
                    dl_event = asyncio.Event()
                    document = None

                    @self._client.on(MessageEdited(chats=utils.get_chat_id(m)))
                    async def handler(event: MessageEdited):
                        nonlocal document
                        try:
                            if (
                                event.message.id == m.id
                                and (
                                    not getattr(event.message, "reply_markup", None)
                                    or all(
                                        button.text != "Подождите, трек скоро скачается."
                                        for button in utils.array_sum(
                                            [row.buttons for row in event.message.reply_markup.rows]
                                        )
                                    )
                                )
                                and event.message.document
                            ):
                                document = event.message.document
                                if text := getattr(event.message, "message", None):
                                    if "FLAC" in text:
                                        document.is_flac = True
                                dl_event.set()
                                raise StopPropagation
                        except StopPropagation:
                            raise
                        except Exception:
                            logging.exception("Failed to download")

                    try:
                        await asyncio.wait_for(dl_event.wait(), timeout=self.config["timeout"])
                    except Exception:
                        await m.delete()
                        document = None
                    else:
                        await m.delete()

        except Exception:
            logging.debug("Can't download", exc_info=True)
            document = None

        if not document:
            document = await self._legacy(full_name)

        if not document:
            return None

        if only_document:
            return document

        file = io.BytesIO(await self._client.download_file(document, bytes))
        file.name = "audio.mp3"

        try:
            skynet = await utils.run_sync(
                requests.post,
                "https://siasky.net/skynet/skyfile",
                files={"file": file},
            )
        except ConnectionError:
            return None

        return f"https://siasky.net/{skynet.json()['skylink']}"
