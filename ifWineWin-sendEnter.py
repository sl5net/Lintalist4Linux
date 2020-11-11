# first_class = window.get_active_class() # first_title = window.get_active_title() 
# autokey-run --script unit-test_ifWineWin-sendEnter
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
active_title= window.get_active_title()
popupNotify("title.class = " + active_title + "." + active_class)

max = 200
for x in range(max):
    active_class = window.get_active_class()
    active_title= window.get_active_title()
    aWaC = active_title + "." + active_class
    if "WINE" in active_title or "wine" in active_title :
        keyboard.send_keys('<enter>')
        popupNotify(str(x) + "/" + str(max) + "sec Enter in " + aWaC)
    else:
        popupNotify(str(x)  + "/" + str(max) + "sec " + "(" + aWaC + ")")
    time.sleep(1)

popupNotify("quit()")
quit()



popupNotify("get_active_class works :) window.get_active_class =" + first_class)
popupNotify("get_active_class works :) clipboard_1 =" + clipboard_1)


# https://stackoverflow.com/questions/48560893/write-and-debug-autokey-script-in-pycharm
quit()




