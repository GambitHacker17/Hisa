# meta developer: @MartyyyK

from hisatl.types import Message
from .. import loader, utils

@loader.tds
class InlineButtons(loader.Module):
    """Модуль для создания inline кнопок"""

    strings = {"name": "InlineButtons"}
    strings_ru = {"_cls_doc": "Модуль для создания inline кнопок"}

    async def parse_buttons(self, buttons_str: str) -> list:
        buttons = []
        for btn in buttons_str.split("|"):
            if ":" not in btn:
                continue
            text, url = btn.split(":", 1)
            buttons.append({"text": text.strip(), "url": url.strip()})
        return buttons

    @loader.command(
        ru_doc="помощь по командам",
    )
    async def cinlinehelp(self, message: Message):
        """help for commands"""
        help_text = """<b>Help for InlineButtons module:</b>

<code>cinline</code> <текст кнопки>, <ссылка кнопки>, <текст сообщения> - Создать сообщение с одной inline кнопкой\n
<code>cinlinemulti</code> <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения> - Создать сообщение с несколькими inline кнопками\n
<code>cinlinephoto</code> <ссылка на изображение>, <текст кнопки>, <ссылка кнопки>, <текст сообщения> - Сообщение с изображением и одной кнопкой\n
<code>cinlinephotomulti</code> <ссылка на изображение>, <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения> - Сообщение с изображением и несколькими кнопками\n
<code>cinlinevideo</code> <ссылка на видео>, <текст кнопки>, <ссылка кнопки>, <текст сообщения> - Сообщение с видео и одной кнопкой\n
<code>cinlinevideomulti</code> <ссылка на видео>, <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения> - Сообщение с видео и несколькими кнопками\n
<code>cinlinegif</code> <ссылка на GIF>, <текст кнопки>, <ссылка кнопки>, <текст сообщения> - Сообщение с GIF и одной кнопкой\n
<code>cinlinegifmulti</code> <ссылка на GIF>, <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения> - Сообщение с GIF и несколькими кнопками\n
<code>cinlinehelp</code> - Показать эту справку"""
        
        await utils.answer(message, help_text)

    async def check_args(self, message: Message, expected: int, command: str):
        args = utils.get_args_raw(message)
        if not args or len(args.split(", ", maxsplit=expected-1)) < expected:
            help_text = f"<b>Ошибка:</b> Недостаточно аргументов для команды {command}\n" \
                       f"Используйте <code>{command}help</code> для справки"
            await utils.answer(message, help_text)
            return False
        return True

    @loader.command(
        ru_doc="<текст кнопки>, <ссылка кнопки>, <текст сообщения>",
    )
    async def cinline(self, message: Message):
        """<button text>, <button link>, <message text>"""
        if not await self.check_args(message, 3, "cinline"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=2)
        btn_text, btn_link, text = args

        await self.inline.form(
            text=text,
            message=message,
            reply_markup=[[{"text": btn_text, "url": btn_link}]]
        )

    @loader.command(
        ru_doc="<текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения>",
    )
    async def cinlinemulti(self, message: Message):
        """<text1:link1|text2:link2|...>, <message text>"""
        if not await self.check_args(message, 2, "cinlinemulti"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=1)
        buttons_str, text = args
        buttons = await self.parse_buttons(buttons_str)

        await self.inline.form(
            text=text,
            message=message,
            reply_markup=[buttons]
        )

    @loader.command(
        ru_doc="<ссылка на изображение>, <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения>",
    )
    async def cinlinephotomulti(self, message: Message):
        """<image link>, <text1:link1|text2:link2>, <message text>"""
        if not await self.check_args(message, 3, "cinlinephotomulti"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=2)
        image_link, buttons_str, text = args
        buttons = await self.parse_buttons(buttons_str)

        await self.inline.form(
            text=text,
            message=message,
            photo=image_link,
            mime_type="photo/jpeg" if image_link.endswith('.jpg') else "photo/png",
            reply_markup=[buttons]
        )

    @loader.command(
        ru_doc="<ссылка на видео>, <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения>",
    )
    async def cinlinevideomulti(self, message: Message):
        """<video link>, <text1:link1|text2:link2>, <message text>"""
        if not await self.check_args(message, 3, "cinlinevideomulti"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=2)
        video_link, buttons_str, text = args
        buttons = await self.parse_buttons(buttons_str)

        await self.inline.form(
            text=text,
            message=message,
            video=video_link,
            mime_type="video/mp4",
            reply_markup=[buttons]
        )

    @loader.command(
        ru_doc="<ссылка на GIF>, <текст1:ссылка1|текст2:ссылка2|...>, <текст сообщения>",
    )
    async def cinlinegifmulti(self, message: Message):
        """<gif link>, <text1:link1|text2:link2>, <message text>"""
        if not await self.check_args(message, 3, "cinlinegifmulti"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=2)
        gif_link, buttons_str, text = args
        buttons = await self.parse_buttons(buttons_str)

        await self.inline.form(
            text=text,
            message=message,
            gif=gif_link,
            mime_type="video/mp4",
            reply_markup=[buttons]
        )

    @loader.command(
        ru_doc="<ссылка на изображение>, <текст кнопки>, <ссылка кнопки>, <текст сообщения>",
    )
    async def cinlinephoto(self, message: Message):
        """<image link>, <button text>, <button link>, <message text>"""
        if not await self.check_args(message, 4, "cinlinephoto"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=3)
        image_link, btn_text, btn_link, text = args

        await self.inline.form(
            text=text,
            message=message,
            photo=image_link,
            mime_type="photo/jpeg" if args[0].endswith('.jpg') else "photo/png",
            reply_markup=[[{"text": btn_text, "url": btn_link}]]
        )

    @loader.command(
        ru_doc="<ссылка на видео>, <текст кнопки>, <ссылка кнопки>, <текст сообщения>",
    )
    async def cinlinevideo(self, message: Message):
        """<video link>, <button text>, <button link>, <message text>"""
        if not await self.check_args(message, 4, "cinlinevideo"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=3)
        video_link, btn_text, btn_link, text = args

        await self.inline.form(
            text=text,
            message=message,
            video=video_link,
            mime_type="video/mp4",
            reply_markup=[[{"text": btn_text, "url": btn_link}]]
        )

    @loader.command(
        ru_doc="<ссылка на GIF>, <текст кнопки>, <ссылка кнопки>, <текст сообщения>",
    )
    async def cinlinegif(self, message: Message):
        """<gif link>, <button text>, <button link>, <message text>"""
        if not await self.check_args(message, 4, "cinlinegif"):
            return
            
        args = utils.get_args_raw(message).split(", ", maxsplit=3)
        gif_link, btn_text, btn_link, text = args

        await self.inline.form(
            text=text,
            message=message,
            gif=gif_link,
            mime_type="video/mp4",
            reply_markup=[[{"text": btn_text, "url": btn_link}]]
        )