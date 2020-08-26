# Lintalist4Linux

Linux and Windows -platform **Text Replacer/Adder/Scripter** written in AutoKey/Phyton and AutoHotKey with the Help from Lintalist  

## How it works
1. The Add-Text-Method: 
    1. set your cursor (looks like `|`) **behind a word** (example: `phone`) in your text.<br> 
Example: `phone|` or `address|`, `email|`, `now|`, `date|`, [... autohotkey commands](https://www.autohotkey.com/docs/commands/FormatTime.htm)
    1. Press shortcut (please configure. recommended `F12`)
    - [x] Database opens, **searching** results from your word (e.g. `phone`), and adds result behind and save result in clipboard.
1. The Replace-Text-Method (and press shortcut): 
    - [x] `:keyword` replaces text with result (if many it opens menu) and save in clipboard
    - without text
        - [x] `:` + press `F12` lets write the clipboard
        - [x] `:` + press `F12` sends your clipboard 1 times. separated with tab-key
        - [x] `²` + press `F12` sends your clipboard 2 times. separated with tab-key

More explanation:
- you don't need write the complete keyword. e.g. writing `address|` or `addr|`  `adr|` or `ad|` my is enough if you use fuzzy search.
- scripting with [... autohotkey commands](https://www.autohotkey.com/docs/commands/FormatTime.htm): 
    - for example `:date` and replaces it with `20.08.2020`
    - for example `:now` and replaces it with `20.08.2020 16:48:24`
- If you want many Results for one keyword the Lintalist-Menu ⇶ is opening before (see more in Lintalist-Configuration about AutoExecuteOnce)
- You always also have the result in your clipboard.
- In some cases (e.g. if you simple want send your clipboard) it not using  `ctrl` + `v` method intern.

Maybe you want to install the following at the same time, as a supplement: [espanso.org](https://espanso.org/)

[lintalist.github.io](https://lintalist.github.io/)  says (10.08.2020):<br>
"Lintalist allows you to store and (incrementally) search <br>
and edit texts in bundles and paste a selected text in your active program.<br>
... Lintalist is open source and developed in AutoHotkey ..."
<br><br>
if you want see how it works while it works open the config file and set:
`doPopupNotify_howItWorks = True`

Tested with the following recommended installation:

# installation (recommended):
- [LinuxMint](https://linuxmint.com/edition.php?id=283) (tested with "Linux Mint 20 Ulyana - ******Xfce****** (64-bit)" may works with other Linux OS or Window OS)
- Wine (HowTo: [linuxbabe.com/ .. install-wine-linux-mint](https://www.linuxbabe.com/linux-mint/install-wine-linux-mint-19-1) )
- [Winetricks wiki](https://wiki.winehq.org/Winetricks#Installing_winetricks) 
- [AutoKey](https://github.com/autokey/autokey#installation) (or may use your Software Manager )
- [AutoHotKey.com](https://www.autohotkey.com/)  ( maybe [github.com/Lexikos/AutoHotkey_L](https://github.com/Lexikos/AutoHotkey_L) )
- [lintalist.github.io](https://lintalist.github.io/)

### copy files and configuration:

1. copy <br>
run-run-lintalistAHK *** .py<br>
scripts to
<br>/home/ YOU /.config/autokey/data/Sample Scripts/
1. copy <br>
run-lintalistAHK.ahk<br>
to<br>
/home/ YOU /Documents/github/Lintalist4Linux/run-lintalistAHK.ahk
1. open AutoKey App
1. click run-run-lintalistAHK-all.py<br> and set shortcut (for e.g. `F12`)

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
```AutoHotKey
FormatTime, timestampyyMMddHHmmss , %A_now%,yyMMddHHmmss
FormatTime, timestampyyMMddHHmmssPretty, %A_now%,yy:MM:dd HH:mm:ss
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


# download

You could download without github account: 

download Latest Version:
- [master.zip](https://github.com/sl5net/Lintalist4Linux/archive/master.zip)

download specific Version:
- https://github.com/sl5net/Lintalist4Linux/archive/0.95.zip
- https://github.com/sl5net/Lintalist4Linux/archive/0.95.tar.gz

### Your are here:
- [github.com/Lintalist4Linux](https://github.com/sl5net/Lintalist4Linux)  <br>or at gitHub-Page:
- [github.io/Lintalist4Linux](https://sl5net.github.io/Lintalist4Linux/) <br> 
Diese Seite auf Deutsch übersetzt: <br>
[translate.google](https://translate.google.com/translate?sl=en&tl=de&u=https%3A%2F%2Fsl5net.github.io%2FLintalist4Linux%2F)


