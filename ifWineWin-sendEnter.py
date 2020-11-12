# first_class = window.get_active_class() # first_title = window.get_active_title() 
# autokey-run --script ifWineWin-sendEnter
#  cp ~/Downloads/Lintalist4Linux/ifWineWin-sendEnter.py ./ ; 
import os, time, datetime, pathlib, subprocess # TODO: one day install: http://omz-software.com/pythonista/docs/ios/clipboard.html
# from pathlib import Path
# home = str(Path.home())
# path = home + "/.config/autokey/data/Sample Scripts/"
def popupNotify(text):
    subprocess.Popen(['notify-send', text])  # will be showed right top
#  path = home + "/.config/autokey/data/Sample Scripts/"
def beeps(duration=.1, freq=2000, loops=1):
    # duration = .8  # second     # freq = 1500  # Hz
    for x in range(loops):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
active_class = window.get_active_class()
active_title = window.get_active_title()
popupNotify("title.class = " + active_title + "." + active_class)

aWaC = active_title + "." + active_class
aWaCOLD = aWaC

maxLoop = 900
for x in range(maxLoop):
    active_title= window.get_active_title()  # AutoHotkey Setup
    active_class = window.get_active_class() # setup.exe.Wine # Installer.control.exe.Wine
    aWaC = active_title + "." + active_class
    # if "Installer.control.exe.Wine" in active_class:  # "WINE" in active_title or "Wine" in active_title:  # Installer.control.exe.Wine
    if ("Wine" in aWaC or "setup.exe" in aWaC or "AutoHotKey" in aWaC or "AutoHotkey" in aWaC) and aWaCOLD != aWaC:  # "WINE" in active_title or "Wine" in active_title:  # Installer.control.exe.Wine
        aWaCOLD = aWaC
        keyboard.send_keys('<enter>')
        popupNotify(str(x) + "/" + str(maxLoop) + "sec Enter in " + aWaC)
    # else:
    #     popupNotify(str(x) + "/" + str(maxLoop) + "sec " + "(" + aWaC + ")")
    time.sleep(3)

popupNotify("quit() ifWineWin-sendEnter")
quit()



popupNotify("get_active_class works :) window.get_active_class =" + first_class)
popupNotify("get_active_class works :) clipboard_1 =" + clipboard_1)


# https://stackoverflow.com/questions/48560893/write-and-debug-autokey-script-in-pycharm
quit()




