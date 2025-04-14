import asyncio
import atexit as _atexit
import contextlib
import functools
import inspect
import io
import json
import logging
import os
import random
import re
import shlex
import signal
import string
import time
import typing
from datetime import timedelta
from urllib.parse import urlparse
import git
import grapheme
import hisatl
import requests
from aiogram.types import Message as AiogramMessage
from hisatl import hints
from hisatl.tl.custom.message import Message
from hisatl.tl.functions.account import UpdateNotifySettingsRequest
from hisatl.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    InviteToChannelRequest,
)
from hisatl.tl.functions.messages import (
    GetDialogFiltersRequest,
    SetHistoryTTLRequest,
    UpdateDialogFilterRequest,
)
from hisatl.tl.types import (
    Channel,
    Chat,
    ChatAdminRights,
    InputDocument,
    InputPeerNotifySettings,
    MessageEntityBankCard,
    MessageEntityBlockquote,
    MessageEntityBold,
    MessageEntityBotCommand,
    MessageEntityCashtag,
    MessageEntityCode,
    MessageEntityEmail,
    MessageEntityHashtag,
    MessageEntityItalic,
    MessageEntityMention,
    MessageEntityMentionName,
    MessageEntityPhone,
    MessageEntityPre,
    MessageEntitySpoiler,
    MessageEntityStrike,
    MessageEntityTextUrl,
    MessageEntityUnderline,
    MessageEntityUnknown,
    MessageEntityUrl,
    MessageMediaWebPage,
    PeerChannel,
    PeerChat,
    PeerUser,
    UpdateNewChannelMessage,
    User,
)
from ._internal import fw_protect
from .inline.types import InlineCall, InlineMessage
from .tl_cache import CustomTelegramClient
from .types import HisaReplyMarkup, ListLike, Module
FormattingEntity = typing.Union[
    MessageEntityUnknown,
    MessageEntityMention,
    MessageEntityHashtag,
    MessageEntityBotCommand,
    MessageEntityUrl,
    MessageEntityEmail,
    MessageEntityBold,
    MessageEntityItalic,
    MessageEntityCode,
    MessageEntityPre,
    MessageEntityTextUrl,
    MessageEntityMentionName,
    MessageEntityPhone,
    MessageEntityCashtag,
    MessageEntityUnderline,
    MessageEntityStrike,
    MessageEntityBlockquote,
    MessageEntityBankCard,
    MessageEntitySpoiler,
]
emoji_pattern = re.compile(
    "["
    "\U0001f600-\U0001f64f"
    "\U0001f300-\U0001f5ff"
    "\U0001f680-\U0001f6ff"
    "\U0001f1e0-\U0001f1ff"
    "]+",
    flags=re.UNICODE,
)
parser = hisatl.utils.sanitize_parse_mode("html")
logger = logging.getLogger(__name__)
def get_args(message: typing.Union[Message, str]) -> typing.List[str]:
    if not (message := getattr(message, "message", message)):
        return False
    if len(message := message.split(maxsplit=1)) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message
    return list(filter(lambda x: len(x) > 0, split))
def get_args_raw(message: typing.Union[Message, str]) -> str:
    if not (message := getattr(message, "message", message)):
        return False
    return args[1] if len(args := message.split(maxsplit=1)) > 1 else ""
def get_args_html(message: Message) -> str:
    prefix = message.client.loader.get_prefix()
    if not (message := message.text):
        return False
    if prefix not in message:
        return message
    raw_text, entities = parser.parse(message)
    raw_text = parser._add_surrogate(raw_text)
    try:
        command = raw_text[
            raw_text.index(prefix) : raw_text.index(" ", raw_text.index(prefix) + 1)
        ]
    except ValueError:
        return ""
    command_len = len(command) + 1
    return parser.unparse(
        parser._del_surrogate(raw_text[command_len:]),
        relocate_entities(entities, -command_len, raw_text[command_len:]),
    )
