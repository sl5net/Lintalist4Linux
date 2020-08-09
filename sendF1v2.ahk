#NoEnv
#NoTrayIcon
#SingleInstance Ignore
#Persistent
SetWorkingDir, %A_ScriptDir%
SetBatchLines, -1
CoordMode, Pixel, Screen

; the same place in different notations:
; C:\users\administrator\Desktop\sendF1v2.ahk
; /home/administrator/Desktop/sendF1v2.ahk
; https://github.com/sl5net/Lintalist4Linux-version-0.00000001-Alpha

; Z:\home\administrator\ahk\lintalist\lintalist.ahk
; /home/administrator/ahk/lintalist/lintalist.ahk

ClipboardFirst := Clipboard

SendLevel 99

Sleep,100

; if( WinExist("Lintalist") ){
; MsgBox,lintalist found :)
; }else{
; MsgBox,Lintalist NOT found :(
; run,Z:\home\administrator\ahk\lintalist\lintalist.ahk
; }

  ; this run commands working at the moment:
  ; ~$ wine ~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Desktop/sendF1v2.ahk

; dont use it like:
; $ wine /home/me/Desktop/sendF1v2.ahk
; wine: Bad EXE format for Z:\home\me\Desktop\sendF1v2.ahk.

SendInput, {f1}

; 2: A window's title can contain WinTitle anywhere inside it to be a match.
DetectHiddenWindows, Off
SetTitleMatchMode, 2
WinWait, Lintalist -, , 3
if ErrorLevel
{
    run,Z:\home\administrator\ahk\lintalist\lintalist.ahk
    ; MsgBox , Options, Title, Text, Timeout
    MsgBox, ,ups pls wait a second, WinWait timed out. '... Lintalist- ...'Window not found => i try again, 2
    reload
    return
}
else
{
	WinActivate ; use the window found above
	sleep, 100
	Send,^a^f
	sleep, 280
	; Send, Hi world^a
	Send,davor %ClipboardFirst% danach
}
; Msgbox,Ok great ExitApp
ExitApp

