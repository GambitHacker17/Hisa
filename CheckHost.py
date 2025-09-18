# meta developer: @MartyyyK
# requires: aiohttp

import asyncio
import aiohttp
import logging
import re

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class CheckHost(loader.Module):
    """Проверка доступности веб-сайтов, серверов, хостов и IP-адресов"""

    strings = {
        "name": "CheckHost",
        "no_url": "<emoji document_id=5440381017384822513>❌</emoji> <b>Нужно <code>{}{} [адрес]</code></b>",
        "checking_http": "<emoji document_id=6332573220868196043>🕓</emoji> <b>Проверяю доступность...</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "limit",
                True,
                lambda: "Включить/выключить лимит геолокаций в проверке",
                validator=loader.validators.Boolean(),
            ),
            loader.ConfigValue(
                "limit_geo",
                10,
                lambda: "Лимит геолокаций",
                validator=loader.validators.Integer(minimum=1, maximum=50),
            ),
        )

    async def client_ready(self, client, db):
        self.db = db
        self._client = client

    @loader.command()
    async def chhttp(self, message):
        """<адрес> - проверить доступность"""

        query = utils.get_args_raw(message)

        if not query:
            return await utils.answer(message, self.strings['no_url'].format(self.get_prefix(), 'chhttp'))

        await utils.answer(message, self.strings['checking_http'])

        url_cr = f"https://check-host.net/check-http?host={query}"

        if self.config['limit']:
            url_cr += f"&max_nodes={self.config['limit_geo']}"

        async with aiohttp.ClientSession() as session:
            cr = await session.get(url_cr, headers={'Accept': 'application/json'})
            create = await cr.json()
            await asyncio.sleep(10)
            res = await session.get(f"https://check-host.net/check-result/{create['request_id']}", headers={'Accept': 'application/json'})
            response = await res.json()

        ip_address = "Не определен"
        for node_data in response.values():
            if node_data and node_data[0] and len(node_data[0]) > 4:
                ip_address = node_data[0][4]
                break

        txt = f"""<b>
🌐 Проверка доступности

📡 IP: <code>{ip_address}</code>
🔗 Адрес: {query}

🛜 Доступность
</b>
"""

        count = 0

        for node_id, node_info in create['nodes'].items():
            if self.config['limit'] and count >= self.config['limit_geo']:
                break

            country_code = node_info[0]
            country = node_info[1].split('#')[0].strip()
            city = node_info[2].split('#')[0].strip()
            ip = node_info[3]

            node_response = response.get(node_id)
            if node_response and node_response[0]:
                response_data = node_response[0]
                response_code = response_data[3] if len(response_data) > 3 else "None"
                responsee = response_data[2] if len(response_data) > 2 else "No response"
                response_seconds = response_data[1] if len(response_data) > 1 else 0

                try:
                    response_seconds = round(float(response_seconds), 2)
                except (ValueError, TypeError):
                    response_seconds = 0.00
            else:
                response_code = "None"
                responsee = "Connection timed out"
                response_seconds = 0.00

            flag = self.flags.get(country_code, "")

            txt += f"""<b>{flag} {country} ({city}) (<code>{ip}</code>)</b>
<i>Response code: {response_code} ({responsee}) {response_seconds:.2f} сек.</i>
"""

            count += 1

        txt += f"\n<b><a href={create['permanent_link']}>🖥 Ссылка на результат в check-host.net</a></b>"

        return await utils.answer(message, txt)

    flags = {
        "ad": "🇦🇩", "ae": "🇦🇪", "af": "🇦🇫", "ag": "🇦🇬", "ai": "🇦🇮", 
        "al": "🇦🇱", "am": "🇦🇲", "ao": "🇦🇴", "aq": "🇦🇶", "ar": "🇦🇷", 
        "at": "🇦🇹", "au": "🇦🇺", "aw": "🇦🇼", "ax": "🇦🇽", "az": "🇦🇿", 
        "ba": "🇧🇦", "bb": "🇧🇧", "bd": "🇧🇩", "be": "🇧🇪", "bf": "🇧🇫", 
        "bg": "🇧🇬", "bh": "🇧🇭", "bi": "🇧🇮", "bj": "🇧🇯", "bl": "🇧🇱", 
        "bm": "🇧🇲", "bn": "🇧🇳", "bo": "🇧🇴", "bq": "🇧🇶", "br": "🇧🇷", 
        "bs": "🇧🇸", "bt": "🇧🇹", "bv": "🇧🇻", "bw": "🇧🇼", "by": "🇧🇾", 
        "bz": "🇧🇿", "ca": "🇨🇦", "cc": "🇨🇨", "cd": "🇨🇩", "cf": "🇨🇫", 
        "cg": "🇨🇬", "ch": "🇨🇭", "ci": "🇨🇮", "ck": "🇨🇰", "cl": "🇨🇱", 
        "cm": "🇨🇲", "cn": "🇨🇳", "co": "🇨🇴", "cr": "🇨🇷", "cu": "🇨🇺", 
        "cv": "🇨🇻", "cw": "🇨🇼", "cx": "🇨🇽", "cy": "🇨🇾", "cz": "🇨🇿", 
        "de": "🇩🇪", "dj": "🇩🇯", "dk": "🇩🇰", "dm": "🇩🇲", "do": "🇩🇴", 
        "dz": "🇩🇿", "ec": "🇪🇨", "ee": "🇪🇪", "eg": "🇪🇬", "eh": "🇪🇭", 
        "er": "🇪🇷", "es": "🇪🇸", "et": "🇪🇹", "fi": "🇫🇮", "fj": "🇫🇯", 
        "fk": "🇫🇰", "fm": "🇫🇲", "fo": "🇫🇴", "fr": "🇫🇷", "ga": "🇬🇦", 
        "gb": "🇬🇧", "gd": "🇬🇩", "ge": "🇬🇪", "gf": "🇬🇫", "gg": "🇬🇬", 
        "gh": "🇬🇭", "gi": "🇬🇮", "gl": "🇬🇱", "gm": "🇬🇲", "gn": "🇬🇳", 
        "gp": "🇬🇵", "gq": "🇬🇶", "gr": "🇬🇷", "gs": "🇬🇸", "gt": "🇬🇹", 
        "gu": "🇬🇺", "gw": "🇬🇼", "gy": "🇬🇾", "hk": "🇭🇰", "hm": "🇭🇲", 
        "hn": "🇭🇳", "hr": "🇭🇷", "ht": "🇭🇹", "hu": "🇭🇺", "id": "🇮🇩", 
        "ie": "🇮🇪", "il": "🇮🇱", "im": "🇮🇲", "in": "🇮🇳", "io": "🇮🇴", 
        "iq": "🇮🇶", "ir": "🇮🇷", "is": "🇮🇸", "it": "🇮🇹", "je": "🇯🇪", 
        "jm": "🇯🇲", "jo": "🇯🇴", "jp": "🇯🇵", "ke": "🇰🇪", "kg": "🇰🇬", 
        "kh": "🇰🇭", "ki": "🇰🇮", "km": "🇰🇲", "kn": "🇰🇳", "kp": "🇰🇵", 
        "kr": "🇰🇷", "kw": "🇰🇼", "ky": "🇰🇾", "kz": "🇰🇿", "la": "🇱🇦", 
        "lb": "🇱🇧", "lc": "🇱🇨", "li": "🇱🇮", "lk": "🇱🇰", "lr": "🇱🇷", 
        "ls": "🇱🇸", "lt": "🇱🇹", "lu": "🇱🇺", "lv": "🇱🇻", "ly": "🇱🇾", 
        "ma": "🇲🇦", "mc": "🇲🇨", "md": "🇲🇩", "me": "🇲🇪", "mf": "🇲🇫", 
        "mg": "🇲🇬", "mh": "🇲🇭", "mk": "🇲🇰", "ml": "🇲🇱", "mm": "🇲🇲", 
        "mn": "🇲🇳", "mo": "🇲🇴", "mp": "🇲🇵", "mq": "🇲🇶", "mr": "🇲🇷", 
        "ms": "🇲🇸", "mt": "🇲🇹", "mu": "🇲🇺", "mv": "🇲🇻", "mw": "🇲🇼", 
        "mx": "🇲🇽", "my": "🇲🇾", "mz": "🇲🇿", "na": "🇳🇦", "nc": "🇳🇨", 
        "ne": "🇳🇪", "nf": "🇳🇫", "ng": "🇳🇬", "ni": "🇳🇮", "nl": "🇳🇱", 
        "no": "🇳🇴", "np": "🇳🇵", "nr": "🇳🇷", "nu": "🇳🇺", "nz": "🇳🇿", 
        "om": "🇴🇲", "pa": "🇵🇦", "pe": "🇵🇪", "pf": "🇵🇫", "pg": "🇵🇬", 
        "ph": "🇵🇭", "pk": "🇵🇰", "pl": "🇵🇱", "pm": "🇵🇲", "pn": "🇵🇳", 
        "pr": "🇵🇷", "ps": "🇵🇸", "pt": "🇵🇹", "pw": "🇵🇼", "py": "🇵🇾", 
        "qa": "🇶🇦", "re": "🇷🇪", "ro": "🇷🇴", "rs": "🇷🇸", "ru": "🇷🇺", 
        "rw": "🇷🇼", "sa": "🇸🇦", "sb": "🇸🇧", "sc": "🇸🇨", "sd": "🇸🇩", 
        "se": "🇸🇪", "sg": "🇸🇬", "sh": "🇸🇭", "si": "🇸🇮", "sj": "🇸🇯", 
        "sk": "🇸🇰", "sl": "🇸🇱", "sm": "🇸🇲", "sn": "🇸🇳", "so": "🇸🇴", 
        "sr": "🇸🇷", "ss": "🇸🇸", "st": "🇸🇹", "sv": "🇸🇻", "sx": "🇸🇽", 
        "sy": "🇸🇾", "sz": "🇸🇿", "tc": "🇹🇨", "td": "🇹🇩", "tf": "🇹🇫", 
        "tg": "🇹🇬", "th": "🇹🇭", "tj": "🇹🇯", "tk": "🇹🇰", "tl": "🇹🇱", 
        "tm": "🇹🇲", "tn": "🇹🇳", "to": "🇹🇴", "tr": "🇹🇷", "tt": "🇹🇹", 
        "tv": "🇹🇻", "tw": "🇹🇼", "tz": "🇹🇿", "ua": "🇺🇦", "ug": "🇺🇬",
        "um": "🇺🇲", "us": "🇺🇸", "va": "🇻🇦", "vc": "🇻🇨", "ve": "🇻🇪",
        "vg": "🇻🇬", "vi": "🇻🇮", "vn": "🇻🇳", "vu": "🇻🇺", "wf": "🇼🇫",
        "ws": "🇼🇸", "xk": "🇽🇰", "ye": "🇾🇪", "yt": "🇾🇹", "za": "🇿🇦",
        "zm": "🇿🇲", "zw": "🇿🇼",
}