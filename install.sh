#!/bin/bash
echo "########## \n Please Exit AutohotKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########"
autokey-qt & sleep 3s ; killall -9 autokey-qt
sudo apt -y install git
mkdir ~/ahk
mkdir ~/ahk/github
cd ~/ahk/github
git clone https://github.com/lintalist/lintalist
cd ~/Downloads
git clone https://github.com/sl5net/Lintalist4Linux
cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py
cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk
~/.config/autokey/data/Sample\ Scripts/
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport
sudo apt update && sudo apt -y install --install-recommends winehq-stable
wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/
wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe
echo "Please Configure AutohotKey and AutoKey"
autokey-qt

# ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ; ~/.config/autokey/data/Sample\ Scripts/ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; autokey-qt;






# from http://ubuntuhandbook.org/index.php/2020/01/install-wine-5-0-stable-ubuntu-18-04-19-10/
# all for your one risk. like everytime
# all for your one risk. like everytime

#dpkg --add-architecture i386
#wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key
#sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
#sudo add-apt-repository ppa:cybermax-dexter/sdl2-backport
#sudo apt update && sudo apt install --install-recommends winehq-stable
