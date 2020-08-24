import time
import subprocess 
# keyboard.send_keys("\n#3")
clipboardKey = ""
cNew = ""
# keyboard.send_keys("\n#5")
# clipboardKey = clipboard.get_selection()
try:
    clipboardKey = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
except:
    clipboardKey = ""
# keyboard.send_keys("\n#9")

# https://stackoverflow.com/questions/25079140/subprocess-popen-checking-for-success-and-errors
# subprocess.Popen(["/bin/bash", "/home/administrator/Desktop/test.sh"]) # <== this is working but python(AutoKey) stops at this line with an error
    

try:
    # proc = subprocess.check_output(["/bin/bash", "/home/administrator/Desktop/test.sh"], stderr=subprocess.STDOUT)
    subprocess.Popen(["/bin/bash", "/home/administrator/Desktop/test.sh"])
    # do something with output
except subprocess.CalledProcessError:
    time.sleep(1)
    # subprocess.CalledProcessError:
    # There was an error - command exited with non-zero code

time.sleep(1)  # <=== if i use a long pause i got no problem here
try:
    cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
except:
    time.sleep(0.1)  
# time.sleep(4) # <=== if i use a long pause i got no problem here

# probably not a better idear:
# To start a program with wine.
# subprocess.Popen(["wine", "~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Desktop/sendF1v2.ahk"])
# subprocess.Popen(["wine", "~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Desktop/sendF1v2.ahk -opengl > /dev/null 2> /dev/null &"])
# subprocess.Popen(["wine", "~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe /home/administrator/Desktop/sendF1v2.ahk -opengl > /dev/null 2> /dev/null &"])

# script not found: subprocess.Popen(["wine", "~/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe Z:\home\administrator\Desktop\sendF1v2.ahk"])
# Z:\home\administrator\Desktop/sendF1v2.ahk

# time.sleep(3)
# keyboard.press_key('<alt>')
# time.sleep(0.2)
# keyboard.fake_keypress('e')
# time.sleep(0.2)
# keyboard.fake_keypress('n')
# keyboard.send_keys("en")
# time.sleep(2)
# keyboard.release_key('<alt>')

# the following f-keys commands are working:    
# keyboard.fake_keypress('<f4>') # edit snippet
# keyboard.fake_keypress('<f5>') # copy snippet
# keyboard.fake_keypress('<f5>') # move snippet
# keyboard.fake_keypress('<f7>') # new snippet
# keyboard.fake_keypress('<f8>') # remove snippet
# keyboard.fake_keypress('<f10>') # manage bundels

# keyboard.fake_keypress('<np_left>') # https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
# follwing is working:
# keyboard.fake_keypress('<left>') # posibility to show script is working. https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
# time.sleep(0.2)
# keyboard.fake_keypress('<escape>') # to close the window https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki

for x in range(0, 1000): # default is 25
    # keyboard.send_keys("\n#39 x='%s'" % str(x))
    # keyboard.send_keys("\n#39b")
    # keyboard.send_key("# plip plop<delete>")
    
    if x > 500:
        # keyboard.fake_keypress('<escape>')  # its better way to close the window first. sometimes needet. https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
        keyboard.fake_keypress('<escape>')  # to close the window https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
        time.sleep(0.2)
        keyboard.send_keys("\n#42 x='%s'" % str(x))
        time.sleep(1)
        # break

    # keyboard.send_keys("\n#15 n='%s'  o='%s'\n" % (cNew, clipboardKey))
    # time.sleep(1) # in seconds
    # cNew = clipboard.get_selection()
    # cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    try:
        cNew = clipboard.get_clipboard()  # found here: https://github.com/autokey/autokey/wiki/Scripting#create-new-abbreviation
    except:
        if x > 200:
            # happened if the window is closed in wine
            keyboard.fake_keypress('<escape>')  # to close the window https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
            time.sleep(0.2)
            keyboard.send_keys("\n#17 the window is closed in wine")  # this is sometimes written inside the app
            break
        time.sleep(0.1)

    # keyboard.send_keys("\n#18 n='%s'  o='%s'\n" % (cNew, clipboardKey))
    if len(cNew) > 0 and clipboardKey != cNew:
        # keyboard.send_keys("\n#20 n='%s'  o='%s'\n" % (cNew, clipboardKey)) # <== thats only for debugging
        # time.sleep(0.1) # window needs time to close
        # keyboard.send_keys("\n#22")
        # keyboard.fake_keypress('<escape>')  # to close the window https://code.google.com/archive/p/autokey/wikis/SpecialKeys.wiki
        time.sleep(0.2)
        # keyboard.send_keys("\n#22 '%s'" % cNew)
        keyboard.send_keys(cNew)
        break
    else:
        time.sleep(0.1)
        # time.sleep(0.1)

keyboard.send_keys("\n#EOF")