def get_args_split_by(
    message: typing.Union[Message, str],
    separator: str,
) -> typing.List[str]:
    return [
        section.strip() for section in get_args_raw(message).split(separator) if section
    ]
def get_chat_id(message: typing.Union[Message, AiogramMessage]) -> int:
    return hisatl.utils.resolve_id(
        getattr(message, "chat_id", None)
        or getattr(getattr(message, "chat", None), "id", None)
    )[0]
def get_entity_id(entity: hints.Entity) -> int:
    return hisatl.utils.get_peer_id(entity)
def escape_html(text: str, /) -> str:
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def escape_quotes(text: str, /) -> str:
    return escape_html(text).replace('"', "&quot;")
def get_base_dir() -> str:
    return get_dir(__file__)
def get_dir(mod: str) -> str:
    return os.path.abspath(os.path.dirname(os.path.abspath(mod)))
async def get_user(message: Message) -> typing.Optional[User]:
    try:
        return await message.get_sender()
    except ValueError:
        logger.debug("User not in session cache. Searching...")
    if isinstance(message.peer_id, PeerUser):
        await message.client.get_dialogs()
        return await message.get_sender()
    if isinstance(message.peer_id, (PeerChannel, PeerChat)):
        async for user in message.client.iter_participants(
            message.peer_id,
            aggressive=True,
        ):
            if user.id == message.sender_id:
                return user
        logger.error("User isn't in the group where they sent the message")
        return None
    logger.error("`peer_id` is not a user, chat or channel")
    return None
def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        None,
        functools.partial(func, *args, **kwargs),
    )
def run_async(loop: asyncio.AbstractEventLoop, coro: typing.Awaitable) -> typing.Any:
    return asyncio.run_coroutine_threadsafe(coro, loop).result()
def censor(
    obj: typing.Any,
    to_censor: typing.Optional[typing.Iterable[str]] = None,
    replace_with: str = "redacted_{count}_chars",
):
    if to_censor is None:
        to_censor = ["phone"]
    for k, v in vars(obj).items():
        if k in to_censor:
            setattr(obj, k, replace_with.format(count=len(v)))
        elif k[0] != "_" and hasattr(v, "__dict__"):
            setattr(obj, k, censor(v, to_censor, replace_with))
    return obj
def relocate_entities(
    entities: typing.List[FormattingEntity],
    offset: int,
    text: typing.Optional[str] = None,
) -> typing.List[FormattingEntity]:
    length = len(text) if text is not None else 0
    for ent in entities.copy() if entities else ():
        ent.offset += offset
        if ent.offset < 0:
            ent.length += ent.offset
            ent.offset = 0
        if text is not None and ent.offset + ent.length > length:
            ent.length = length - ent.offset
        if ent.length <= 0:
            entities.remove(ent)
    return entities
async def answer_file(
    message: typing.Union[Message, InlineCall, InlineMessage],
    file: typing.Union[str, bytes, io.IOBase, InputDocument],
    caption: typing.Optional[str] = None,
    **kwargs,
):
    if isinstance(message, (InlineCall, InlineMessage)):
        message = message.form["caller"]
    if topic := get_topic(message):
        kwargs.setdefault("reply_to", topic)
    try:
        response = await message.client.send_file(
            message.peer_id,
            file,
            caption=caption,
            **kwargs,
        )
    except Exception:
        if caption:
            logger.warning(
                "Failed to send file, sending plain text instead", exc_info=True
            )
            return await answer(message, caption, **kwargs)
        raise
    with contextlib.suppress(Exception):
        await message.delete()
    return response
