import asyncio
import atexit
import logging
import os
import random
import signal
import sys

async def fw_protect():
    await asyncio.sleep(random.randint(1000, 3000) / 1000)

def get_startup_callback() -> callable:
    return lambda *_: os.execl(
        sys.executable,
        sys.executable,
        "-m",
        os.path.relpath(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))),
        *sys.argv[1:],
    )

def die():
    if "DOCKER" in os.environ:
        sys.exit(0)
    else:
        os.killpg(os.getpgid(os.getpid()), signal.SIGTERM)

def restart():
    logging.getLogger().setLevel(logging.CRITICAL)
    print("🔄 Restarting...")

    if "LAVHOST" in os.environ:
        os.system("lavhost restart")
        return

    if "DOCKER" in os.environ:
        atexit.register(get_startup_callback())
        return

    if "TERMUX" in os.environ:
        os.execv(sys.executable, [sys.executable] + sys.argv)

    signal.signal(signal.SIGTERM, get_startup_callback())
    die()

def print_banner(banner: str):
    print("\033[2J\033[3;1f")
    with open(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "assets",
                banner,
            )
        ),
        "r",
    ) as f:
        print(f.read())