# meta developer: @MartyyyK

from telethon import events, types
from .. import loader, utils

@loader.tds
class AutoReactMod(loader.Module):
    """Автореакции на сообщения"""
    strings = {
        "name": "AutoReact",
        "enabled": "✅ Автореакции включены в текущем чате",
        "disabled": "🚫 Автореакции выключены в текущем чате",
        "reaction_set": "✅ Установлена реакция: {}",
        "no_reaction": "⚠️ Укажите эмодзи или его ID для реакции",
        "premium_set": "✅ Установлена Premium реакция по ID: {}",
        "all_pm_enabled": "✅ Автореакции включены во всех личных чатах",
        "all_pm_disabled": "🚫 Автореакции выключены во всех личных чатах"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "current_reaction",
            "👍",
            "Текущая реакция (эмодзи или ID)",
            
            "is_premium",
            False,
            "Является ли реакция Premium эмодзи"
        )

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.active_chats = self.get("active_chats", {})
        self.all_pm = self.get("all_pm", False)

    def get_active_chats(self):
        return self.active_chats

    def save_active_chats(self):
        self.set("active_chats", self.active_chats)
        self.set("all_pm", self.all_pm)

    @loader.command(ru_doc="- вкл/выкл в текущем чате")
    async def artoggle(self, message):
        chat_id = str(message.chat_id)

        if self.all_pm:
            self.all_pm = False
            await utils.answer(message, self.strings["all_pm_disabled"])
        
        if chat_id in self.active_chats:
            del self.active_chats[chat_id]
            status = False
        else:
            self.active_chats[chat_id] = True
            status = True
            
        self.save_active_chats()
        
        await utils.answer(
            message,
            self.strings["enabled"] if status else self.strings["disabled"]
        )

    @loader.command(ru_doc="- вкл/выкл во всех ЛС")
    async def arallpm(self, message):
        """- toggle auto-reactions in all private messages"""
        self.all_pm = not self.all_pm

        if self.all_pm:
            self.active_chats.clear()

        self.save_active_chats()

        await utils.answer(
            message,
            self.strings["all_pm_enabled"] if self.all_pm else self.strings["all_pm_disabled"]
        )

    @loader.command(ru_doc="<эмодзи или ID> - установить реакцию")
    async def setr(self, message):
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_reaction"])
            return

        is_premium = args.isdigit()

        self.config["current_reaction"] = args
        self.config["is_premium"] = is_premium

        await utils.answer(
            message,
            self.strings["premium_set"].format(args) if is_premium else self.strings["reaction_set"].format(args)
        )

    @loader.watcher()
    async def watcher(self, message):
        if not isinstance(message, types.Message):
            return

        chat_id = str(message.chat_id)

        is_private = isinstance(message.peer_id, types.PeerUser)

        should_react = (
            (self.all_pm and is_private) or
            (chat_id in self.active_chats)
        )

        if not should_react:
            return

        try:
            if self.config["is_premium"]:
                await message.react(types.ReactionCustomEmoji(document_id=int(self.config["current_reaction"])))
            else:
                await message.react(self.config["current_reaction"])
        except Exception as e:
            return