async def answer(
    message: typing.Union[Message, InlineCall, InlineMessage],
    response: str,
    *,
    reply_markup: typing.Optional[HisaReplyMarkup] = None,
    **kwargs,
) -> typing.Union[InlineCall, InlineMessage, Message]:
    if isinstance(message, list) and message:
        message = message[0]
    if reply_markup is not None:
        if not isinstance(reply_markup, (list, dict)):
            raise ValueError("reply_markup must be a list or dict")
        if reply_markup:
            kwargs.pop("message", None)
            if isinstance(message, (InlineMessage, InlineCall)):
                await message.edit(response, reply_markup, **kwargs)
                return
            reply_markup = message.client.loader.inline._normalize_markup(reply_markup)
            result = await message.client.loader.inline.form(
                response,
                message=message if message.out else get_chat_id(message),
                reply_markup=reply_markup,
                **kwargs,
            )
            return result
    if isinstance(message, (InlineMessage, InlineCall)):
        await message.edit(response)
        return message
    kwargs.setdefault("link_preview", False)
    if not (edit := (message.out and not message.via_bot_id and not message.fwd_from)):
        kwargs.setdefault(
            "reply_to",
            getattr(message, "reply_to_msg_id", None),
        )
    elif "reply_to" in kwargs:
        kwargs.pop("reply_to")
    parse_mode = hisatl.utils.sanitize_parse_mode(
        kwargs.pop(
            "parse_mode",
            message.client.parse_mode,
        )
    )
    if isinstance(response, str) and not kwargs.pop("asfile", False):
        text, entities = parse_mode.parse(response)
        if len(text) >= 4096 and not hasattr(message, "hisa_grepped"):
            try:
                if not message.client.loader.inline.init_complete:
                    raise
                strings = list(smart_split(text, entities, 4096))
                if len(strings) > 10:
                    raise
                list_ = await message.client.loader.inline.list(
                    message=message,
                    strings=strings,
                )
                if not list_:
                    raise
                return list_
            except Exception:
                file = io.BytesIO(text.encode("utf-8"))
                file.name = "command_result.txt"
                result = await message.client.send_file(
                    message.peer_id,
                    file,
                    caption=message.client.loader.lookup("translations").strings(
                        "too_long"
                    ),
                    reply_to=kwargs.get("reply_to") or get_topic(message),
                )
                if message.out:
                    await message.delete()
                return result
        result = await (message.edit if edit else message.respond)(
            text,
            parse_mode=lambda t: (t, entities),
            **kwargs,
        )
    elif isinstance(response, Message):
        if message.media is None and (
            response.media is None or isinstance(response.media, MessageMediaWebPage)
        ):
            result = await message.edit(
                response.message,
                parse_mode=lambda t: (t, response.entities or []),
                link_preview=isinstance(response.media, MessageMediaWebPage),
            )
        else:
            result = await message.respond(response, **kwargs)
    else:
        if isinstance(response, bytes):
            response = io.BytesIO(response)
        elif isinstance(response, str):
            response = io.BytesIO(response.encode("utf-8"))
        if name := kwargs.pop("filename", None):
            response.name = name
        if message.media is not None and edit:
            await message.edit(file=response, **kwargs)
        else:
            kwargs.setdefault(
                "reply_to",
                getattr(message, "reply_to_msg_id", get_topic(message)),
            )
            result = await message.client.send_file(message.peer_id, response, **kwargs)
            if message.out:
                await message.delete()
    return result
async def get_target(message: Message, arg_no: int = 0) -> typing.Optional[int]:
    if any(
        isinstance(entity, MessageEntityMentionName)
        for entity in (message.entities or [])
    ):
        e = sorted(
            filter(lambda x: isinstance(x, MessageEntityMentionName), message.entities),
            key=lambda x: x.offset,
        )[0]
        return e.user_id
    if len(get_args(message)) > arg_no:
        user = get_args(message)[arg_no]
    elif message.is_reply:
        return (await message.get_reply_message()).sender_id
    elif hasattr(message.peer_id, "user_id"):
        user = message.peer_id.user_id
    else:
        return None
    try:
        entity = await message.client.get_entity(user)
    except ValueError:
        return None
    else:
        if isinstance(entity, User):
            return entity.id
