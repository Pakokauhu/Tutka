#!/usr/bin/env bash

LOG_DIR=$PWD/logs
DB_DIR=$PWD/db
ILOG=$LOG_DIR/asennus.log

mkdir -p $LOG_DIR $DB_DIR

tilan_tarkistus() {
    if [ $? -eq 0 ]
    then
        echo -e "$1 - Asennettu"
    else
        echo -e "$1 - Epäonnistui!"
    fi
}

debian_asennus() {
    echo -e '=====================\nASENNETAAN DEBIANILLE\n=====================\n' > "$ILOG"

    pkgs="python3 python3-pip python3-requests python3-packaging python3-psutil php"

    asenna_cmd() {
        echo -ne '$1\r'
        sudo apt -y install $1 &>> "$ILOG"
        tilan_tarkistus $1
        echo -e '\n--------------------\n' >> "$ILOG"
    }

    for pkg_name in $pkgs; do
        asenna_cmd $pkg_name
    done
}

fedora_asennus() {
    echo -e '=====================\nASENNETAAN FEDORALLE\n=====================\n' > "$ILOG"

    pkgs="python3 python3-pip python3-requests python3-packaging python3-psutil php"

    asenna_cmd() {
        echo -ne "$1\r"
        sudo dnf install $1 -y &>> "$ILOG"
        tilan_tarkistus $1
        echo -e '\n--------------------\n' >> "$ILOG"
    }

    for pkg_name in $pkgs; do
        asenna_cmd $pkg_name
    done
}

termux_asennus() {
    echo -e '=====================\nASENNETAAN TERMUXILLE\n=====================\n' > "$ILOG"

    pkgs="python php"
    pip_pkgs="requests packaging psutil"

    asenna_cmd() {
        echo -ne "$1\r"
        apt -y install $1 &>> "$ILOG"
        tilan_tarkistus $1
        echo -e '\n--------------------\n' >> "$ILOG"
    }

    asenna_pip() {
        echo -ne "$1\r"
        pip install -U $1 &>> "$ILOG"
        tilan_tarkistus $1
        echo -e '\n--------------------\n' >> "$ILOG"
    }

    for pkg_name in $pkgs; do
        asenna_cmd $pkg_name
    done

    for pkg_name in $pip_pkgs; do
        asenna_pip $pkg_name
    done
}

arch_asennus() {
    echo -e '=========================\nASENNETAAN ARCH LINUXILLE\n=========================\n' > "$ILOG"

    asenna_cmd() {
        echo -ne "$1\r"
        yes | sudo pacman -S $1 --needed &>> "$ILOG"
        tilan_tarkistus $1
        echo -e '\n--------------------\n' >> "$ILOG"
    }

    pkgs="python3 python-pip python-requests python-packaging python-psutil php"

    for pkg_name in $pkgs; do
        asenna_cmd $pkg_name
    done
}

echo -e '[!] Asennetaan riippuvuuksia...\n'

if [ -f '/etc/arch-release' ]; then
    arch_asennus
elif [ -f '/etc/fedora-release' ]; then
    fedora_asennus
else
    if [ -z "${TERMUX_VERSION}" ]; then
        debian_asennus
    else
        termux_asennus
    fi
fi

echo -e '=========\nVALMIS\n=========\n' >> "$ILOG"

echo -e '\n[+] Lokitiedosto tallennettu :' "$ILOG"
