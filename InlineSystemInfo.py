# requires: psutil py-cpuinfo
# meta developer: @MartyyyK

import telethon
import aiogram
import git

import datetime
import logging
from typing import Union
import platform
import cpuinfo
import psutil
from aiogram.utils.markdown import quote_html
from os.path import exists
from .. import loader, utils

logger = logging.getLogger(__name__)

def remove_empty_lines(string_with_empty_lines):
    lines = string_with_empty_lines.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]

    return "".join(line + "\n" for line in non_empty_lines)

backslash = "\n"

def get_os_release():
    if not exists("/etc/os-release"):
        return False

    list_ = []
    with open("/etc/os-release") as f:
        list_.extend(item.split("=") for item in f.readlines())
    return {item[0]: item[1].replace(backslash, "").replace('"', "") for item in list_}

def get_distro():
    if not exists("/etc/issue"):
        return "N/A"

    try:
        with open("/etc/issue") as f:
            return f.read().split()[0]
    except:
        return "N/A"

def progressbar(iteration: int, length: int) -> str:
    if iteration is None:
        return "N/A"
    
    percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(100)))
    filledLength = int(length * iteration // 100)
    return "█" * filledLength + "▒" * (length - filledLength)

def chunks(_list: Union[list, tuple, set], n: int, /) -> list:
    return [_list[i : i + n] for i in range(0, len(_list), n)]

def bytes2human(n):
    if n is None:
        return "N/A"

    symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
    prefix = {s: 1 << (i + 1) * 10 for i, s in enumerate(symbols)}
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return "%.1f%s" % (value, s)
    return "%sB" % n

@loader.tds
class InlineSystemInfoMod(loader.Module):
    """Подробная информация о сервере"""

    strings = {
        "name": "InlineSystemInfo",
    }

    AddressFamily = {
        2: "IPv4",
        10: "IPv6",
        28: "IPv6",
        17: "Link",
        18: "Link",
    }

    def menu_keyboard(self) -> list:
        keyboard = [
            [
                {
                    "text": "😼 General",
                    "callback": self.change_stuff,
                    "args": ("General",),
                }
            ],
        ]

        keyboard.extend(
            iter(
                chunks(
                    [
                        {
                            "text": "🧠 CPU",
                            "callback": self.change_stuff,
                            "args": ("CPU",),
                        },
                        {
                            "text": "🐧 Linux",
                            "callback": self.change_stuff,
                            "args": ("Linux",),
                        },
                        {
                            "text": "🗄 Memory",
                            "callback": self.change_stuff,
                            "args": ("Memory",),
                        },
                        {
                            "text": "🌐 Network Address",
                            "callback": self.change_stuff,
                            "args": ("Network Address",),
                        },
                        {
                            "text": "🌐 Network Stats",
                            "callback": self.change_stuff,
                            "args": ("Network Stats",),
                        },
                        {
                            "text": "💽 Disk",
                            "callback": self.change_stuff,
                            "args": ("Disk",),
                        },
                        {
                            "text": "🌡 Sensors",
                            "callback": self.change_stuff,
                            "args": ("Sensors",),
                        },
                        {
                            "text": "🐍 Python",
                            "callback": self.change_stuff,
                            "args": ("Python",),
                        }
                    ],
                    3,
                )
            )
        )

        keyboard.append([{"text": "🔻 Close", "callback": self.inline__close}])
        try:
            return keyboard[3].remove([])
        except ValueError:
            return keyboard

    def safe_cpu_info(self):
        try:
            return cpuinfo.get_cpu_info()
        except:
            return {"brand_raw": "N/A", "arch_string_raw": "N/A", "flags": []}

    def safe_cpu_count(self):
        try:
            return psutil.cpu_count()
        except:
            return "N/A"

    def safe_cpu_count_logical(self):
        try:
            return psutil.cpu_count(logical=False)
        except:
            return "N/A"

    def safe_cpu_freq(self):
        try:
            return psutil.cpu_freq()
        except:
            return None

    def safe_virtual_memory(self):
        try:
            return psutil.virtual_memory()
        except:
            return type('obj', (object,), {
                'percent': None,
                'used': None, 
                'total': None
            })()

    def safe_swap_memory(self):
        try:
            return psutil.swap_memory()
        except:
            return type('obj', (object,), {
                'percent': None,
                'used': None, 
                'total': None
            })()

    def safe_disk_partitions(self):
        try:
            return psutil.disk_partitions()
        except:
            return []

    def safe_disk_usage(self, path):
        try:
            return psutil.disk_usage(path)
        except:
            return type('obj', (object,), {
                'percent': None,
                'used': None, 
                'total': None
            })()

    def safe_net_if_addrs(self):
        try:
            return psutil.net_if_addrs()
        except:
            return {}

    def safe_net_if_stats(self):
        try:
            return psutil.net_if_stats()
        except:
            return {}

    def safe_sensors_temperatures(self):
        try:
            if hasattr(psutil, "sensors_temperatures"):
                return psutil.sensors_temperatures()
            return {}
        except:
            return {}

    def safe_sensors_fans(self):
        try:
            if hasattr(psutil, "sensors_fans"):
                return psutil.sensors_fans()
            return {}
        except:
            return {}

    def safe_loadavg(self):
        try:
            loadavg = psutil.getloadavg()
            return tuple(float(x) for x in loadavg)
        except:
            return ("N/A", "N/A", "N/A")

    def safe_boot_time(self):
        try:
            return datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        except:
            return "N/A"

    def general_info(self):
        cpu_info = self.safe_cpu_info()
        cpu_count_logic = self.safe_cpu_count_logical()
        cpu_count = self.safe_cpu_count()
        virtual_memory = self.safe_virtual_memory()
        swap_memory = self.safe_swap_memory()
        
        string = "😼 <b>System Info</b>\n"
        string += f"  ├──<b>CPU Name</b>: <code>{cpu_info.get('brand_raw', 'N/A')}</code> {cpu_count_logic}/{cpu_count} ({cpu_info.get('arch_string_raw', 'N/A')})\n"
        string += f"  ├──<b>RAM</b>: {progressbar(virtual_memory.percent, 10)} <code>({bytes2human(virtual_memory.used)}/{bytes2human(virtual_memory.total)})</code>\n"
        string += f"  └──<b>Swap</b>: {progressbar(swap_memory.percent, 10)} <code>({bytes2human(swap_memory.used)}/{bytes2human(swap_memory.total)})</code>\n\n"

        string += "🐧 <b>Linux Info</b>\n"
        string += f"  ├──<b>Name</b>: <code>{get_distro()}</code>\n"
        string += f"  └──<b>Kernel</b>: <code>{platform.release()}</code>\n\n"

        disk_partitions = self.safe_disk_partitions()
        for disk_root in disk_partitions:
            if disk_root.mountpoint == '/':
                disk_usage = self.safe_disk_usage(disk_root.mountpoint)

                string += "💽 <b>Disk Info</b> <code>(/)</code>\n"
                string += f"  └──<b>{disk_root.device}</b>\n"
                string += f"        ├── <b>Mount</b> {disk_root.mountpoint}\n"
                string += f"        ├── <b>FS</b> {disk_root.fstype}\n"
                string += f"        ├── <b>Disk Usage</b> {disk_usage.percent if disk_usage.percent is not None else 'N/A'}% ({bytes2human(disk_usage.used)}/{bytes2human(disk_usage.total)})\n"
                string += f"        │       └──{progressbar(disk_usage.percent, 10)}\n"
                string += f"        └── <b>Options</b> {disk_root.opts}\n\n"

        return string

    def cpu_string(self):
        cpu_info = self.safe_cpu_info()
        cpu_count_logic = self.safe_cpu_count_logical()
        cpu_count = self.safe_cpu_count()
        cpu_freq = self.safe_cpu_freq()
        loadavg = self.safe_loadavg()
        
        string = "🧠  <b>CPU Info</b>\n"
        string += f"⦁ <b>Name</b>: {cpu_info.get('brand_raw', 'N/A')} ({cpu_info.get('arch_string_raw', 'N/A')})\n"
        string += f"⦁ <b>Count</b>: {cpu_count_logic} ({cpu_count})\n"
        
        if cpu_freq:
            string += f"⦁ <b>Freq</b>: {cpu_freq.current:.2f} MHz (max: {cpu_freq.max:.2f} MHz / min: {cpu_freq.min:.2f} MHz)\n"
        else:
            string += f"⦁ <b>Freq</b>: N/A\n"
            
        string += f"⦁ <b>Flags</b>: {' '.join(cpu_info.get('flags', ['No flags']))}\n"

        if all(isinstance(x, (int, float)) for x in loadavg):
            string += f"⦁ <b>Load avg</b>: {loadavg[0]:.2f} {loadavg[1]:.2f} {loadavg[2]:.2f}\n"
        else:
            string += f"⦁ <b>Load avg</b>: {loadavg[0]} {loadavg[1]} {loadavg[2]}\n"

        return string

    def disks_string(self):
        disk_partitions = self.safe_disk_partitions()
        if not disk_partitions:
            return "💽  <b>Disk Info</b>\nNo disk information available\n\n"

        string = "💽  <b>Disk Info</b>\n"
        for disk in disk_partitions:
            disk_usage = self.safe_disk_usage(disk.mountpoint)

            string += f"<b>{disk.device}</b>\n"
            string += f"├── <b>Mount</b> {disk.mountpoint}\n"
            string += f"├── <b>FS</b> {disk.fstype}\n"
            string += f"├── <b>Disk Usage</b> {disk_usage.percent if disk_usage.percent is not None else 'N/A'}% ({bytes2human(disk_usage.used)}/{bytes2human(disk_usage.total)})\n"
            string += f"│       └──{progressbar(disk_usage.percent, 10)}\n"
            string += f"└── <b>Options</b> {disk.opts}\n\n"

        return string

    def network_addr_string(self):
        net_if_addrs = self.safe_net_if_addrs()
        if not net_if_addrs:
            return "🌐  <b>Network Info</b>\nNo network address information available\n\n"

        string = "🌐  <b>Network Info</b>\n"
        string += "<b>Address</b>:\n"
        for interf in net_if_addrs:
            interface = net_if_addrs[interf]
            string += f"<b>{interf}</b>\n"
            for addr in interface:
                attr = [
                    a
                    for a in dir(addr)
                    if not a.startswith("__")
                    and not a.startswith("_")
                    and not callable(getattr(addr, a))
                ]
                family_name = self.AddressFamily.get(addr.family, f"Unknown ({addr.family})")
                string += f"{family_name}\n"
                for item in attr[:-1]:
                    string += f"├── {item}: {getattr(addr, item)}\n"
                string += f"└── {attr[-1]}: {getattr(addr, attr[-1])}\n"
            string += "\n"

        return string

    def memory_string(self):
        virtual_memory = self.safe_virtual_memory()
        swap_memory = self.safe_swap_memory()
        
        string = "🗄  <b>Memory Info</b>\n"
        string += f"<b>RAM</b>: {progressbar(virtual_memory.percent, 10)} <code>({bytes2human(virtual_memory.used)}/{bytes2human(virtual_memory.total)})</code>\n"
        string += f"<b>Swap</b>: {progressbar(swap_memory.percent, 10)} <code>({bytes2human(swap_memory.used)}/{bytes2human(swap_memory.total)})</code>\n"

        return string

    def sensors_string(self):
        sensors_temperatures = self.safe_sensors_temperatures()
        sensors_fans = self.safe_sensors_fans()
        
        string = ""
        if sensors_temperatures:
            string = "🌡  <b>Sensors Info</b>\n" + "<b>Temperature</b>:\n"
            for sensor_name in sensors_temperatures:
                sensor = sensors_temperatures[sensor_name]
                string += f"<b>{sensor_name}</b>\n"
                for sensor_info in sensor:
                    attr = [
                        a
                        for a in dir(sensor_info)
                        if not a.startswith("__")
                        and not a.startswith("_")
                        and not callable(getattr(sensor_info, a))
                    ]
                    for item in attr[:-1]:
                        string += f"├── {item}: {getattr(sensor_info, item)}\n"
                    string += f"└── {attr[-1]}: {getattr(sensor_info, attr[-1])}\n"
                string += "\n"

        if sensors_fans:
            string += "<b>Fans</b>:\n"
            for sensor_name in sensors_fans:
                sensor = sensors_fans[sensor_name]
                string += f"<b>{sensor_name}</b>\n"
                for sensor_info in sensor:
                    attr = [
                        a
                        for a in dir(sensor_info)
                        if not a.startswith("__")
                        and not a.startswith("_")
                        and not callable(getattr(sensor_info, a))
                    ]
                    for item in attr[:-1]:
                        string += f"├── {item}: {getattr(sensor_info, item)}\n"
                    string += f"└── {attr[-1]}: {getattr(sensor_info, attr[-1])}\n"

        if not string:
            return "🌡  <b>Sensors Info</b>\nNo sensor information available\n\n"
            
        return string

    def network_stats_string(self):
        net_if_stats = self.safe_net_if_stats()
        if not net_if_stats:
            return "🌐  <b>Network Info</b>\nNo network statistics available\n\n"

        string = "🌐  <b>Network Info</b>\n" + "<b>Stats</b>:\n"
        for interf in net_if_stats:
            interface = net_if_stats[interf]
            string += f"<b>{interf}</b>\n"
            string += f"└── {quote_html(str(interface))}\n\n"

        return string

    def linux_string(self):
        os_release = get_os_release()
        boot_time = self.safe_boot_time()

        string = f"""🐧  <b>Linux Info</b>
        Name: {get_distro()}
        Kernel: {platform.release()}
        Hostname: {platform.node()}
        {f'glibc ver: {platform.glibc()[1]}' if hasattr(platform, 'glibc') else ''}
        Boot time: {boot_time}

        """
        if os_release:
            string += f"""<b>\n        /etc/os-releases Info:</b>
        Pretty Name: {os_release.get("PRETTY_NAME", "N/A")}
        Name: {os_release.get("NAME", "N/A")}
        Version: {os_release.get("VERSION", "Not available")}
        Documentation: {os_release.get("DOCUMENTATION_URL", "Not available")}
        Support: {os_release.get("SUPPORT_URL", "Not available")}
        Bug Report: {os_release.get("BUG_REPORT_URL", "Not available")}
            """

        return remove_empty_lines(string)
    
    def python_string(self):
        try:
            cpuinfo_version = cpuinfo.get_cpu_info().get('cpuinfo_version_string', 'N/A')
        except:
            cpuinfo_version = 'N/A'
            
        string = "🐍 <b>Python Info</b>\n"
        string += f"  ├──<b>Version</b>: <code>{platform.python_version()}</code>\n"
        string += f"  ├──<b>Version (More details)</b>: <code>{platform.python_version()}</code>\n"
        string += f"  └──<b>Python Packages version</b>\n"
        string += f"         ├──<b>Telethon</b>: <code>{telethon.__version__}</code>\n"
        string += f"         ├──<b>AIOgram</b>: <code>{aiogram.__version__}</code>\n"
        string += f"         ├──<b>Cpuinfo</b>: <code>{cpuinfo_version}</code>\n"
        string += f"         ├──<b>psutil</b>: <code>{psutil.__version__}</code>\n"
        string += f"         └──<b>git</b>: <code>{git.__version__}</code>\n"

        return string

    def __init__(self):
        pass

    def update_data(self):
        self.info_string = {
            "General": self.general_info(),
            "CPU": self.cpu_string(),
            "Disk": self.disks_string(),
            "Network Address": self.network_addr_string(),
            "Network Stats": self.network_stats_string(),
            "Memory": self.memory_string(),
            "Sensors": self.sensors_string(),
            "Linux": self.linux_string(),
            "Python": self.python_string(),
        }

    async def systeminfocmd(self, message):
        """- получить информацию о сервере"""
        await utils.run_sync(self.update_data)

        await self.inline.form(
            text=self.info_string["General"],
            message=message,
            reply_markup=self.menu_keyboard(),
        )

    async def change_stuff(self, call, stuff):
        if self.info_string.get(stuff):
            await call.edit(text=self.info_string[stuff], reply_markup=self.menu_keyboard())
        else:
            await call.answer("No data")

    async def inline__close(self, call) -> None:
        await call.delete()