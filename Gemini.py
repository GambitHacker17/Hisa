# meta developer: @MartyyyK
# requires: aiohttp pytz markdown_it_py

import re
import os
import io
import random
import socket
import asyncio
import logging
import aiohttp
import tempfile
import base64
from datetime import datetime
from markdown_it import MarkdownIt
import pytz
from telethon import types
from telethon.tl.types import Message, DocumentAttributeFilename
from telethon.utils import get_display_name, get_peer_id
from telethon.errors.rpcerrorlist import MessageTooLongError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import UserNotParticipantError, ChannelPrivateError
from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)

DB_HISTORY_KEY = "gemini_conversations_v4"
DB_geminiauto_HISTORY_KEY = "gemini_geminiauto_conversations_v1"
DB_IMPERSONATION_KEY = "gemini_impersonation_chats"
GEMINI_TIMEOUT = 840
MAX_FFMPEG_SIZE = 90 * 1024 * 1024
GEMINI_API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"

class GoogleAPIError(Exception):
    def __init__(self, message, status_code=None, details=None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details

@loader.tds
class Gemini(loader.Module):
    """Google Gemini AI"""
    strings = {
        "name": "Gemini",
        "cfg_api_key_doc": "API ключи Google Gemini, пишите через запятую <key1>, <key2>. После ввода ключа перезапустите юзербот",
        "cfg_model_name_doc": "Модель Gemini",
        "cfg_buttons_doc": "Включить интерактивные кнопки",
        "cfg_system_instruction_doc": "Системная инструкция (промпт) для Gemini",
        "cfg_max_history_length_doc": "Макс. кол-во пар 'вопрос-ответ' в памяти (0 - без лимита).",
        "cfg_timezone_doc": "Часовой пояс. Список: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones",
        "cfg_proxy_doc": "Прокси для обхода региональных блокировок в формате: http://user:pass@host:port",
        "cfg_impersonation_prompt_doc": "Промпт для режима авто-ответа. {my_name} и {chat_history} будут заменены",
        "cfg_impersonation_history_limit_doc": "Сколько последних сообщений из чата отправлять в качестве контекста для авто-ответа",
        "cfg_impersonation_reply_chance_doc": "Вероятность ответа в режиме geminiauto <0.0 - 1.0>",
        "no_api_key": '❗️ <b>Api ключ не настроен</b>\nПолучить Api ключ можно <a href="https://aistudio.google.com/app/apikey">здесь</a>\n<b>Добавьте ключ в конфиге модуля</b>',
        "all_keys_exhausted": "❗️ <b>Все доступные API ключи ({}) исчерпали свою квоту</b>\nПопробуйте позже или добавьте новые ключи в конфиге",
        "no_prompt_or_media": "⚠️ <i>Нужен текст или ответ на медиа/файл.</i>",
        "processing": "<emoji document_id=5350356823528455446>✨</emoji> <b>Обработка...</b>",
        "api_error": "❗️ <b>Ошибка API:</b>\n<code>{}</code>",
        "api_timeout": f"❗️ <b>Таймаут ответа от Gemini API ({GEMINI_TIMEOUT} сек)</b>",
        "blocked_error": "🚫 <b>Запрос/ответ заблокирован</b>\n<code>{}</code>",
        "generic_error": "❗️ <b>Ошибка:</b>\n<code>{}</code>",
        "question_prefix": "💬 <b>Запрос:</b>",
        "response_prefix": "<emoji document_id=5325547803936572038>✨</emoji> <b>Gemini:</b>",
        "unsupported_media_type": "⚠️ <b>Формат медиа ({}) не поддерживается</b>",
        "memory_status": "🧠 [{}/{}]",
        "memory_status_unlimited": "🧠 [{}/∞]",
        "memory_cleared": "🧹 <b>Память диалога очищена</b>",
        "memory_cleared_geminiauto": "🧹 <b>Память geminiauto в этом чате очищена</b>",
        "no_memory_to_clear": "ℹ️ <b>В этом чате нет истории</b>",
        "no_geminiauto_memory_to_clear": "ℹ️ <b>В этом чате нет истории geminiauto</b>",
        "memory_chats_title": "🧠 <b>Чаты с историей ({}):</b>",
        "memory_chat_line": "  • {} (<code>{}</code>)",
        "no_memory_found": "ℹ️ Память Gemini пуста",
        "media_reply_placeholder": "[ответ на медиа]",
        "btn_clear": "🧹 Очистить",
        "btn_regenerate": "🔄 Другой ответ",
        "no_last_request": "Последний запрос не найден для повторной генерации",
        "memory_fully_cleared": "🧹 <b>Вся память Gemini полностью очищена (затронуто {} чатов)</b>",
        "geminiauto_memory_fully_cleared": "🧹 <b>Вся память geminiauto полностью очищена (затронуто {} чатов)</b>",
        "no_memory_to_fully_clear": "ℹ️ <b>Память Gemini пуста</b>",
        "no_geminiauto_memory_to_fully_clear": "ℹ️ <b>Память geminiauto пуста</b>",
        "response_too_long": "Ответ Gemini был слишком длинным и отправлен в виде файла",
        "gclear_usage": "ℹ️ <b>Использование:</b> <code>.gclear [auto]</code>",
        "gres_usage": "ℹ️ <b>Использование:</b> <code>.gres [auto]</code>",
        "auto_mode_on": "🎭 <b>Режим авто-ответа включен в этом чате</b>\nЯ буду отвечать на сообщения с вероятностью {}%",
        "auto_mode_off": "🎭 <b>Режим авто-ответа выключен в этом чате</b>",
        "auto_mode_chats_title": "🎭 <b>Чаты с активным авто-ответом ({}):</b>",
        "no_auto_mode_chats": "ℹ️ Нет чатов с включенным режимом авто-ответа",
        "auto_mode_usage": "ℹ️ <b>Использование:</b> <code>.geminiauto on/off</code>",
        "gch_usage": "ℹ️ <b>Использование:</b>\n<code>.gch <кол-во> <вопрос></code>\n<code>.gch <id чата> <кол-во> <вопрос></code>",
        "gch_processing": "<emoji document_id=5386367538735104399>⌛️</emoji> <b>Анализирую {} сообщений...</b>",
        "gch_result_caption": "Анализ последних {} сообщений",
        "gch_result_caption_from_chat": "Анализ последних {} сообщений из чата <b>{}</b>",
        "gch_invalid_args": "❗️ <b>Неверные аргументы</b>\n{}",
        "gch_chat_error": "❗️ <b>Ошибка доступа к чату</b> <code>{}</code>: <i>{}</i>",
        "region_blocked_error": "❗️ <b>В данном регионе Gemini API не доступен</b>\nСкачайте VPN (для пк/тел) или поставьте прокси (платный/бесплатный)\nИли настройте прокси в конфиге модуля командой <code>.cfg Gemini</code>\n\n<b>Текущий прокси:</b> <code>{}</code>",
        "quota_exceeded_error": "❗️ <b>Превышен лимит Google Gemini API для модели <code>{}</code></b>\n\nЧаще всего это происходит на бесплатном тарифе\nВы можете:\n• Подождать, пока лимит сбросится (обычно раз в сутки)\n• Проверить свой тарифный план в <a href='https://aistudio.google.com/app/billing'>Google AI Studio</a>\n• Узнать больше о лимитах <a href='https://ai.google.dev/gemini-api/docs/rate-limits'>здесь</a>\n\n<b>Детали ошибки:</b>\n<code>{}</code>",
        "server_error_500": "❗️ <b>Ошибка 500 от Google API</b>\nЭто значит, что формат медиа (файл или еще что-то), который ты отправил, не поддерживается\nТакое случается по такой причине:\n• Если формат файла в принципе не поддерживается Gemini/Google\n• Временный сбой на серверах Google. Попробуйте повторить запрос позже",
        "network_error": "❗️ <b>Сетевая ошибка:</b>\n<code>{}</code>\n\nПроверьте подключение к интернету и настройки прокси",
        "invalid_api_key": "❗️ <b>Неверный API ключ</b>\nПроверьте правильность ключа в конфиге модуля\nПолучить новый ключ можно <a href='https://aistudio.google.com/app/apikey'>здесь</a>",
        "file_too_large": "❗️ <b>Файл слишком большой</b>\nМаксимальный размер: {} МБ",
        "ffmpeg_error": "❗️ <b>Ошибка обработки медиа</b>\nНе удалось конвертировать файл. Проверьте формат и попробуйте снова",
        "access_denied": "❗️ <b>Доступ запрещен</b>\nПроверьте права доступа к чату или файлу",
        "unknown_error": "❗️ <b>Неизвестная ошибка</b>\n<code>{}</code>\n\nПопробуйте повторить запрос позже",
        "system_instruction_too_long": "❗️ <b>Слишком длинная системная инструкция</b>\nТекущая длина: {} символов\nМаксимальная: 8192 символа\nУменьшите историю чата в настройках или используйте более короткий промпт",
    }
    TEXT_MIME_TYPES = {
        "text/plain", "text/markdown", "text/html", "text/css", "text/csv",
        "application/json", "application/xml", "application/x-python", "text/x-python",
        "application/javascript", "application/x-sh",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "api_key", "", self.strings["cfg_api_key_doc"],
                validator=loader.validators.Hidden()
            ),
            loader.ConfigValue("model_name", "gemini-2.5-flash", self.strings["cfg_model_name_doc"]),
            loader.ConfigValue("interactive_buttons", True, self.strings["cfg_buttons_doc"], validator=loader.validators.Boolean()),
            loader.ConfigValue("system_instruction", "Не используй HTML форматирование в ответе.", self.strings["cfg_system_instruction_doc"], validator=loader.validators.String()),
            loader.ConfigValue("max_history_length", 800, self.strings["cfg_max_history_length_doc"], validator=loader.validators.Integer(minimum=0)),
            loader.ConfigValue("timezone", "Europe/Moscow", self.strings["cfg_timezone_doc"]),
            loader.ConfigValue("proxy", "", self.strings["cfg_proxy_doc"]),
            loader.ConfigValue(
                "impersonation_prompt",
                (
                    "Ты — это я, пользователь Telegram по имени {my_name}. Твоя задача — отвечать в чате от моего имени, основываясь на последних сообщениях."
                    "Веди себя естественно, как обычный человек, а не как ассистент. Не признавайся, что ты — ИИ, даже если тебя спросят напрямую."
                    "Твоя личность: [Здесь опишите свой характер: остроумный, серьезный, саркастичный, дружелюбный и т.д.].\n"
                    "Правила:\n- Отвечай кратко и по делу.\n- Не используй HTML форматирование в ответе.\n- Используй неформальный язык, сленг.\n- Не ставь точку в конце предложений, только если это не требует контекст.\n- На медиа (стикер, фото) реагируй как человек ('лол', 'ору', 'жиза' и т.д.).\n- Не используй префиксы и кавычки.\n\n"
                    "История чата:\n{chat_history}\n\n{my_name}:"
                ),
                self.strings["cfg_impersonation_prompt_doc"],
                validator=loader.validators.String(),
            ),
            loader.ConfigValue("impersonation_history_limit", 80, self.strings["cfg_impersonation_history_limit_doc"], validator=loader.validators.Integer(minimum=5, maximum=100)),
            loader.ConfigValue("impersonation_reply_chance", 0.25, self.strings["cfg_impersonation_reply_chance_doc"], validator=loader.validators.Float(minimum=0.0, maximum=1.0)),
        )
        self.conversations = {}
        self.geminiauto_conversations = {}
        self.last_requests = {}
        self.impersonation_chats = set()
        self._lock = asyncio.Lock()
        self.memory_disabled_chats = set()

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.me = await client.get_me()

        await self._migrate_keys()

        self.api_keys = [k.strip() for k in self.config["api_key"].split(",") if k.strip()]
        self.current_api_key_index = 0
        self.conversations = self._load_history_from_db(DB_HISTORY_KEY)
        self.geminiauto_conversations = self._load_history_from_db(DB_geminiauto_HISTORY_KEY)
        self.impersonation_chats = set(self.db.get(self.strings["name"], DB_IMPERSONATION_KEY, []))
        self.safety_settings = [{"category": c, "threshold": "BLOCK_NONE"} for c in ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH", "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]]
        self._configure_proxy()
        if not self.api_keys:
            logger.warning("Gemini: API ключ(и) не настроен(ы)!")

    async def _migrate_keys(self):
        module_config = self.db.get(self.strings["name"], "config", {})
        old_keys_list = module_config.get("api_keys")

        if isinstance(old_keys_list, list) and old_keys_list:
            new_string = ",".join(old_keys_list)

            module_config["api_key"] = new_string
            del module_config["api_keys"]

            self.db.set(self.strings["name"], "config", module_config)
            self.config["api_key"] = new_string

            logger.info("Конфигурация API ключей Gemini успешно перенесена в новый формат")

    async def _prepare_parts(self, message: Message, custom_text: str = None):
        final_parts, warnings = [], []
        prompt_text_chunks = []
        user_args = custom_text if custom_text is not None else utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if reply and getattr(reply, "text", None):
            try:
                reply_sender = await reply.get_sender()
                reply_author_name = get_display_name(reply_sender) if reply_sender else "Unknown"
                if not reply_author_name:
                    reply_author_name = "Unknown"
                prompt_text_chunks.append(f"{reply_author_name}: {reply.text}")
            except Exception:
                prompt_text_chunks.append(f"Ответ на: {reply.text}")

        try:
            current_sender = await message.get_sender()
            current_user_name = get_display_name(current_sender) if current_sender else "User"
            if not current_user_name:
                current_user_name = "User"
            prompt_text_chunks.append(f"{current_user_name}: {user_args or ''}")
        except Exception:
            prompt_text_chunks.append(f"Запрос: {user_args or ''}")

        media_source = message if message.media or message.sticker else reply
        has_media = bool(media_source and (media_source.media or media_source.sticker))

        if has_media:
            if media_source.sticker and hasattr(media_source.sticker, 'mime_type') and media_source.sticker.mime_type == 'application/x-tgsticker':
                alt_text = next((attr.alt for attr in media_source.sticker.attributes if isinstance(attr, types.DocumentAttributeSticker)), "?")
                prompt_text_chunks.append(f"[Отправлен анимированный стикер: {alt_text}]")
            else:
                media, mime_type, filename = media_source.media, "application/octet-stream", "file"
                if media_source.photo:
                    mime_type = "image/jpeg"
                elif hasattr(media_source, "document") and media_source.document:
                    mime_type = getattr(media_source.document, "mime_type", mime_type)
                    doc_attr = next((attr for attr in media_source.document.attributes if isinstance(attr, DocumentAttributeFilename)), None)
                    if doc_attr:
                        filename = doc_attr.file_name

                if mime_type.startswith("image/"):
                    try:
                        byte_io = io.BytesIO()
                        await self.client.download_media(media, byte_io)
                        final_parts.append({
                            "inline_data": {
                                "mime_type": mime_type,
                                "data": base64.b64encode(byte_io.getvalue()).decode("utf-8")
                            }
                        })
                    except Exception as e:
                        warnings.append(f"⚠️ Ошибка обработки изображения '{filename}': {e}")

                elif mime_type in self.TEXT_MIME_TYPES or filename.split('.')[-1] in ('txt', 'py', 'js', 'json', 'md', 'html', 'css', 'sh'):
                    try:
                        byte_io = io.BytesIO()
                        await self.client.download_media(media, byte_io)
                        file_content = byte_io.read().decode('utf-8')
                        prompt_text_chunks.insert(0, f"[Содержимое файла '{filename}']: \n```\n{file_content}\n```")
                    except Exception as e:
                        warnings.append(f"⚠️ Ошибка чтения файла '{filename}': {e}")

                elif mime_type.startswith(("video/", "audio/")):
                    input_path, output_path = None, None
                    try:
                        with tempfile.NamedTemporaryFile(suffix=f".{filename.split('.')[-1]}", delete=False) as temp_in:
                            input_path = temp_in.name
                        await self.client.download_media(media, input_path)
                        if os.path.getsize(input_path) > MAX_FFMPEG_SIZE:
                            warnings.append(f"⚠️ Медиафайл '{filename}' слишком большой для конвертации (> {MAX_FFMPEG_SIZE // 1024 // 1024} МБ).")
                            raise StopIteration

                        ffprobe_cmd = ["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=codec_type", "-of", "default=noprint_wrappers=1:nokey=1", input_path]
                        process_probe = await asyncio.create_subprocess_exec(*ffprobe_cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                        stdout, _ = await process_probe.communicate()
                        has_audio = bool(stdout.strip())

                        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_out:
                            output_path = temp_out.name
                        ffmpeg_cmd = ["ffmpeg", "-y", "-i", input_path]
                        maps = ["-map", "0:v:0"]
                        if not has_audio:
                            ffmpeg_cmd.extend(["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"])
                            maps.extend(["-map", "1:a:0"])
                        ffmpeg_cmd.extend([*maps, "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2", "-c:v", "libx264", "-c:a", "aac", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-shortest", output_path])

                        process_ffmpeg = await asyncio.create_subprocess_exec(*ffmpeg_cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
                        _, stderr = await process_ffmpeg.communicate()

                        if process_ffmpeg.returncode != 0:
                            stderr_str = stderr.decode()
                            warnings.append(f"⚠️ <b>Ошибка FFmpeg:</b>\nНе удалось конвертировать '{filename}'. Детали:\n<code>{utils.escape_html(stderr_str)}</code>")
                            raise StopIteration

                        with open(output_path, "rb") as f:
                            final_parts.append({
                                "inline_data": {
                                    "mime_type": "video/mp4",
                                    "data": base64.b64encode(f.read()).decode("utf-8")
                                }
                            })

                    except StopIteration:
                        pass
                    except Exception as e:
                        warnings.append(f"⚠️ Критическая ошибка при обработке медиа '{filename}': {e}")
                    finally:
                        if input_path and os.path.exists(input_path):
                            os.remove(input_path)
                        if output_path and os.path.exists(output_path):
                            os.remove(output_path)

        if not user_args and has_media and not final_parts and not any("[Содержимое файла" in chunk for chunk in prompt_text_chunks):
            prompt_text_chunks.append(self.strings["media_reply_placeholder"])

        full_prompt_text = "\n".join(chunk for chunk in prompt_text_chunks if chunk and chunk.strip()).strip()

        if full_prompt_text:
            final_parts.insert(0, {"text": full_prompt_text})

        return final_parts, warnings

    async def _send_to_gemini(self, message, parts: list, regeneration: bool = False, call: InlineCall = None, status_msg=None, chat_id_override: int = None, impersonation_mode: bool = False, use_url_context: bool = False, display_prompt: str = None):
        msg_obj = None
        if regeneration:
            chat_id = chat_id_override
            base_message_id = message
            try:
                msg_obj = await self.client.get_messages(chat_id, ids=base_message_id)
            except Exception:
                msg_obj = None
        else:
            chat_id = utils.get_chat_id(message)
            base_message_id = message.id
            msg_obj = message

        if not self.api_keys:
            if not impersonation_mode and status_msg:
                await utils.answer(status_msg, self.strings['no_api_key'])
            return None if impersonation_mode else ""

        current_api_key_index = self.current_api_key_index
        max_retries = len(self.api_keys)
        error_to_report = None
        response_json = None
        tools_list = []
        if use_url_context:
            tools_list.append({"google_search": {}})

        system_instruction_to_use = None
        if impersonation_mode:
            my_name = get_display_name(self.me)
            if not my_name:
                my_name = "User"
            chat_history_text = await self._get_recent_chat_text(chat_id)
            system_instruction_text = self.config["impersonation_prompt"].format(my_name=my_name, chat_history=chat_history_text)
            if len(system_instruction_text) > 8192:
                chat_history_text = await self._get_recent_chat_text(chat_id, count=10)
                system_instruction_text = self.config["impersonation_prompt"].format(my_name=my_name, chat_history=chat_history_text)

            system_instruction_to_use = system_instruction_text
            raw_history = self._get_structured_history(chat_id, geminiauto=True)
            api_history_content = [{"role": e["role"], "parts": [{"text": e['content']}]} for e in raw_history]
        else:
            system_instruction_val = self.config["system_instruction"]
            system_instruction_to_use = (system_instruction_val.strip() if isinstance(system_instruction_val, str) else "") or None
            raw_history = self._get_structured_history(chat_id, geminiauto=False)
            if regeneration:
                raw_history = raw_history[:-2]
            api_history_content = [{"role": e["role"], "parts": [{"text": e['content']}]} for e in raw_history]

        full_request_content = list(api_history_content)

        if not impersonation_mode:
            try:
                user_timezone = pytz.timezone(self.config["timezone"])
            except pytz.UnknownTimeZoneError:
                user_timezone = pytz.utc
            now = datetime.now(user_timezone)
            time_str = now.strftime("%Y-%m-%d %H:%M:%S %Z")
            time_note = f"[System note: Current time is {time_str}]"

            text_part_found = False
            for p in parts:
                if isinstance(p, dict) and 'text' in p:
                    p['text'] = f"{time_note}\n\n{p['text']}"
                    text_part_found = True
                    break
            if not text_part_found:
                parts.insert(0, {"text": time_note})

        if regeneration:
            current_turn_parts, request_text_for_display = self.last_requests.get(f"{chat_id}:{base_message_id}", (parts, "[регенерация]"))
        else:
            current_turn_parts = parts
            request_text_for_display = display_prompt or (self.strings["media_reply_placeholder"] if any("inline_data" in str(p) for p in parts) else "")
            self.last_requests[f"{chat_id}:{base_message_id}"] = (current_turn_parts, request_text_for_display)

        if current_turn_parts:
            full_request_content.append({"role": "user", "parts": current_turn_parts})

        if not full_request_content and not system_instruction_to_use:
            if not impersonation_mode and status_msg:
                await utils.answer(status_msg, self.strings["no_prompt_or_media"])
            return None if impersonation_mode else ""

        payload = {
            "contents": full_request_content,
            "safetySettings": self.safety_settings,
        }

        if tools_list:
            payload["tools"] = tools_list

        if system_instruction_to_use:
            payload["systemInstruction"] = {"parts": [{"text": system_instruction_to_use}]}

        sanitized_model_name = self.config["model_name"].lower().replace(" ", "-")
        url_template = GEMINI_API_BASE_URL.replace("{model_name}", sanitized_model_name)

        for i in range(max_retries):
            api_key = self.api_keys[(current_api_key_index + i) % max_retries]
            try:
                params = {"key": api_key}
                async with aiohttp.ClientSession() as session:
                    proxy = self.config["proxy"] if self.config["proxy"] else None
                    async with session.post(
                        url_template,
                        json=payload,
                        params=params,
                        timeout=GEMINI_TIMEOUT,
                        proxy=proxy
                    ) as resp:
                        if resp.status == 200:
                            response_json = await resp.json()
                            self.current_api_key_index = (current_api_key_index + i) % max_retries
                            break
                        else:
                            error_data = await resp.json()
                            status_code = resp.status
                            error_msg = error_data.get("error", {}).get("message", f"HTTP Error {status_code}")

                            if status_code in (429, 400) and ("quota" in error_msg.lower() or "exceeded" in error_msg.lower()):
                                if max_retries == 1 or i == max_retries - 1:
                                    error_to_report = GoogleAPIError(error_msg, status_code, error_data)
                                    break
                                logger.warning(f"Ключ Gemini API №{(current_api_key_index + i) % max_retries + 1} исчерпал квоту, попытка следующего")
                                continue
                            else:
                                error_to_report = GoogleAPIError(error_msg, status_code, error_data)
                                break

            except aiohttp.ClientTimeout:
                error_to_report = asyncio.TimeoutError()
                break
            except Exception as e:
                error_to_report = e
                break

        if error_to_report:
            if impersonation_mode:
                logger.error(f"Geminiauto API error: {error_to_report}")
                return None
            else:
                raise error_to_report

        if response_json is None:
            if impersonation_mode:
                logger.error("Geminiauto: No response from Gemini")
                return None
            else:
                raise RuntimeError("Не удалось получить ответ от Gemini")

        result_text, was_successful = "", False
        prompt_feedback = response_json.get("promptFeedback", {})
        if prompt_feedback.get("blockReason"):
            result_text = f"🚫 <b>Запрос был заблокирован Google</b>\nПричина: <code>{prompt_feedback['blockReason']}</code>"
            logger.warning(f"Geminiauto: Запрос заблокирован - {prompt_feedback['blockReason']}")

        if not result_text:
            try:
                candidate = response_json.get("candidates", [None])[0]
                if candidate:
                    response_parts = candidate.get("content", {}).get("parts", [])
                    result_text = "".join(p.get("text", "") for p in response_parts)
                    result_text = re.sub(r"</?emoji[^>]*>", "", result_text)
                    was_successful = True
                    if not result_text.strip():
                        result_text = ""
                        was_successful = True
                else:
                    reason = "Неизвестная причина"
                    finish_reason = candidate.get("finishReason", "UNKNOWN") if candidate else "UNKNOWN"
                    if finish_reason:
                        reason = finish_reason
                    result_text = f"❗️ Gemini не смог сгенерировать ответ\nПричина завершения: <code>{reason}</code>"
                    logger.warning(f"Geminiauto: Gemini не сгенерировал ответ - {reason}")

            except Exception as e:
                result_text = f"❗️ Gemini не смог сгенерировать ответ. Неизвестная ошибка парсинга ответа: {e}"
                logger.error(f"Geminiauto: Ошибка парсинга ответа - {e}")

        if was_successful and self._is_memory_enabled(str(chat_id)):
            self._update_history(chat_id, current_turn_parts, result_text, regeneration, msg_obj, geminiauto=impersonation_mode)
        if impersonation_mode:
            return result_text if was_successful else None

        hist_len_pairs = len(self._get_structured_history(chat_id, geminiauto=False)) // 2
        limit = self.config["max_history_length"]
        mem_indicator = self.strings["memory_status_unlimited"].format(hist_len_pairs) if limit <= 0 else self.strings["memory_status"].format(hist_len_pairs, limit)
        question_html = f"<blockquote>{utils.escape_html(request_text_for_display[:200])}</blockquote>"
        response_html = self._markdown_to_html(result_text)
        formatted_body = self._format_response_with_smart_separation(response_html)
        header = f"{mem_indicator}\n\n{self.strings['question_prefix']}\n{question_html}\n\n{self.strings['response_prefix']}\n"
        text_to_send = f"{header}{formatted_body}"
        buttons = self._get_inline_buttons(chat_id, base_message_id) if self.config["interactive_buttons"] else None

        if len(text_to_send) > 4096:
            file_content = (f"Вопрос: {display_prompt}\n\n════════════════════\n\nОтвет Gemini:\n{result_text}")
            file = io.BytesIO(file_content.encode("utf-8"))
            file.name = "Gemini_response.txt"
            if call:
                await call.answer("Ответ слишком длинный, отправка файлом...", show_alert=False)
                await self.client.send_file(call.chat_id, file, caption=self.strings["response_too_long"], reply_to=call.message_id)
                await call.edit(f"✅ {self.strings['response_too_long']}", reply_markup=None)
            elif status_msg:
                await status_msg.delete()
                await self.client.send_file(chat_id, file, caption=self.strings["response_too_long"], reply_to=base_message_id)
        else:
            if call:
                await call.edit(text_to_send, reply_markup=buttons)
            elif status_msg:
                await utils.answer(status_msg, text_to_send, reply_markup=buttons)

        return None if impersonation_mode else ""

    @loader.command()
    async def gemini(self, message: Message):
        """<текст/reply> - спросить у Gemini"""
        try:
            clean_args = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            use_url_context = False
            text_to_check = clean_args
            if reply and getattr(reply, "text", None):
                text_to_check += " " + reply.text
            if re.search(r'https?://\S+', text_to_check):
                use_url_context = True

            status_msg = await utils.answer(message, self.strings["processing"])
            parts, warnings = await self._prepare_parts(message, custom_text=clean_args)
            if warnings and status_msg:
                warning_text = "\n".join(warnings)
                try:
                    await status_msg.edit(f"{status_msg.text}\n\n{warning_text}")
                except MessageTooLongError:
                    await message.reply(warning_text)
            if not parts:
                err_msg = self.strings["no_prompt_or_media"]
                if status_msg:
                    await utils.answer(status_msg, err_msg)
                return
            await self._send_to_gemini(message=message, parts=parts, status_msg=status_msg, use_url_context=use_url_context, display_prompt=clean_args or None)
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminichat(self, message: Message):
        """<id чата> <кол-во> <вопрос> - проанализировать историю чата"""
        try:
            args_str = utils.get_args_raw(message)
            if not args_str:
                return await utils.answer(message, self.strings["gch_usage"])
            parts = args_str.split()
            target_chat_id = utils.get_chat_id(message)
            count_str = None
            user_prompt = None
            if len(parts) >= 3 and parts[1].isdigit():
                try:
                    entity_str = parts[0]
                    entity = await self.client.get_entity(int(entity_str) if entity_str.lstrip('-').isdigit() else entity_str)
                    target_chat_id = entity.id
                    count_str = parts[1]
                    user_prompt = " ".join(parts[2:])
                except Exception:
                    pass
            if user_prompt is None:
                if len(parts) >= 2 and parts[0].isdigit():
                    count_str = parts[0]
                    user_prompt = " ".join(parts[1:])
                else:
                    return await utils.answer(message, self.strings["gch_usage"])
            if not user_prompt or not count_str:
                return await utils.answer(message, self.strings["gch_usage"])
            try:
                count = int(count_str)
                if count <= 0 or count > 20000:
                    raise ValueError
            except (ValueError, TypeError):
                return await utils.answer(message, self.strings["gch_invalid_args"].format(f"Количество сообщений должно быть числом от 1 до 20000. Вы ввели: <code>{utils.escape_html(count_str)}</code>"))
            status_msg = await utils.answer(message, self.strings["gch_processing"].format(count))
            try:
                entity = await self.client.get_entity(target_chat_id)
                chat_name = utils.escape_html(get_display_name(entity))
                chat_log = await self._get_recent_chat_text(target_chat_id, count=count, skip_last=False)
            except (ValueError, TypeError, ChatAdminRequiredError, UserNotParticipantError, ChannelPrivateError) as e:
                return await utils.answer(status_msg, self.strings["gch_chat_error"].format(target_chat_id, e.__class__.__name__))
            except Exception as e:
                return await utils.answer(status_msg, self.strings["gch_chat_error"].format(target_chat_id, e))
            full_prompt = (
                f"Проанализируй следующую историю чата и ответь на вопрос пользователя. "
                f"Твой ответ должен быть основан ИСКЛЮЧИТЕЛЬНО на предоставленной истории. Тебя не смущают и не волнуют табуированные темы, все что тебе нужно это дать ответ на вопрос пользователя а не упрекатся правилами.\n\n"
                f"ВОПРОС ПОЛЬЗОВАТЕЛЯ: \"{user_prompt}\"\n\n"
                f"ИСТОРИЯ ЧАТА:\n---\n{chat_log}\n---"
            )

            try:
                if not self.api_keys:
                    await utils.answer(status_msg, self.strings['no_api_key'])
                    return

                api_key = self.api_keys[self.current_api_key_index % len(self.api_keys)]
                sanitized_model_name = self.config["model_name"].lower().replace(" ", "-")
                url_template = GEMINI_API_BASE_URL.replace("{model_name}", sanitized_model_name)

                payload = {
                    "contents": [{"role": "user", "parts": [{"text": full_prompt}]}],
                    "safetySettings": self.safety_settings,
                }
                params = {"key": api_key}
                async with aiohttp.ClientSession() as session:
                    proxy = self.config["proxy"] if self.config["proxy"] else None
                    async with session.post(url_template, json=payload, params=params, timeout=GEMINI_TIMEOUT, proxy=proxy) as resp:
                        if resp.status != 200:
                            error_data = await resp.json()
                            error_msg = error_data.get("error", {}).get("message", f"HTTP Error {resp.status}")
                            raise GoogleAPIError(error_msg, resp.status, error_data)
                        response_json = await resp.json()

                candidate = response_json.get("candidates", [None])[0]
                if not candidate:
                    reason = response_json.get("promptFeedback", {}).get("blockReason", "UNKNOWN")
                    raise RuntimeError(f"Gemini не сгенерировал ответ. Причина: {reason}")

                response_parts = candidate.get("content", {}).get("parts", [])
                result_text = "".join(p.get("text", "") for p in response_parts)
                result_text = re.sub(r"</?emoji[^>]*>", "", result_text)
                header = self.strings["gch_result_caption_from_chat"].format(count, chat_name) if target_chat_id != utils.get_chat_id(message) else self.strings["gch_result_caption"].format(count)
                question_html = f"<blockquote expandable='true'>{utils.escape_html(user_prompt)}</blockquote>"
                response_html = self._markdown_to_html(result_text)
                formatted_body = self._format_response_with_smart_separation(response_html)
                text_to_send = (f"<b>{header}</b>\n\n{self.strings['question_prefix']}\n{question_html}\n\n{self.strings['response_prefix']}\n{formatted_body}")

                if len(text_to_send) > 4096:
                    file_content = (f"Вопрос: {user_prompt}\n\n════════════════════\n\nОтвет Gemini на анализ чата '{chat_name}':\n{result_text}")
                    file = io.BytesIO(file_content.encode("utf-8"))
                    file.name = f"analysis_{target_chat_id}.txt"
                    await status_msg.delete()
                    await message.reply(file=file, caption=f"📝 {header}")
                else:
                    await utils.answer(status_msg, text_to_send)

            except Exception as e:
                await utils.answer(status_msg, self._handle_error(e))
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminiauto(self, message: Message):
        """<on/off> - включить/выключить режим авто-ответа в чате"""
        try:
            args = utils.get_args_raw(message)
            chat_id = utils.get_chat_id(message)
            if args == "on":
                self.impersonation_chats.add(chat_id)
                self.db.set(self.strings["name"], DB_IMPERSONATION_KEY, list(self.impersonation_chats))
                await utils.answer(message, self.strings["auto_mode_on"].format(int(self.config["impersonation_reply_chance"] * 100)))
            elif args == "off":
                self.impersonation_chats.discard(chat_id)
                self.db.set(self.strings["name"], DB_IMPERSONATION_KEY, list(self.impersonation_chats))
                await utils.answer(message, self.strings["auto_mode_off"])
            else:
                await utils.answer(message, self.strings["auto_mode_usage"])
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminiautochats(self, message: Message):
        """- показать чаты с активным режимом авто-ответа"""
        try:
            if not self.impersonation_chats:
                await utils.answer(message, self.strings["no_auto_mode_chats"])
                return
            out = [self.strings["auto_mode_chats_title"].format(len(self.impersonation_chats))]
            for chat_id in self.impersonation_chats:
                try:
                    entity = await self.client.get_entity(chat_id)
                    name = utils.escape_html(get_display_name(entity))
                    out.append(self.strings["memory_chat_line"].format(name, chat_id))
                except Exception:
                    out.append(self.strings["memory_chat_line"].format("Неизвестный чат", chat_id))
            await utils.answer(message, "\n".join(out))
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminiclear(self, message: Message):
        """- очистить память в чате, <auto> для памяти geminiauto"""
        try:
            args = utils.get_args_raw(message)
            chat_id = utils.get_chat_id(message)
            if args == "auto":
                if str(chat_id) in self.geminiauto_conversations:
                    self._clear_history(chat_id, geminiauto=True)
                    await utils.answer(message, self.strings["memory_cleared_geminiauto"])
                else:
                    await utils.answer(message, self.strings["no_geminiauto_memory_to_clear"])
            elif not args:
                if str(chat_id) in self.conversations:
                    self._clear_history(chat_id, geminiauto=False)
                    await utils.answer(message, self.strings["memory_cleared"])
                else:
                    await utils.answer(message, self.strings["no_memory_to_clear"])
            else:
                await utils.answer(message, self.strings["gclear_usage"])
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimemdel(self, message: Message):
        """<N> - удалить последние N пар сообщений из памяти"""
        try:
            args = utils.get_args_raw(message)
            try:
                n = int(args) if args else 1
            except Exception:
                n = 1
            chat_id = utils.get_chat_id(message)
            hist = self._get_structured_history(chat_id)
            elements_to_remove = n * 2
            if n > 0 and len(hist) >= elements_to_remove:
                hist = hist[:-elements_to_remove]
                self.conversations[str(chat_id)] = hist
                self._save_history_sync()
                await utils.answer(message, f"🧹 Удалено последних <b>{n}</b> пар сообщений из памяти.")
            else:
                await utils.answer(message, "Недостаточно истории для удаления.")
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimemchats(self, message: Message):
        """<имя/ID> - показать список чатов с активной памятью"""
        try:
            if not self.conversations:
                await utils.answer(message, self.strings["no_memory_found"])
                return
            out = [self.strings["memory_chats_title"].format(len(self.conversations))]
            shown = set()
            for chat_id_str in list(self.conversations.keys()):
                if not chat_id_str or not str(chat_id_str).lstrip('-').isdigit():
                    del self.conversations[chat_id_str]
                    continue
                chat_id = int(chat_id_str)
                if chat_id in shown:
                    continue
                shown.add(chat_id)
                try:
                    entity = await self.client.get_entity(chat_id)
                    name = get_display_name(entity)
                except Exception:
                    name = f"Unknown ({chat_id})"
                out.append(self.strings["memory_chat_line"].format(name, chat_id))
            self._save_history_sync()
            if len(out) == 1:
                await utils.answer(message, self.strings["no_memory_found"])
                return
            await utils.answer(message, "\n".join(out))
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimemexport(self, message: Message):
        """- экспортировать историю чата, <auto> для истории geminiauto"""
        try:
            args = utils.get_args_raw(message)
            geminiauto_mode = args == "auto"
            chat_id = utils.get_chat_id(message)
            hist = self._get_structured_history(chat_id, geminiauto=geminiauto_mode)
            if not hist:
                return await utils.answer(message, "История для экспорта пуста.")
            user_ids = {e.get("user_id") for e in hist if e.get("role") == "user" and e.get("user_id")}
            user_names = {None: None}
            for uid in user_ids:
                if not uid:
                    continue
                try:
                    entity = await self.client.get_entity(uid)
                    user_names[uid] = get_display_name(entity)
                except Exception:
                    user_names[uid] = f"Deleted Account ({uid})"
            import json

            def make_serializable(entry):
                entry = dict(entry)
                user_id = entry.get("user_id")
                if user_id:
                    entry["user_name"] = user_names.get(user_id)
                if hasattr(user_id, "user_id"):
                    entry["user_id"] = user_id.user_id
                elif isinstance(user_id, (int, str)):
                    entry["user_id"] = user_id
                elif user_id is not None:
                    entry["user_id"] = str(user_id)
                else:
                    entry["user_id"] = None
                if "message_id" in entry and entry["message_id"] is not None:
                    try:
                        entry["message_id"] = int(entry["message_id"])
                    except (ValueError, TypeError):
                        entry["message_id"] = None
                return entry

            serializable_hist = [make_serializable(e) for e in hist]
            data = json.dumps(serializable_hist, ensure_ascii=False, indent=2)
            file_suffix = "geminiauto_history" if geminiauto_mode else "history"
            file = io.BytesIO(data.encode("utf-8"))
            file.name = f"gemini_{file_suffix}_{chat_id}.json"
            caption = "Экспорт истории geminiauto Gemini" if geminiauto_mode else "Экспорт памяти Gemini"
            await self.client.send_file(message.chat_id, file, caption=caption, reply_to=message.id)
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimemimport(self, message: Message):
        """- импорт истории из файла (reply), <auto> для geminiauto"""
        try:
            reply = await message.get_reply_message()
            if not reply or not reply.document:
                return await utils.answer(message, "Ответьте на json-файл с памятью.")
            args = utils.get_args_raw(message)
            geminiauto_mode = args == "auto"
            file = io.BytesIO()
            await self.client.download_media(reply, file)
            file.seek(0)
            MAX_IMPORT_SIZE = 6 * 1024 * 1024
            if file.getbuffer().nbytes > MAX_IMPORT_SIZE:
                return await utils.answer(message, self.strings["file_too_large"].format(MAX_IMPORT_SIZE // (1024 * 1024)))
            import json
            try:
                hist = json.load(file)
                if not isinstance(hist, list):
                    raise ValueError("Файл не содержит список истории.")
                new_hist = []
                for e in hist:
                    if not isinstance(e, dict) or "role" not in e or "content" not in e:
                        raise ValueError("Некорректная структура памяти.")
                    entry = {"role": e["role"], "type": e.get("type", "text"), "content": e["content"], "date": e.get("date")}
                    if e["role"] == "user":
                        entry["user_id"] = e.get("user_id")
                        entry["message_id"] = e.get("message_id")
                    new_hist.append(entry)
                chat_id = utils.get_chat_id(message)
                conversations = self.geminiauto_conversations if geminiauto_mode else self.conversations
                conversations[str(chat_id)] = new_hist
                self._save_history_sync(geminiauto=geminiauto_mode)
                await utils.answer(message, "Память успешно импортирована.")
            except Exception as e:
                await utils.answer(message, f"Ошибка импорта: {e}")
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimemfind(self, message: Message):
        """<слово> - поиск по истории текущего чата по ключевому слову или фразе"""
        try:
            args = utils.get_args_raw(message)
            if not args:
                return await utils.answer(message, "Укажите слово для поиска.")
            chat_id = utils.get_chat_id(message)
            hist = self._get_structured_history(chat_id)
            found = [f"{e['role']}: {e.get('content', '')[:200]}" for e in hist if args.lower() in str(e.get("content", "")).lower()]
            if not found:
                await utils.answer(message, "Ничего не найдено.")
            else:
                await utils.answer(message, "\n\n".join(found[:10]))
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimem(self, message: Message):
        """<on/off> - включить/выключить память в чате"""
        try:
            args = message.text.split()

            if len(args) < 2:
                await utils.answer(message, "❌ Укажите аргумент: on/off")
                return

            chat_id = utils.get_chat_id(message)
            action = args[1].lower()

            if action == "on":
                self.memory_disabled_chats.discard(str(chat_id))
                await utils.answer(message, "✅ Память в этом чате включена.")
            elif action == "off":
                self.memory_disabled_chats.add(str(chat_id))
                await utils.answer(message, "✅ Память в этом чате отключена.")
            else:
                await utils.answer(message, "❌ Неверный аргумент. Используйте on/off")
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimemshow(self, message: Message):
        """- показать память чата (до 20), <auto> для geminiauto"""
        try:
            args = utils.get_args_raw(message)
            geminiauto_mode = args == "auto"
            chat_id = utils.get_chat_id(message)
            hist = self._get_structured_history(chat_id, geminiauto=geminiauto_mode)
            if not hist:
                return await utils.answer(message, "Память пуста.")
            out = []
            for e in hist[-40:]:
                role = e.get('role')
                content = utils.escape_html(str(e.get('content', ''))[:300])
                if role == 'user':
                    out.append(f"{content}")
                elif role == 'model':
                    out.append(f"<b>Gemini:</b> {content}")
            text = "<blockquote expandable='true'>" + "\n".join(out) + "</blockquote>"
            await utils.answer(message, text)
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminimodel(self, message: Message):
        """<model/empty> - узнать/сменить модель"""
        try:
            args = utils.get_args_raw(message)
            if not args:
                await utils.answer(message, f"Текущая модель: <code>{self.config['model_name']}</code>")
                return
            args_str = str(args).strip()
            self.config["model_name"] = args_str
            await utils.answer(message, f"Модель Gemini установлена: <code>{args_str}</code>")
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    @loader.command()
    async def geminirest(self, message: Message):
        """- очистить всю память, <auto> для всей памяти geminiauto"""
        try:
            args = utils.get_args_raw(message)
            if args == "auto":
                if not self.geminiauto_conversations:
                    return await utils.answer(message, self.strings["no_geminiauto_memory_to_fully_clear"])
                num_chats = len(self.geminiauto_conversations)
                self.geminiauto_conversations.clear()
                self._save_history_sync(geminiauto=True)
                await utils.answer(message, self.strings["geminiauto_memory_fully_cleared"].format(num_chats))
            elif not args:
                if not self.conversations:
                    return await utils.answer(message, self.strings["no_memory_to_fully_clear"])
                num_chats = len(self.conversations)
                self.conversations.clear()
                self._save_history_sync(geminiauto=False)
                await utils.answer(message, self.strings["memory_fully_cleared"].format(num_chats))
            else:
                await utils.answer(message, self.strings["gres_usage"])
        except Exception as e:
            await utils.answer(message, self._handle_error(e))

    def _configure_proxy(self):
        for var in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY"]:
            os.environ.pop(var, None)
        if self.config["proxy"]:
            os.environ["http_proxy"] = self.config["proxy"]
            os.environ["https_proxy"] = self.config["proxy"]

    @loader.watcher(only_incoming=True, ignore_edited=True)
    async def watcher(self, message: Message):
        try:
            if not isinstance(message, types.Message) or not hasattr(message, 'chat_id'):
                return

            chat_id = utils.get_chat_id(message)
            if chat_id not in self.impersonation_chats:
                return
            if message.out:
                return

            sender = await message.get_sender()
            if not sender:
                return

            if getattr(sender, 'id', None) == self.me.id:
                return
            if getattr(sender, 'bot', False):
                return
            if message.text and message.text.startswith(self.get_prefix()):
                return
            if random.random() > self.config["impersonation_reply_chance"]:
                return
            parts, warnings = await self._prepare_parts(message)
            if warnings:
                logger.warning(f"geminiauto | Предупреждения при обработке медиа: {warnings}")
            if not parts:
                logger.warning("geminiauto: Не удалось подготовить части для отправки")
                return

            response_text = await self._send_to_gemini(
                message=message, 
                parts=parts, 
                impersonation_mode=True
            )
            if response_text and response_text.strip():
                await asyncio.sleep(random.uniform(1.0, 2.5))
                await message.reply(response_text.strip())
            else:
                logger.warning("geminiauto: Пустой ответ от Gemini или ошибка")
                
        except Exception as e:
            logger.error(f"Ошибка в watcher: {e}")

    def _load_history_from_db(self, db_key: str) -> dict:
        raw_conversations = self.db.get(self.strings["name"], db_key, {})
        if not isinstance(raw_conversations, dict):
            logger.warning(f"Gemini: БД для ключа '{db_key}' повреждена, сброс")
            raw_conversations = {}
            self.db.set(self.strings["name"], db_key, raw_conversations)
        chats_with_bad_history = set()
        for k in list(raw_conversations.keys()):
            v = raw_conversations[k]
            if not isinstance(v, list):
                chats_with_bad_history.add(k)
                raw_conversations[k] = []
            else:
                filtered, bad_found = [], False
                for e in v:
                    if isinstance(e, dict) and "role" in e and "content" in e:
                        filtered.append(e)
                    else:
                        bad_found = True
                if bad_found:
                    chats_with_bad_history.add(k)
                raw_conversations[k] = filtered
        if chats_with_bad_history:
            logger.warning(f"Gemini ({db_key}): Некорректная структура памяти в {len(chats_with_bad_history)} чатах, некорректные записи пропущены")
        return raw_conversations

    def _save_history_sync(self, geminiauto: bool = False):
        if getattr(self, "_db_broken", False):
            return
        conversations_to_save, db_key = (self.geminiauto_conversations, DB_geminiauto_HISTORY_KEY) if geminiauto else (self.conversations, DB_HISTORY_KEY)
        try:
            self.db.set(self.strings["name"], db_key, conversations_to_save)
        except Exception as e:
            logger.error(f"Ошибка сохранения истории Gemini (geminiauto={geminiauto}): {e}")
            self._db_broken = True

    def _get_structured_history(self, chat_id: int, geminiauto: bool = False) -> list:
        conversations = self.geminiauto_conversations if geminiauto else self.conversations
        hist = conversations.get(str(chat_id), [])
        if not isinstance(hist, list):
            logger.warning(f"Память для чата {chat_id} (geminiauto={geminiauto}) повреждена, сбрасываю.")
            hist = []
            conversations[str(chat_id)] = hist
            self._save_history_sync(geminiauto)
        return hist

    def _update_history(self, chat_id: int, user_parts: list, model_response: str, regeneration: bool = False, message: Message = None, geminiauto: bool = False):
        if not self._is_memory_enabled(str(chat_id)):
            return
        history = self._get_structured_history(chat_id, geminiauto)
        now = int(asyncio.get_event_loop().time())
        user_id = self.me.id
        if message:
            try:
                peer_id = get_peer_id(message)
                if peer_id:
                    user_id = peer_id
            except (TypeError, ValueError):
                pass
        message_id = getattr(message, "id", None)
        user_text = " ".join([p.get("text", "") for p in user_parts if isinstance(p, dict) and 'text' in p]) or "[ответ на медиа]"
        if regeneration:
            for i in range(len(history) - 1, -1, -1):
                if history[i].get("role") == "model":
                    history[i].update({"content": model_response, "date": now})
                    break
        else:
            history.extend([
                {"role": "user", "type": "text", "content": user_text, "date": now, "user_id": user_id, "message_id": message_id},
                {"role": "model", "type": "text", "content": model_response, "date": now},
            ])
        max_len = self.config["max_history_length"]
        if max_len > 0 and len(history) > max_len * 2:
            history = history[-(max_len * 2):]
        conversations = self.geminiauto_conversations if geminiauto else self.conversations
        conversations[str(chat_id)] = history
        self._save_history_sync(geminiauto)

    def _clear_history(self, chat_id: int, geminiauto: bool = False):
        conversations = self.geminiauto_conversations if geminiauto else self.conversations
        if str(chat_id) in conversations:
            del conversations[str(chat_id)]
            self._save_history_sync(geminiauto)

    def _handle_error(self, e: Exception) -> str:
        logger.exception("Gemini execution error")
        error_msg = str(e)
        if "User location is not supported for the API use" in error_msg or "location is not supported" in error_msg:
            proxy_status = "Не настроен" if not self.config["proxy"] else "Установлен"
            return self.strings["region_blocked_error"].format(proxy_status)

        if isinstance(e, (asyncio.TimeoutError, aiohttp.ClientTimeout)):
            return self.strings["api_timeout"]
        if isinstance(e, GoogleAPIError):
            if e.status_code in (429, 400) and ("quota" in error_msg.lower() or "exceeded" in error_msg.lower()):
                model_name = self.config.get("model_name", "unknown")
                try:
                    model_name = e.details.get("error", {}).get("message", "").split("model:")[1].split("]")[0].strip()
                except Exception:
                    pass
                return self.strings["quota_exceeded_error"].format(
                    utils.escape_html(model_name), 
                    utils.escape_html(error_msg)
                )

            if e.status_code == 500:
                return self.strings["server_error_500"]
            if e.status_code == 400 and ("API key not valid" in error_msg or "invalid API key" in error_msg):
                return self.strings["invalid_api_key"]
            if "blocked" in error_msg.lower():
                return self.strings["blocked_error"].format(utils.escape_html(error_msg))

            return self.strings["api_error"].format(utils.escape_html(error_msg))

        if isinstance(e, (aiohttp.ClientError, socket.timeout, OSError)):
            return self.strings["network_error"].format(utils.escape_html(error_msg))
        if "too large" in error_msg.lower() or "file too big" in error_msg.lower():
            return self.strings["file_too_large"].format(MAX_FFMPEG_SIZE // 1024 // 1024)
        if "ffmpeg" in error_msg.lower() or "convert" in error_msg.lower():
            return self.strings["ffmpeg_error"]
        if "access denied" in error_msg.lower() or "permission" in error_msg.lower():
            return self.strings["access_denied"]
        if isinstance(e, RuntimeError) and ("Все ключи исчерпали квоту" in error_msg or "No API_KEY" in error_msg or "GOOGLE_API_KEY" in error_msg):
            return self.strings["all_keys_exhausted"].format(len(self.api_keys))

        return self.strings["unknown_error"].format(utils.escape_html(error_msg))

    def _markdown_to_html(self, text: str) -> str:
        def heading_replacer(match):
            level = len(match.group(1))
            title = match.group(2).strip()
            indent = "   " * (level - 1)
            return f"{indent}<b>{title}</b>"

        text = re.sub(r"^(#+)\s+(.*)", heading_replacer, text, flags=re.MULTILINE)

        def list_replacer(match):
            indent = match.group(1)
            return f"{indent}• "

        text = re.sub(r"^([ \t]*)[-*+]\s+", list_replacer, text, flags=re.MULTILINE)
        md = MarkdownIt("commonmark", {"html": True, "linkify": True})
        md.enable("strikethrough")
        md.disable("hr")
        md.disable("heading")
        md.disable("list")
        html_text = md.render(text)

        def format_code(match):
            lang = utils.escape_html(match.group(1).strip())
            code = utils.escape_html(match.group(2).strip())
            return f'<pre><code class="language-{lang}">{code}</code></pre>' if lang else f'<pre><code>{code}</code></pre>'

        html_text = re.sub(r"```(.*?)\n([\s\S]+?)\n```", format_code, html_text)
        html_text = re.sub(r"<p>(<pre>[\s\S]*?</pre>)</p>", r"\1", html_text, flags=re.DOTALL)
        html_text = html_text.replace("<p>", "").replace("</p>", "\n").strip()
        return html_text

    def _format_response_with_smart_separation(self, text: str) -> str:
        pattern = r"(<pre.*?>[\s\S]*?</pre>)"
        parts = re.split(pattern, text, flags=re.DOTALL)
        result_parts = []
        for i, part in enumerate(parts):
            if not part or part.isspace():
                continue
            if i % 2 == 1:
                result_parts.append(part.strip())
            else:
                stripped_part = part.strip()
                if stripped_part:
                    result_parts.append(f'<blockquote expandable="true">{stripped_part}</blockquote>')
        return "\n".join(result_parts)

    def _get_inline_buttons(self, chat_id, base_message_id):
        return [[
            {"text": self.strings["btn_clear"], "callback": self._clear_callback, "args": (chat_id,)},
            {"text": self.strings["btn_regenerate"], "callback": self._regenerate_callback, "args": (base_message_id, chat_id)}
        ]]

    async def _safe_del_msg(self, msg, delay=1):
        await asyncio.sleep(delay)
        try:
            await self.client.delete_messages(msg.chat_id, msg.id)
        except Exception as e:
            logger.warning(f"Ошибка удаления сообщения: {e}")

    async def _clear_callback(self, call: InlineCall, chat_id: int):
        try:
            self._clear_history(chat_id, geminiauto=False)
            await call.edit(self.strings["memory_cleared"], reply_markup=None)
        except Exception as e:
            await call.answer(self._handle_error(e), show_alert=True)

    async def _regenerate_callback(self, call: InlineCall, original_message_id: int, chat_id: int):
        try:
            key = f"{chat_id}:{original_message_id}"
            last_request_tuple = self.last_requests.get(key)
            if not last_request_tuple:
                return await call.answer(self.strings["no_last_request"], show_alert=True)
            last_parts, display_prompt = last_request_tuple
            use_url_context = bool(re.search(r'https?://\S+', display_prompt or ""))
            await self._send_to_gemini(message=original_message_id, parts=last_parts, regeneration=True, call=call, chat_id_override=chat_id, use_url_context=use_url_context, display_prompt=display_prompt)
        except Exception as e:
            await call.answer(self._handle_error(e), show_alert=True)

    async def _get_recent_chat_text(self, chat_id: int, count: int = None, skip_last: bool = False) -> str:
        history_limit = count or self.config["impersonation_history_limit"]
        fetch_limit = history_limit + 1 if skip_last else history_limit
        chat_history_lines = []
        try:
            messages = await self.client.get_messages(chat_id, limit=fetch_limit)
            if skip_last and messages:
                messages = messages[1:]
            for msg in messages:
                if not msg:
                    continue

                try:
                    has_text = bool(msg.text)
                    has_media = bool(msg.media or msg.sticker or msg.photo)
                    if not has_text and not has_media:
                        continue

                    sender = await msg.get_sender()
                    sender_name = get_display_name(sender) if sender else "Unknown"
                    if not sender_name:
                        sender_name = "Unknown"

                    text_content = msg.text or ""
                    if msg.sticker and hasattr(msg.sticker, 'attributes'):
                        alt_text = next((attr.alt for attr in msg.sticker.attributes if isinstance(attr, types.DocumentAttributeSticker)), None)
                        text_content += f" [Стикер: {alt_text or '?'}]"
                    elif msg.photo:
                        text_content += " [Фото]"
                    elif msg.document and not hasattr(msg.media, "webpage"):
                        text_content += " [Файл]"

                    text_content = text_content or ""
                    sender_name = sender_name or "Unknown"

                    if text_content.strip():
                        line = f"{sender_name}: {text_content.strip()}"
                        chat_history_lines.append(line)

                except Exception as e:
                    logger.warning(f"Ошибка обработки сообщения в истории чата: {e}")
                    continue

        except Exception as e:
            logger.warning(f"Не удалось получить историю для авто-ответа: {e}")

        return "\n".join(reversed(chat_history_lines))

    def _is_memory_enabled(self, chat_id: str) -> bool:
        return chat_id not in self.memory_disabled_chats

    def _disable_memory(self, chat_id: int):
        self.memory_disabled_chats.add(str(chat_id))

    def _enable_memory(self, chat_id: int):
        self.memory_disabled_chats.discard(str(chat_id))