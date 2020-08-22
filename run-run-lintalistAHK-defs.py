# this file will be (hopefully merged to) ...-all.py

# the following f-keys commands are working:
# keyboard.fake_keypress('<f4>') # edit snippet
# keyboard.fake_keypress('<f5>') # copy snippet
# keyboard.fake_keypress('<f5>') # move snippet
# keyboard.fake_keypress('<f7>') # new snippet
# keyboard.fake_keypress('<f8>') # remove snippet
# keyboard.fake_keypress('<f10>') # manage bundels


import os, time, datetime, pathlib, subprocess

#<<<<<<<<<<<<
# Todo: do this: https://github.com/autokey/autokey/issues/248
#>>>>>>>>>>>>


def writeAllFile_from_main_defs():
    path = "/home/administrator/.config/autokey/data/Sample Scripts/"
    # global data
    data = "# Attention: !!! don`t edit thi file. this file will be result from other files merged.\n"

    getmtimeDefs = os.path.getmtime(path + 'run-run-lintalistAHK-defs.py')
    getmtimeMain = os.path.getmtime(path + 'run-run-lintalistAHK-main.py')
    getmtimeAll = os.path.getmtime(path + 'run-run-lintalistAHK-all.py')

    if getmtimeAll < getmtimeDefs or getmtimeAll < getmtimeMain:
        subprocess.Popen(['notify-send', ' need update'])  # will be showed right top
        # Reading data from file1
        with open(path + 'run-run-lintalistAHK-defs.py') as fp:
            data += fp.read()
        # Reading data from file2
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

def beeps(duration, freq, loops):
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
    global cOld, first_title, duration, freq, doReplace, x, active_title, timeValueInLoopInSec, timeValueForBREAKLoopInSec
    if doReplaceIfPrefixIsThis:
        # selct word and prefix e.g.  :test
        doSelctWordAndPrefix = True
    cOld = ""
    # line 20 Heide kjkjhkjh 5
    # kjhlkjhvv
    if do_ifNoPrefix_useFocusedWord_pasteResultRight:
        # unselct maybe selected word word
        keyboard.send_keys('<left><right>')

        # keyboard.send_keys('<right>')

        if doSelctWordAndPrefix:
            keyboard.release_key('<ctrl>')  # keyboard.press_key('<ctrl>')
            time.sleep(.1)  # seems importend time while using in pycharm
            keyboard.send_keys('<ctrl>+<left>')  # not works in every e.g. editor like pycharm
            # time.sleep(.1)
            # keyboard.press_key('<ctrl>')
            # keyboard.send_keys('<left>')
            # time.sleep(.1)
            # keyboard.release_key('<ctrl>')
            # time.sleep(.1)
            keyboard.send_keys('<left>')

            # time.sleep(2) # asdf

            keyboard.send_keys('<shift>+<right>')
            keyboard.send_keys('<ctrl>+<shift>+<right>')
        else:
            # selct word
            keyboard.send_keys('<ctrl>+<left>')
            keyboard.send_keys('<ctrl>+<shift>+<right>')
        keyboard.send_keys('<ctrl>+c')
        # keyboard.send_keys('<ctrl>+v')

        keyboard.release_key('<shift>')  # sometimes i got hanging shift key
        # keyboard.release_key('<ctrl>')
    # 30 line
    #####################
    # this file must be run in:
    # /home/ you /.config/autokey/data/Sample Scripts/
    # or so
    # this file i store it in local repo like:
    # /home/ you /Documents/github/Lintalist4Linux/
    #####################
    first_title = window.get_active_title()
    # first_class = window.get_active_class()
    # keyboard.send_keys("\n#1 first_class='%s'" % first_class)
    # 1 first_class='autokey-gtk.Autokey-gtkinitialContent'
    # https://exceptionshub.com/python-sound-alarm-when-code-finishes.html
    # On Debian/Ubuntu/LinuxMint you need to run in your terminal:
    # sudo apt install sox
    duration = 0.25  # seconhi worldhi worldd ###hi worldhi worldhi world
    freq = 5000  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    # 50 line
    # keyboard.release_key('<f1>') # mayby problems ?
    # keyboard.release_key('<ctrl>')
    try:
        # subprocess.Popen(["/bin/bash", "/home/administrator/Documents/github/Lintalist4Linux/run-run-lintalistAHK.sh"])
        # import os
        myCmd = 'wine ~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Documents/github/Lintalist4Linux/run-lintalistAHK.ahk'
        os.system(myCmd)

        # myCmd = kotlinc - script "/home/administrator/.config/autokey/data/Sample Scripts/PyLink.kts" - - -d. /
        # os.system(myCmd)
    except subprocess.CalledProcessError:
        time.sleep(0.2)
    # cOld = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    doReplace = False
    try:
        cOld = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
        if cOld[0:1] == doReplaceIfPrefixIsThis:  # :test :test
            doReplace = True
            if True:
                duration = .2  # second
                freq = 2000  # Hz
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
            # first_chars = sample_str[0:3]
            # quit()

    except:
        cOld = ""
        duration = 0.1  # second
        freq = 1500  # Hz
        for x in range(3):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
            time.sleep(0.1)
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
    return (timeValueForBREAKLoopInSec, timeValueInLoopInSec, first_title)
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
#>>>>>>>>>>>>>> read_keyword