def merge(a: dict, b: dict, /) -> dict:
    for key in a:
        if key in b:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                b[key] = merge(a[key], b[key])
            elif isinstance(a[key], list) and isinstance(b[key], list):
                b[key] = list(set(b[key] + a[key]))
            else:
                b[key] = a[key]
        b[key] = a[key]
    return b
async def set_avatar(
    client: CustomTelegramClient,
    peer: hints.Entity,
    avatar: str,
) -> bool:
    if isinstance(avatar, str) and check_url(avatar):
        f = (
            await run_sync(
                requests.get,
                avatar,
            )
        ).content
    elif isinstance(avatar, bytes):
        f = avatar
    else:
        return False
    await fw_protect()
    res = await client(
        EditPhotoRequest(
            channel=peer,
            photo=await client.upload_file(f, file_name="photo.png"),
        )
    )
    await fw_protect()
    try:
        await client.delete_messages(
            peer,
            message_ids=[
                next(
                    update
                    for update in res.updates
                    if isinstance(update, UpdateNewChannelMessage)
                ).message.id
            ],
        )
    except Exception:
        pass
    return True
async def invite_inline_bot(
    client: CustomTelegramClient,
    peer: hints.EntityLike,
) -> None:
    try:
        await client(InviteToChannelRequest(peer, [client.loader.inline.bot_username]))
    except Exception as e:
        raise RuntimeError(
            "Can't invite inline bot to old asset chat, which is required by module"
        ) from e
    with contextlib.suppress(Exception):
        await client(
            EditAdminRequest(
                channel=peer,
                user_id=client.loader.inline.bot_username,
                admin_rights=ChatAdminRights(ban_users=True),
                rank="Hisa",
            )
        )
async def asset_channel(
    client: CustomTelegramClient,
    title: str,
    description: str,
    *,
    channel: bool = False,
    silent: bool = False,
    archive: bool = False,
    invite_bot: bool = False,
    avatar: typing.Optional[str] = None,
    ttl: typing.Optional[int] = None,
    _folder: typing.Optional[str] = None,
) -> typing.Tuple[Channel, bool]:
    if not hasattr(client, "_channels_cache"):
        client._channels_cache = {}
    if (
        title in client._channels_cache
        and client._channels_cache[title]["exp"] > time.time()
    ):
        return client._channels_cache[title]["peer"], False
    async for d in client.iter_dialogs():
        if d.title == title:
            client._channels_cache[title] = {"peer": d.entity, "exp": int(time.time())}
            if invite_bot:
                if all(
                    participant.id != client.loader.inline.bot_id
                    for participant in (
                        await client.get_participants(d.entity, limit=100)
                    )
                ):
                    await fw_protect()
                    await invite_inline_bot(client, d.entity)
            return d.entity, False
    await fw_protect()
    peer = (
        await client(
            CreateChannelRequest(
                title,
                description,
                megagroup=not channel,
            )
        )
    ).chats[0]
    if invite_bot:
        await fw_protect()
        await invite_inline_bot(client, peer)
    if silent:
        await fw_protect()
        await dnd(client, peer, archive)
    elif archive:
        await fw_protect()
        await client.edit_folder(peer, 1)
    if avatar:
        await fw_protect()
        await set_avatar(client, peer, avatar)
    if ttl:
        await fw_protect()
        await client(SetHistoryTTLRequest(peer=peer, period=ttl))
    if _folder:
        if _folder != "hisa":
            raise NotImplementedError
        folders = await client(GetDialogFiltersRequest())
        try:
            folder = next(folder for folder in folders if folder.title == "hisa")
        except Exception:
            folder = None
        if folder is not None and not any(
            peer.id == getattr(folder_peer, "channel_id", None)
            for folder_peer in folder.include_peers
        ):
            folder.include_peers += [await client.get_input_entity(peer)]
            await client(
                UpdateDialogFilterRequest(
                    folder.id,
                    folder,
                )
            )
    client._channels_cache[title] = {"peer": peer, "exp": int(time.time())}
    return peer, True
