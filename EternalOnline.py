# meta developer: @MartyyyK

from .. import loader
from asyncio import sleep
from telethon.tl.functions.account import UpdateStatusRequest

@loader.tds
class EternalOnlineMod(loader.Module):
    """Вечный онлайн"""
    
    strings = {
        'name': 'Eternal Online',
        'enabled': '🌐 Вечный онлайн <b>включен</b>\n'
                  '⏱ Отправка запросов: <code>{}</code> сек',
        'disabled': '🌐 Вечный онлайн <b>выключен</b>'
    }

    async def client_ready(self, client, db):
        self.db = db
        if not self.db.get("EternalOnline", "delay"):
            self.db.set("EternalOnline", "delay", 60)
        if not self.db.get("EternalOnline", "status"):
            self.db.set("EternalOnline", "status", False)

    async def onlinecmd(self, message):
        """Управление онлайном.
        Пример: .online <задержка/сек>"""
        args = message.text.split()
        
        current_delay = self.db.get("EternalOnline", "delay")
        current_status = self.db.get("EternalOnline", "status")
        
        if len(args) > 1 and args[1].isdigit():
            new_delay = int(args[1])
            self.db.set("EternalOnline", "delay", new_delay)
            current_delay = new_delay

        if not current_status:
            self.db.set("EternalOnline", "status", True)
            await message.edit(self.strings['enabled'].format(current_delay))

            while self.db.get("EternalOnline", "status"):
                await message.client(UpdateStatusRequest(offline=False))
                await sleep(self.db.get("EternalOnline", "delay"))
        else:
            self.db.set("EternalOnline", "status", False)
            await message.edit(self.strings['disabled'])

    async def checkonlinecmd(self, message):
        """Текущий статус"""
        status = self.db.get("EternalOnline", "status")
        delay = self.db.get("EternalOnline", "delay")
        
        if status:
            await message.edit(self.strings['enabled'].format(delay))
        else:
            await message.edit(self.strings['disabled'])