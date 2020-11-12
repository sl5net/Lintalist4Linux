A few notes on installation. They'll help if things don't go quite smoothly for you. The notes have more of the character of a card box at the moment.
The part of the shell script that sometimes doesn't work properly is near the end. Below is the one-liner from the reame a bit disassembled. So much more understandable.
( 12.11.2020 )

following used in [0.990](https://github.com/sl5net/Lintalist4Linux/releases/tag/0.990) :
```
sudo apt -y install autokey-qt ; echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########" ; autokey-qt & sleep 3s ; killall -9 autokey-qt ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cd ~/.config/autokey/data/Sample\ Scripts/ ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ./ ; cp ~/Downloads/Lintalist4Linux/.run-run-lintalistAHK-all.json ./ ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ./ ; cp ~/Downloads/Lintalist4Linux/configParser-set-ini-defaults.ahk ./ ; cp ~/Downloads/Lintalist4Linux/configParser-set-defaults.py ./ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; python3 ~/.config/autokey/data/Sample\ Scripts/configParser-set-defaults.py & 
```

- *autokey-qt* install only errors visible:
	- sudo apt -y install autokey-qt  >/dev/null 2>/dev/null ;
		- (BTW sudo apt-get remove autokey-qt )

	all of the following producing some 5 ugly error lines (i just ignored that). i take the last one:
	- 1 autokey-qt & sleep 3s ; killall -3 autokey-qt >/dev/null 2>/dev/null ; 
	- 2 autokey-qt > /dev/null & sleep 1s ; clear ; killall -3 autokey-qt ; 
	- 3 autokey-qt & sleep 1s ; clear ; killall -3 autokey-qt ; 

	- sudo apt -y install git ;
	- BTW just one line: sudo apt -y install git > /dev/null ;
- *git clones*:
 - mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; git clone https://github.com/sl5net/Lintalist4Linux ; cd ~/.config/autokey/data/Sample\ Scripts/ ; 
 - cd ~/Downloads/ ; 
 	- cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ./ & cp ~/Downloads/Lintalist4Linux/.run-run-lintalistAHK-all.json ./ & cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ./ & cp ~/Downloads/Lintalist4Linux/configParser-set-ini-defaults.ahk ./ & cp ~/Downloads/Lintalist4Linux/configParser-set-defaults.py ./ ; 
- *winehq*:
	- *winehq downloads:*
		- sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; 
	- *winehq install:*
			- sudo apt update && sudo apt -y install --install-recommends winehq-stable ; 
	- *AutohotKey:* Really need sudo!!! installing Autohotkey
		- wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; autokey-run --script ifWineWin-sendEnter ; sudo wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe  >/dev/null 2>/dev/null ;  
		- BTW AutoHotkey_1.1.33.02_setup.exe  shows many ERROR not pretty and usfull. dont want see it. ... >/dev/null 2>/dev/null

######### hera are problems with lintalist. becouse ^--- Autohotkey not correct installed.

	- python3 ~/.config/autokey/data/Sample\ Scripts/configParser-set-defaults.py
	- ============> wine: cannot find '/home/m/.wine/drive_c/Program Files/AutoHotkey/AutoHotkey.exe'

suppress all output not error messages (the first may not work in all shells):
scriptname >/dev/null 2>/dev/null
https://stackoverflow.com/a/617184/2891692