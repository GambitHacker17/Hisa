# meta developer: @MartyyyK

import subprocess
try:
    import emoji
    from emoji import is_emoji
except:
    mod_inst = subprocess.Popen("pip install emoji==2.0.0", shell=True) 
    mod_inst.wait()
    import emoji
    from emoji import is_emoji
from .. import loader, utils
import string, pickle, re
from telethon.tl.types import Channel

conf_default = {
    '-s1': {
        '1': [False, '<b>жирный</b>', '<b>', '</b>'], 
        '2': [False, '<i>курсив</i>', '<i>', '</i>'], 
        '3': [False, '<u>подчеркнутый</u>', '<u>', '</u>'],
        '4': [False, '<s>зачёркнутый</s>', '<s>', '</s>'],
        '5': [False, '<tg-spoiler>скрытый</tg-spoiler>', '<tg-spoiler>', '</tg-spoiler>'],
    },
    '-s2': {
        '1': [True, '<b>жирный</b>', '<b>', '</b>'], 
        '2': [False, '<i>курсив</i>', '<i>', '</i>'], 
        '3': [False, '<u>подчеркнутый</u>', '<u>', '</u>'],
        '4': [False, '<s>зачёркнуто</s>', '<s>', '</s>'],
        '5': [False, '<tg-spoiler>скрытый</tg-spoiler>', '<tg-spoiler>', '</tg-spoiler>'],
    }, 
    '-s3': {
        '1': [False, '<b>жирный</b>', '<b>', '</b>'], 
        '2': [False, '<i>курсив</i>', '<i>', '</i>'], 
        '3': [False, '<u>подчеркнутый</u>', '<u>', '</u>'],
        '4': [False, '<s>зачёркнутый</s>', '<s>', '</s>'],
        '5': [False, '<tg-spoiler>скрытый</tg-spoiler>', '<tg-spoiler>', '</tg-spoiler>'],
    },
    '-sE': {
        '1': [True, '💬'], 
        '2': [False, '💭'], 
        '3': [False, '🗯'], 
        '4': [False, '✉️'],
        '5': [False, '🔊'],
        '6': [False, '🏳️‍🌈']
    }, 
    '-sS': {
        '1': [True, 'пробел', ' '], 
        '2': [False, 'разрыв строки', '\n'],
        '3': [False, 'точка + пробел', '. '],
        '4': [False, 'запятая + пробел', ', ']
    } 
}

