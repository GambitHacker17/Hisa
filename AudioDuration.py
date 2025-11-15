# meta developer: @MartyyyK

from .. import loader, utils
from telethon.tl.types import DocumentAttributeAudio
import os

@loader.tds
class AudioDuration(loader.Module):
    """Отправить голосовое с визуальной длительностью"""
    strings = {"name": "AudioDuration"}

    async def client_ready(self, client, db):
        self.client = client

    async def parse_duration(self, args):
        duration = 0
        i = 0

        while i < len(args):
            if args[i] == '-h' and i + 1 < len(args):
                try:
                    duration += int(args[i + 1]) * 3600
                    i += 2
                except ValueError:
                    return None, "Неверное значение для часов"
            elif args[i] == '-m' and i + 1 < len(args):
                try:
                    duration += int(args[i + 1]) * 60
                    i += 2
                except ValueError:
                    return None, "Неверное значение для минут"
            elif args[i] == '-s' and i + 1 < len(args):
                try:
                    duration += int(args[i + 1])
                    i += 2
                except ValueError:
                    return None, "Неверное значение для секунд"
            else:
                return None, f"Неизвестный флаг {args[i]}"
        
        return duration, None

    @loader.command()
    async def audiomsg(self, message):
        """- изменить длительность\n-s секунды\n-m минуты\n-h часы"""
        args = utils.get_args_raw(message).split()
        if len(args) < 2:
            await message.edit("Используй: -h часы -m минуты -s секунды")
            return

        duration, error = await self.parse_duration(args)
        if error:
            await message.edit(error)
            return

        if duration <= 0:
            await message.edit("<b>Длительность должна быть положительной</b>")
            return

        if duration > 2147483647:
            await message.edit("<b>Слишком большая длительность</b>")
            return

        reply = await message.get_reply_message()
        if not reply or not reply.file:
            await message.edit("<b>Ответь на сообщение с голосовым</b>")
            return

        file = await message.client.download_media(reply.media)
        attributes = [DocumentAttributeAudio(duration=duration, voice=True)]

        await self.client.send_file(
            message.to_id, 
            file, 
            voice_note=True, 
            attributes=attributes,
            reply_to=reply.id
        )
        os.remove(file)
        await message.delete()