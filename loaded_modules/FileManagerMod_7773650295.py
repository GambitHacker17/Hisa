from pyrogram import types
import os
import mimetypes
from .. import loader, utils

@loader.tds
class FileManagerMod(loader.Module):
    """Продвинутый файловый менеджер с отправкой файлов"""
    strings = {
        "name": "FileManager+",
        "current_dir": "<b>📁 {}</b>",
        "dir_contents": "<i>Содержимое директории:</i>",
        "file_info": "<b>📄 {}</b>\n<blockquote>{}</blockquote>",
        "file_not_found": "❌ Файл не найден",
        "dir_not_found": "❌ Директория не найдена",
        "no_permission": "❌ Нет прав доступа",
        "file_deleted": "✅ Файл удален: {}",
        "dir_deleted": "✅ Директория удалена: {}",
        "file_edited": "✅ Файл изменен: {}",
        "enter_new_text": "✏️ Отправьте новый текст или файл для замены",
        "invalid_path": "❌ Неверный путь",
        "action_cancelled": "❌ Действие отменено",
        "closed": "🚪 Проводник закрыт",
        "back_btn": "◀ Назад",
        "edit_btn": "✏️ Редакт.",
        "delete_btn": "🗑 Удалить",
        "close_btn": "❌ Закрыть",
        "confirm_btn": "✅ Подтвердить",
        "cancel_btn": "❌ Отменить",
        "prev_page": "⬅ Пред.",
        "next_page": "След. ➡",
        "page_info": "Стр. {}/{}",
        "file_too_large": "⚠ Файл слишком большой ({} KB)",
        "send_file_btn": "📤 Отправить файл",
        "sending_file": "🔄 Отправляю файл...",
        "file_sent": "✅ Файл отправлен"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "start_dir",
                os.path.expanduser("~"),
                "Стартовая директория",
                validator=loader.validators.String()
            ),
            loader.ConfigValue(
                "max_display_size",
                512 * 1024,
                "Макс. размер для просмотра (байты)",
                validator=loader.validators.Integer(minimum=1024)
            ),
            loader.ConfigValue(
                "chunk_size",
                3900,
                "Размер части для больших файлов",
                validator=loader.validators.Integer(minimum=500, maximum=3900)
            ),
        )
        self.current_dir = self.config["start_dir"]
        self.edit_buffer = {}
        self._current_page = 0
        self._file_chunks = {}
        self._current_chunk = {}
        self._page_history = {}
        self._dir_history = {}

    async def client_ready(self, client, db):
        self._client = client

    def _get_dir_contents(self, path):
        try:
            items = os.listdir(path)
            dirs = [(item, "📁") for item in items if os.path.isdir(os.path.join(path, item))]
            files = [(item, "📄") for item in items if not os.path.isdir(os.path.join(path, item))]
            return sorted(dirs) + sorted(files)
        except Exception as e:
            print(f"Error getting dir contents: {e}")
            return None

    def _is_text_file(self, path):
        """Проверяет, является ли файл текстовым"""
        try:
            with open(path, 'rb') as f:
                chunk = f.read(1024)
                if b'\x00' in chunk:
                    return False
                try:
                    chunk.decode('utf-8')
                    return True
                except UnicodeDecodeError:
                    return False
        except Exception:
            return False

    def _get_file_type(self, path):
        """Определение типа файла"""
        try:
            file_size = os.path.getsize(path)
            if file_size == 0:
                return "🕳 Пустой файл"
            
            if self._is_text_file(path):
                return f"📄 Текстовый файл ({file_size//1024} KB)"
            
            mime_type = mimetypes.guess_type(path)[0] or "application/octet-stream"
            
            if mime_type.startswith("image/"):
                return f"🖼 Изображение ({file_size//1024} KB)"
            elif mime_type.startswith("audio/"):
                return f"🎵 Аудио ({file_size//1024} KB)"
            elif mime_type.startswith("video/"):
                return f"🎬 Видео ({file_size//1024} KB)"
            
            return f"📦 Файл ({file_size//1024} KB)"
        except Exception as e:
            print(f"Error determining file type: {e}")
            return "⚠ Неизвестный тип файла"

    def _split_content(self, content, path):
        """Разделение содержимого на части"""
        if not isinstance(content, str):
            content = str(content)
        chunks = [
            content[i:i+self.config["chunk_size"]]
            for i in range(0, len(content), self.config["chunk_size"])
        ]
        self._file_chunks[path] = chunks
        return chunks

    def generate_dir_markup(self, contents, page_num=0):
        """Генерация кнопок для директории"""
        if not contents:
            return None
            
        self._current_page = page_num
        items_per_page = 8
        num_pages = max(1, (len(contents) + items_per_page - 1) // items_per_page)
        page_items = contents[page_num*items_per_page : (page_num+1)*items_per_page]

        markup = []
        row = []
        for name, icon in page_items:
            if len(row) == 2:
                markup.append(row)
                row = []
            row.append({
                'text': f"{icon} {name[:15]}" + ("..." if len(name) > 15 else ""),
                'callback': self.item_action,
                'args': [name]
            })
        if row:
            markup.append(row)

        nav_buttons = []
        if page_num > 0:
            nav_buttons.append({
                'text': self.strings["prev_page"],
                'callback': self.change_page,
                'args': [page_num - 1]
            })
        
        nav_buttons.append({
            'text': self.strings["page_info"].format(page_num+1, num_pages),
            'callback': self.change_page,
            'args': [page_num]
        })
        
        if page_num < num_pages - 1:
            nav_buttons.append({
                'text': self.strings["next_page"],
                'callback': self.change_page,
                'args': [page_num + 1]
            })

        if nav_buttons:
            markup.append(nav_buttons)

        parent_dir = os.path.dirname(self.current_dir)
        if parent_dir != self.current_dir:
            markup.append([{
                'text': self.strings["back_btn"],
                'callback': self.navigate_dir,
                'args': [parent_dir]
            }])

        markup.append([{
            'text': self.strings["close_btn"],
            'callback': self.close_menu
        }])

        return markup

    def generate_file_markup(self, path, chunk_index=0, total_chunks=1):
        """Генерация кнопок для файла"""
        markup = []
        
        if total_chunks > 1:
            nav_buttons = []
            if chunk_index > 0:
                nav_buttons.append({
                    'text': self.strings["prev_page"],
                    'callback': self.show_file,
                    'args': [path, chunk_index-1]
                })
            
            nav_buttons.append({
                'text': self.strings["page_info"].format(chunk_index+1, total_chunks),
                'callback': self.show_file,
                'args': [path, chunk_index]
            })
            
            if chunk_index < total_chunks - 1:
                nav_buttons.append({
                    'text': self.strings["next_page"],
                    'callback': self.show_file,
                    'args': [path, chunk_index+1]
                })
            
            markup.append(nav_buttons)

        markup.append([{
            'text': self.strings["edit_btn"],
            'callback': self.edit_file,
            'args': [path]
        }, {
            'text': self.strings["delete_btn"],
            'callback': self.delete_file,
            'args': [path]
        }])

        markup.append([{
            'text': self.strings["send_file_btn"],
            'callback': self.send_file_to_chat,
            'args': [path]
        }])

        markup.append([{
            'text': self.strings["back_btn"],
            'callback': self.navigate_dir,
            'args': [os.path.dirname(path)]
        }, {
            'text': self.strings["close_btn"],
            'callback': self.close_menu
        }])

        return markup

    async def send_file_to_chat(self, call, path):
        """Отправка файла в чат"""
        await call.answer(self.strings["sending_file"])
        try:
            await self._client.send_document(
                chat_id=call.message.chat.id,
                document=path,
                reply_to_message_id=call.message.id
            )
            await call.answer(self.strings["file_sent"])
        except Exception as e:
            await call.answer(f"Ошибка отправки: {str(e)}")

    async def show_file(self, call, path, chunk_index=0):
        """Показать содержимое файла"""
        try:
            if not os.path.isfile(path):
                await call.answer(self.strings["file_not_found"])
                return

            file_type = self._get_file_type(path)
            file_size = os.path.getsize(path)
            
            if "Текстовый файл" in file_type:
                if file_size > self.config["max_display_size"]:
                    await call.edit(
                        self.strings["file_info"].format(path, self.strings["file_too_large"].format(file_size//1024)),
                        reply_markup=self.generate_file_markup(path)
                    )
                    return

                with open(path, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()

                chunks = self._split_content(content, path)
                total_chunks = len(chunks)
                chunk_index = min(chunk_index, total_chunks - 1)

                await call.edit(
                    self.strings["file_info"].format(path, utils.escape_html(chunks[chunk_index])),
                    reply_markup=self.generate_file_markup(path, chunk_index, total_chunks)
                )
            else:
                await call.edit(
                    self.strings["file_info"].format(path, f"{file_type}\n\nФайл нельзя отобразить, но можно отправить"),
                    reply_markup=self.generate_file_markup(path)
                )
        except Exception as e:
            print(f"Error showing file: {e}")
            await call.answer(f"Ошибка: {str(e)}")

    async def item_action(self, call, item_name):
        """Обработка выбора элемента"""
        path = os.path.join(self.current_dir, item_name)
        if os.path.isdir(path):
            self._dir_history[os.path.dirname(path)] = self._current_page
            await self.navigate_dir(call, path)
        else:
            await self.show_file(call, path)

    async def navigate_dir(self, call, path):
        """Навигация по директориям"""
        self.current_dir = path
        contents = self._get_dir_contents(path)
        if contents is None:
            await call.answer(self.strings["no_permission"])
            return

        page_num = self._dir_history.get(path, 0)
        await call.edit(
            f"{self.strings['current_dir'].format(path)}\n{self.strings['dir_contents']}",
            reply_markup=self.generate_dir_markup(contents, page_num)
        )

    async def edit_file(self, call, path):
        """Редактирование файла"""
        try:
            if os.path.getsize(path) > self.config["max_display_size"]:
                await call.answer("Файл слишком большой для редактирования")
                return

            with open(path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            
            self.edit_buffer[call.from_user.id] = {"path": path, "text": content}
            
            await call.edit(
                self.strings["file_info"].format(path, self.strings["enter_new_text"]),
                reply_markup=self.generate_confirm_markup(path, "edit")
            )
        except Exception as e:
            await call.answer(f"Ошибка: {str(e)}")

    async def delete_file(self, call, path):
        """Удаление файла"""
        await call.edit(
            self.strings["file_info"].format(path, "⚠ Вы уверены, что хотите удалить этот файл?"),
            reply_markup=self.generate_confirm_markup(path, "delete")
        )

    def generate_confirm_markup(self, path, action):
        """Кнопки подтверждения"""
        return [[
            {
                'text': self.strings["confirm_btn"],
                'callback': self.confirm_action,
                'args': [path, action]
            },
            {
                'text': self.strings["cancel_btn"],
                'callback': self.navigate_dir,
                'args': [os.path.dirname(path)]
            }
        ]]

    async def confirm_action(self, call, path, action):
        """Подтверждение действия"""
        if action == "delete":
            try:
                if os.path.isdir(path):
                    os.rmdir(path)
                    msg = self.strings["dir_deleted"].format(path)
                else:
                    os.remove(path)
                    msg = self.strings["file_deleted"].format(path)
                await self.navigate_dir(call, os.path.dirname(path))
                await call.answer(msg)
            except Exception as e:
                await call.answer(f"Ошибка: {str(e)}")
        elif action == "edit" and call.from_user.id in self.edit_buffer:
            edit_data = self.edit_buffer[call.from_user.id]
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(edit_data["text"])
                del self.edit_buffer[call.from_user.id]
                await self.show_file(call, path)
                await call.answer(self.strings["file_edited"].format(path))
            except Exception as e:
                await call.answer(f"Ошибка: {str(e)}")

    async def change_page(self, call, page_num):
        """Смена страницы"""
        contents = self._get_dir_contents(self.current_dir)
        if contents is None:
            await call.answer(self.strings["no_permission"])
            return

        self._dir_history[self.current_dir] = page_num
        await call.edit(
            f"{self.strings['current_dir'].format(self.current_dir)}\n{self.strings['dir_contents']}",
            reply_markup=self.generate_dir_markup(contents, page_num)
        )

    async def close_menu(self, call):
        """Закрытие меню"""
        await call.edit(self.strings["closed"], reply_markup=None)

    @loader.command(aliases=["fm"])
    async def filemanagercmd(self, message):
        """Открыть файловый менеджер"""
        args = utils.get_args_raw(message)
        path = args or self.config["start_dir"]
        
        try:
            path = os.path.abspath(os.path.expanduser(path))
            if not os.path.exists(path):
                await utils.answer(message, self.strings["dir_not_found"])
                return
            
            contents = self._get_dir_contents(path)
            if contents is None:
                await utils.answer(message, self.strings["no_permission"])
                return

            self.current_dir = path
            await utils.answer(
                message,
                f"{self.strings['current_dir'].format(path)}\n{self.strings['dir_contents']}",
                reply_markup=self.generate_dir_markup(contents)
            )
        except Exception as e:
            await utils.answer(message, f"Ошибка: {str(e)}")

    async def watcher(self, message):
        """Обработка новых сообщений"""
        if not isinstance(message, types.Message):
            return
            
        user_id = message.from_user.id
        if user_id not in self.edit_buffer:
            return

        edit_data = self.edit_buffer[user_id]
        path = edit_data["path"]
        
        try:
            if message.document:
                file = await message.download()
                os.replace(file, path)
                del self.edit_buffer[user_id]
                await message.delete()
                await self._client.send_message(
                    message.chat.id,
                    self.strings["file_edited"].format(path),
                    reply_to_message_id=message.id
                )
            elif message.text:
                edit_data["text"] = message.text
                await message.delete()
                await self._client.send_message(
                    message.chat.id,
                    self.strings["file_info"].format(path, "Новое содержимое:\n```" + message.text[:2000] + "```"),
                    reply_markup=self.generate_confirm_markup(path, "edit")
                )
        except Exception as e:
            await message.reply(f"Ошибка: {str(e)}")