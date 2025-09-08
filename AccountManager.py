# meta developer: @MartyyyK

from telethon import functions, types
from telethon.tl.functions.users import GetFullUserRequest
import logging
from .. import loader, utils

logging.basicConfig(level=logging.INFO)

@loader.tds
class AccountManager(loader.Module):
    """Менеджер Telegram аккаунта"""

    strings = {
        "name": "AccountManager",
        "error": "<emoji document_id=5237814653010076467>❌</emoji> не удалось совершить какие-либо ваши действия",
        "bio_success": "<emoji document_id=5229132514060167056>✅</emoji> <b>Био успешно обновлено!</b>\n<b><emoji document_id=5237814653010076467>❌</emoji> новое био:</b> <code>{}</code>",
        "name_success": "<emoji document_id=5233429444156223307>🔄</emoji> <b>имя успешно изменено!</b>\n<b><emoji document_id=5237814653010076467>❌</emoji> новое имя:</b> <code>{}</code>",
        "user_success": "<emoji document_id=5235875883297824772>👤</emoji> <b>Юзернейм изменен!</b>\n<b><emoji document_id=5237814653010076467>❌</emoji> новый юзернейм:</b> @{}",
        "user_removed": "<emoji document_id=5235875883297824772>👤</emoji> <b>Юзернейм удален!</b>",
        "user_taken": "<emoji document_id=5237814653010076467>❌</emoji> <b>Юзернейм @{} уже занят!</b>",
        "avatar_success": "<emoji document_id=5228764435362900200>🖼️</emoji> <b>ваша аватарка обновлена!</b>",
        "avatar_error": "<emoji document_id=5237814653010076467>❌</emoji> <b>отсутствует фото сообщения!</b>",
        "privacy_settings": "<emoji document_id=5237814653010076467>❌</emoji> <b>настройки конфиденциальности:</b>\n\n{}",
        "arg_missing": "<emoji document_id=5237814653010076467>❌</emoji> <b>укажите аргументы!</b>",
        "check_true": "<emoji document_id=5229132514060167056>✅</emoji> <b>Юзернейм:</b> @{} <b>(доступен!)</b>",
        "check_false": "<emoji document_id=5235875883297824772>👤</emoji> <b>Юзернейм:</b> @{} <b>(не доступен!)</b>",
        "check_false_args": "<emoji document_id=5237814653010076467>❌</emoji> <b>пожалуйста впишите юзернейм который вы хотите проверить</b>",
        "full_profile_info": "<emoji document_id=5237814653010076467>❌</emoji> Полная информация о профиле:",
        "id": "<emoji document_id=5228764435362900200>🖼️</emoji> Идентификатор: {}",
        "first_name": "<emoji document_id=5237814653010076467>❌</emoji> Имя: {}",
        "username": "<emoji document_id=5231112502573555738>👤</emoji> Юзернейм: @{}",
        "bio": "<emoji document_id=5233261334841289002>📝</emoji> Описание профиля: {}",
        "is_bot": "<emoji document_id=5231188729653127746>🤖</emoji> Бот-Аккаунт: {}",
        "verified": "<emoji document_id=5229132514060167056>✅</emoji> Верифицированный Аккаунт: {}",
        "restricted": "<emoji document_id=5235875883297824772>👤</emoji> Ограничение на аккаунте: {}",
        "privacy_everybody": "<emoji document_id=5235875883297824772>👤</emoji> Все",
        "privacy_contacts": "<emoji document_id=5233429444156223307>🔄</emoji> Контакты",
        "privacy_nobody": "<emoji document_id=5237814653010076467>❌</emoji> Никто"
    }

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    @loader.command()
    async def setbio(self, message):
        """<описание> - изменить био"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["arg_missing"])
            return

        try:
            await self._client(functions.account.UpdateProfileRequest(about=args))
            await utils.answer(message, self.strings["bio_success"].format(args))
        except Exception:
            await utils.answer(message, self.strings["error"])

    @loader.command()
    async def setname(self, message):
        """<имя> - изменить имя"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["arg_missing"])
            return

        try:
            await self._client(functions.account.UpdateProfileRequest(first_name=args))
            await utils.answer(message, self.strings["name_success"].format(args))
        except Exception:
            await utils.answer(message, self.strings["error"])

    @loader.command()
    async def setuser(self, message):
        """<юзернейм> - изменить юзернейм"""
        args = utils.get_args_raw(message)

        try:
            await self._client(functions.account.UpdateUsernameRequest(username=args or ""))
            if args:
                await utils.answer(message, self.strings["user_success"].format(args))
            else:
                await utils.answer(message, self.strings["user_removed"])
        except Exception as e:
            if "USERNAME_OCCUPIED" in str(e):
                await utils.answer(message, self.strings["user_taken"].format(args))
            else:
                await utils.answer(message, self.strings["error"])

    @loader.command()
    async def setavatar(self, message):
        """<реплай на фото> - установить новый аватар"""
        reply = await message.get_reply_message()
        if not reply or not reply.photo:
            await utils.answer(message, self.strings["avatar_error"])
            return

        try:
            file = await reply.download_media(bytes)
            await self._client(functions.photos.UploadProfilePhotoRequest(
                file=await self._client.upload_file(file)))
            await utils.answer(message, self.strings["avatar_success"])
        except Exception:
            await utils.answer(message, self.strings["error"])

    @loader.command()
    async def checkuser(self, message):
        """<юзернейм> - проверить доступность имени пользователя"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings["check_false_args"])
            return

        username = args.strip()

        result = await self.check_username_availability(username)

        if result:
            await utils.answer(message, self.strings["check_false"].format(username))
        else:
            await utils.answer(message, self.strings["check_true"].format(username))

    async def check_username_availability(self, username: str) -> bool:
        try:
            request = functions.account.CheckUsernameRequest(username=username)
            result = await self._client(request)
            return result
        except Exception as e:
            logging.exception(f"Ошибка при проверке юзернейма {username}: {e}")
            return False

    @loader.command()
    async def profile(self, message):
        """- отображает информацию о профиле"""
        args = utils.get_args_raw(message)
        user_id = None
        if args:
            try:
                user_id = int(args)
            except ValueError:
                await utils.answer(message, "⚠ ID пользователя должен быть числом.")
                return
        else:
            user_id = message.sender_id
            full_user = await self._client(GetFullUserRequest(id=types.InputUser(user_id=user_id, access_hash=0)))

            user = full_user.users[0]
            profile = full_user.full_user

            text = self.strings["full_profile_info"] + "\n\n"
            text += self.strings["id"].format(user.id) + "\n"
            text += self.strings["first_name"].format(user.first_name) + "\n"
            text += self.strings["username"].format(user.username or "Отсутствует") + "\n"
            text += self.strings["bio"].format(profile.about or "Отсутствует") + "\n"
            text += self.strings["is_bot"].format(user.bot or "Нет") + "\n"
            text += self.strings["verified"].format(user.verified or "Нет") + "\n"
            text += self.strings["restricted"].format(user.restricted or "Нет") + "\n"

            await utils.answer(message, text)

    @loader.command()
    async def getprivacy(self, message):
        """- показать текущие настройки конфиденциальности"""
        last_seen = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyStatusTimestamp()
        ))
        phone = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyPhoneNumber()
        ))
        profile_photo = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyProfilePhoto()
        ))
        forwards = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyForwards()
        ))
        groups = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyChatInvite()
        ))
        call = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyPhoneCall()
        ))
        voice = await self._client(functions.account.GetPrivacyRequest(
            key=types.InputPrivacyKeyVoiceMessages()
        ))
        time_account_ttl = await self._client(functions.account.GetAccountTTLRequest(
        ))

        global_settings = await self._client(functions.account.GetGlobalPrivacySettingsRequest())

        privacy_info = (
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>время последнего посещения:</b> {self._format_privacy(last_seen.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>номер телефона:</b> {self._format_privacy(phone.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>фото профиля:</b> {self._format_privacy(profile_photo.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>пересылки сообщений:</b> {self._format_privacy(forwards.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>приглашения в группы:</b> {self._format_privacy(groups.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>кружки/голосовые:</b> {self._format_privacy(voice.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>звонки:</b> {self._format_privacy(call.rules)}",
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>установленная дата удаления аккаунта:</b> {time_account_ttl.days} Дней\n"
            f"<emoji document_id=5231112502573555738>👤</emoji> <b>архив и новые чаты:</b> {'<emoji document_id=5237814653010076467>❌</emoji> Скрыто' if global_settings.archive_and_mute_new_noncontact_peers else '<emoji document_id=5229132514060167056>✅</emoji> Не скрыто'}"
        )

        await utils.answer(
            message,
            self.strings["privacy_settings"].format("\n".join(privacy_info))
            )    

    def _format_privacy(self, rules):
        if any(isinstance(rule, types.PrivacyValueAllowAll) for rule in rules):
            return "<emoji document_id=5235875883297824772>👤</emoji> Все"
        elif any(isinstance(rule, types.PrivacyValueAllowContacts) for rule in rules):
            return "<emoji document_id=5233429444156223307>🔄</emoji> Контакты"
        elif any(isinstance(rule, types.PrivacyValueDisallowContacts) for rule in rules):
            return "<emoji document_id=5229132514060167056>✅</emoji> Близкие друзья"
        else:
            return "<emoji document_id=5237814653010076467>❌</emoji> Никто"