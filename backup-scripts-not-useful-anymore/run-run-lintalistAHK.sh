#!/bin/bash
# Start it for e.g. so:
#/‾‾‾ problems installing autohokey using this line
# clear ; cd /tmp ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ;    sudo chmod +wx ./install.sh ; ./install.sh ; rm ./install.sh ;
#/‾‾‾ no problems # chmod +rwx
# clear ; cd /tmp ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ;    sudo chmod 777 ./install.sh ; ./install.sh ; rm ./install.sh ;
#/‾‾‾ no problems bash: ./install.sh: Permission denied
# clear ; sudo wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ~/Downloads/install.sh ; cd ~/Downloads ; sudo chmod 750 ./install.sh ; ./install.sh
#/‾‾‾ solution without sh-script
# sudo apt -y install autokey-qt ; echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#/‾‾‾" ; autokey-qt & sleep 3s ; killall -9 autokey-qt ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ; ~/.config/autokey/data/Sample\ Scripts/ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; autokey-qt;

# https://stackoverflow.com/a/20538015/2891692
















#!/bin/bash

# the name of this file is test.sh 
#  /home/administrator/.config/espanso/default.yml

# i have found in Linux-Mint the Keyboard menu and there the 'application shortcuts'
# there i used:
# /home/administrator/Desktop/test.sh with F1

# the same place in different notations:
# C:\users\administrator\Desktop\test.sh
# /home/administrator/Desktop/test.sh

# cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe WindowSpy.ahk -opengl > /dev/null 2> /dev/null &

cd ~/.wine/drive_c/Program\ Files/AutoHotkey/
# cd ~/.wine/drive_c/Program\ Files/Warcraft3/
# wine WindowSpy.exe -opengl > /dev/null 2> /dev/null & # run W3
# wine AutoHotkey.chm # run W3
# wine WindowSpy.ahk # AutoHotkey

# the same place in different notations:
# C:\users\administrator\Desktop\sendF1v2.ahk
# /home/administrator/Desktop/sendF1v2.ahk

# BTW interseting folders:
# /etc/xdg/autostart # folder is common for all users of the operating system
# /home/your user name/.config/autostart


# all of the following working:
# wine AutoHotkey.exe WindowSpy.ahk # this is working
# wine AutoHotkey.exe WindowSpy.ahk -opengl > /dev/null 2> /dev/null &
# wine AutoHotkey.exe sendF1.ahk -opengl > /dev/null 2> /dev/null &
# wine AutoHotkey.exe sendF1v2.ahk -opengl > /dev/null 2> /dev/null &
wine AutoHotkey.exe /home/administrator/Documents/github/Lintalist4Linux/run-lintalistAHK.ahk -opengl > /dev/null 2> /dev/null &
# wine  ~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Desktop/sendF1v2.ahk
# wine AutoHotkey.exe sendF1v2.ahk

# sleep 2500; # wait until animation fades out
# xvkbd -text "b" # "b" is for Battle.net
# sleep 7;
# xvkbd -text "password\r" # password
# sleep 3;
# xvkbd -text "h" # "h" is for channel
# sleep 5;
# xvkbd -text "h" # honestly I don't know why, but without this the script might not work
# sleep 5;
# xvkbd -text "zcu\r" # type in your channel and join the room
# sleep 5;
# xvkbd -text ".load\r" # I'm using ghost, so I'll ask him what map is loaded
