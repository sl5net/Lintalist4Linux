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

ClipboardFirst := Trim(Clipboard)

SendLevel, 99

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

SendInput,{f1}

;  A window's title can contain WinTitle anywhere inside it to be a match. A window's title can contain WinTitle anywhere inside it to be a match. A window's title can contain WinTitle anywhere inside it to be a match.

; 2: A window's title can contain WinTitle anywhere inside it to be a match. 
DetectHiddenWindows, Off
SetTitleMatchMode, 2
; winTitleLintalist := "administrator^ Lintalist - 1.9.13 ahk_class AutoHotkeyGUI ahk_exe AutoHotkey.exe ahk_pid 140"
winTitleLintalist := "Lintalist - 1.9.13 ahk_class AutoHotkeyGUI"
WinWait, % winTitleLintalist, , 3
if ErrorLevel
{
    run,Z:\home\administrator\ahk\lintalist\lintalist.ahk
    ; MsgBox , Options, Title, Text, Timeout
    ; MsgBox, ,ups pls wait a second, WinWait timed out. '... Lintalist- ...'Window not found => i try again, 3
    MsgBox, ,ups lintalist not found. Try again?, Try again? '... Lintalist- ...'Window not found
    ; ExitApp
    reload
    return
}
else
{

  WinActivate ; use the window found above  
  WinWaitActive, % winTitleLintalist, , 3, 
	sleep, 40
	; Send,^a^f
	; sleep, 280
	; Send,world
	; Send,%ClipboardFirst%^a
  if(False){
    ; SendLevel, 1   
    Send,^v 
  } else {
    IfWinNotActive, % winTitleLintalist
    {
      isLintalistWinExist := ( WinExist(winTitleLintalist) ) ? True : False
      MsgBox, :( ups WinNotActive, winTitleLintalist isLintalistWinExist=%isLintalistWinExist%
      ExitApp
    }
    if( StrLen(ClipboardFirst) > 100 ){
      ClipboardFirstShort := RTrim( SubStr(ClipboardFirst, 1, 60) )
      ControlSetText, Edit1, % ClipboardFirstShort, % winTitleLintalist
      ; MsgBox, % ClipboardFirstShort
    } else {
      ControlSetText, Edit1, % ClipboardFirst, % winTitleLintalist
    }
  }

  Send,^a
  ; SendLevel   A window's title can contain WinTitle anywhere inside it to be a match. A window's title can contain WinTitle anywhere inside it to be a match. A window's title can contain WinTitle anywhere inside it to be a match.
  ;   A window's title can contain WinTitle anywhere inside it to be a match. A window's title can contain WinTitle anywhere inside it to be a match. A window's title can contain WinTitle anywhere inside it to be a match.

}
; Msgbox,Ok  MsgboxMsgboxMsgboxMsgbox  box  box  
ExitApp

