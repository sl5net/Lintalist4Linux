# autokey-run --script {script-name}.
# autokey-run --script unit-tests 
import os, time, datetime, pathlib, subprocess # TODO: one day install: http://omz-software.com/pythonista/docs/ios/clipboard.html
from pathlib import Path
home = str(Path.home())
#/‾‾‾ 
#\___ 
path = home + "/.config/autokey/data/Sample Scripts/"
def popupNotify(text):
    subprocess.Popen(['notify-send', text])  # will be showed right top
path = home + "/.config/autokey/data/Sample Scripts/"
def beeps(duration=.1, freq=2000, loops=1):
    # duration = .8  # second     # freq = 1500  # Hz
    for x in range(loops):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))


beeps(duration=.1, freq=2000, loops=1)

doPopupNotify_howItWorks_ifFirstCharsIs = "#/‾"  #  subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
doPopupNotify_howItWorks = True  #  subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
# doPopupNotify_howItWorks = False
# subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
popupNotify(doPopupNotify_howItWorks_ifFirstCharsIs)
popupNotify(str(len(doPopupNotify_howItWorks_ifFirstCharsIs)))
if not doPopupNotify_howItWorks_ifFirstCharsIs == doPopupNotify_howItWorks_ifFirstCharsIs[:len(doPopupNotify_howItWorks_ifFirstCharsIs)] and doPopupNotify_howItWorks == True:
    popupNotify("quit")
    time.sleep(6)  
    quit()

text = doPopupNotify_howItWorks_ifFirstCharsIs + " blala "
if not doPopupNotify_howItWorks_ifFirstCharsIs == text[:len(doPopupNotify_howItWorks_ifFirstCharsIs)]:
    nop = "nop"
else:
    popupNotify("found FirstChars = " + text[:len(doPopupNotify_howItWorks_ifFirstCharsIs)])
# test