async def dnd(
    client: CustomTelegramClient,
    peer: hints.Entity,
    archive: bool = True,
) -> bool:
    try:
        await client(
            UpdateNotifySettingsRequest(
                peer=peer,
                settings=InputPeerNotifySettings(
                    show_previews=False,
                    silent=True,
                    mute_until=2**31 - 1,
                ),
            )
        )
        if archive:
            await fw_protect()
            await client.edit_folder(peer, 1)
    except Exception:
        logger.exception("utils.dnd error")
        return False
    return True
def get_link(user: typing.Union[User, Channel], /) -> str:
    return (
        f"tg://user?id={user.id}"
        if isinstance(user, User)
        else (
            f"tg://resolve?domain={user.username}"
            if getattr(user, "username", None)
            else ""
        )
    )
def chunks(_list: ListLike, n: int, /) -> typing.List[typing.List[typing.Any]]:
    return [_list[i : i + n] for i in range(0, len(_list), n)]
def get_named_platform() -> str:
    from . import main
    with contextlib.suppress(Exception):
        if os.path.isfile("/proc/device-tree/model"):
            with open("/proc/device-tree/model") as f:
                model = f.read()
                if "Orange" in model:
                    return f"🍊 {model}"
                return f"🍇 {model}" if "Raspberry" in model else f"❓ {model}"
    if main.IS_WSL:
        return "🍀 WSL"
    if main.IS_GOORM:
        return "🦾 GoormIDE"
    if main.IS_RAILWAY:
        return "🚂 Railway"
    if main.IS_DOCKER:
        return "🐳 Docker"
    if main.IS_TERMUX:
        return "🕶 Termux"
    if main.IS_CODESPACES:
        return "🐈‍⬛ Codespaces"
    return f"✌️ lavHost {os.environ['LAVHOST']}" if main.IS_LAVHOST else "📻 VDS"
def get_platform_emoji() -> str:
    from . import main
    BASE = "".join(
        (
            "<emoji document_id={}>🌘</emoji>",
            "<emoji document_id=5195311729663286630>🌘</emoji>",
            "<emoji document_id=5195045669324201904>🌘</emoji>",
        )
    )
    if main.IS_DOCKER:
        return BASE.format(5298554256603752468)
    if main.IS_LAVHOST:
        return BASE.format(5301078610747074753)
    if main.IS_GOORM:
        return BASE.format(5298947740032573902)
    if main.IS_CODESPACES:
        return BASE.format(5194976881127989720)
    if main.IS_TERMUX:
        return BASE.format(5193051778001673828)
    if main.IS_RAILWAY:
        return BASE.format(5199607521593007466)
    return BASE.format(5192765204898783881)
def uptime() -> int:
    return round(time.perf_counter() - init_ts)
def formatted_uptime() -> str:
    return str(timedelta(seconds=uptime()))
