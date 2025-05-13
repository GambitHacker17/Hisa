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
    
    @loader.owner
    async def b64encodecmd(self, message):
        """<text/media or reply>"""
        reply = await message.get_reply_message()
        mtext = utils.get_args_raw(message)
        
        if message.media:
            file_ext = os.path.splitext(message.file.name)[1].lower() if message.file.name else ""
            if file_ext == '.txt':
                await message.edit("<b>Чтение текстового файла</b>")
                txt_data = (await message.download_media(bytes)).decode('utf-8')
                data = bytes(txt_data, "utf-8")
            else:
                await message.edit("<b>Загрузка файла</b>")
                data = await message.client.download_file(message, bytes)
        elif mtext:
            data = bytes(mtext, "utf-8")
        elif reply:
            if reply.media:
                file_ext = os.path.splitext(reply.file.name)[1].lower() if reply.file.name else ""
                if file_ext == '.txt':
                    await message.edit("<b>Чтение текстового файла</b>")
                    txt_data = (await reply.download_media(bytes)).decode('utf-8')
                    data = bytes(txt_data, "utf-8")
                else:
                    await message.edit("<b>Загрузка файла</b>")
                    data = await message.client.download_file(reply, bytes)
            else:
                data = bytes(reply.raw_text, "utf-8")
        else:
            await message.edit("<b>Что нужно закодировать?</b>")
            return
            
        output = b64encode(data)
        if len(output) > 4000:
            output = io.BytesIO(output)
            output.name = "base64.txt"
            output.seek(0)
            await message.client.send_file(message.to_id, output, reply_to=reply)
            await message.delete()
        else:
            await message.edit(str(output, "utf-8"))
    
    @loader.owner
    async def b64decodecmd(self, message):
        """<text or reply to text/file>"""
        reply = await message.get_reply_message()
        mtext = utils.get_args_raw(message)
        
        if mtext:
            data = mtext
        elif reply:
            if reply.media:
                file_ext = os.path.splitext(reply.file.name)[1].lower() if reply.file.name else ""
                if file_ext == '.txt':
                    await message.edit("<b>Чтение текстового файла</b>")
                    data = (await reply.download_media(bytes)).decode('utf-8')
                else:
                    await message.edit("<b>Расшифровка файлов невозможна</b>")
                    return
            else:
                data = reply.raw_text
        else:
            await message.edit("<b>Что нужно декодировать?</b>")
            return
            
        try:
            if re.match(r'^[A-Za-z0-9+/]+={0,2}$', data):
                output = b64decode(data)

                if output.startswith(b'\xFF\xD8') or output.startswith(b'\x89PNG') or output.startswith(b'GIF8'):
                    file = io.BytesIO(output)
                    ext = '.jpg'
                    if output.startswith(b'\x89PNG'):
                        ext = '.png'
                    elif output.startswith(b'GIF8'):
                        ext = '.gif'
                    
                    file.name = f"decoded_image{ext}"
                    file.seek(0)
                    await message.client.send_file(message.to_id, file, reply_to=reply)
                    await message.delete()
                    return

                try:
                    text_output = output.decode('utf-8')
                    if len(text_output) > 4000:
                        file = io.BytesIO(output)
                        file.name = "decoded.txt"
                        file.seek(0)
                        await message.client.send_file(message.to_id, file, reply_to=reply)
                        await message.delete()
                    else:
                        await message.edit(text_output)
                except UnicodeDecodeError:
                    file = io.BytesIO(output)
                    file.name = "decoded.bin"
                    file.seek(0)
                    await message.client.send_file(message.to_id, file, reply_to=reply)
                    await message.delete()
            else:
                await message.edit("<b>Это не похоже на данные в формате base64</b>")
        except Exception as e:
            await message.edit(f"<b>Ошибка декодирования: {str(e)}</b>")