# this file will be (hopefully merged to) ...-all.py

# the following f-keys commands are working:
# keyboard.fake_keypress('<f4>') # edit snippet
# keyboard.fake_keypress('<f5>') # copy snippet
# keyboard.fake_keypress('<f5>') # move snippet
# keyboard.fake_keypress('<f7>') # new snippet
# keyboard.fake_keypress('<f8>') # remove snippet
# keyboard.fake_keypress('<f10>') # manage bundels

# from time import sleep

def slow_send(word, delay):
    for c in word:
        keyboard.send_keys(c)
        time.sleep(delay)

import os, time, datetime, pathlib, subprocess # TODO: one day install: http://omz-software.com/pythonista/docs/ios/clipboard.html

#<<<<<<<<<<<<
# Todo: do this: https://github.com/autokey/autokey/issues/248
#>>>>>>>>>>>>


def popupNotify(text):
    subprocess.Popen(['notify-send', text])  # will be showed right top

def popupNotify_howItWorks(text):
    global doPopupNotify_howItWorks
    if doPopupNotify_howItWorks:
        subprocess.Popen(['notify-send', text])  # will be showed right top

def writeAllFile_from_main_defs(path):
    global do_DisableUpdatingThe_all_file
    if do_DisableUpdatingThe_all_file:
        return
    # path = "/home/administrator/.config/autokey/data/Sample Scripts/"
    # global data
    data = "# Attention: !!! don`t edit thi file. this file will be result from other files merged."

    getmtimeConfig = os.path.getmtime(path + 'run-run-lintalistAHK-config.py')
    getmtimeDefs = os.path.getmtime(path + 'run-run-lintalistAHK-defs.py')
    getmtimeMain = os.path.getmtime(path + 'run-run-lintalistAHK-main.py')
    getmtimeAll = os.path.getmtime(path + 'run-run-lintalistAHK-all.py')

    if getmtimeAll < getmtimeDefs or getmtimeAll < getmtimeConfig or getmtimeAll < getmtimeMain:
        subprocess.Popen(['notify-send', ' need update'])  # will be showed right top
        # Reading data from file1
        with open(path + 'run-run-lintalistAHK-config.py') as fp:
            data += "\n" + fp.read()
        with open(path + 'run-run-lintalistAHK-defs.py') as fp:
            data += "\n" + fp.read()
        with open(path + 'run-run-lintalistAHK-main.py') as fp:
            data += "\n" + fp.read()
        with open(path + 'run-run-lintalistAHK-all.py', 'w') as fp:
            fp.write(data)

    # from module.run_run_lintalist_fuctions import read_keyword
    # HowTo import modules in AutoKey: https://stackoverflow.com/a/23186143/2891692
    # not best way: # >~/.config/autokey/autokey.json >Find a line that looks like >    "userCodeDir": "", >and put your directory path in manually.
    # https://groups.google.com/g/autokey-users/c/ykEoQygDw40?pli=1
    # https://stackoverflow.com/questions/16226607/any-way-to-import-autokey-libraries-into-python-script
    # https://github.com/autokey/autokey/issues/248#issue-406386345


#################
def beeps(duration=.1, freq=2000, loops=1):
    # duration = .8  # second
    # freq = 1500  # Hz
    for x in range(loops):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