def ascii_face() -> str:
    return escape_html(
        random.choice(
            [
                "ヽ(๑◠ܫ◠๑)ﾉ",
                "(◕ᴥ◕ʋ)",
                "ᕙ(`▽´)ᕗ",
                "(✿◠‿◠)",
                "(▰˘◡˘▰)",
                "(˵ ͡° ͜ʖ ͡°˵)",
                "ʕっ•ᴥ•ʔっ",
                "( ͡° ᴥ ͡°)",
                "(๑•́ ヮ •̀๑)",
                "٩(^‿^)۶",
                "(っˆڡˆς)",
                "ψ(｀∇´)ψ",
                "⊙ω⊙",
                "٩(^ᴗ^)۶",
                "(´・ω・)っ由",
                "( ͡~ ͜ʖ ͡°)",
                "✧♡(◕‿◕✿)",
                "โ๏௰๏ใ ื",
                "∩｡• ᵕ •｡∩ ♡",
                "(♡´౪`♡)",
                "(◍＞◡＜◍)⋈。✧♡",
                "╰(✿´⌣`✿)╯♡",
                "ʕ•ᴥ•ʔ",
                "ᶘ ◕ᴥ◕ᶅ",
                "▼・ᴥ・▼",
                "ฅ^•ﻌ•^ฅ",
                "(΄◞ิ౪◟ิ‵)",
                "٩(^ᴗ^)۶",
                "ᕴｰᴥｰᕵ",
                "ʕ￫ᴥ￩ʔ",
                "ʕᵕᴥᵕʔ",
                "ʕᵒᴥᵒʔ",
                "ᵔᴥᵔ",
                "(✿╹◡╹)",
                "(๑￫ܫ￩)",
                "ʕ·ᴥ·　ʔ",
                "(ﾉ≧ڡ≦)",
                "(≖ᴗ≖✿)",
                "（〜^∇^ )〜",
                "( ﾉ･ｪ･ )ﾉ",
                "~( ˘▾˘~)",
                "(〜^∇^)〜",
                "ヽ(^ᴗ^ヽ)",
                "(´･ω･`)",
                "₍ᐢ•ﻌ•ᐢ₎*･ﾟ｡",
                "(。・・)_且",
                "(=｀ω´=)",
                "(*•‿•*)",
                "(*ﾟ∀ﾟ*)",
                "(☉⋆‿⋆☉)",
                "ɷ◡ɷ",
                "ʘ‿ʘ",
                "(。-ω-)ﾉ",
                "( ･ω･)ﾉ",
                "(=ﾟωﾟ)ﾉ",
                "(・ε・`*) …",
                "ʕっ•ᴥ•ʔっ",
                "(*˘︶˘*)",
            ]
        )
    )
def array_sum(
    array: typing.List[typing.List[typing.Any]], /
) -> typing.List[typing.Any]:
    result = []
    for item in array:
        result += item
    return result
def rand(size: int, /) -> str:
    return "".join(
        [random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(size)]
    )
def smart_split(
    text: str,
    entities: typing.List[FormattingEntity],
    length: int = 4096,
    split_on: ListLike = ("\n", " "),
    min_length: int = 1,
) -> typing.Iterator[str]:
    encoded = text.encode("utf-16le")
    pending_entities = entities
    text_offset = 0
    bytes_offset = 0
    text_length = len(text)
    bytes_length = len(encoded)
    while text_offset < text_length:
        if bytes_offset + length * 2 >= bytes_length:
            yield parser.unparse(
                text[text_offset:],
                list(sorted(pending_entities, key=lambda x: x.offset)),
            )
            break
        codepoint_count = len(
            encoded[bytes_offset : bytes_offset + length * 2].decode(
                "utf-16le",
                errors="ignore",
            )
        )
        for search in split_on:
            search_index = text.rfind(
                search,
                text_offset + min_length,
                text_offset + codepoint_count,
            )
            if search_index != -1:
                break
        else:
            search_index = text_offset + codepoint_count
        split_index = grapheme.safe_split_index(text, search_index)
        split_offset_utf16 = (
            len(text[text_offset:split_index].encode("utf-16le"))
        ) // 2
        exclude = 0
        while (
            split_index + exclude < text_length
            and text[split_index + exclude] in split_on
        ):
            exclude += 1
        current_entities = []
        entities = pending_entities.copy()
        pending_entities = []
        for entity in entities:
            if (
                entity.offset < split_offset_utf16
                and entity.offset + entity.length > split_offset_utf16 + exclude
            ):
                current_entities.append(
                    _copy_tl(
                        entity,
                        length=split_offset_utf16 - entity.offset,
                    )
                )
                pending_entities.append(
                    _copy_tl(
                        entity,
                        offset=0,
                        length=entity.offset
                        + entity.length
                        - split_offset_utf16
                        - exclude,
                    )
                )
            elif entity.offset < split_offset_utf16 < entity.offset + entity.length:
                current_entities.append(
                    _copy_tl(
                        entity,
                        length=split_offset_utf16 - entity.offset,
                    )
                )
            elif entity.offset < split_offset_utf16:
                current_entities.append(entity)
            elif (
                entity.offset + entity.length
                > split_offset_utf16 + exclude
                > entity.offset
            ):
                pending_entities.append(
                    _copy_tl(
                        entity,
                        offset=0,
                        length=entity.offset
                        + entity.length
                        - split_offset_utf16
                        - exclude,
                    )
                )
            elif entity.offset + entity.length > split_offset_utf16 + exclude:
                pending_entities.append(
                    _copy_tl(
                        entity,
                        offset=entity.offset - split_offset_utf16 - exclude,
                    )
                )
        current_text = text[text_offset:split_index]
        yield parser.unparse(
            current_text,
            list(sorted(current_entities, key=lambda x: x.offset)),
        )
        text_offset = split_index + exclude
        bytes_offset += len(current_text.encode("utf-16le"))
