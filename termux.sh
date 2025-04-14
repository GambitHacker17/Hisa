#!/bin/bash

eval "cat ~/Hisa/assets/banner.txt"
printf "\n\n\033[1;35mHisa is being installed... ✨\033[0m"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ASSETS_DIR="$SCRIPT_DIR/assets"

TARGET_DIR="/data/data/com.termux/files/usr/lib/python3.12/site-packages"

HAS_HISATL=false
HAS_HISAPYRO=false

[ -d "$TARGET_DIR/hisatl" ] && HAS_HISATL=true
[ -d "$TARGET_DIR/hisapyro" ] && HAS_HISAPYRO=true

if $HAS_HISATL && $HAS_HISAPYRO; then
    rm -rf "$ASSETS_DIR/hisatl"
    rm -rf "$ASSETS_DIR/hisapyro"
else

    $HAS_HISATL && rm -rf "$TARGET_DIR/hisatl"
    $HAS_HISAPYRO && rm -rf "$TARGET_DIR/hisapyro"

    cp -r "$ASSETS_DIR/hisatl" "$TARGET_DIR/"
    cp -r "$ASSETS_DIR/hisapyro" "$TARGET_DIR/"

    rm -rf "$ASSETS_DIR/hisatl"
    rm -rf "$ASSETS_DIR/hisapyro"

printf "\r\033[0;34mInstalling requirements...\e[0m"

eval "pip install -r requirements.txt --no-cache-dir --no-warn-script-location --disable-pip-version-check --upgrade"

printf "\r\033[K\033[0;32mRequirements installed!\e[0m\n"

if [[ -z "${NO_AUTOSTART}" ]]; then
    printf "\n\r\033[0;34mConfiguring autostart...\e[0m"

    eval "echo '' > ~/../usr/etc/motd &&
    echo 'clear && cd ~/Hisa && python3 -m hisa' > ~/.bash_profile"

    printf "\r\033[K\033[0;32mAutostart enabled!\e[0m\n"
fi

echo -e "\033[0;96mStarting Hisa...\033[0m"
echo -e "\033[2J\033[3;1f"

printf "\033[1;32mHisa is starting...\033[0m\n"

eval "python3 -m hisa"