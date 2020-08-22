# this file will be (hopefully merged to) ...-all.py

subprocess.Popen(['notify-send', "will be showed right top"])  # will be showed right top
# copy file https://stackoverflow.com/a/123212/2891692
# demonstrate merging of two files

writeAllFile_from_main_defs(path)
subprocess.Popen(['notify-send', path + 'run-run-lintalistAHK-all.py'])  # will be showed right top

if doBeepsWelcomeAtEachRun:
    beeps(duration=.8, freq=1500, loops=2)

(timeValueForBREAKLoopInSec, timeValueInLoopInSec, first_title) = read_keyword(doReplaceIfPrefixIsThis,do_ifNoPrefix_useFocusedWord_pasteResultRight,keyboard,window,clipboard)
# quit()

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
            beeps(duration=.4, freq=3000, loops=1)
        break
    time.sleep(timeValueInLoopInSec)
cNew = ""
try:
    cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    if len(str(cNew)) < 1 and cNew != cOld:
        exit()  # quit()
except:
    time.sleep(0.1)
cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation

# if True:
#     try:
#        cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
#    except:
#        cNew = "" 

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

