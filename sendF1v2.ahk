#NoEnv
#NoTrayIcon
#SingleInstance Ignore
#Persistent
SetWorkingDir, %A_ScriptDir%
SetBatchLines, -1
CoordMode, Pixel, Screen

; the same place in different notations:
; C:\users\ YOU \Desktop\sendF1v2.ahk
; /home/ YOU /Desktop/sendF1v2.ahk

; Z:\home\ YOU \ahk\lintalist\lintalist.ahk
; /home/ YOU /ahk/lintalist/lintalist.ahk


if( ! WinExist("lintalist") )
  run,Z:\home\ YOU \ahk\lintalist\lintalist.ahk

  ; this run commands working at the moment:
  ; ~$ wine ~/.wine/drive_c/Program\ Files/ YOU /AutoHotkey.exe /home/ YOU /Desktop/sendF1v2.ahk

; dont use it like:
; $ wine /home/me/Desktop/sendF1v2.ahk
; wine: Bad EXE format for Z:\home\me\Desktop\sendF1v2.ahk.

SendLevel 99

SendInput, {f1}

; 2: A window's title can contain WinTitle anywhere inside it to be a match.
SetTitleMatchMode, 2
WinWait, Lintalist -, , 3
if ErrorLevel
{
    run,Z:\home\    \ahk\lintalist\lintalist.ahk
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
	Send, Hi world^a
}
; Msgbox,Ok great ExitApp
ExitApp
