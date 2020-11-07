yourUserName := A_UserName

pathHome := "Z:\home\" ; dont change this. its same for all users
path := pathHome yourUserName "\ahk\github\lintalist\" ; configure folder where lintalist is stored
iniPath := path "Settings.ini"

# WinWait, Untitled - Notepad, , 3

if !FileExist(iniPath){
    MsgBox, %iniPath% file does not exist.
    exit
}
; /home/administrator/ahk/github/lintalist/Settings.ini

;# config['Settings']['QuickSearchHotkey'] = 'F11'  # create or update
; IniWrite, Value, Filename, Section, Key
IniWrite, F11, % iniPath, Settings, QuickSearchHotkey
; MsgBox,% iniPath


