# meta developer: @MartyyyK
# requires: speedtest-cli

from typing import Tuple

from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.functions.channels import JoinChannelRequest

import speedtest

from .. import loader, utils

@loader.tds
class SpeedtestMod(loader.Module):
    """Tests your internet speed"""

    strings = {
        "name": "Speedtest",
        "author": "@MartyyyK",
        "running": "<emoji document_id=5334904192622403796>🫥</emoji> <b>Checking your internet speed...</b>",
        "result": (
            "<b><emoji document_id=5962848855341928446>⬇️</emoji> Download: <code>{download}</code> MBit/s</b>\n"
            "<b><emoji document_id=5974082402434157917>🎙</emoji> Upload: <code>{upload}</code> MBit/s</b>\n"
            "<b><emoji document_id=5974475701179387553>😀</emoji> Ping: <code>{ping}</code> ms</b>"
        ),
    }

    strings_ru = {
        "_cls_doc": "Проверяет скорость интернета на вашем сервере",
        "_cmd_doc_speedtest": "Проверить скорость интернета",
        "running": "<emoji document_id=5334904192622403796>🫥</emoji> <b>Проверяем скорость интернета...</b>",
        "result": (
            "<b><emoji document_id=5962848855341928446>⬇️</emoji> Скачать: <code>{download}</code> МБит/с</b>\n"
            "<b><emoji document_id=5974082402434157917>🎙</emoji> Загрузить: <code>{upload}</code> МБит/с</b>\n"
            "<b><emoji document_id=5974475701179387553>😀</emoji> Пинг: <code>{ping}</code> мс</b>"
        ),
    }

    async def client_ready(self, client: TelegramClient, _):
        """client_ready hook"""
        await client(JoinChannelRequest(channel=self.strings("author")))

    async def speedtestcmd(self, message: Message):
        """Run speedtest"""
        m = await utils.answer(message, self.strings("running"))
        results = await utils.run_sync(self.run_speedtest)
        await utils.answer(
            m,
            self.strings("result").format(
                download=round(results[0] / 1024 / 1024),
                upload=round(results[1] / 1024 / 1024),
                ping=round(results[2], 3),
            ),
        )

    @staticmethod
    def run_speedtest() -> Tuple[float, float, float]:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]