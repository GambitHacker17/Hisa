#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS_DIR="$SCRIPT_DIR/assets"
VENV_DIR="$SCRIPT_DIR/venv"
TARGET_DIR="$VENV_DIR/lib/python$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')/site-packages"

if [ -f "$ASSETS_DIR/banner.txt" ]; then
    cat "$ASSETS_DIR/banner.txt"
    printf "\n\n\033[1;35mУстановка Hisa... ✨\033[0m\n"
fi

if [ ! -d "$VENV_DIR" ]; then
    printf "\033[0;34mСоздание виртуального окружения...\033[0m\n"
    python3 -m venv "$VENV_DIR" || {
        echo "❌ Ошибка создания виртуального окружения"
        exit 1
    }
    printf "\033[0;32mВиртуальное окружение создано!\033[0m\n"
fi

source "$VENV_DIR/bin/activate" || {
    echo "❌ Ошибка активации виртуального окружения"
    exit 1
}

MODULES=("hisatl" "hisapyro")
for module in "${MODULES[@]}"; do
    if [ -d "$ASSETS_DIR/$module" ]; then
        printf "\n\033[0;34mУстановка модуля $module...\033[0m\n"
        [ -d "$TARGET_DIR/$module" ] && rm -rf "$TARGET_DIR/$module"
        cp -r "$ASSETS_DIR/$module" "$TARGET_DIR/" || {
            echo "❌ Ошибка копирования модуля $module"
            exit 1
        }
        rm -rf "$ASSETS_DIR/$module"
        printf "\033[0;32mМодуль $module установлен!\033[0m\n"
    fi
done

printf "\n\033[0;34mУстановка зависимостей...\033[0m\n"
pip install --upgrade pip || {
    echo "❌ Ошибка обновления pip"
    exit 1
}

pip install -r "$SCRIPT_DIR/requirements.txt" \
    --no-cache-dir \
    --no-warn-script-location \
    --disable-pip-version-check || {
    echo "❌ Ошибка установки зависимостей"
    exit 1
}

pip install aiogram==2.12 --no-deps || {
    echo "❌ Ошибка установки aiogram"
    exit 1
}
printf "\033[0;32mЗависимости установлены!\033[0m\n"

if [[ -z "${NO_AUTOSTART}" ]]; then
    printf "\n\033[0;34mНастройка автозапуска...\033[0m\n"
    [ -f ~/../usr/etc/motd ] && echo '' > ~/../usr/etc/motd
    echo "clear && cd \"$SCRIPT_DIR\" && source \"$VENV_DIR/bin/activate\" && python3 -m hisa" > ~/.bash_profile
    printf "\033[0;32mАвтозапуск настроен!\033[0m\n"
fi

printf "\n\033[0;96mЗапуск Hisa...\033[0m\n"
echo -e "\033[2J\033[3;1f"
printf "\033[1;32mHisa запускается...\033[0m\n"
python3 -m hisa

deactivate