__version__ = (1, 0, 0)
          
# meta developer: @MartyyyK
# scope: hisa_only
# scope: hisa_min 0.0.1

import asyncio
import logging
from telethon.tl.types import DocumentAttributeFilename
from .. import loader, utils

renamer_fire = "🔥 "
renamer_warn = "🚨 "
renamer_wait = "🕒 "
renamer_done = "✅ "

class ReanemerMod(loader.Module):
	"""Rename file name"""
	
	strings = {
	           "name": "Rename",
			   "renamer_no_reply": renamer_warn + "<b>Reply to file</b>",
			   "renamer_no_name": renamer_fire + "<b>You have not specified the name</b>",
			   "renamer_wait": renamer_wait + "<b>Please, wait...</b>",
			   "renamer_load": renamer_fire + "<b>Loading »»</b>",
			   "renamer_down": renamer_fire + "<b>Downloading »»</b>",
			   "renamer_done": renamer_done + "<b>Done</b>",
			   }
	
	strings_ru = {
			   "renamer_no_reply": renamer_warn + "<b>Ответьте на файл</b>",
			   "renamer_no_name": renamer_fire + "<b>Вы не указали название</b>",
			   "renamer_wait": renamer_wait + "<b>Пожалуйста, подождите...</b>",
			   "renamer_load": renamer_fire + "<b>Загрузка »»</b>",
			   "renamer_down": renamer_fire + "<b>Скачивание »»</b>",
			   "renamer_done": renamer_done + "<b>Готово</b>",
			   }
			   
	async def renamecmd(self, message):
		"""> rename [name.format]"""
        
		await message.edit(f"{self.strings('renamer_wait')}")
		reply = await message.get_reply_message()
		if not reply or not reply.file:
			await message.edit(self.strings["renamer_no_reply"])
			return
		name = utils.get_args_raw(message)
		if not name:
			await message.edit(self.strings["renamer_no_name"])
			return
		fn = reply.file.name
		if not fn:
			fn = ""
		fs = reply.file.size
		
		[await message.edit(f"<b>{self.strings('renamer_down')} {fn}</b>") if fs > 500000 else ...]
		file = await reply.download_media(bytes)
		[await message.edit(f"<b>{self.strings('renamer_load')}</b> <code>{name}</code>") if fs > 500000 else ...]
		await message.client.send_file(message.to_id, file, force_document=True, reply_to=reply, attributes=[DocumentAttributeFilename(file_name=name)], caption=f"{self.strings('renamer_done')} | <code>{name}</code>")
		await message.delete()