@loader.tds
class RPMod(loader.Module):
    """Role Play module"""
    strings = {'name': 'RPMod'}

    async def client_ready(self, client, db):
        self.db = db
        if not self.db.get("RPMod", "exlist", False):
            self.db.set("RPMod", "exlist", [])
        if not self.db.get("RPMod", "status", False):
            self.db.set("RPMod", "status", 1)
        if not self.db.get("RPMod", "rprezjim", False):
            self.db.set("RPMod", "rprezjim", 1)
        if not self.db.get('RPMod', 'rpnicks', False):
            self.db.set('RPMod', 'rpnicks', {})
        if not self.db.get('RPMod', 'rpemoji', False):
            self.db.set('RPMod', 'rpemoji', {})
        if not self.db.get('RPMod', 'rpcomands', False):
            comands = {'чмок': 'чмокнул', 'кусь': 'кусьнул', 'поцеловать': 'поцеловал', 'шлепнуть': 'шлепнул', 'прижать': 'прижал', 'погладить': 'погладил', 'обнять': 'обнял'}
            self.db.set('RPMod', 'rpcomands', comands)
        if not self.db.get('RPMod', 'useraccept', False):
            self.db.set('RPMod', 'useraccept', {"chats": [], "users": []})
        elif type(self.db.get('RPMod', 'useraccept')) == type([]):
            self.db.set('RPMod', 'useraccept', {"chats": [], "users": self.db.get('RPMod', 'useraccept')})
        if self.db.get("RPMod", "rpconfigurate", False):
            self.db.set("RPMod", "rpconfigurate", self.merge_dict(conf_default, self.db.get("RPMod", "rpconfigurate")))

    async def addrpcmd(self, message):
        """<команда> / <действие> / <эмодзи> - добавить команду"""
        args = utils.get_args_raw(message)
        dict_rp = self.db.get('RPMod', 'rpcomands') or {}

        try:
            key_rp = str(args.split('/')[0]).strip()
            value_rp = str(args.split('/', maxsplit=2)[1]).strip()
            lenght_args = args.split('/')
            count_emoji = 0

            if len(lenght_args) >= 3:
                emoji_rp = str(args.split('/', maxsplit=2)[2]).strip()
                dict_emoji_rp = self.db.get('RPMod', 'rpemoji') or {}

                r = emoji_rp
                lst = []
                count_emoji = 1
                for x in r:
                    if is_emoji(x): 
                        lst.append(x)
                    if x.isalpha() or x.isspace() or x.isdigit() or x in string.punctuation:
                        await utils.answer(message, f"<b>Были введены не только эмодзи(пробел тоже символ)</b>")
                        return
                if len(lst) > 3:
                    await utils.answer(message, f"<b>Было введено более 3 эмодзи</b>")
                    return
                elif not emoji_rp or not emoji_rp.strip():
                    await utils.answer(message, f"<b>Разделитель для эмодзи есть, а их нет</b>")
                    return

            key_len = [len(x) for x in key_rp.split()]

            if len(dict_rp) >= 70:
                await utils.answer(message, '<b>Достигнут лимит RP команд</b>')
            elif not key_rp or not key_rp.strip():
                await utils.answer(message, '<b>Вы не ввели название RP команды</b>')
            elif not value_rp or not value_rp.strip():
                await utils.answer(message, '<b>Вы не ввели действие для RP команды</b>')
            elif int(len(key_len)) > 1:
                await utils.answer(message, '<b>В качестве RP команды было введено больше одного слова</b>')
            elif key_rp == 'all':
                await utils.answer(message, '<b>Использовать \'<code>all</code>\' в качестве названия команды запрещено</b>')
            elif count_emoji == 1:
                dict_emoji_rp[key_rp] = emoji_rp
                dict_rp[key_rp] = value_rp
                self.db.set('RPMod', 'rpcomands', dict_rp)
                self.db.set('RPMod', 'rpemoji', dict_emoji_rp)
                await utils.answer(message, f'<b>Команda \'<code>{key_rp}</code>\' успешно добавлена с эмодзи \'{emoji_rp}\'</b>')
            else:
                dict_rp[key_rp] = value_rp
                self.db.set('RPMod', 'rpcomands', dict_rp)
                await utils.answer(message, f'<b>Команda \'<code>{key_rp}</code>\' успешно добавлена</b>')
        except:
            await utils.answer(message, '<b>Вы не ввели разделитель /</b>')

    async def delrpcmd(self, message):
        """<команда> - удалить команду, <all> - удалить все"""
        args = utils.get_args_raw(message)
        dict_rp = self.db.get('RPMod', 'rpcomands') or {}
        dict_emoji_rp = self.db.get('RPMod', 'rpemoji') or {}
        key_rp = str(args)
        count = 0
        if key_rp == 'all':
            dict_rp.clear()
            dict_emoji_rp.clear()
            self.db.set('RPMod', 'rpcomands', dict_rp)
            self.db.set('RPMod', 'rpemoji', dict_emoji_rp)
            await utils.answer(message, '<b>Список RP команд очищен</b>')
            return
        elif not key_rp or not key_rp.strip():
            await utils.answer(message, '<b>Вы не ввели команду</b>')
        else:
            try:
                if key_rp in dict_emoji_rp:
                    dict_rp.pop(key_rp)
                    dict_emoji_rp.pop(key_rp)
                    self.db.set('RPMod', 'rpcomands', dict_rp)
                    self.db.set('RPMod', 'rpemoji', dict_emoji_rp)
                else:
                    dict_rp.pop(key_rp)
                    self.db.set('RPMod', 'rpcomands', dict_rp)
                await utils.answer(message, f'<b>Команda \'<code>{key_rp}</code>\' успешно удалена</b>')
            except KeyError:
                await utils.answer(message, '<b>Команда не найдена</b>')

    async def rpmodcmd(self, message):
        """- вкл/выкл RP режим"""
        status = self.db.get("RPMod", "status")
        rezjim = self.db.get("RPMod", "rprezjim")
        args = utils.get_args_raw(message)
        if not args:
            if status == 1:
                self.db.set("RPMod", "status", 2)
                await utils.answer(message, "<b>RP Режим <code>выключен</code></b>")
            else:
                self.db.set("RPMod", "status", 1)
                await utils.answer(message, "<b>RP Режим <code>включен</code></b>")
        elif args.strip() == 'toggle':
            if rezjim == 1:
                self.db.set("RPMod", "rprezjim", 2)
                await utils.answer(message, "<b>RP Режим изменён на <code>отправку смс</code></b>")
            else:
                self.db.set("RPMod", "rprezjim", 1)
                await utils.answer(message, "<b>RP Режим изменён на <code>изменение смс</code></b>")
        else:
            await utils.answer(message, 'Что то не так..')

    async def rplistcmd(self, message):
        """- список RP команд"""
        com = self.db.get('RPMod', 'rpcomands') or {}
        emojies = self.db.get('RPMod', 'rpemoji') or {}
        l = len(com)

        listComands = f'У вас RP команд: <b>{l}</b> из <b>70</b>'
        if len(com) == 0:
            await utils.answer(message, '<b>У вас нету RP команд</b>')
            return
        for i in com:
            if i in emojies.keys():
                listComands += f'\n• <b><code>{i}</code> - {com[i]} |</b> {emojies[i]}'
            else:
                listComands += f'\n• <b><code>{i}</code> - {com[i]}</b>'
        await utils.answer(message, listComands)

    async def rpnickcmd(self, message):
        """<ник> - сменить ник пользователю или себе, -l покажет все"""
        args = utils.get_args_raw(message).strip()
        reply = await message.get_reply_message()
        nicks = self.db.get('RPMod', 'rpnicks') or {}
        if args == '-l':
            str_nicks = '• ' + '\n •'.join(' --- '.join([f'<code>{user_id}</code>', f'<b>{nick}</b>']) for user_id, nick in nicks.items())
            return await utils.answer(message, str_nicks)

        if not reply:
            user = await message.client.get_entity(message.sender_id)
        else:
            user = await message.client.get_entity(reply.sender_id)
        if not args:
            if str(user.id) in nicks: 
                nicks.pop(str(user.id))
            self.db.set('RPMod', 'rpnicks', nicks)
            return await utils.answer(message, f"Ник пользователя <b>{str(user.id)}</b> изменён на '<b>{user.first_name}</b>'")
        
        lst = []
        nick = ''
        for x in args:
            if is_emoji(x): 
                lst.append(x)
            if not is_emoji(x): 
                nick += x
        if len(lst) > 3:
            await utils.answer(message, f"<b>Нельзя использовать более 3 эмодзи</b>")
        elif len(nick) + len(lst) > 45:
            await utils.answer(message, f"<b>Ник превышает лимит в 45 символов</b>")
        else:
            nicks[str(user.id)] = args
            self.db.set('RPMod', 'rpnicks', nicks)
            await utils.answer(message, f"Ник пользователя <b>{str(user.id)}</b> изменён на '<b>{args}</b>'")

    async def rpbackcmd(self, message):
        """- бекап RP команд"""
        args = utils.get_args_raw(message).strip()
        comands = self.db.get('RPMod', 'rpcomands') or {}
        emojies = self.db.get('RPMod', 'rpemoji') or {}
        file_name = 'RPModBackUp.pickle'
        id = message.to_id
        reply = await message.get_reply_message()
        if not args:
            await utils.answer(message, '<b>Аргументы:</b>\n<code>-b</code> <b>-- сделать бекап</b>\n<code>-r</code> <b><reply> загрузить бекап.</b>')
        if args == '-b':
            try:
                await message.delete()
                dict_all = { 'rp': comands, 'emj': emojies}
                with open(file_name, 'wb') as f:
                    pickle.dump(dict_all, f)
                await message.client.send_file(id, file_name)
            except Exception as e:
                await utils.answer(message, f"<b>Ошибка:\n</b>{e}")
        elif args == '-r' and reply:
            try:
                if not reply.document:
                    await utils.answer(message, f"<b>Это не файл.</b>")
                await reply.download_media(file_name)
                with open(file_name, 'rb') as f:
                    data = pickle.load(f)
                rp = data['rp']
                emj = data['emj']
                result_rp = {**comands, **rp}
                result_emj = {**emojies, **emj}
                self.db.set('RPMod', 'rpcomands', result_rp)
                self.db.set('RPMod', 'rpemoji', result_emj)
                await utils.answer(message, f"<b>Команды обновлены!</b>")
            except Exception as e:
                await utils.answer(message, f"<b>Ошибка:\n</b>{e}")

    async def rpblockcmd(self, message):
        """- добавить/удалить исключение, list для просмотра чатов"""
        args = utils.get_args_raw(message)
        ex = self.db.get("RPMod", "exlist") or []
        if not args:
            a = await message.client.get_entity(message.to_id)
            if a.id in ex:
                ex.remove(a.id)
                self.db.set("RPMod", "exlist", ex)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>[<code>{a.id}</code>] удален из исключений</i>')
            else:
                ex.append(a.id)
                self.db.set("RPMod", "exlist", ex)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>[<code>{a.id}</code>] добавлен в исключения</i>')
        elif args.isdigit():
            args = int(args)
            if args in ex:
                ex.remove(args)
                self.db.set("RPMod", "exlist", ex)
                a = await message.client.get_entity(args)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>(<code>{args}</code>) удален из исключений</i>')
            else:
                try:
                    a = await message.client.get_entity(args)
                except:
                    await utils.answer(message, '<b>Неверный ID.</b>')
                    return
                ex.append(args)
                self.db.set("RPMod", "exlist", ex)
                try:
                    name = a.title
                except:
                    name = a.first_name
                await utils.answer(message, f'<i>Чат <b><u>{name}</u></b>[<code>{a.id}</code>] добавлен в исключения</i>')
        elif args == 'list':
            ex_len = len(ex)
            if ex_len == 0:
                await utils.answer(message, f'<b>Список исключений пуст</b>')
                return
            sms = f'<i> Чаты, которые есть в исключениях({ex_len}):</i>'
            for i in ex:
                try:
                    a = await message.client.get_entity(i)
                except:
                    sms += f'\n<b>• Неверный ID -- {i}</b>'
                    continue
                try:
                    name = a.title
                except:
                    name = a.first_name
                sms += f'\n• <b><u>{name}</u> --- </b><code>{i}</code>'
            await utils.answer(message, sms)
        else:
            await utils.answer(message, 'Что-то пошло не так..')

    async def useracceptcmd(self, message):
        """- добавить/удалить чат в список разрешённых"""
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        userA = self.db.get('RPMod', 'useraccept') or {"chats": [], "users": []}
        if not reply and not args and message.is_group:
            chat = message.chat
            if chat.id not in userA["chats"]:
                userA["chats"].append(chat.id)
                self.db.set('RPMod', 'useraccept', userA)
                return await utils.answer(message, f'<i>Чату <b><u>{chat.title}</u></b>[<code>{chat.id}</code>] открыт доступ.</i>')
            else:
                userA["chats"].remove(chat.id)
                self.db.set('RPMod', 'useraccept', userA)
                return await utils.answer(message, f'<i>Чату <b><u>{chat.title}</u></b>[<code>{chat.id}</code>] закрыт доступ.</i>')
        elif args == '-l':
            sms = '<b>Пользователи, у которых есть доступ к командам:</b>'
            for k, v in userA.items():
                if k == 'chats':
                    sms += f'\n<b>Чатов:</b>'
                    for i in v: 
                        try:
                            chat = await message.client.get_entity(int(i))
                            name = chat.title
                            sms += f'\n<b>• <u>{name}</u> ---</b> <code>{i}</code>'
                        except:
                            sms += f'\n<b>•</b> <code>{i}</code>'
                else:
                    sms += f'\n<b>Пользователей:</b>'
                    for i in v: 
                        try:
                            user = await message.client.get_entity(int(i))
                            name = user.first_name
                            sms += f'\n<b>• <u>{name}</u> ---</b> <code>{i}</code>'
                        except:
                            sms += f'\n<b>•</b> <code>{i}</code>'
            await utils.answer(message, sms)
        elif args or reply:
            args = int(args) if args.isdigit() else reply.sender_id
            if args in userA["users"]:
                userA["users"].remove(args)
                self.db.set('RPMod', 'useraccept', userA)
                await utils.answer(message, f'<b>Пользователю <code>{args}</code> был закрыт доступ</b>')
            elif args in userA["chats"]:
                userA["chats"].remove(args)
                self.db.set('RPMod', 'useraccept', userA)
                await utils.answer(message, f'<b>Чату <code>{args}</code> был закрыт доступ</b>')
            else:
                try:
                    entity = await message.client.get_entity(args)
                    if isinstance(entity, Channel):
                        userA["chats"].append(args)
                        self.db.set('RPMod', 'useraccept', userA)
                        await utils.answer(message, f'<b>Чату <code>{args}</code> был открыт доступ</b>')
                    else:
                        userA["users"].append(args)
                        self.db.set('RPMod', 'useraccept', userA)
                        await utils.answer(message, f'<b>Пользователю <code>{args}</code> был открыт доступ</b>')
                except:
                    await utils.answer(message, f'<b>Не удалось найти entity для {args}</b>')
        else:
            await utils.answer(message, 'Что-то не так..')

    async def rpconfcmd(self, message):
        """- настройка шаблона для RP"""
        conf = self.db.get("RPMod", "rpconfigurate") or conf_default
        args = utils.get_args_raw(message)
        if not args:
            s1 = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-s1'].items()])
            s2 = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-s2'].items()])
            s3 = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-s3'].items()])
            sE = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-sE'].items()])
            sS = '\n'.join([' | '.join([key, value[1], '✅' if value[0] else '❌']) for key, value in conf['-sS'].items()])
            msg_text = f'⚙️ <b>Настройка шаблона для команды:</b>\n-s1 --- включить/выключить стиль для действия:\n{s1}\n-s2 --- действует на текст "С репликой":\n{s2}\n-s3 --- действует на саму реплику:\n{s3}\n-sE --- выбор эмодзи перед репликой:\n{sE}\n-sS --- выбор символа для разрыва строк в реплике:\n{sS}'
            return await utils.answer(message, msg_text)
        args = args.split(' ')
        if len(args) <= 1:
            return await utils.answer(message, 'Было введено меньше двух аргументов')
        try:
            if args[0] in ['-s1', '-s2', '-s3']:
                if conf[args[0]][args[1]][0]:
                    conf[args[0]][args[1]][0] = False
                else:
                    conf[args[0]][args[1]][0] = True
            elif args[0] in ['-sE', '-sS']:
                for i in conf[args[0]].keys():
                    conf[args[0]][i][0] = False
                conf[args[0]][args[1]][0] = True
            else:
                return await utils.answer(message, 'Неизвестный аргумент')
        except:
            return await utils.answer(message, 'Неверная цифра')
        self.db.set("RPMod", "rpconfigurate", conf)
        await utils.answer(message, f'Конфигурация успешно изменена')

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            comand = self.db.get('RPMod', 'rpcomands') or {}
            rezjim = self.db.get('RPMod', 'rprezjim')
            emojies = self.db.get('RPMod', 'rpemoji') or {}
            ex = self.db.get("RPMod", "exlist") or []
            nicks = self.db.get('RPMod', 'rpnicks') or {}
            users_accept = self.db.get('RPMod', 'useraccept') or {"chats": [], "users": []}
            conf = self.db.get("RPMod", "rpconfigurate") or conf_default

            chat_rp = await message.client.get_entity(message.to_id)
            if status != 1 or chat_rp.id in ex: 
                return
            me_id = (await message.client.get_me()).id

            if message.sender_id not in users_accept["users"] and message.sender_id != me_id and chat_rp.id not in users_accept["chats"]: 
                return
            
            me = await message.client.get_entity(message.sender_id)

            if str(me.id) in nicks.keys():
                nick = nicks[str(me.id)]
            else:
                nick = me.first_name
                
            args = message.text.lower()
            lines = args.splitlines()
            tags = lines[0].split(' ')

            if not tags[-1].startswith('@'):
                reply = await message.get_reply_message()
                if not reply:
                    return
                user = await message.client.get_entity(reply.sender_id)
            else:
                if not tags[-1][1:].isdigit():
                    try:
                        user = await message.client.get_entity(tags[-1])
                    except:
                        return
                else:
                    try:
                        user = await message.client.get_entity(int(tags[-1][1:]))
                    except:
                        return
                lines[0] = lines[0].rsplit(' ', 1)[0]

            detail = lines[0].split(' ', maxsplit=1)
            if len(detail) < 2:
                detail.append(' ')
            if detail[0] not in comand.keys(): 
                return
                
            detail[1] = ' ' + detail[1] 
            user.first_name = nicks[str(user.id)] if str(user.id) in nicks else user.first_name

            sE = ''.join([value[1] if value[0] else '' for value in conf['-sE'].values()])
            s1 = [
                ''.join([value[2] if value[0] else '' for value in conf['-s1'].values()]),
                ''.join([value[3] if value[0] else '' for value in conf['-s1'].values()])
            ]
            s2 = [
                ''.join([value[2] if value[0] else '' for value in conf['-s2'].values()]),
                ''.join([value[3] if value[0] else '' for value in conf['-s2'].values()])
            ]
            s3 = [
                ''.join([value[2] if value[0] else '' for value in conf['-s3'].values()]),
                ''.join([value[3] if value[0] else '' for value in conf['-s3'].values()])
            ]
            sS = ''.join([value[2] if value[0] else '' for value in conf['-sS'].values()])

            rpMessageSend = ''
            if detail[0] in emojies.keys(): 
                rpMessageSend += emojies[detail[0]] + ' | '

            rpMessageSend += f"<a href=tg://user?id={me.id}>{nick}</a> {s1[0]}{comand[detail[0]]}{s1[1]} <a href=tg://user?id={user.id}>{user.first_name}</a>{detail[1]}"

            if len(lines) >= 2: 
                rpMessageSend += f"\n{sE} {s2[0]}С репликой:{s2[1]} {s3[0]}{sS.join(lines[1:])}{s3[1]}"

            if rezjim == 1:
                await utils.answer(message, rpMessageSend)
            else:
                await message.respond(rpMessageSend)

        except Exception as e:
            pass

    def merge_dict(self, d1, d2):
        d_all = {**d1, **d2}
        for key in d_all:
            d_all[key] = {**d1[key], **d_all[key]}
        return d_all