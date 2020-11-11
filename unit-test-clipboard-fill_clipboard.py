# autokey-run --script {script-name}.
# autokey-run --script unit-test-clipboard-fill_clipboard

 
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

clipboard_backup = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation

clipboard_expected = "a"
clipboard.fill_clipboard(clipboard_expected)
clipboard_1 = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
if clipboard_expected != clipboard_expected:
    popupNotify("ERROR clipboard_expected != clipboard_expected. its " + clipboard_1)
    beeps(duration=.1, freq=2000, loops=3)
    quit()    

clipboard_expected = clipboard_backup
clipboard.fill_clipboard(clipboard_expected)
clipboard_1 = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
if clipboard_expected != clipboard_expected:
    popupNotify("ERROR clipboard_expected != clipboard_expected. its " + clipboard_1)
    beeps(duration=.1, freq=2000, loops=3)
    quit()    

popupNotify("unit-test-clipboard-fill_clipboard works :)")

# https://stackoverflow.com/questions/48560893/write-and-debug-autokey-script-in-pycharm
quit()

# 


