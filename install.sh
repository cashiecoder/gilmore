#!/bin/bash
clear
echo "Updating package lists"
sudo apt update -y

echo "Installing required packages"
sudo apt install -y git python3-pip libdbus-1{,-dev}

echo "Installing required Python modules"
pip install -r requirements.txt

echo "Preparing Raspberry Pi"
sudo raspi-config nonint do_boot_behaviour B2

echo "Installing Bluetooth connection module"
sudo apt purge bluealsa
sudo apt-get install pulseaudio pulseaudio-module-bluetooth
sudo usermod -a -G bluetooth pi

echo "Installing WiFi connection module"
git clone https://github.com/cashiecoder/DragonPi-wifi.git
cd DragonPi-wifi/scripts
sudo ./rpi_headless_wifi_install.sh
sudo reboot

