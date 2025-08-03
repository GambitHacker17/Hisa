from hisatl.types import Message
from .. import loader, utils
import asyncio

@loader.tds
class InfiniteSpinnerMod(loader.Module):
    """Infinite message spinner that alternates between dots and commas"""
    
    strings = {
        "name": "InfiniteSpinner",
        "usage": "❌ Usage: .sbot <start/stop>",
        "started": "🔄 Started infinite spinning! Use .sbot stop to end",
        "stopped": "✅ Stopped spinning!",
        "already_running": "❌ Spinner is already running!",
        "not_running": "❌ No spinner is currently running",
    }
    
    strings_ru = {
        "usage": "❌ Использование: .sbot <start/stop>",
        "started": "🔄 Запущено бесконечное кручение! Используйте .sbot stop для остановки",
        "stopped": "✅ Кручение остановлено!",
        "already_running": "❌ Кручение уже запущено!",
        "not_running": "❌ Кручение в данный момент не активно",
    }
    
    def __init__(self):
        self.spin_task = None
        self.stop_flag = False
        
    async def spin_message(self, target):
        """Background task for infinite spinning"""
        original_text = target.text
        counter = 0
        
        while not self.stop_flag:
            counter += 1
            if counter % 2 == 0:
                new_text = original_text + "."
            else:
                new_text = original_text + ","
                
            try:
                await utils.answer(target, new_text)
                await asyncio.sleep(0.5)  # Adjustable delay
            except:
                break  # Stop if message was deleted or error occurred

    @loader.command(ru_doc="Бесконечное кручение сообщения")
    async def sbotcmd(self, message: Message):
        """Start/stop infinite message spinning"""
        args = utils.get_args_raw(message).lower()
        
        # Start spinning
        if args == "start":
            if self.spin_task and not self.spin_task.done():
                await utils.answer(message, self.strings("already_running"))
                return
                
            target = await message.get_reply_message()
            if not target:
                target = message
                
            self.stop_flag = False
            self.spin_task = asyncio.ensure_future(self.spin_message(target))
            await utils.answer(message, self.strings("started"))
            
        # Stop spinning
        elif args == "stop":
            if not self.spin_task or self.spin_task.done():
                await utils.answer(message, self.strings("not_running"))
                return
                
            self.stop_flag = True
            await self.spin_task  # Wait for task to complete
            await utils.answer(message, self.strings("stopped"))
            
        # Invalid usage
        else:
            await utils.answer(message, self.strings("usage"))
            
    async def on_unload(self):
        """Cleanup when module is unloaded"""
        if self.spin_task and not self.spin_task.done():
            self.stop_flag = True
            await self.spin_task