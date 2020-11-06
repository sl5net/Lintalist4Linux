#!/bin/bash
# Start it for e.g. so:
# clear ; cd /tmp ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ; ./install.sh ; rm ./install.sh ;
# clear ; sudo wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ~/Downloads/install.sh ; cd ~/Downloads ; sudo chmod 750 ./install.sh ; ./install.sh
# sudo apt -y install autokey-qt ; echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########" ; autokey-qt & sleep 3s ; killall -9 autokey-qt ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ; ~/.config/autokey/data/Sample\ Scripts/ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; autokey-qt;
sudo apt -y install autokey-qt ; autokey-qt & sleep 3s ; killall -9 autokey-qt
echo "########## Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. #########"
sudo apt -y install git || exit
mkdir ~/ahk ;
mkdir ~/ahk/github ;
cd ~/ahk/github || exit ;
git clone https://github.com/lintalist/lintalist ;
cd ~/Downloads || exit ;
git clone https://github.com/sl5net/Lintalist4Linux ;
cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ~/.config/autokey/data/Sample\ Scripts/ ;
cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ~/.config/autokey/data/Sample\ Scripts/ ;
cp ~/Downloads/Lintalist4Linux/ConfigParser-set-ini-defaults.ahk ~/.config/autokey/data/Sample\ Scripts/ConfigParser-set-ini-defaults.ahk ;
sudo apt update ;
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key ;
sudo apt-key add winehq.key
sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport
sudo apt update && sudo apt -y install --install-recommends winehq-stable
wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; wine ~/.config/autokey/data/Sample\ Scripts/ConfigParser-set-ini-defaults.ahk
echo "Please Configure AutohotKey and AutoKey"
autokey-qt


#sudo apt -y install autokey-qt
#echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########"
#autokey-qt & sleep 3s
#killall -9 autokey-qt
#sudo apt -y install git
#mkdir ~/ahk
#mkdir ~/ahk/github
#cd ~/ahk/github/
#git clone https://github.com/lintalist/lintalist
#cd ~/Downloads/
#git clone https://github.com/sl5net/Lintalist4Linux
#cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py
#cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk
#~/.config/autokey/data/Sample\ Scripts/
#sudo dpkg --add-architecture i386
#wget -nc https://dl.winehq.org/wine-builds/winehq.key
#sudo apt-key add winehq.key
#sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
#sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport
#sudo apt update && sudo apt -y install --install-recommends winehq-stable
#wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/
#wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe
#echo "Please Configure AutohotKey and AutoKey"
#autokey-qt
#
