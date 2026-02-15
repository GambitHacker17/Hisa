#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

IS_TERMUX=false
if [[ -d "/data/data/com.termux" ]] || [[ -n "$PREFIX" ]]; then
    IS_TERMUX=true
fi

progress_bar() {
    local duration=${1:-3}
    local width=50
    local increment=0.06
    local progress=0

    printf "\033[0;34m["
    for ((i=0; i<width; i++)); do
        sleep $increment
        printf "▓"
        progress=$((progress + 2))
        printf "\033[0;34m] %d%%\r" $progress
    done
    printf "\033[0;34m["
    for ((i=0; i<width; i++)); do
        printf "▓"
    done
    printf "] 100%%\033[0m\n"
}

simple_progress() {
    local width=30
    printf "\033[0;34m["
    for ((i=0; i<width; i++)); do
        sleep 0.1
        printf "▓"
    done
    printf "] Done!\033[0m\n"
}

if [[ -f "$SCRIPT_DIR/assets/banner.txt" ]]; then
    cat "$SCRIPT_DIR/assets/banner.txt"
else
    echo "====================================="
    echo "           Hisa Userbot"
    echo "====================================="
fi
printf "\n\n\033[1;35mHisa is being installed... ✨\033[0m\n"

if ! command -v python3 &> /dev/null; then
    echo -e "\033[1;31m✗ Python3 not found. Please install Python 3.8 or higher.\033[0m"
    exit 1
fi

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3,8) else 1)"; then
    PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    echo -e "\033[1;31m✗ Python 3.8+ required, found $PY_VERSION\033[0m"
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo -e "\033[1;33m⚠️  Git not found. Some dependencies may fail to install.\033[0m"
fi

printf "\n\033[0;34mInstalling Python requirements...\033[0m\n"

printf "\033[0;34mProcessing main requirements...\033[0m\n"
simple_progress
pip install -r "$SCRIPT_DIR/requirements.txt" \
    --no-cache-dir \
    --no-warn-script-location \
    --disable-pip-version-check \
    --upgrade > /dev/null 2>&1

printf "\033[0;34mInstalling aiogram...\033[0m\n"
simple_progress
pip install aiogram==2.12 --no-deps > /dev/null 2>&1

printf "\033[0;32m✓ Requirements installed successfully!\033[0m\n"

if [[ "$IS_TERMUX" == true ]] && [[ -z "${NO_AUTOSTART}" ]]; then
    printf "\n\033[0;34mConfiguring autostart for Termux...\033[0m\n"
    simple_progress
    echo '' > ~/../usr/etc/motd 2>/dev/null || true
    echo "clear && termux-wake-lock && cd \"$SCRIPT_DIR\" && python3 -m hisa" > ~/.bash_profile
    printf "\033[0;32m✓ Autostart enabled!\033[0m\n"
fi

echo -e "\n\033[0;96mStarting Hisa...\033[0m"
echo -e "\033[2J\033[3;1f"
printf "\033[1;32mHisa is starting...\033[0m\n"

printf "\033[0;34mFinalizing setup...\033[0m\n"
simple_progress

cd "$SCRIPT_DIR"
python3 -m hisa