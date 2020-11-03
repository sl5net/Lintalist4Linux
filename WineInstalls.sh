#!/usr/bin/env  sh

# from http://ubuntuhandbook.org/index.php/2020/01/install-wine-5-0-stable-ubuntu-18-04-19-10/
# all for your one risk. like everytime
# all for your one risk. like everytime

dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
sudo add-apt-repository ppa:cybermax-dexter/sdl2-backport
sudo apt update && sudo apt install --install-recommends winehq-stable
