# meta developer: @MartyyyK

from asyncio import sleep, Event
from telethon import functions
from random import randint
from .. import loader, utils


@loader.tds
class FakeMod(loader.Module):
    """Имитация действий с возможностью выбора времени(сек)"""

    strings = {"name": "Fake Actions"}

    def __init__(self):
        self.stop_event = Event()
        self.stop_event.set()

    async def typecmd(self, message):
        """Набор текста"""
        await self._handle_action(message, "typing")

    async def voicecmd(self, message):
        """Отправка голосового сообщения"""
        await self._handle_action(message, "voice")

    async def gamecmd(self, message):
        """Активность в игре"""
        await self._handle_action(message, "game")

    async def videocmd(self, message):
        """Отправка видео"""
        await self._handle_action(message, "video")

    async def photocmd(self, message):
        """Отправка фото"""
        await self._handle_action(message, "photo")

    async def documentcmd(self, message):
        """Отправка документа"""
        await self._handle_action(message, "document")

    async def locationcmd(self, message):
        """Отправка геолокации"""
        await self._handle_action(message, "location")

    async def recordvideocmd(self, message):
        """Запись видео"""
        await self._handle_action(message, "record-video")

    async def recordvoicecmd(self, message):
        """Запись голосового сообщения"""
        await self._handle_action(message, "record-audio")

    async def recordroundcmd(self, message):
        """Запись видеосообщения"""
        await self._handle_action(message, "record-round")

    async def stopimitcmd(self, message):
        """Остановить текущую имитацию"""
        await message.delete()
        if not self.stop_event.is_set():
            self.stop_event.set()

    async def _handle_action(self, message, action):
        await message.delete()
        self.stop_event.set()
        
        args = utils.get_args(message)
        duration = int(args[0]) if args else 60
        
        if duration <= 0:
            return
            
        self.stop_event.clear()
        
        try:
            async with message.client.action(message.chat_id, action):
                await self._wait_with_stop(duration)
        except BaseException:
            pass
        finally:
            self.stop_event.set()

    async def _wait_with_stop(self, duration):
        for _ in range(duration):
            if self.stop_event.is_set():
                break
            await sleep(1)