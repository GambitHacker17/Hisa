# meta developer: @MartyyyK

from .. import loader, utils
from datetime import timedelta

@loader.tds
class BanWordMod(loader.Module):
    """Управление запрещёнными словами в чате"""

    strings = {
        "name": "BanWord",
        "word_added": "<b><emoji document_id=5873153278023307367>📄</emoji> Запрещённое слово добавлено:</b> <code>{}</code>",
        "word_removed": "<b><emoji document_id=5445267414562389170>🗑</emoji> Запрещённое слово удалено:</b> <code>{}</code>",
        "none_bw": "<b><emoji document_id=5287613115180006030>🤬</emoji> Список запрещённых слов пуст</b>",
        "bword_enabled": "<b><emoji document_id=5398001711786762757>✅</emoji> Банворды включены в этом чате</b>",
        "bword_disabled": "<b><emoji document_id=5388785832956016892>❌</emoji> Банворды выключены в этом чате</b>",
        "action_set": "<b><emoji document_id=5255999175174137421>🛡</emoji> Действие установлено:</b> <code>{}</code>",
        "no_action": "<b><emoji document_id=5980953710157632545>❌</emoji> Действие не указано. Используйте: <kick> <mute> <delete></b>",
        "no_word": "<b><emoji document_id=5443038326535759644>💬</emoji> Слово не указано</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "BAN_ACTION",
                "delete",
                lambda: "действие при нахождении запрещённого слова <kick>, <mute>, <delete>",
            ),
        )

    async def watcher(self, message):
        chat_id = utils.get_chat_id(message)
        enabled_chats = self.db.get("BanWord", "enabled_chats", [])
        if str(chat_id) not in enabled_chats:
            return

        banned_words = self.db.get("BanWord", "banned_words", [])
        if any(word in message.text for word in banned_words):
            action = self.config["BAN_ACTION"]
            if action == "delete":
                await message.delete()
            elif action == "kick":
                entity = await message.client.get_input_entity(chat_id)
                await message.client.kick_participant(entity, message.sender_id)
                await message.respond(f"<b><emoji document_id=5442879640379076105>👤</emoji> | User tg://user?id={message.sender.id} used a banned word and was kicked. <emoji document_id=5253780051471642059>🛡</emoji></b>")
            elif action == "mute":
                mute_duration = timedelta(hours=1)
                until_date = message.date + mute_duration
                entity = await message.client.get_input_entity(chat_id)
                await message.client.edit_permissions(
                    entity, 
                    message.sender_id, 
                    until_date=until_date, 
                    send_messages=False
                )
                await message.respond(f"<b><emoji document_id=5442879640379076105>👤</emoji> | User tg://user?id={message.sender.id} used a banned word and was muted for 1 hour. <emoji document_id=5253780051471642059>🛡</emoji></b>")

    @loader.command()
    async def bwadd(self, message):
        """- добавить запрещённое слово"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_word"])
            return
        banned_words = self.db.get("BanWord", "banned_words", [])
        if args not in banned_words:
            banned_words.append(args)
            self.db.set("BanWord", "banned_words", banned_words)
            await utils.answer(message, self.strings["word_added"].format(args))
    
    @loader.command()
    async def bwdel(self, message):
        """- удалить запрещённое слово"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_word"])
            return
        banned_words = self.db.get("BanWord", "banned_words", [])
        if args in banned_words:
            banned_words.remove(args)
            self.db.set("BanWord", "banned_words", banned_words)
            await utils.answer(message, self.strings["word_removed"].format(args))

    @loader.command()
    async def bwon(self, message):
        """- включает банворды в чате"""
        chat_id = str(utils.get_chat_id(message))
        enabled_chats = self.db.get("BanWord", "enabled_chats", [])
        if chat_id not in enabled_chats:
            enabled_chats.append(chat_id)
            self.db.set("BanWord", "enabled_chats", enabled_chats)
            await utils.answer(message, self.strings["bword_enabled"])

    @loader.command()
    async def bwoff(self, message):
        """- отключает банворды в чате."""
        chat_id = str(utils.get_chat_id(message))
        enabled_chats = self.db.get("BanWord", "enabled_chats", [])
        if chat_id in enabled_chats:
            enabled_chats.remove(chat_id)
            self.db.set("BanWord", "enabled_chats", enabled_chats)
            await utils.answer(message, self.strings["bword_disabled"])

    @loader.command()
    async def bword(self, message):
        """- действие при нахождении запрещённого слова <kick>, <mute>, <delete>"""
        args = utils.get_args_raw(message)
        if args not in ["kick", "mute", "delete"]:
            await utils.answer(message, self.strings["no_action"])
            return
        self.config["BAN_ACTION"] = args
        await utils.answer(message, self.strings["action_set"].format(args))

    @loader.command()
    async def bwlist(self, message):
        """- выводит список запрещённых слов"""
        banned_words = self.db.get("BanWord", "banned_words", [])
        if not banned_words:
            await utils.answer(message, self.strings["none_bw"])
            return

        word_list = "\n".join(f"• {word}" for word in banned_words)
        await utils.answer(message, f"<b><emoji document_id=5870984130560266604>💬</emoji> Banned Words:</b>\n<i>{word_list}</i>")