def _copy_tl(o, **kwargs):
    d = o.to_dict()
    del d["_"]
    d.update(kwargs)
    return o.__class__(**d)
def check_url(url: str) -> bool:
    try:
        return bool(urlparse(url).netloc)
    except Exception:
        return False
def get_git_hash() -> typing.Union[str, bool]:
    try:
        return git.Repo().head.commit.hexsha
    except Exception:
        return False
def get_commit_url() -> str:
    try:
        hash_ = get_git_hash()
        return (
            f'<a href="https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/{hash_}">#{hash_[:7]}</a>'
        )
    except Exception:
        return "Unknown"
def is_serializable(x: typing.Any, /) -> bool:
    try:
        json.dumps(x)
        return True
    except Exception:
        return False
def get_lang_flag(countrycode: str) -> str:
    if (
        len(
            code := [
                c
                for c in countrycode.lower()
                if c in string.ascii_letters + string.digits
            ]
        )
        == 2
    ):
        return "".join([chr(ord(c.upper()) + (ord("🇦") - ord("A"))) for c in code])
    return countrycode
def get_entity_url(
    entity: typing.Union[User, Channel],
    openmessage: bool = False,
) -> str:
    return (
        (
            f"tg://openmessage?id={entity.id}"
            if openmessage
            else f"tg://user?id={entity.id}"
        )
        if isinstance(entity, User)
        else (
            f"tg://resolve?domain={entity.username}"
            if getattr(entity, "username", None)
            else ""
        )
    )
async def get_message_link(
    message: Message,
    chat: typing.Optional[typing.Union[Chat, Channel]] = None,
) -> str:
    if message.is_private:
        return (
            f"tg://openmessage?user_id={get_chat_id(message)}&message_id={message.id}"
        )
    if not chat and not (chat := message.chat):
        chat = await message.get_chat()
    topic_affix = (
        f"?topic={message.reply_to.reply_to_msg_id}"
        if getattr(message.reply_to, "forum_topic", False)
        else ""
    )
    return (
        f"https://t.me/{chat.username}/{message.id}{topic_affix}"
        if getattr(chat, "username", False)
        else f"https://t.me/c/{chat.id}/{message.id}{topic_affix}"
    )
def remove_html(text: str, escape: bool = False, keep_emojis: bool = False) -> str:
    return (escape_html if escape else str)(
        re.sub(
            (
                r"(<\/?a.*?>|<\/?b>|<\/?i>|<\/?u>|<\/?strong>|<\/?em>|<\/?code>|<\/?strike>|<\/?del>|<\/?pre.*?>)"
                if keep_emojis
                else r"(<\/?a.*?>|<\/?b>|<\/?i>|<\/?u>|<\/?strong>|<\/?em>|<\/?code>|<\/?strike>|<\/?del>|<\/?pre.*?>|<\/?emoji.*?>)"
            ),
            "",
            text,
        )
    )
