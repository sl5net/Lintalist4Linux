# this file will be (hopefully merged to) ...-all.py

from pathlib import Path
home = str(Path.home())

path = home + "/.config/autokey/data/Sample Scripts/"

doBeepsWelcomeAtEachRun = False
doPopupNotify_welcomeAtEachRun = False  #  subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
doPopupNotify_howItWorks = True  #  subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
# subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top

doReplaceIfPrefixIsThis = ":"
do_ifNoPrefix_useFocusedWord_pasteResultRight = True
do_ifNoPrefix_useFocusedWord_pasteResultNewLine = True

do_DisableUpdatingThe_all_file = False  # not recommended if you developing at this py files !

#__________________ end of config


####### dont change to following:
cNew = clipboardKey = ""

# TODO s : delete or read a time in future:
# https://exceptionshub.com/python-sound-alarm-when-code-finishes.html
# On Debian/Ubuntu/LinuxMint you need to run in your terminal: # sudo apt install sox


