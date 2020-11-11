#NoEnv
#NoTrayIcon
#SingleInstance force
#Persistent
SetWorkingDir, %A_ScriptDir%
SetBatchLines, -1
CoordMode, Pixel, Screen


; MsgBox,% A_UserName
; hallo


pathHome := "Z:\home\" ; dont change this. its same for all users

loop 5
{
    Clipboard := "Hello World"
    Tooltip, % A_Index ": " Clipboard
    sleep,1000
    Tooltip, % A_Index ":  ^_^"
    sleep,1000
}
sleep,100
Tooltip, % ""
