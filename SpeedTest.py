# meta developer: @MartyyyK
# requires: speedtest-cli

from typing import Tuple

from telethon import TelegramClient
from telethon.tl.custom import Message

import speedtest

from .. import loader, utils

@loader.tds
class SpeedtestMod(loader.Module):
    """Tests your internet speed with unit selection"""

    strings = {
        "name": "Speedtest",
        "author": "@MartyyyK",
        "running": "<emoji document_id=5334904192622403796>🫥</emoji> <b>Checking your internet speed...</b>",
        "result": (
            "<b><emoji document_id=5962848855341928446>⬇️</emoji> Download: <code>{download}</code> {unit}/s</b>\n"
            "<b><emoji document_id=5974082402434157917>🎙</emoji> Upload: <code>{upload}</code> {unit}/s</b>\n"
            "<b><emoji document_id=5974475701179387553>😀</emoji> Ping: <code>{ping}</code> ms</b>"
        ),
    }

    strings_ru = {
        "_cls_doc": "Проверяет скорость интернета с выбором единиц измерения",
        "_cmd_doc_speedtest": "Проверить скорость интернета",
        "running": "<emoji document_id=5334904192622403796>🫥</emoji> <b>Проверяем скорость интернета...</b>",
        "result": (
            "<b><emoji document_id=5962848855341928446>⬇️</emoji> Скачать: <code>{download}</code> {unit}/с</b>\n"
            "<b><emoji document_id=5974082402434157917>🎙</emoji> Загрузить: <code>{upload}</code> {unit}/с</b>\n"
            "<b><emoji document_id=5974475701179387553>😀</emoji> Пинг: <code>{ping}</code> мс</b>"
        ),
    }

    async def speedtestcmd(self, message: Message):
        """Run speedtest with unit selection"""
        m = await utils.answer(message, self.strings("running"))
        results = await utils.run_sync(self.run_speedtest)
        
        # Save raw results in bits per second
        self.raw_results = results
        
        # Create inline buttons for unit selection
        buttons = [
            [
                {"text": "KB/s", "callback": self._unit_kb},
                {"text": "MB/s", "callback": self._unit_mb},
                {"text": "Mbit/s", "callback": self._unit_mbit}
            ]
        ]
        
        # Show results in Mbit/s by default
        await self._show_results(m, results, "Mbit", buttons)

    @staticmethod
    def run_speedtest() -> Tuple[float, float, float]:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]

    async def _unit_kb(self, call):
        """Handle KB/s button"""
        await self._show_results(call, self.raw_results, "KB", self._get_buttons())

    async def _unit_mb(self, call):
        """Handle MB/s button"""
        await self._show_results(call, self.raw_results, "MB", self._get_buttons())

    async def _unit_mbit(self, call):
        """Handle Mbit/s button"""
        await self._show_results(call, self.raw_results, "Mbit", self._get_buttons())

    def _get_buttons(self):
        """Return buttons markup"""
        return [
            [
                {"text": "KB/s", "callback": self._unit_kb},
                {"text": "MB/s", "callback": self._unit_mb},
                {"text": "Mbit/s", "callback": self._unit_mbit}
            ]
        ]

    async def _show_results(self, message, results, unit, buttons):
        """Show results with proper unit conversion"""
        download, upload, ping = results
        
        if unit == "KB":
            # 1 KB = 8 Kbit, 1 B = 8 bit
            download_speed = round(download / 8 / 1024, 2)
            upload_speed = round(upload / 8 / 1024, 2)
        elif unit == "MB":
            # 1 MB = 8 Mbit
            download_speed = round(download / 8 / 1024 / 1024, 2)
            upload_speed = round(upload / 8 / 1024 / 1024, 2)
        else:  # Mbit
            # 1 Mbit = 1024 Kbit = 1024 * 1024 bit
            download_speed = round(download / 1024 / 1024, 2)
            upload_speed = round(upload / 1024 / 1024, 2)
        
        await utils.answer(
            message,
            self.strings("result").format(
                download=download_speed,
                upload=upload_speed,
                ping=round(ping, 3),
                unit=unit
            ),
            reply_markup=buttons
        )