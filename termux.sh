#!/bin/bash

# Показать баннер
cat ~/Hisa/assets/banner.txt
printf "\n\n\033[1;35mHisa is being installed... ✨\033[0m\n"

# Определение путей
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS_DIR="$SCRIPT_DIR/assets"
TARGET_DIR="/data/data/com.termux/files/usr/lib/python3.12/site-packages"

# Проверка наличия директорий
HAS_HISATL=false
HAS_HISAPYRO=false

[ -d "$TARGET_DIR/hisatl" ] && HAS_HISATL=true
[ -d "$TARGET_DIR/hisapyro" ] && HAS_HISAPYRO=true

# Копирование директорий, если нужно
if [[ "$HAS_HISATL" == true && "$HAS_HISAPYRO" == true ]]; then
    echo "Hisa modules already exist in site-packages."
else
    if [[ "$HAS_HISATL" == true ]]; then
        rm -rf "$TARGET_DIR/hisatl"
    fi
    if [[ "$HAS_HISAPYRO" == true ]]; then
        rm -rf "$TARGET_DIR/hisapyro"
    fi

    cp -r "$ASSETS_DIR/hisatl" "$TARGET_DIR/"
    cp -r "$ASSETS_DIR/hisapyro" "$TARGET_DIR/"

    # Удаляем скопированные папки из assets
    rm -rf "$ASSETS_DIR/hisatl"
    rm -rf "$ASSETS_DIR/hisapyro"
fi

# Установка зависимостей
printf "\n\033[0;34mInstalling requirements...\033[0m\n"
pip install -r requirements.txt --no-cache-dir --no-warn-script-location --disable-pip-version-check --upgrade
printf "\033[0;32mRequirements installed!\033[0m\n"

# Настройка автозапуска (если переменная NO_AUTOSTART не установлена)
if [[ -z "${NO_AUTOSTART}" ]]; then
    printf "\n\033[0;34mConfiguring autostart...\033[0m\n"
    echo '' > ~/../usr/etc/motd
    echo 'clear && cd ~/Hisa && python3 -m hisa' > ~/.bash_profile
    printf "\033[0;32mAutostart enabled!\033[0m\n"
fi

# Запуск Hisa
echo -e "\n\033[0;96mStarting Hisa...\033[0m"
echo -e "\033[2J\033[3;1f"
printf "\033[1;32mHisa is starting...\033[0m\n"
python3 -m hisa
