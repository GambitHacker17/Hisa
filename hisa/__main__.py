import getpass
import os
import subprocess
import sys
from pathlib import Path

assets_path = Path(__file__).parent.parent / 'assets'
if assets_path.exists():
    sys.path.insert(0, str(assets_path))

os.environ["GIT_PYTHON_REFRESH"] = "quiet"

if (
    getpass.getuser() == "root"
    and "--root" not in " ".join(sys.argv)
    and all(trigger not in os.environ for trigger in {"DOCKER", "GOORM"})
):
    print("🚫" * 15)
    print("You attempted to run Hisa on behalf of root user")
    print("Please, create a new user and restart script")
    print("If this action was intentional, pass --root argument instead")
    print("🚫" * 15)
    print()
    print("Type force_insecure to ignore this warning")
    if input("> ").lower() != "force_insecure":
        sys.exit(1)

def deps():
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "-q",
                "--disable-pip-version-check",
                "--no-warn-script-location",
                "-r",
                "requirements.txt",
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)

if sys.version_info < (3, 8, 0):
    print("🚫 Error: you must use at least Python version 3.8.0")
    sys.exit(1)
elif __package__ != "hisa":  
    print("🚫 Error: you cannot run this as a script; you must execute as a package")
    sys.exit(1)
else:
    try:
        from . import log
        log.init()
        from . import main
    except ImportError as e:
        print(f"❌ Import Error: {str(e)}")
        print("🔄 Attempting dependencies installation...")
        deps()

        try:
            from . import log
            log.init()
            from . import main
        except ImportError as e:
            print(f"❌ Still missing dependencies: {str(e)}")
            print("Please install them manually and try again")
            sys.exit(1)
    
    try:
        main.hisa.main()
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        sys.exit(1)