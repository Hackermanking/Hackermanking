#!/bin/bash

trap 'printf "\n"; stop; exit 1' 2

user_interrupt() {
    printf "\e[0m\n"
    printf "\e[0m\e[1;36m\t CTRL + C Pressé !!\n"
    sleep 2
    printf "\e[0m\n"
    printf " \e[0m\e[1;42m Merci d'utiliser cet outil !!\e[0m  \e[1;44m Visitez https://github.com/htr-tech pour plus d'informations\e[0m\n"
    printf "\e[0m\n"
    exit 1
}

trap user_interrupt SIGINT
trap user_interrupt SIGTSTP

stop() {
    checkngrok=$(ps aux | grep -o "ngrok" | head -n1)
    checkphp=$(ps aux | grep -o "php" | head -n1)
    checkssh=$(ps aux | grep -o "ssh" | head -n1)

    if [[ $checkngrok == *'ngrok'* ]]; then
        pkill -f -2 ngrok > /dev/null 2>&1
        killall ngrok > /dev/null 2>&1
    fi
    if [[ $checkphp == *'php'* ]]; then
        pkill -f -2 php > /dev/null 2>&1
        killall php > /dev/null 2>&1
    fi
    if [[ $checkssh == *'ssh'* ]]; then
        pkill -f -2 ssh > /dev/null 2>&1
        killall ssh > /dev/null 2>&1
    fi
    if [[ -e .nexlink ]]; then
        rm -rf .nexlink
    fi
}

reqs() {
    command -v php > /dev/null 2>&1 || { printf "\n\e[0m\e[96m Les packages ne sont pas installés ! Tapez \e[0m\e[93mbash setup\e[0m\n\n"; exit 1; }
    command -v curl > /dev/null 2>&1 || { printf "\n\e[0m\e[96m Les packages ne sont pas installés ! Tapez \e[0m\e[93mbash setup\e[0m\n\n"; exit 1; }
    command -v ssh > /dev/null 2>&1 || { printf "\n\e[0m\e[96m Les packages ne sont pas installés ! Tapez \e[0m\e[93mbash setup\e[0m\n\n"; exit 1; }
    command -v unzip > /dev/null 2>&1 || { printf "\n\e[0m\e[96m Les packages ne sont pas installés ! Tapez \e[0m\e[93mbash setup\e[0m\n\n"; exit 1; }

    if [[ -d .htr ]]; then
        printf ""
    else
        printf "\n\e[0m\e[96m Les packages ne sont pas trouvés ! Tapez \e[0m\e[93mbash setup\e[0m\n\n"
        exit 1 
    fi

    if [[ -d .Modules ]]; then
        printf ""
    else
        printf "\n\e[0m\e[96m Les packages ne sont pas trouvés ! Tapez \e[0m\e[93mbash setup\e[0m\n\n"
        exit 1 
    fi

    if [[ -d .htr/www ]]; then
        rm -rf .htr/www
        mkdir .htr/www
    else
        mkdir .htr/www
    fi
}

banner() {
    clear
    printf "\e[0m\n"
    printf "\e[0m\e[92m  _   _            \e[0m\e[93m _____  _     _     _                \e[0m\n"
    printf "\e[0m\e[92m | \ | |           \e[0m\e[93m|  __ \| |   (_)   | |               \e[0m\n"
    printf "\e[0m\e[92m |  \| | _____  __ \e[0m\e[93m| |__) | |__  _ ___| |__   ___ _ __  \e[0m\n"
    printf "\e[0m\e[92m | .   |/ _ \ \/ / \e[0m\e[93m|  ___/|  _ \| / __|  _ \ / _ \  __| \e[0m\n"
    printf "\e[0m\e[92m | |\  |  __/>  <  \e[0m\e[93m| |    | | | | \__ \ | | |  __/ |    \e[0m\n"
    printf "\e[0m\e[92m |_|  |_|\___/_/\_\ \e[0m\e[93m|_|    |_| |_|_|___/_| |_|\___|_|    \e[0m\n"
    printf "\e[0m\n"
}

banner