# <<<<<<<<<< read_keyword
def read_keyword(doReplaceIfPrefixIsThis,do_ifNoPrefix_useFocusedWord_pasteResultRight,keyboard,window,clipboard):
    global doPopupNotify_howItWorks, clipboardKey, first_title, duration, freq, doReplace, x, active_title, timeValueInLoopInSec, timeValueForBREAKLoopInSec
    if doReplaceIfPrefixIsThis:
        # selct word and prefix e.g.  :test
        doSelctWordAndPrefix = True
    clipboardBackup = ""

    clipboardBackup = ''
    try:
        clipboardBackup = clipboard.get_clipboard()  #  .lstrip  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    except:
        clipboardBackup = ""
        beeps(duration=.1, freq=2000, loops=1)
        popupNotify_howItWorks("get_clipboard except :-O")

    # check if its only :
    clipboardKey_endChar = check_key_endChar_and_may_replace(clipboard, clipboardBackup, doReplaceIfPrefixIsThis, keyboard)
    copy_word_2_clipboard_focusedInTheMiddle(clipboard, keyboard)
    clipboardKey = try_read_clipboard_without_visible_errors(clipboard)


    keyboard.release_key('<shift>')  # sometimes i got hanging shift key

    first_title = window.get_active_title()

    popupNotify_howItWorks('get_clipboard')

    doReplace = False

    popupNotify_howItWorks("clipboardKey = " + clipboardKey)
    # time.sleep(1)
    # quit() # klkj klkjklkj lklkjlklkjlklkjlklkj

    # :seb

    firstChar = clipboardKey[0:1]

    if not clipboardKey:
        popupNotify_howItWorks("NOT clipboardKey = " + clipboardKey + " ==> exit()")
        beeps(duration=.1, freq=2000, loops=2)
        exit()
    if not doReplaceIfPrefixIsThis:
        popupNotify_howItWorks("NOT doReplaceIfPrefixIsThis = " + doReplaceIfPrefixIsThis + " ==> exit()")
        beeps(duration=.1, freq=2000, loops=3)
        exit()

    # popupNotify_howItWorks('firstChar = ' + firstChar + ' , clipboardKey = ' + clipboardKey)
    # time.sleep(2)
    # quit()


    if firstChar == doReplaceIfPrefixIsThis:  # :test :test ff uihu : :
        doReplace = True
        popupNotify_howItWorks("found doReplaceIfPrefixIsThis = " + doReplaceIfPrefixIsThis)
        # if doPopupNotify_howItWorks:   :test
        #     beeps(duration=.2, freq=1000, loops=2)
    else:
        try:
            popupNotify_howItWorks("NOT found in keyword = >>" + clipboardKey + "<<\n , doReplaceIfPrefixIsThis = >>" + doReplaceIfPrefixIsThis + "<<")
        except:
            popupNotify_howItWorks("NOT found in keyword")
    # asdf

    #if doReplaceIfPrefixIsThis == clipboardKey:
    # keyboard.send_keys('-' + clipboardKey + '-')
    # keyboard.send_keys('-' + clipboardBackup + '-')
    # quit()  # testk testk : : clipboardBackup  : : :  clipboardBackup'-' clipboardBackupclipboardBackupclipboardBackup


    # keyboard.release_key('<ctrl>')
    popupNotify_howItWorks("run run-lintalistAHK.ahk")
    # beeps(duration=.25, freq=5000, loops=1)
    try:
        # subprocess.Popen(["/bin/bash", "/home/administrator/Documents/github/Lintalist4Linux/run-run-lintalistAHK.sh"])
        # import os :seb

        myCmd = 'wine ~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Documents/github/Lintalist4Linux/run-lintalistAHK.ahk'
        os.system(myCmd)

        # myCmd = kotlinc - script "/home/administrator/.config/autokey/data/Sample Scripts/PyLink.kts" - - -d. /
        # os.system(myCmd)
    except subprocess.CalledProcessError:
        time.sleep(0.2)


    # :lo :Heide

    # :tes2016/01t Heide
    # 100 line
    # php2012/01 cello-technologie.de
    for i in range(0, 30):
        time.sleep(0.1)
        # active_class = window.get_active_class()
        active_title = window.get_active_title()
        # if active_class != first_class:
        if active_title != first_title:
            break
    timeValueInLoopInSec = 0.2
    timeValueForBREAKLoopInSec = 90  # timeOut. Prevention for endless loops
    # BREAK x is '101
    # time.sleep(2)
    # keyboard.send_keys('<ctrl>+v')
    return (clipboardKey, doReplace, timeValueForBREAKLoopInSec, timeValueInLoopInSec, first_title)


