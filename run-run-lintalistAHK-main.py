# this file will be (hopefully merged to) ...-all.py

writeAllFile_from_main_defs(path)

if doPopupNotify_welcomeAtEachRun:
    popupNotify("doPopupNotify_welcomeAtEachRun")
    pass
if doBeepsWelcomeAtEachRun:
    popupNotify("doBeepsWelcomeAtEachRun")
    beeps()  # beeps(duration=.8, freq=1500, loops=2)

popupNotify_howItWorks(path + 'run-run-lintalistAHK-all.py')
(timeValueForBREAKLoopInSec, timeValueInLoopInSec, first_title) = read_keyword(doReplaceIfPrefixIsThis,do_ifNoPrefix_useFocusedWord_pasteResultRight,keyboard,window,clipboard)

for x in range(0, 900):  # default is 25
    if timeValueForBREAKLoopInSec < x * timeValueInLoopInSec:
        popupNotify_howItWorks("BREAK at Loop %s because timeValueForBREAKLoopInSec > '%s'" % (str(x), str(timeValueForBREAKLoopInSec)))
        break
    active_title = window.get_active_title()
    if active_title == first_title:
        popupNotify("active_title == first_title ==> we are back")
        break
    time.sleep(timeValueInLoopInSec)

try:
    cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
except:
    time.sleep(0.1)
if len(str(cNew)) < 1 or cNew == cOld:
    popupNotify_howItWorks("no new result ==> exit")
    exit()  # quit()

popupNotify_howItWorks("result = " + cNew)

if doReplace:  # :test  :test  :test  :test  :test
    popupNotify_howItWorks("doReplace")
    keyboard.send_keys('<ctrl>+v')  # work without problem        print(" ")
    if True:
        beeps(duration=.8, freq=7000, loops=1)
    quit()

# keyboard.send_keys('<right><left>') #  deselect  :test MONDSdd

if do_ifNoPrefix_useFocusedWord_pasteResultRight:
    keyboard.send_keys('<right>')  # <right>
if do_ifNoPrefix_useFocusedWord_pasteResultNewLine:
    keyboard.send_keys('<right><enter>')  # <right>
else:
    time.sleep(0.2)
    keyboard.send_keys(" ")
    # print(" ")
time.sleep(0.2)

keyboard.send_keys('<ctrl>+v')  # work without problem        print(" ")

time.sleep(0.1)  # <== its needet
if do_ifNoPrefix_useFocusedWord_pasteResultNewLine:
    time.sleep(0.1)
    keyboard.send_keys('<shift>+<home>')
else:
    # time.sleep(0.1)
    # keyboard.send_keys('<ctrl>+<left>')
    keyboard.send_keys('<ctrl>+<shift>+<left>')  # right
keyboard.release_key('<shift>')  # sometimes i got hanging shift key

# 200 line

time.sleep(1)

