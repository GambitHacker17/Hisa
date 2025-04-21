# meta developer: @MartyyyK

from asyncio import sleep
from telethon import functions
from random import randint
from .. import loader, utils


@loader.tds
class FakeMod(loader.Module):
    """Имитация действий"""

    strings = {"name": "Fake Actions"}

    async def typecmd(self, message):
        """Набор текста"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def voicecmd(self, message):
        """Отправка голосового сообщения"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "voice"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "voice"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def gamecmd(self, message):
        """Активность в игре"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "game"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "game"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def videocmd(self, message):
        """Отправка видео"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "video"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "video"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def photocmd(self, message):
        """Отправка фото"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "photo"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "photo"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def documentcmd(self, message):
        """Отправка документа"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "document"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "document"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def locationcmd(self, message):
        """Отправка геолокации"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "location"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "location"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def recordvideocmd(self, message):
        """Запись видео"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "record-video"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "record-video"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def recordvoicecmd(self, message):
        """Запись голосового сообщения"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "record-audio"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "record-audio"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def recordroundcmd(self, message):
        """Запись видеосообщения"""
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "record-round"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "record-round"):
                    await sleep(randint(30, 60))
            except BaseException:
                return

    async def scrncmd(self, message):
        """Уведомление о скриншоте (только в лс)"""
        a = 1
        r = utils.get_args(message)
        if r and r[0].isdigit():
            a = int(r[0])
        for _ in range(a):
            await message.client(
                functions.messages.SendScreenshotNotificationRequest(
                    peer=message.to_id, reply_to_msg_id=message.id
                )
            )
        await message.delete()