def get_kwargs() -> typing.Dict[str, typing.Any]:
    keys, _, _, values = inspect.getargvalues(inspect.currentframe().f_back)
    return {key: values[key] for key in keys if key != "self"}
def mime_type(message: Message) -> str:
    return (
        ""
        if not isinstance(message, Message) or not getattr(message, "media", False)
        else getattr(getattr(message, "media", False), "mime_type", False) or ""
    )
def find_caller(
    stack: typing.Optional[typing.List[inspect.FrameInfo]] = None,
) -> typing.Any:
    caller = next(
        (
            frame_info
            for frame_info in stack or inspect.stack()
            if hasattr(frame_info, "function")
            and any(
                inspect.isclass(cls_)
                and issubclass(cls_, Module)
                and cls_ is not Module
                for cls_ in frame_info.frame.f_globals.values()
            )
        ),
        None,
    )
    if not caller:
        return next(
            (
                frame_info.frame.f_locals["func"]
                for frame_info in stack or inspect.stack()
                if hasattr(frame_info, "function")
                and frame_info.function == "future_dispatcher"
                and (
                    "CommandDispatcher"
                    in getattr(getattr(frame_info, "frame", None), "f_globals", {})
                )
            ),
            None,
        )
    return next(
        (
            getattr(cls_, caller.function, None)
            for cls_ in caller.frame.f_globals.values()
            if inspect.isclass(cls_) and issubclass(cls_, Module)
        ),
        None,
    )
def validate_html(html: str) -> str:
    text, entities = hisatl.extensions.html.parse(html)
    return hisatl.extensions.html.unparse(escape_html(text), entities)
def iter_attrs(obj: typing.Any, /) -> typing.List[typing.Tuple[str, typing.Any]]:
    return ((attr, getattr(obj, attr)) for attr in dir(obj))
def atexit(
    func: typing.Callable,
    use_signal: typing.Optional[int] = None,
    *args,
    **kwargs,
) -> None:
    if use_signal:
        signal.signal(use_signal, lambda *_: func(*args, **kwargs))
        return
    _atexit.register(functools.partial(func, *args, **kwargs))
def get_topic(message: Message) -> typing.Optional[int]:
    return (
        (message.reply_to.reply_to_top_id or message.reply_to.reply_to_msg_id)
        if (
            isinstance(message, Message)
            and message.reply_to
            and message.reply_to.forum_topic
        )
        else (
            message.form["top_msg_id"]
            if isinstance(message, (InlineCall, InlineMessage))
            else None
        )
    )
def get_ram_usage() -> float:
    try:
        import psutil
        current_process = psutil.Process(os.getpid())
        mem = current_process.memory_info()[0] / 2.0**20
        for child in current_process.children(recursive=True):
            mem += child.memory_info()[0] / 2.0**20
        return round(mem, 1)
    except Exception:
        return 0
def get_cpu_usage() -> float:
    try:
        import psutil
        current_process = psutil.Process(os.getpid())
        cpu = current_process.cpu_percent()
        for child in current_process.children(recursive=True):
            cpu += child.cpu_percent()
        return round(cpu, 1)
    except Exception:
        return 0
init_ts = time.perf_counter()
def get_git_info() -> typing.Tuple[str, str]:
    hash_ = get_git_hash()
    return (
        hash_,
        f"https://raw.githubusercontent.com/GambitHacker17/Hisa/Master/{hash_}" if hash_ else "",
    )
def get_version_raw() -> str:
    from . import version
    return ".".join(map(str, list(version.__version__)))
get_platform_name = get_named_platform