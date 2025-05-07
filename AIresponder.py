# meta developer: @MartyyyK

import json
import aiohttp
from .. import loader, utils
from telethon import events
import base64

@loader.tds
class AutoResponderMod(loader.Module):
    """Автоответчик с ИИ"""
    strings = {"name": "AIresponder"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            "ENABLED", False, "Включен ли автоответчик",
            "PROMPT", "Ты - полезный ассистент. Отвечай вежливо и информативно.", "Промт для ИИ",
            "SHOW_PREFIX", True, "Показывать префикс 'Ответ автоответчика'",
            "MAX_HISTORY", 500, "Максимальная длина истории диалога"
        )
        self.history = {}
        self.blacklist = set()

    async def client_ready(self, client, db):
        self.client = client
        self._db = db
        self.history = self._db.get(__name__, "history", {})
        self.blacklist = set(self._db.get(__name__, "blacklist", []))

    def save_data(self):
        self._db.set(__name__, "history", self.history)
        self._db.set(__name__, "blacklist", list(self.blacklist))

    async def airespondcmd(self, message):
        """Включить/выключить автоответчик"""
        self.config["ENABLED"] = not self.config["ENABLED"]
        status = "включен" if self.config["ENABLED"] else "выключен"
        await message.edit(f"<b>Автоответчик {status}</b>")

    async def ailistcmd(self, message):
        """Показать список пользователей в белом списке"""
        users_info = []
        for user_id in self.blacklist:
            try:
                user = await self.client.get_entity(user_id)
                name = getattr(user, 'first_name', '') or getattr(user, 'title', '') or str(user_id)
                users_info.append(f"{name}")
            except:
                users_info.append(f"ID: {user_id}")

        users_list = "\n".join(users_info) if users_info else "Список пуст"
        await message.edit(
            f"<b>Белый список автоответчика ({len(self.blacklist)}):</b>\n"
            f"{users_list}"
        )

    async def aipromptcmd(self, message):
        """Установить промт для автоответчика"""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit(f"<b>Текущий промт:</b>\n{self.config['PROMPT']}")
            return
        self.config["PROMPT"] = args
        await message.edit("<b>Промт обновлен</b>")

    async def aiprefixcmd(self, message):
        """Включить/выключить префикс 'Ответ автоответчика'"""
        self.config["SHOW_PREFIX"] = not self.config["SHOW_PREFIX"]
        status = "включен" if self.config["SHOW_PREFIX"] else "выключен"
        await message.edit(f"<b>Префикс 'Ответ автоответчика' {status}</b>")

    async def aihistorycmd(self, message):
        """Очистить историю диалогов (all или ID)"""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit("<b>Укажите all или chat_id для очистки истории</b>")
            return

        if args.lower() == "all":
            self.history = {}
            self.save_data()
            await message.edit("<b>Вся история диалогов очищена</b>")
        else:
            try:
                chat_id = int(args)
                if chat_id in self.history:
                    del self.history[chat_id]
                    self.save_data()
                    await message.edit(f"<b>История для чата {chat_id} очищена</b>")
                else:
                    await message.edit("<b>История для этого чата не найдена</b>")
            except ValueError:
                await message.edit("<b>Некорректный chat_id</b>")

    async def aiwhitelistcmd(self, message):
        """Добавить/удалить пользователя из белого списка <reply>"""
        target_id = None

        reply = await message.get_reply_message()
        if reply:
            target_id = reply.sender_id
        elif message.is_private:
            target_id = message.chat_id

        if not target_id:
            await message.edit("<b>Ответьте на сообщение пользователя или используйте в личном чате</b>")
            return

        if target_id in self.blacklist:
            self.blacklist.remove(target_id)
            action = "удален из белого списка"
        else:
            self.blacklist.add(target_id)
            action = "добавлен в белый список"

        self.save_data()
        await message.edit(f"<b>Пользователь {action}</b>")

    async def watcher(self, message):
        if not self.config["ENABLED"] or not message.is_private:
            return

        if message.sender_id == (await self.client.get_me()).id:
            return

        if message.sender_id in self.blacklist:
            return

        if not message.text:
            return

        await message.mark_read()

        chat_id = message.chat_id
        if chat_id not in self.history:
            self.history[chat_id] = []

        self.history[chat_id].append({"role": "user", "content": message.text})

        max_history = self.config["MAX_HISTORY"]
        if len(self.history[chat_id]) > max_history * 2:
            self.history[chat_id] = self.history[chat_id][-max_history * 2:]

        try:
            async with message.client.action(message.chat_id, "typing"):
                answer = await self.get_ai_response(chat_id)
                self.history[chat_id].append({"role": "assistant", "content": answer})
                self.save_data()
 
                if self.config["SHOW_PREFIX"]:
                    answer = f"<b>Ответ автоответчика:</b>\n{answer}"
                await message.reply(answer)
        except Exception as e:
            await message.reply(f"⚠️ Ошибка: {str(e)}")

    async def get_ai_response(self, chat_id):
        messages = [{"role": "system", "content": self.config["PROMPT"]}]

        if chat_id in self.history:
            messages.extend(self.history[chat_id])

        api_url = "http://109.172.94.236:5001/Zetta/v1/models"
        payload = {
            "model": "gpt-4o-mini",
            "request": {
                "messages": messages
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                answer = data.get("answer", "Не удалось получить ответ").strip()
                try:
                    decoded_bytes = base64.b64decode(answer)
                    return decoded_bytes.decode('utf-8')
                except:
                    return answer