# meta developer: @MartyyyK

from .. import loader, utils
import io
import os
import re
from base64 import b64encode, b64decode

@loader.tds
class base64Mod(loader.Module):
    """Кодирование и декодирование base64"""
    strings = {"name": "Base64"}
    
    def extract_pure_base64(self, text: str) -> str:
        """Извлекает чистый base64 текст, игнорируя всё остальное"""
        matches = re.findall(r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?', text)
        if matches:
            valid_matches = [m for m in matches if len(m) >= 20 and re.fullmatch(r'[A-Za-z0-9+/]+={0,2}', m)]
            if valid_matches:
                return max(valid_matches, key=len)
        return ""

    async def detect_file_type(self, data: bytes) -> tuple:
        """Определяет тип файла по сигнатурам"""
        if data.startswith(b'\xFF\xD8'):
            return data, 'image/jpeg', '.jpg'
        elif data.startswith(b'\x89PNG'):
            return data, 'image/png', '.png'
        elif data.startswith(b'GIF8'):
            return data, 'image/gif', '.gif'
        elif data.startswith(b'\x49\x49\x2A\x00') or data.startswith(b'\x4D\x4D\x00\x2A'):
            return data, 'image/tiff', '.tiff'
        elif data.startswith(b'BM'):
            return data, 'image/bmp', '.bmp'
        elif data.startswith(b'\x00\x00\x01\x00'):
            return data, 'image/x-icon', '.ico'
        elif data.startswith(b'\x52\x49\x46\x46') and data[8:12] == b'WEBP':
            return data, 'image/webp', '.webp'
        elif data.startswith(b'\x00\x00\x00 ftyp'):
            return data, 'video/mp4', '.mp4'
        elif data.startswith(b'\x1A\x45\xDF\xA3'):
            return data, 'video/webm', '.webm'
        elif data.startswith(b'\x52\x49\x46\x46') and data[8:12] == b'AVI ':
            return data, 'video/x-msvideo', '.avi'
        elif data.startswith(b'\x30\x26\xB2\x75'):
            return data, 'video/wmv', '.wmv'
        elif data.startswith(b'\x46\x4C\x56\x01'):
            return data, 'video/x-flv', '.flv'
        elif data.startswith(b'ID3'):
            return data, 'audio/mpeg', '.mp3'
        elif data.startswith(b'OggS'):
            return data, 'audio/ogg', '.ogg'
        elif data.startswith(b'fLaC'):
            return data, 'audio/flac', '.flac'
        elif data.startswith(b'RIFF') and data[8:12] == b'WAVE':
            return data, 'audio/wav', '.wav'
        elif data.startswith(b'%PDF'):
            return data, 'application/pdf', '.pdf'
        elif data.startswith(b'PK\x03\x04'):
            return data, 'application/zip', '.zip'
        elif data.startswith(b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'):
            return data, 'application/vnd.ms-office', '.doc'
        elif data.startswith(b'\x50\x4B\x03\x04\x14\x00\x06\x00'):
            return data, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.docx'
        try:
            text_output = data.decode('utf-8')
            if len(text_output) > 1000 or '\x00' in text_output:
                return data, 'application/octet-stream', '.bin'
            return data, 'text/plain', '.txt'
        except UnicodeDecodeError:
            return data, 'application/octet-stream', '.bin'

    @loader.owner
    async def b64encodecmd(self, message):
        """<text/media or reply> - Закодировать в base64"""
        reply = await message.get_reply_message()
        mtext = utils.get_args_raw(message)
        try:
            if message.media:
                await message.edit("<b>📥 Загрузка файла...</b>")
                data = await message.client.download_file(message, bytes)
            elif mtext:
                data = bytes(mtext, "utf-8")
            elif reply:
                if reply.media:
                    await message.edit("<b>📥 Загрузка файла...</b>")
                    data = await message.client.download_file(reply, bytes)
                else:
                    data = bytes(reply.raw_text, "utf-8")
            else:
                await message.edit("<b>❌ Что нужно закодировать?</b>")
                return

            output = b64encode(data)
            if len(output) > 4000:
                output_file = io.BytesIO(output)
                output_file.name = "base64.txt"
                output_file.seek(0)
                await message.client.send_file(
                    message.to_id, 
                    output_file, 
                    reply_to=reply,
                    caption="<b>🔐 Закодированные данные в base64</b>"
                )
                await message.delete()
            else:
                await message.edit(f"<b>🔐 Base64:</b>\n<code>{str(output, 'utf-8')}</code>")
                
        except Exception as e:
            await message.edit(f"<b>❌ Ошибка кодирования:</b>\n<code>{str(e)}</code>")

    @loader.owner
    async def b64decodecmd(self, message):
        """<text or reply to text/file> - Декодировать из base64"""
        reply = await message.get_reply_message()
        mtext = utils.get_args_raw(message)
        try:
            if mtext:
                text_data = mtext
            elif reply:
                if reply.media:
                    file_ext = os.path.splitext(reply.file.name)[1].lower() if reply.file.name else ""
                    if file_ext == '.txt':
                        await message.edit("<b>📖 Чтение текстового файла...</b>")
                        text_data = (await reply.download_media(bytes)).decode('utf-8')
                    else:
                        await message.edit("<b>❌ Можно декодировать только из текста или .txt файлов</b>")
                        return
                else:
                    text_data = reply.raw_text
            else:
                await message.edit("<b>❌ Что нужно декодировать?</b>")
                return

            base64_data = self.extract_pure_base64(text_data)
            if not base64_data:
                await message.edit("<b>❌ Не найдены валидные base64 данные</b>")
                return

            output = b64decode(base64_data)
            file_data, mime_type, file_ext = await self.detect_file_type(output)

            if mime_type.startswith(('image/', 'video/', 'audio/')):
                file = io.BytesIO(file_data)
                file.name = f"decoded{file_ext}"
                file.seek(0)
                await message.client.send_file(
                    message.to_id,
                    file,
                    reply_to=reply,
                    caption=f"<b>📤 Декодированный файл</b>"
                )
                await message.delete()
            elif mime_type == 'text/plain':
                text_output = file_data.decode('utf-8')
                if len(text_output) > 4000:
                    file = io.BytesIO(file_data)
                    file.name = f"decoded{file_ext}"
                    file.seek(0)
                    await message.client.send_file(
                        message.to_id,
                        file,
                        reply_to=reply
                    )
                    await message.delete()
                else:
                    await message.edit(f"<b>📝 Декодированный текст:</b>\n<code>{text_output}</code>")
            else:
                file = io.BytesIO(file_data)
                file.name = f"decoded{file_ext}"
                file.seek(0)
                await message.client.send_file(
                    message.to_id,
                    file,
                    reply_to=reply,
                    caption=f"<b>📦 Декодированный файл</b>"
                )
                await message.delete()
                
        except Exception as e:
            await message.edit(f"<b>❌ Ошибка декодирования:</b>\n<code>{str(e)}</code>")