# this file will be (hopefully merged to) ...-all.py

writeAllFile_from_main_defs(path)

if doPopupNotify_howItWorks:
    popupNotify_howItWorks("doPopupNotify_howItWorks is set TRUE\n in the ..config.py file. Great :)")


if doPopupNotify_welcomeAtEachRun:
    popupNotify("doPopupNotify_welcomeAtEachRun")
    pass
if doBeepsWelcomeAtEachRun:
    popupNotify("doBeepsWelcomeAtEachRun")
    beeps()  # beeps(duration=.8, freq=1500, loops=2)



# popupNotify_howItWorks(path + 'run-run-lintalistAHK-all.py')
(doReplace, timeValueForBREAKLoopInSec, timeValueInLoopInSec, first_title) = read_keyword(doReplaceIfPrefixIsThis,do_ifNoPrefix_useFocusedWord_pasteResultRight,keyboard,window,clipboard)

for x in range(0, 900):  # default is 25
    if timeValueForBREAKLoopInSec < x * timeValueInLoopInSec:
        popupNotify_howItWorks("BREAK at Loop %s because timeValueForBREAKLoopInSec > '%s'" % (str(x), str(timeValueForBREAKLoopInSec)))
        break
    if window.get_active_title() == first_title:
        popupNotify("active_title == first_title ==> we are back")
        break
    time.sleep(timeValueInLoopInSec)
try:
    cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
except:
    time.sleep(0.1)

len_clipboardNew = len(str(cNew))

if len_clipboardNew < 1 or cNew == clipboardKey:
    popupNotify_howItWorks("no new result ==> exit")
    exit()  # quit()

# L@SL5.de Sebastian

if doReplace:  # :test  :test  :test  :test  :test 20-08-22 16:02:21

    keyboard.send_keys('<ctrl>+v')  # work without problem        print(" ")
    time.sleep(0.2) #  200mili needed in some apps   20-08-24 17:18:48
    select_text(keyboard, len_clipboardNew)
    popupNotify_howItWorks("do replace because Prefix " + doReplaceIfPrefixIsThis + " is found.")
    # beeps(duration=.8, freq=1500, loops=2)
    quit()

if doPopupNotify_howItWorks:
    popupNotify_howItWorks("result = " + cNew)
    # beeps(duration=.8, freq=1500, loop L@SL5.de : : L@SL5.de L@SL5.de L@SL5.de  L@SL5.de
    # loopss=5)

popupNotify_howItWorks("no Prefix " + doReplaceIfPrefixIsThis + " in " + clipboardKey )

# keyboard.send_keys('<right><left>') #  deselect  :uff

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

