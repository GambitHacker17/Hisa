#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="/data/data/com.termux/files/usr/lib/python3.12/site-packages"
GITHUB_REPO="https://github.com/GambitHacker17/Hisa"
BRANCH="Master"

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

cat "$SCRIPT_DIR/assets/banner.txt"
printf "\n\n\033[1;35mHisa is being installed... ✨\033[0m\n"

download_hisatl() {
    printf "\n\033[0;34mStarting download process...\033[0m\n"

    TEMP_DIR="/data/data/com.termux/files/usr/tmp/hisa_temp"
    mkdir -p "$TEMP_DIR"

    printf "\033[0;34mConnecting to GitHub...\033[0m\n"
    progress_bar 1

    if git clone --branch "$BRANCH" --depth 1 "$GITHUB_REPO" "$TEMP_DIR" 2>/dev/null; then
        printf "\033[0;32m✓ Repository cloned successfully\033[0m\n"
        printf "\033[0;34mCopying library files...\033[0m\n"
        simple_progress

        if [ -d "$TEMP_DIR/libs/hisatl" ]; then
            cp -r "$TEMP_DIR/libs/hisatl" "$TARGET_DIR/"
            printf "\033[0;32m✓ Library files copied successfully\033[0m\n"
        else
            printf "\033[1;31m✗ Error: hisatl directory not found\033[0m\n"
            rm -rf "$TEMP_DIR"
            return 1
        fi

        printf "\033[0;34mCleaning up...\033[0m\n"
        sleep 1
        rm -rf "$TEMP_DIR"

        return 0
    else
        printf "\033[1;31m✗ Error: Failed to clone repository\033[0m\n"
        rm -rf "$TEMP_DIR"
        return 1
    fi
}

if [ -d "$TARGET_DIR/hisatl" ]; then
    echo "Hisa module already exists in site-packages"

    printf "\033[1;33mDo you want to replace the existing library? (y/N): \033[0m"
    read -r response

    if [[ "$response" =~ ^[Yy]$ ]]; then
        printf "\033[0;34mRemoving old library...\033[0m\n"
        simple_progress
        rm -rf "$TARGET_DIR/hisatl"

        if download_hisatl; then
            printf "\033[0;32m✓ Library replaced successfully!\033[0m\n"
        else
            printf "\033[1;31m✗ Failed to download new library. Continuing with existing one.\033[0m\n"
        fi
    else
        printf "\033[0;32m✓ Keeping existing library. Continuing...\033[0m\n"
    fi
else
    if download_hisatl; then
        printf "\033[0;32m✓ Library installed successfully!\033[0m\n"
    else
        printf "\033[1;31m✗ Failed to download library. Creating basic structure...\033[0m\n"

        printf "\033[0;34mCreating basic structure...\033[0m\n"
        simple_progress

        mkdir -p "$TARGET_DIR/hisatl"
        cat > "$TARGET_DIR/hisatl/__init__.py" << 'EOF'
"""
hisatl - Basic Hisa Telegram Library
This is a fallback version. Some features may be limited.
"""
__version__ = "1.0.0-fallback"
EOF
        printf "\033[0;33m✓ Basic library structure created. Some features may not work.\033[0m\n"
    fi
fi

printf "\n\033[0;34mInstalling Python requirements...\033[0m\n"

printf "\033[0;34mProcessing main requirements...\033[0m\n"
simple_progress
pip install -r "$SCRIPT_DIR/requirements.txt" --no-cache-dir --no-warn-script-location --disable-pip-version-check --upgrade > /dev/null 2>&1

printf "\033[0;34mInstalling aiogram...\033[0m\n"
simple_progress
pip install aiogram==2.12 --no-deps > /dev/null 2>&1

printf "\033[0;32m✓ Requirements installed successfully!\033[0m\n"

if [[ -z "${NO_AUTOSTART}" ]]; then
    printf "\n\033[0;34mConfiguring autostart...\033[0m\n"
    simple_progress
    echo '' > ~/../usr/etc/motd
    echo "clear && termux-wake-lock && cd \"$SCRIPT_DIR\" && python3 -m hisa" > ~/.bash_profile
    printf "\033[0;32m✓ Autostart enabled!\033[0m\n"
fi

echo -e "\n\033[0;96mStarting Hisa...\033[0m"
echo -e "\033[2J\033[3;1f"
printf "\033[1;32mHisa is starting...\033[0m\n"

printf "\033[0;34mFinalizing setup...\033[0m\n"
simple_progress

python3 -m hisa