yourUserName := A_UserName

pathHome := "Z:\home\" ; dont change this. its same for all users
path := pathHome yourUserName "\ahk\github\lintalist\" ; configure folder where lintalist is stored
iniPath := path "Settings.ini"

; WinWait, Untitled - Notepad, , 3

if !FileExist(iniPath){
    MsgBox, %iniPath% file does not exist.
    exit
}
; /home/m/ahk/github/lintalist/Settings.ini

;# config['Settings']['QuickSearchHotkey'] = 'F11'  # create or update
; IniWrite, Value, Filename, Section, Key
IniWrite, F11, % iniPath, Settings, QuickSearchHotkey
IniWrite, 2, % iniPath, Settings, PasteMethod
IniWrite, 2, % iniPath, Settings, SearchMethod
IniWrite, Part1-Logical, % iniPath, Settings, ColumnSort
IniWrite, 10, % iniPath, Settings, PasteDelay
IniWrite, 1, % iniPath, Settings, AutoExecuteOne


; MsgBox,% iniPath
; 20:11:10 12:54:00
; :time
; 20:11:10 12:54:23
; :time
; :time
; :time
; :time
; :time


