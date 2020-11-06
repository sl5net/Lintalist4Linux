#!/bin/bash
# Start it for e.g. so:
#/‾‾‾ problems installing autohokey using this line
# clear ; cd /tmp ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ;    sudo chmod +wx ./install.sh ; ./install.sh ; rm ./install.sh ;
#/‾‾‾ no problems # chmod +rwx
# clear ; cd /tmp ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ;    sudo chmod 777 ./install.sh ; ./install.sh ; rm ./install.sh ;
#/‾‾‾ no problems bash: ./install.sh: Permission denied
# clear ; sudo wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ~/Downloads/install.sh ; cd ~/Downloads ; sudo chmod 750 ./install.sh ; ./install.sh
#/‾‾‾ solution without sh-script
# sudo apt -y install autokey-qt ; echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########" ; autokey-qt & sleep 3s ; killall -9 autokey-qt ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ; ~/.config/autokey/data/Sample\ Scripts/ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; autokey-qt;

# https://stackoverflow.com/a/20538015/2891692

sudo apt -y install autokey-qt ; autokey-qt & sleep 3s ; killall -9 autokey-qt
# echo -e "\ņ Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. #########"
sudo apt -y install git || exit
mkdir ~/ahk ;
mkdir ~/ahk/github ;
cd ~/ahk/github || exit ;
git clone https://github.com/lintalist/lintalist ;
# ~/ahk/github/lintalist ;
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
wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe

# wine AutoHotkey.exe /home/administrator/Documents/github/Lintalist4Linux/run-lintalistAHK.ahk -opengl > /dev/null 2> /dev/null &
#wine AutoHotkey.exe ~/ahk/github/lintalist/lintalist.ahk -opengl > /dev/null 2> /dev/null &
#cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe WindowSpy.ahk -opengl > /dev/null 2> /dev/null &
cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe ~/.config/autokey/data/Sample\ Scripts/ConfigParser-set-ini-defaults.ahk -opengl > /dev/null 2> /dev/null &
cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe ~/ahk/github/lintalist/lintalist.ahk -opengl > /dev/null 2> /dev/null &
sleep 1s;

# sleep 3s ; killall -9 lintalist
# wine AutoHotkey.exe ~/.config/autokey/data/Sample\ Scripts/ConfigParser-set-ini-defaults.ahk
#cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe ~/.config/autokey/data/Sample\ Scripts/ConfigParser-set-ini-defaults.ahk -opengl > /dev/null 2> /dev/null &
echo -e "\n\nPlease Configure AutohotKey and AutoKey\n\n"
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
# ~/.config/autokey/data/Sample Scripts/.run-run-lintalistAHK-all.json

