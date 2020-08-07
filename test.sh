#!/bin/bash

# the name of this file is test.sh 

# i have found in Linux-Mint the Keyboard menu and there the 'application shortcuts'
# there i used:
# /home/ YOU /Desktop/test.sh with F1

# the same place in different notations:
# C:\users\ YOU \Desktop\test.sh
# /home/ YOU /Desktop/test.sh


cd ~/.wine/drive_c/Program\ Files/AutoHotkey/
# cd ~/.wine/drive_c/Program\ Files/Warcraft3/
# wine WindowSpy.exe -opengl > /dev/null 2> /dev/null & # run W3
# wine AutoHotkey.chm # run W3
# wine WindowSpy.ahk # AutoHotkey

# the same place in different notations:
# C:\users\ YOU \Desktop\sendF1v2.ahk
# /home/ YOU /Desktop/sendF1v2.ahk

# BTW interseting folders:
# /etc/xdg/autostart # folder is common for all users of the operating system
# /home/your user name/.config/autostart


# all of the following working:
# wine AutoHotkey.exe WindowSpy.ahk # this is working
# wine AutoHotkey.exe WindowSpy.ahk -opengl > /dev/null 2> /dev/null &
# wine AutoHotkey.exe sendF1.ahk -opengl > /dev/null 2> /dev/null &
# wine AutoHotkey.exe sendF1v2.ahk -opengl > /dev/null 2> /dev/null &
wine AutoHotkey.exe /home/ YOU /Desktop/sendF1v2.ahk -opengl > /dev/null 2> /dev/null &
# wine  ~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/ YOU /Desktop/sendF1v2.ahk
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
