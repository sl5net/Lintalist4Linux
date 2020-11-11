doPopupNotify_howItWorks = True  #  subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
def popupNotify(text):
    subprocess.Popen(['notify-send', text])  # will be showed right top
def popupNotify_howItWorks(text):
    global doPopupNotify_howItWorks
    if doPopupNotify_howItWorks:
        subprocess.Popen(['notify-send', text])  # will be showed right top
        time.sleep(.2)
def beeps(duration=.1, freq=2000, loops=1):
    # duration = .8  # second
    # freq = 1500  # Hz
    for x in range(loops):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
popupNotify_howItWorks("#/‾‾‾ release_key('<shift>")
keyboard.release_key('<shift>')  # sometimes i got hanging shift key
popupNotify_howItWorks("#\___ release_key('<shift>")
