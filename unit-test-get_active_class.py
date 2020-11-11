# autokey-run --script {script-name}.
# first_class = window.get_active_class()
# autokey-run --script unit-test.get_active_class

 
import os, time, datetime, pathlib, subprocess # TODO: one day install: http://omz-software.com/pythonista/docs/ios/clipboard.html
from pathlib import Path
home = str(Path.home())
#/‾‾‾ CPU too high !!!!!!!!!!!!!!!!
#\___ CPU too high !!!!!!!!!!!!!!!!
path = home + "/.config/autokey/data/Sample Scripts/"
def popupNotify(text):
    subprocess.Popen(['notify-send', text])  # will be showed right top
path = home + "/.config/autokey/data/Sample Scripts/"
def beeps(duration=.1, freq=2000, loops=1):
    # duration = .8  # second     # freq = 1500  # Hz
    for x in range(loops):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

first_class = window.get_active_class()
popupNotify("get_active_class = " + first_class)

# clipboard.fill_clipboard(first_class)
time.sleep(0.2)

clipboard.fill_clipboard(first_class)
clipboard_1 = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
popupNotify("clipboard = " + clipboard_1)


if first_class != "autokey-gtk.Autokey-gtk":
    popupNotify("focus is not in autokey. " + clipboard_1)
    if first_class != "konsole.konsole":
        popupNotify("focus is not in Konsole. " + clipboard_1)
        popupNotify("ERROR clipboard = " + clipboard_1)
        beeps(duration=.1, freq=2000, loops=3)

popupNotify("get_active_class works :) window.get_active_class =" + first_class)
popupNotify("get_active_class works :) clipboard_1 =" + clipboard_1)


# https://stackoverflow.com/questions/48560893/write-and-debug-autokey-script-in-pycharm
quit()




