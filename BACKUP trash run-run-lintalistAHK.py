import time
import subprocess
import os


import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []



keyboard.send_keys("\n#1 user_paths='%s'" % user_paths)
quit()
exit()
#

# <<<<<<<<<< config begin
# doSelectWord 
# doCopyWord2clipboard = True 
doReplaceIfPrefixIsThis = ":"
do_ifNoPrefix_useFocusedWord_pasteResultRight = True
# useEnter = True
do_ifNoPrefix_useFocusedWord_pasteResultNewLine = True

# >>>>>>>>>> config end




if doReplaceIfPrefixIsThis:
    # select word and prefix e.g.  :test
    doSelctWordAndPrefix = True

cOld = ""

# line 20 :Heide kjkjhkjh
# now

if do_ifNoPrefix_useFocusedWord_pasteResultRight:
    # unselect maybe selected word
    keyboard.send_keys('<left><right>')

    if doSelctWordAndPrefix:
        keyboard.send_keys('<ctrl>+<left><left><shift>+<right>')
        keyboard.send_keys('<ctrl>+<shift>+<right>')
    else:
        # select word
        keyboard.send_keys('<ctrl>+<left>')
        keyboard.send_keys('<ctrl>+<shift>+<right>')
    keyboard.send_keys('<ctrl>+c')
    # keyboard.send_keys('<ctrl>+v')

    keyboard.release_key('<shift>')  # sometimes i got hanging shift key
    # keyboard.release_key('<ctrl>')

# 30 line

#####################
# this file must be run in:
# /home/administrator/.config/autokey/data/Sample Scripts/
# or so
# this file i store it in local repo like:
# /home/administrator/Documents/github/Lintalist4Linux/
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
except subprocess.CalledProcessError:
    time.sleep(0.2)

cOld = ""
# cOld = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
# Found exeptions: no content into the clipboard 20:08:20 16:48:24


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
    freq = 1800  # Hz
    for x in range(4):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        time.sleep(0.1)

# :tes2016/01t


# 100 line
# php2012/01 cello-technologie.de     


for i in range(0, 30):
    time.sleep(0.1)
    # active_class = window.get_active_class()
    active_title = window.get_active_title()
    # if active_class != first_class:
    if active_title != first_title:
        break

timeValueInLoopInSec = 0.4
timeValueForBREAKLoopInSec = 90  # timeOut. Prevention for endless loops

# Sebas

# BREAK x is '101
# time.sleep(2) 
# keyboard.send_keys('<ctrl>+v')


for x in range(0, 900):  # default is 25
    if timeValueForBREAKLoopInSec < x * timeValueInLoopInSec:
        # keyboard.send_keys("BREAK at Loop %s because timeValueForBREAKLoopInSec > '%s'" % (str(x), str(timeValueForBREAKLoopInSec)))
        # ^- too check the last x value if interested in
        break

    active_title = window.get_active_title()
    # active_class = window.get_active_class()

    # if active_title == first_title and active_class == first_class:
    # if active_class == first_class:
    if active_title == first_title:
        #  keyboard.fake_keypress('<left>') # posibility to show script is working. https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
        if False:
            duration = 0.4  # second
            freq = 3000  # Hz
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        break

    time.sleep(timeValueInLoopInSec)

cNew = ""

try:
    cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    cNew = cNew.strip(' \t\n\r')
if len(str(cNew)) < 1 and cNew != cOld:
        exit()  # quit()
except:
    time.sleep(0.1)

### 150 line

# cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
if True:
    try:
        cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
        cNew = cNew.strip(' \t\n\r')
except:
        cNew = ""  # Found exeptions: no content into the clipboard 20:08:20 16:48:24
        duration = 0.1  # second
        freq = 1500  # Hz
        for x in range(2):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
            time.sleep(0.1)

# if len(cNew) > 0 AND cNew == cOld:
if cNew == cOld:
    quit()  # exit() # quit() asdffasdff asdffasdffasdffasdff  javajava
    # try:

    # cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation

    # time.sleep(0.4) 
    # keyboard.fake_keypress('<control>') # posibility to show script is working. https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki

    # keyboard.release_key('<ctrl>')

if doReplace:  # :test  :test  :test  :test  :test
    keyboard.send_keys('<ctrl>+v')  # work without problem        print(" ")
    if True:
        duration = .8  # second
        freq = 7000  # Hz
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    quit()

# keyboard.send_keys('<right><left>') #  deselect  test MONDSdd

if True:
    duration = .8  # second
    freq = 1500  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

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
if useEnter:
    time.sleep(0.1)
    keyboard.send_keys('<shift>+<home>')
else:
    # time.sleep(0.1)
    # keyboard.send_keys('<ctrl>+<left>')
    keyboard.send_keys('<ctrl>+<shift>+<left>')  # right
keyboard.release_key('<shift>')  # sometimes i got hanging shift key

# 200 line

time.sleep(1)

if False:  # except:
    duration = 0.1  # second
    freq = 1500  # Hz
    for x in range(4):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
        time.sleep(0.1)

time.sleep(0.4)

# the following f-keys commands are working:    
# keyboard.fake_keypress('<f4>') # edit snippet
# keyboard.fake_keypress('<f5>') # copy snippet
# keyboard.fake_keypress('<f5>') # move snippet
# keyboard.fake_keypress('<f7>') # new snippet
# keyboard.fake_keypress('<f8>') # remove snippet
# keyboard.fake_keypress('<f10>') # manage bundels
