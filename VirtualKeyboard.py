# meta developer: @MartyyyK

from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class VirtualKeyboardMod(loader.Module):
    """Виртуальная клавиатура"""
    strings = {
        "name": "VirtualKeyboard",
        "keyboard_title": "Виртуальная клавиатура",
        "message_placeholder": "Введите текст...",
        "help_text": (
            "Пишем <code>.security</code> и включаем everyone (inline)\n"
            "Дальше пишем <code>.security keyb</code> и тоже ставим everyone (inline)\n"
            "Готово, теперь другие могут печатать за тебя"
        )
    }

    def __init__(self):
        self.current_text = {}
        self.current_layout = {}
        self.caps_lock = {}

    @loader.command(ru_doc="Показать виртуальную клавиатуру")
    async def keyb(self, message: Message):
        chat_id = str(message.chat_id)
        if chat_id not in self.current_text:
            self.current_text[chat_id] = ""
            self.current_layout[chat_id] = "ru"
            self.caps_lock[chat_id] = False

        await self.inline.form(
            text=self.strings["message_placeholder"],
            message=message,
            reply_markup=self.generate_keyboard(chat_id),
        )

    @loader.command(ru_doc="Показать помощь")
    async def keybhelp(self, message: Message):
        await utils.answer(message, self.strings["help_text"])

    def generate_keyboard(self, chat_id: str):
        layout = self.current_layout[chat_id]
        caps = self.caps_lock[chat_id]

        layouts = {
            "ru": [
                ['й', 'ц', 'у', 'к', 'е', 'ё', 'н', 'г'],
                ['ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы'],
                ['в', 'а', 'п', 'р', 'о', 'л', 'д'],
                ['ж', 'э', 'я', 'ч', 'с', 'м', 'и'],
                ['т', 'ь', 'б', 'ю']
            ],
            "en": [
                ['q', 'w', 'e', 'r', 't', 'y', 'u'],
                ['i', 'o', 'p', 'a', 's', 'd', 'f'],
                ['g', 'h', 'j', 'k', 'l', 'z', 'x'],
                ['c', 'v', 'b', 'n', 'm', ',', '.'],
                ['?', '!', '-', "'"]
            ],
            "symbols": [
                ['1', '2', '3', '4', '5', '6', '7'],
                ['8', '9', '0', '@', '#', '$', '%'],
                ['&', '*', '(', ')', '-', '_', '='],
                ['+', '[', ']', '{', '}', ';', ':'],
                ['"', "'", '<', '>', ',', '.', '?'],
                ['/', '\\', '|', '~', '`', '^', '¡']
            ]
        }

        rows = []
        letters = layouts[layout]

        for row in letters:
            btn_row = [
                {
                    "text": letter.upper() if caps and layout != "symbols" else letter,
                    "callback": self.add_letter,
                    "args": (letter.upper() if caps and layout != "symbols" else letter, chat_id),
                } for letter in row
            ]
            rows.append(btn_row)

        bottom_row = [
            {
                "text": "⌫",
                "callback": self.delete_last_char,
                "args": (chat_id,),
            },
            {
                "text": "Пробел" if layout == "ru" else "Space",
                "callback": self.add_space,
                "args": (chat_id,),
            },
            {
                "text": "Caps" if not self.caps_lock[chat_id] else "CAPS",
                "callback": self.toggle_caps,
                "args": (chat_id,),
            },
            {
                "text": "EN" if layout == "ru" else "RU" if layout == "en" else "ABC",
                "callback": self.switch_layout,
                "args": (chat_id,),
            },
            {
                "text": "!@#" if layout != "symbols" else "ABC",
                "callback": self.toggle_symbols,
                "args": (chat_id,),
            },
            {
                "text": "Отправить ✅" if layout == "ru" else "Send ✅",
                "callback": self.send_message,
                "args": (chat_id,),
            },
        ]
        rows.append(bottom_row)
        return rows

    async def add_letter(self, call, letter: str, chat_id: str):
        self.current_text[chat_id] += letter
        await call.edit(
            text=self.current_text[chat_id] or self.strings["message_placeholder"],
            reply_markup=self.generate_keyboard(chat_id),
        )

    async def add_space(self, call, chat_id: str):
        self.current_text[chat_id] += " "
        await call.edit(
            text=self.current_text[chat_id] or self.strings["message_placeholder"],
            reply_markup=self.generate_keyboard(chat_id),
        )

    async def delete_last_char(self, call, chat_id: str):
        if self.current_text[chat_id]:
            self.current_text[chat_id] = self.current_text[chat_id][:-1]
        await call.edit(
            text=self.current_text[chat_id] or self.strings["message_placeholder"],
            reply_markup=self.generate_keyboard(chat_id),
        )

    async def toggle_caps(self, call, chat_id: str):
        self.caps_lock[chat_id] = not self.caps_lock[chat_id]
        await call.edit(
            text=self.current_text[chat_id] or self.strings["message_placeholder"],
            reply_markup=self.generate_keyboard(chat_id),
        )

    async def switch_layout(self, call, chat_id: str):
        if self.current_layout[chat_id] == "ru":
            self.current_layout[chat_id] = "en"
        else:
            self.current_layout[chat_id] = "ru"
        await call.edit(
            text=self.current_text[chat_id] or self.strings["message_placeholder"],
            reply_markup=self.generate_keyboard(chat_id),
        )

    async def toggle_symbols(self, call, chat_id: str):
        if self.current_layout[chat_id] == "symbols":
            self.current_layout[chat_id] = "ru"
        else:
            self.current_layout[chat_id] = "symbols"
        await call.edit(
            text=self.current_text[chat_id] or self.strings["message_placeholder"],
            reply_markup=self.generate_keyboard(chat_id),
        )

    async def send_message(self, call, chat_id: str):
        text = self.current_text.get(chat_id, "")
        if text:
            await self._client.send_message(int(chat_id), text)
            del self.current_text[chat_id]
            del self.current_layout[chat_id]
            del self.caps_lock[chat_id]
            await call.delete()
        else:
            await call.answer("Сообщение пустое!", show_alert=True)