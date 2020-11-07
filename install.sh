#!/bin/bash
# Start it for e.g. so:
#/‾‾‾ problems installing autohokey using this line
# clear ; cd /tmp ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ;    sudo chmod +wx ./install.sh ; ./install.sh ; rm ./install.sh ;

#/‾‾‾ no problems # chmod +rwx :))))
# clear ; cd /tmp ; rm ./install.sh ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ;    sudo chmod 777 ./install.sh ; ./install.sh ; rm ./install.sh ;
#/‾‾‾ no problems bash: ./install.sh: Permission denied
# clear ; sudo wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ~/Downloads/install.sh ; cd ~/Downloads ; sudo chmod 750 ./install.sh ; ./install.sh
#/‾‾‾ solution without sh-script
# sudo apt -y install autokey-qt ; echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########" ; autokey-qt & sleep 3s ; killall -9 autokey-qt ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ; ~/.config/autokey/data/Sample\ Scripts/ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; autokey-qt;

# https://stackoverflow.com/a/20538015/2891692

echo -e "\n\n install autokey-qt \n"
sudo apt -y install autokey-qt > /dev/null
autokey-qt > /dev/null & sleep 3s ; killall -9 autokey-qt
echo - "\n\n installs now AutoKey AutoHotKey wine Lintalist4Linux #########\n\n"

# clear ; cd /tmp ; rm ./install.sh ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ; sudo chmod +rwx ./install.sh ; ./install.sh ; rm ./install.sh ;
echo -e "\n\n install git \n"
sudo apt -y install git || exit

echo -e "\n\n Downloads \n"
mkdir ~/ahk ;
mkdir ~/ahk/github ;
cd ~/ahk/github || exit ;
git clone https://github.com/lintalist/lintalist ;
# ~/ahk/github/lintalist ;
cd ~/Downloads || exit ;
git clone https://github.com/sl5net/Lintalist4Linux ;
cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ~/.config/autokey/data/Sample\ Scripts/ ;
cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ~/.config/autokey/data/Sample\ Scripts/ ;
cp ~/Downloads/Lintalist4Linux/ConfigParser-set-ini-defaults.ahk ~/.config/autokey/data/Sample\ Scripts/configParser-set-ini-defaults.ahk ;

echo -e "\n\n wine \n"
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key ;
sudo apt-key add winehq.key
sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'
sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport
sudo apt update && sudo apt -y install --install-recommends winehq-stable 2> /dev/null

echo -e "\n\n apt update \n"
#sudo apt update
sudo apt -y upgrade

# Autohotkey # clear # AutoHotkey_1.1.33.02_setup.exe
echo -e "\n\n wine ./ahk-install.exe \n"
cd ~/Downloads || exit ;
wget https://www.autohotkey.com/download/ahk-install.exe ;
cd ~/Downloads || exit ;
sudo wine ./ahk-install.exe
sleep 3s;

# wine AutoHotkey.exe /home/administrator/Documents/github/Lintalist4Linux/run-lintalistAHK.ahk -opengl > /dev/null 2> /dev/null &
#wine AutoHotkey.exe ~/ahk/github/lintalist/lintalist.ahk -opengl > /dev/null 2> /dev/null &
#cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe WindowSpy.ahk -opengl > /dev/null 2> /dev/null &

# https://askubuntu.com/questions/350208/what-does-2-dev-null-mean
# /dev/null is the null device it takes any input you want and throws it away. It can be used to suppress any output.
# & detaches app from the shell.
echo -e "\n\n ConfigParser-set-ini-defaults.ahk \n"
cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe ~/.config/autokey/data/Sample\ Scripts/ConfigParser-set-ini-defaults.ahk -opengl > /dev/null 2> /dev/null


echo -e "\n\n#/‾‾‾ lintalist.ahk \n"
sleep 1s;
cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe ~/ahk/github/lintalist/lintalist.ahk -opengl > /dev/null 2> /dev/null &
sleep 1s;
echo -e "\n works tested"
echo -e "\n\n#\\___ lintalist.ahk \n"

#sleep 10s;
python3 ~/.config/autokey/data/Sample\ Scripts/configParser-set-defaults.py
echo -e "\n\nPlease Configure AutoKey (and Lintalist later)\n\n"
autokey-qt > /dev/null &