def try_read_clipboard_without_visible_errors(clipboard):
    clipboardKey = ""
    for i in range(1, 3):
        try:
            clipboardKey = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
            slepSec = i * .1
            time.sleep(slepSec)
        except:
            slepSec = i * .1
            time.sleep(slepSec)
        if clipboardKey:
            break
    return clipboardKey   # test


def copy_word_2_clipboard_focusedInTheMiddle(clipboard, keyboard):
    doSelect1charBefore = True
    # read rest for beginning clipboardKey
    keyboard.release_key('<ctrl>')  # keyboard.press_key('<ctrl>')
    time.sleep(.1)  # seems importend time while using in pycharm
    keyboard.send_keys('<ctrl>+<right>')  # not works in every e.g. editor like pycharm
    keyboard.send_keys('<ctrl>+<left>')  # not works in every e.g. editor like pycharm
    if doSelect1charBefore:
        keyboard.send_keys('<left>')
    keyboard.send_keys('<shift>+<right>')
    keyboard.send_keys('<ctrl>+<shift>+<right>')
    # time.sleep(.4)
    keyboard.send_keys('<ctrl>+c')
    time.sleep(.1)

    # quit() # asdfasf k  Sebastian Sebastian sl5 L@SL5.de
    # test

def check_key_endChar_and_may_replace(clipboard, clipboardBackup, doReplaceIfPrefixIsThis, keyboard):
    # this all works not in some websites. for e.g. career5.successfactors.eu
    # in some register forms alls specialkey send the form. only letters not


    # check if its only dummy_send :
    # keyboard.press_key('<shift>')
    # quit()
    # keyboard.release_key('<shift>')

    keyboard.send_keys('<shift>+<left>') # this works not in some websites. for e.g. career5.successfactors.eu

    keyboard.send_keys('<ctrl>+c')
    time.sleep(0.1)
    try:
        clipboardKey_endChar = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    except:
        clipboardKey_endChar = ''
    popupNotify_howItWorks("clipboardKey_endChar = " + clipboardKey_endChar)
    if clipboardKey_endChar == doReplaceIfPrefixIsThis:
        # doReplace = True
        popupNotify_howItWorks("found doReplaceIfPrefixIsThis = " + doReplaceIfPrefixIsThis)
        keyboard.send_keys(clipboardBackup)
        # slow_send(clipboardBackup, 1)
        len_clipboardBackup = len(clipboardBackup)
        select_text(keyboard, len_clipboardBackup)
        keyboard.send_keys('<ctrl>+c')  # stay with old clipboard. copy clipboardBackup
        quit()  #
    if clipboardKey_endChar == "²":  # special comando. sends it two times with tab beetween
        # doReplace = True
        popupNotify_howItWorks("found doReplaceIfPrefixIsThis = " + doReplaceIfPrefixIsThis)
        keyboard.send_keys(clipboardBackup)
        keyboard.send_keys("<tab>")
        keyboard.send_keys(clipboardBackup)
        # slow_send(clipboardBackup, 1)
        len_clipboardBackup = len(clipboardBackup)
        select_text(keyboard, len_clipboardBackup)
        keyboard.send_keys('<ctrl>+c')  # stay with old clipboard. copy clipboardBackup
        quit()  #
    return clipboardKey_endChar


# asdf  ² :  : asdasdfasdasdfasdasdf Sebastian Sebastian ² Sebastian :  Sebastian : Sebastian : Sebastian Sebastian :



def select_text(keyboard, len_clipboardBackup = 0):  #  0 if dont know the clipboard/text but try select anyway
    keyboard.release_key('<ctrl>')
    if not len_clipboardBackup or len_clipboardBackup > 100:
        keyboard.send_keys('<ctrl>+<shift>+<left>')  # faster but not as exact. forgets special letters.
    else:
        # keyboard.press_key('<shift>') ### <=== disabled this way of selection 20-08-24 21:23:35
        for i in range(0, len_clipboardBackup):
            # keyboard.send_keys('<left>') # exact method
            keyboard.send_keys('<shift>+<left>') # exact method
        # keyboard.release_key('<shift>')

#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword

# :umm