# meta developer: @MartyyyK
# requires: speedtest-cli

from typing import Tuple

from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.tl.types import ReplyInlineMarkup, KeyboardButtonRow, KeyboardButtonCallback

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
        "select_unit": "Select speed unit:",
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
        "select_unit": "Выберите единицу измерения:",
    }

    async def speedtestcmd(self, message: Message):
        """Run speedtest with unit selection"""
        m = await utils.answer(message, self.strings("running"))
        results = await utils.run_sync(self.run_speedtest)
        
        # Save raw results in memory for callback
        self.raw_results = results
        
        # Create inline buttons for unit selection
        buttons = [
            KeyboardButtonRow([
                KeyboardButtonCallback(
                    "KB/s",
                    data="unit_kb"
                ),
                KeyboardButtonCallback(
                    "MB/s",
                    data="unit_mb"
                ),
                KeyboardButtonCallback(
                    "Mbit/s",
                    data="unit_mbit"
                )
            ])
        ]
        
        # Show results in Mbit/s by default (original behavior)
        await utils.answer(
            m,
            self.strings("result").format(
                download=round(results[0] / 1024 / 1024, 2),
                upload=round(results[1] / 1024 / 1024, 2),
                ping=round(results[2], 3),
                unit="Mbit"
            ),
            reply_markup=ReplyInlineMarkup(buttons)
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

    async def callback_handler(self, call):
        """Handle inline button callbacks"""
        if not hasattr(self, 'raw_results'):
            await call.answer("Results expired, please run test again")
            return
            
        download, upload, ping = self.raw_results
        
        if call.data == "unit_kb":
            # Convert to KB/s
            download_speed = round(download / 1024, 2)
            upload_speed = round(upload / 1024, 2)
            unit = "KB"
        elif call.data == "unit_mb":
            # Convert to MB/s
            download_speed = round(download / 1024 / 1024, 2)
            upload_speed = round(upload / 1024 / 1024, 2)
            unit = "MB"
        elif call.data == "unit_mbit":
            # Convert to Mbit/s
            download_speed = round(download / 1024 / 1024, 2)
            upload_speed = round(upload / 1024 / 1024, 2)
            unit = "Mbit"
        else:
            await call.answer("Unknown option")
            return
            
        buttons = [
            KeyboardButtonRow([
                KeyboardButtonCallback(
                    "KB/s",
                    data="unit_kb"
                ),
                KeyboardButtonCallback(
                    "MB/s",
                    data="unit_mb"
                ),
                KeyboardButtonCallback(
                    "Mbit/s",
                    data="unit_mbit"
                )
            ])
        ]
        
        await call.edit(
            self.strings("result").format(
                download=download_speed,
                upload=upload_speed,
                ping=round(ping, 3),
                unit=unit
            ),
            reply_markup=ReplyInlineMarkup(buttons)
        )
        await call.answer()