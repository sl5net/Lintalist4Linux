# Lintalist4Linux

Linux and Windows -platform **Text Replacer/Adder/Scripter** written in AutoKey/Phyton and AutoHotKey with the Help from Lintalist  

## How it works
1. The Add-Text-Method: 
    1. set your cursor (looks like `|`) **behind a word** (example: `phone`) in your text.<br> 
Example: `phone|` or `address|`, `email|`, `now|`, `date|` etc. Or use [autohotkey commands](https://www.autohotkey.com/docs/commands/FormatTime.htm)
    1. Press key combination (please configure. recommended `F12`)
    - [x] The database opens and **searches** for results for your search term (e.g. `phone`)
     and lists all matching results. <br>
    - [x] With the Enter key, your selection is placed after your search term and saved in the clipboard.
1. The Replace-Text-Method (its when you using your text after the “:” character (and then press shortcut `F12`): 
    - [x] `:keyword` **replaces** text with result (if many it opens menu) and save in clipboard
    - without text: 
        - [x] `:` and press `F12` writes out your clipboard content
        - [x] `²` and press `F12` writes out your clipboard 2 times. separated with tab-key

More explanation:
- Where can I use that, type the text?
    - All over. On websites in a chat, in the console. All over.
- you don't need write the complete keyword. e.g. writing `address|` or `addr|`  `adr|` or `ad|` is may enough if you use fuzzy search.
- scripting with [... autohotkey commands](https://www.autohotkey.com/docs/commands/FormatTime.htm): 
    - for example `:date` and replaces it with `20.08.2020`
    - for example `:now` and replaces it with `20.08.2020 16:48:24`
- If you want many Results for one keyword the Lintalist-Menu ⇶ is opening before (see more in Lintalist-Configuration about AutoExecuteOnce)
- You always also have the result in your clipboard.
- In some cases (e.g. if you simple want send your clipboard) it is not using  `ctrl` + `v` method intern. it`is writing it, not pasting it.

### For just simple replacements you like maybe:

#### Using only simple replacements in its app:
Telegram [telegram.org](telegram.org) or [element.io](https://element.io/) Chat emoji codes.<br> 
For e.g. `:smiley:` or `:-)` More examples: [telegram-emoji-list-codes-descriptions/](https://k3a.me/telegram-emoji-list-codes-descriptions/)

#### Using only simple replacements everywhere:
Maybe you want to install the following at the same time, as a supplement: [espanso.org](https://espanso.org/)

#### Using simple and complex replacements everywhere:

[lintalist.github.io](https://lintalist.github.io/)  says (10.08.2020):<br>
"Lintalist allows you to store and (incrementally) search <br>
and edit texts in bundles and paste a selected text in your active program.<br>
... Lintalist is open source and developed in AutoHotkey ..."
<br><br>
if you want see how it works while it works open the config file and set:
`doPopupNotify_howItWorks = True`



# installation step by step:

Tested with the following recommended installation:

1. [LinuxMint](https://linuxmint.com/edition.php?id=283) at 2019 (tested with "Linux Mint 20 Ulyana - ******Xfce****** (64-bit)" may works with other Linux OS or Window OS)
1. Ubuntu-minimal in Virtualbox at 20.08.2020<br>
needs **minimum 12 GB** Hard Disk. Use RAM more then 4 GB. Maybe RAM 6GB ( 20-08-27 18:33:08 )<br> 
https://youtu.be/XtV0OQmUYy8 at 27.08.2020
1. KDEneon (User Edition 64bit) at 24.09.2020<br>
needs winetricks. Looks great but AutoKey missing some functionality.
⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠ Important: autokey "will not function 100% on distributions that default to using Wayland (like KDE) instead of Xorg."
1. [Kubuntu 20.10](https://kubuntu.org/getkubuntu/) at 03.11.2020 (******KDE Desktop****** (64-bit)" may works with other Linux OS or Window OS)

You need maybe Linux, maybe kubuntu, maybe with KDE Desktop.

1. install Wine like here:
<br>⚠⚠ i got error message installing Wine at Linux Ubuntu and installing wine in Linux Mint:
This helps me: 
<br>[http://ubuntuhandbook.org/index.php/2020/01/install-wine-5-0-stable-ubuntu-18-04-19-10/](http://ubuntuhandbook.org/index.php/2020/01/install-wine-5-0-stable-ubuntu-18-04-19-10/)
1. install [AutoHotKey.com](https://www.autohotkey.com/download/ahk-install.exe)
1. install [AutoKey](https://github.com/autokey/autokey#installation) (or may use your Software Manager )
1. start AutoKey GUI
1. close AutoKey GUI (a folder may not be created until Autokey is started for the first time))
1. extract [master.zip from Lintalist4Linux](https://github.com/sl5net/Lintalist4Linux/archive/master.zip) to<br>
~/.config/autokey/data/Sample Scripts/
1. extract [lintalist.zip from lintalist.github.io](https://github.com/lintalist/lintalist/releases/download/v1.9.13/lintalist.zip) to<br>
~/ahk/github/lintalist
1. set in lintalist.ahk the Hotkey QuickSearchHotkey <kbd>F11</kbd>
1. set in AutoKey the Hotkey -run-lintalistAHK-all.py to for e.g. <kbd>F12</kbd>


# installation using just one line:

[recommended](https://github.com/autokey/autokey/wiki/Installing): 

1. for systems using a **Qt**-based desktop environment such as **KDE Plasma**, **Lumina**, etc.


following used in [0.990](https://github.com/sl5net/Lintalist4Linux/releases/tag/0.990) :
```
sudo apt -y install autokey-qt ; echo "########## \n Please Exit AutoKey (right Click Taskbar on little Icon) then the installation will continue automatically. \n#########" ; autokey-qt & sleep 3s ; killall -9 autokey-qt ; sudo apt -y install git ; mkdir ~/ahk ; mkdir ~/ahk/github; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cd ~/.config/autokey/data/Sample\ Scripts/ ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ./ ; cp ~/Downloads/Lintalist4Linux/.run-run-lintalistAHK-all.json ./ ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ./ ; cp ~/Downloads/Lintalist4Linux/configParser-set-ini-defaults.ahk ./ ; cp ~/Downloads/Lintalist4Linux/configParser-set-defaults.py ./ ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; wine ~/Downloads/AutoHotkey_1.1.33.02_setup.exe ; echo "Please Configure AutohotKey and AutoKey" ; python3 ~/.config/autokey/data/Sample\ Scripts/configParser-set-defaults.py & 
```

following experimental: 

```
sudo apt -y install autokey-qt ; echo "\n\n#/‾‾‾ AutoKey \n" ; autokey-qt & sleep 2s ; killall -9 autokey-qt ; echo "\n\n#/‾‾‾ git \n" ; sudo apt -y install git ; mkdir ~/ahk ; echo "\n\n#/‾‾‾ github \n" ; mkdir ~/ahk/github ; cd ~/ahk/github/ ; git clone https://github.com/lintalist/lintalist ; cd ~/Downloads/ ; git clone https://github.com/sl5net/Lintalist4Linux ; cd ~/.config/autokey/data/Sample\ Scripts/ ; cp ~/Downloads/Lintalist4Linux/run-run-lintalistAHK-all.py ./ ; cp ~/Downloads/Lintalist4Linux/.run-run-lintalistAHK-all.json ./ ; cp ~/Downloads/Lintalist4Linux/run-lintalistAHK.ahk ./ ; cp ~/Downloads/Lintalist4Linux/configParser-set-ini-defaults.ahk ./ ; cp ~/Downloads/Lintalist4Linux/configParser-set-defaults.py ./ ; cp ~/Downloads/Lintalist4Linux/ifWineWin-sendEnter.py ./ ; echo "\n\n#/‾‾‾ start AutoKey \n" ; autokey-qt > /dev/null & echo "DONT delete this echo!!!! \n\n#/‾‾‾ winehq \n" ; sudo dpkg --add-architecture i386 ; wget -nc https://dl.winehq.org/wine-builds/winehq.key ; sudo apt-key add winehq.key ; sudo apt-add-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main' ; sudo add-apt-repository -y ppa:cybermax-dexter/sdl2-backport ; sudo apt update && sudo apt -y install --install-recommends winehq-stable ; wget https://www.autohotkey.com/download/ahk-install.exe ~/Downloads/ ; python3 ~/.config/autokey/data/Sample\ Scripts/configParser-set-defaults.py ; autokey-run --script ifWineWin-sendEnter ; echo "Please Configure AutohotKey and AutoKey" & 
```




hints for uninstalling autokey-gtk:<br>
https://installlion.com/ubuntu/wily/universe/a/autokey-gtk/uninstall/index.html

or (alpha stage)
```
clear ; cd /tmp ; rm ./install.sh ; wget https://raw.githubusercontent.com/sl5net/Lintalist4Linux/master/install.sh ./install.sh ; sudo chmod +rwx ./install.sh ; ./install.sh ; rm ./install.sh ; cd ~
```

.2. not yet explained here. for systems using a GTK-based desktop environment such as GNOME, MATE, Ubuntu Unity, etc.


## Video installation: 
Video installation of [v0.990](https://github.com/sl5net/Lintalist4Linux/releases/tag/0.990):<br> 
[Lintalist4Linux Instalation liveDemo on Kubunto - no sound - 23min](https://youtu.be/Xc4ALTB7gEw) with https://github.com/sl5net/Lintalist4Linux/releases/tag/0.990

Video installation of [v0.988](https://github.com/sl5net/Lintalist4Linux/releases/tag/0.988):<br> 
[Lintalist4Linux Instalation liveDemo on Kubunto - no sound - 23min](https://youtu.be/CFi3tdCCdxw) with https://github.com/sl5net/Lintalist4Linux/releases/tag/0.988

Video installation of [v0.989]( https://github.com/sl5net/Lintalist4Linux/releases/tag/0.989 ):<br> 
[Lintalist4Linux v0.989 Instalation liveDemo on Kubunto](https://youtu.be/6-QNnTuaYbM) with https://github.com/sl5net/Lintalist4Linux/releases/tag/0.989

# recommended Preferences:

## Autokey - Preferences recommended:
1. enable: Automatically start Autokey at login

## Lintalist - Settings recommended:
- PasteMethod s recommended (you find it in the middle of the long settings list):
    - 2=Don't paste snippet content but copy it to the clipboard (phyton past it for you or you manually later).
- BTW i like the SearchMethod 2=Fuzzy (you find it in the middle)

- use part 3 sometimes: don't use part 2 use part 3 for Script and run part 3 using Shift+Enter
    - Example: field 1: now , field 2: clipboard := a_now

Or:    
```AutoHotKey
FormatTime, timestampyyMMddHHmmss , %A_now%,yyMMdd-HHmmss
clipboard := timestampyyMMddHHmmss
```
```AutoHotKey
FormatTime, timestampyyMMddHHmmssPretty, %A_now%,dd.MM.yy HH:mm:ss
clipboard := timestampyyMMddHHmmssPretty
```

- AutoExecuteOnce: 2
<pre>
Default: 0
If only one result is left during the search AutoExecute (no need to press enter)
0=No
1=Yes, use part 1 (or run script)
2=Yes, use part 2 (or run script)
</pre>

## History:

solved 9.8.2020: https://gist.github.com/sl5net/f68d302f0f5a40d05e6a2e182b453a51

### not professional Videos in german/deutsch:

https://youtu.be/EWW3IOWKyu8

https://www.youtube.com/watch?v=ApYBcKEq53A&list=PLWkx_y_OWhl1rYx79ungQIz8D7sqNSv35&index=11&t=0s

## Thank you too:

- Linux, and all the people there
- https://wiki.winehq.org/Winetricks
- autohotkey, and all the people there
- https://lintalist.github.io/ , and all the people there
- thanks espanso for inspirations: https://espanso.org/install/linux/
- https://element.io/
- and much more


##### Tip's for developer:

if you use PyCharm as external Editor and AutoKey Editor you may do the following:

⚠⚠⚠⚠ "If you disable "Settings/Preferences | Appearance & Behavior | System Settings | Synchronization | Synchronize files on frame or editor tab activation" option ... IDE will show notification bar on top with "Reload" prompt (and possible other options -- depends on situation). But if you have it enabled .. it reloads file with no extra questions asked."
 (Andriy Bazanov, https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000395260-Auto-reload-file-changes?page=1#community_comment_360000080239 )

- TODO/Off-topic:
 As developer i use (as workaround) kotlinC as Linker .py files together zu an bigger file:
 I used for installation SDKMAN!. Details here:
 `$ curl -s https://get.sdkman.io | bash`
 new terminal:
 `$ sdk install kotlin`

https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md

### Motivation
I having trouble fixing bugs in the [global-IntelliSense-everywhere](https://github.com/sl5net/global-IntelliSense-everywhere)
 program and was looking for an alternative. 
The solution here is a little different, but it works.

# download

You could download without github account: 

download Latest Version:
- [master.zip](https://github.com/sl5net/Lintalist4Linux/archive/master.zip)

download specific Version:
- https://github.com/sl5net/Lintalist4Linux/archive/0.98.zip
- https://github.com/sl5net/Lintalist4Linux/archive/0.98.tar.gz

### Your are here:
- [github.com/Lintalist4Linux](https://github.com/sl5net/Lintalist4Linux)  <br>or at gitHub-Page:
- [github.io/Lintalist4Linux](https://sl5net.github.io/Lintalist4Linux/) <br> 
Diese Seite auf Deutsch übersetzt: <br>
[translate.google](https://translate.google.com/translate?sl=en&tl=de&u=https%3A%2F%2Fsl5net.github.io%2FLintalist4Linux%2F)


# Known problems:

## Known problems with wine:

May this helps (sometimes me): Check: `Wintrick` > `wineprefix` > `Change settings` > `Prevent windbg from launching when an unhandled exception occurs`
( https://unix.stackexchange.com/questions/572266/remove-or-prevent-launch-of-winebrowser-kubuntu-kde-plasma-5 )

## Known problems with autoKey: 

recommended:

- dont us the script part
 # :now 20:11:10 11:49:25
 
 
- dont use `.` into Script-Names:<br>
not `unit-test.get_active_class` better  `unit-test-get_active_class`
- move keyboard-shortcut: first delete, then set again   
- set keyboard-shortcut: first enter easy later then the special key. dont record a combination (may autokey freezing)   


# Tipps (thanks to Lintalist):

<pre>
Type: Text
Default: @
Define the character you wish to use to start the Omnisearch.
If you your search query starts with this character it will search in all bundles

**SendMethod**
Default: 1
If you experience any problems with the way text is sent to the various applications you use you may try various methods to see if it resolves the issues
1=SendInput
2=SendEvent
3=SendPlay
4=ControlSend

0=No
1=Yes, use part 1 (or run script)
2=Yes, use part 2 (or run script)