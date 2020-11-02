#NoEnv
#NoTrayIcon
#SingleInstance Ignore
#Persistent
SetWorkingDir, %A_ScriptDir%
SetBatchLines, -1
CoordMode, Pixel, Screen


; MsgBox,% A_UserName
; hallo


pathHome := "Z:\home\" ; dont change this. its same for all users

;<<<<<<<< configure
yourUserName := A_UserName
path := pathHome yourUserName "\ahk\lintalist64\" ; configure folder where lintalist is stored
; path := pathHome yourUserName "\Documents\github\lintalist64\" ; configure folder where lintalist is stored

;>>>>>>>> configure

ClipboardFirst := RTrim(LTrim(Clipboard, " `n`t:"))

SendLevel, 99

Sleep,100

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
    lintalistAHK_path := path . "\lintalist.ahk"
    run, % lintalistAHK_path
    ; MsgBox , Options, Title, Text, Timeout
    ; MsgBox, ,ups pls wait a second, WinWait timed out. '... Lintalist- ...'Window not found => i try again, 3
    ; MsgBox, ,ups lintalist not found. Try again?, Try again? '... Lintalist- ...'Window not found
    WinWait, % winTitleLintalist, , 3
    if ErrorLevel
      ExitApp


    ; reload
    ; return
}
if True
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
      ; if isLintalistWinExist == 1 may he is in the preferences or so.
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

Send,{ShiftUp} ; sometimes it was hanging 20-08-22 16:28:15

; Msgbox,Ok  MsgboxMsgboxMsgboxMsgbox  MsgboxMsgboxMsgboxMsgbox box  box     MsgboxMsgboxMsgboxMsgbox

; protection for empty clipboard if there is no result from lintalist
sleep,1000
c := Clipboard
if(!StrLen(c)){
  Clipboard := ClipboardFirst
}




ExitApp

; 
