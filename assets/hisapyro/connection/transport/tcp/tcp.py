import asyncio
import ipaddress
import logging
import socket
from concurrent.futures import ThreadPoolExecutor
import socks
log = logging.getLogger(__name__)
class TCP:
    TIMEOUT = 10
    def __init__(self, ipv6: bool, proxy: dict):
        self.socket = None
        self.reader = None
        self.writer = None
        self.lock = asyncio.Lock()
        self.loop = asyncio.get_event_loop()
        self.proxy = proxy
        if proxy:
            hostname = proxy.get("hostname")
            try:
                ip_address = ipaddress.ip_address(hostname)
            except ValueError:
                self.socket = socks.socksocket(socket.AF_INET)
            else:
                if isinstance(ip_address, ipaddress.IPv6Address):
                    self.socket = socks.socksocket(socket.AF_INET6)
                else:
                    self.socket = socks.socksocket(socket.AF_INET)
            self.socket.set_proxy(
                proxy_type=getattr(socks, proxy.get("scheme").upper()),
                addr=hostname,
                port=proxy.get("port", None),
                username=proxy.get("username", None),
                password=proxy.get("password", None)
            )
            self.socket.settimeout(TCP.TIMEOUT)
            log.info("Using proxy %s", hostname)
        else:
            self.socket = socket.socket(
                socket.AF_INET6 if ipv6
                else socket.AF_INET
            )
            self.socket.setblocking(False)
    async def connect(self, address: tuple):
        if self.proxy:
            with ThreadPoolExecutor(1) as executor:
                await self.loop.run_in_executor(executor, self.socket.connect, address)
        else:
            try:
                await asyncio.wait_for(asyncio.get_event_loop().sock_connect(self.socket, address), TCP.TIMEOUT)
            except asyncio.TimeoutError:  
                raise TimeoutError("Connection timed out")
        self.reader, self.writer = await asyncio.open_connection(sock=self.socket)
    async def close(self):
        try:
            if self.writer is not None:
                self.writer.close()
                await asyncio.wait_for(self.writer.wait_closed(), TCP.TIMEOUT)
        except Exception as e:
            log.info("Close exception: %s %s", type(e).__name__, e)
    async def send(self, data: bytes):
        async with self.lock:
            try:
                if self.writer is not None:
                    self.writer.write(data)
                    await self.writer.drain()
            except Exception as e:
                log.info("Send exception: %s %s", type(e).__name__, e)
                raise OSError(e)
    async def recv(self, length: int = 0):
        data = b""
        while len(data) < length:
            try:
                chunk = await asyncio.wait_for(
                    self.reader.read(length - len(data)),
                    TCP.TIMEOUT
                )
            except (OSError, asyncio.TimeoutError):
                return None
            else:
                if chunk:
                    data += chunk
                else:
                    return None
        return data