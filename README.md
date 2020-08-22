# Lintalist4Linux

Linux and Windows -platform Text Replacer/Adder/Scripter written in AutoKey/Phyton and AutoHotKey with the Help from Lintalist  

## How it works

Lintalist4Linux

1. waits for shortcut (recommended Ctrl+K or simple F12)
1. reads your word as keyword (for example `:date` , `:now` or `now` or `address` etc.)
    1. replace your word
        1. for example `:date` and replaces it with 20.08.2020
        1. for example `:now` and replaces it with 20.08.2020 16:48:24
    1. adds new line behind your word
        1. for example `now` adds the result into a new line. for e.g. 20.08.2020 16:48:24 and selects this line
1. If you want many Results for one keyword the Lintalist-Menu ⇶ is opening before (see more in Lintalist-Configuration about AutoExecuteOnce)
1. Also you have the result in your clipboard.

https://lintalist.github.io/ says (10.08.2020):
"Lintalist allows you to store and (incrementally) search <br>
and edit texts in bundles and paste a selected text in your active program.<br>
... Lintalist is open source and developed in AutoHotkey ..."
<br><br>
if you want see how it works while it works open the config file and set:
`doPopupNotify_howItWorks = True`

Tested with LinuxMint Version 20
not tested with Windows (probably work ?)

# installation (recommended):
- LinuxMint (new versions) or maybe other Linux
- wine (may use your Software Manager)
- Winetricks (maybe not needet) (may use your Software Manager)
- AutoKey (may use your Software Manager)
- AutoHotKey
- Lintalist

### copy files and configuration:

1. copy <br>
run-run-run-lintalistAHK *** .py<br>
scripts to
<br>/home/ YOU /.config/autokey/data/Sample Scripts/
1. copy <br>
run-lintalistAHK.ahk<br>
to<br>
/home/ YOU /Documents/github/Lintalist4Linux/run-lintalistAHK.ahk
1. open AutoKey App
1. click run-run-lintalistAHK-all.py<br> and set shortcut

# recommended Preferences:

edit one line of each file (so they find your scripts)

## Autokey - Preferences:
- enable: Automatically start Autokey at login
- Set a Hotkey in that py-File

## Lintalist - Settings:
- QuickSearchHotkey: F1 (needed reflected inside run-lintalistAHK.ahk)<br>
You find QuickSearchHotkey nearly at the last page inside this long list into the 'Lintalist - Settings'
- PasteMethod s recommended (you find it in the middle of the long settings list):
    - 1=Paste snippet and keep it as the current clipboard content (so you can manually paste it again)
    - 2=Don't paste snippet content but copy it to the clipboard so you can manually paste it.
- BTW i like the SearchMethod 2=Fuzzy (you find it in the middle)

- use part 3 sometimes: don't use part 2 use part 3 for Script and run part 3 using Shift+Enter
    - Example: field 1: now , field 2: clipboard := a_now

Or:    
<pre>
FormatTime, timestampyyMMddHHmmss , %A_now%,yyMMddHHmmss
FormatTime, timestampyyMMddHHmmssPretty, %A_now%,yy:MM:dd HH:mm:ss
clipboard := timestampyyMMddHHmmssPretty
</pre>

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


##### Tipps for developer:

if you use PyCharm as external Editor and AutoKey Editor you may do the following:

⚠⚠⚠⚠ "If you disable "Settings/Preferences | Appearance & Behavior | System Settings | Synchronization | Synchronize files on frame or editor tab activation" option ... IDE will show notification bar on top with "Reload" prompt (and possible other options -- depends on situation). But if you have it enabled .. it reloads file with no extra questions asked."
 (Andriy Bazanov, https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000395260-Auto-reload-file-changes?page=1#community_comment_360000080239 )

 As developer i use (as workaround) to link AutoKey .py files together too an bigger file.
 Please read first comments inside the files.

  TODO/Off-topic:
 As developer i use (as workaround) kotlinC as Linker .py files together zu an bigger file:
 I used for installation SDKMAN!. Details here:
 `$ curl -s https://get.sdkman.io | bash`
 new terminal:
 `$ sdk install kotlin`


##### Tips for user don't want use github now:

You could download without account or login: 

Latest:
- https://github.com/sl5net/Lintalist4Linux/archive/master.zip

Specific Version:
- https://github.com/sl5net/Lintalist4Linux/archive/0.95.zip
- https://github.com/sl5net/Lintalist4Linux/archive/0.95.tar.gz
