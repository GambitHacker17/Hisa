# meta developer: @MartyyyK

import os
import shutil
import asyncio
from pathlib import Path
from hisatl.types import Message
from .. import loader, utils

@loader.tds
class CacheCleanerMod(loader.Module):
    """Модуль для очистки кеша"""
    strings = {
        "name": "CacheCleaner",
        "cleaning": "🧹 Очищаю кеш...",
        "done": "✅ <b>Очистка завершена!</b>\nУдалено папок: {folders}\nУдалено файлов: {files}",
        "error": "❌ Ошибка при очистке: {error}",
        "invalid_path": "❌ Указан неверный путь"
    }

    async def clcachecmd(self, message: Message):
        """- очистить кеш Hisa"""
        args = utils.get_args_raw(message)
        base_dir = Path(args) if args else Path.cwd()

        if not base_dir.exists():
            await utils.answer(message, self.strings("invalid_path"))
            return

        await utils.answer(message, self.strings("cleaning"))
        
        try:
            result = await asyncio.to_thread(self.remove_python_cache, base_dir)
            await utils.answer(
                message, 
                self.strings("done").format(
                    folders=result["folders"],
                    files=result["files"]
                )
            )
        except Exception as e:
            await utils.answer(
                message,
                self.strings("error").format(error=str(e))
            )

    def remove_python_cache(self, base_dir: Path) -> dict:
        total_folders = 0
        total_files = 0

        for cache_dir in base_dir.rglob('__pycache__'):
            if cache_dir.is_dir():
                try:
                    file_count = sum(len(files) for _, _, files in os.walk(cache_dir))
                    shutil.rmtree(cache_dir)
                    total_folders += 1
                    total_files += file_count
                except Exception as e:
                    raise Exception(f"Ошибка при удалении {cache_dir}: {str(e)}")

        for pattern in ['*.pyc', '*.pyo']:
            for file_path in base_dir.rglob(pattern):
                if file_path.is_file():
                    try:
                        file_path.unlink()
                        total_files += 1
                    except Exception as e:
                        raise Exception(f"Ошибка при удалении {file_path}: {str(e)}")

        return {"folders": total_folders, "files": total_files}