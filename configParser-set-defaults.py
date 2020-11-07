# whereis here: ~/Documents/github/PycharmProjects/Lintalist4Linux/configParser-set-defaults.py
# it sets defaults to:
# - LintaList (configParser-set-ini-defaults.ahk)
# - autokey

from pathlib import Path
import json, os
import subprocess
home = str(Path.home())
path = home + "/.config/autokey/data/Sample Scripts/"
jsonFilePath = home + "/.config/autokey/data/Sample Scripts/.run-run-lintalistAHK-all.json"
file = open(jsonFilePath)
data = json.load(file)
# for x in data['hotkey']:
data['hotkey']['hotKey'] = '<f12>'

if False:
    subprocess = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    output, error = subprocess.communicate()
    target_process = "autokey"
    for line in output.splitlines():
        if target_process in str(line):
            pid = int(line.split(None, 1)[0])
            os.kill(pid, 9)
else:
    myCmd = 'sudo killall -9 autokey &'
    os.system(myCmd)  # print(data)
    print(myCmd)

os.system("sleep 1s")

with open(jsonFilePath, 'w') as file:
    json.dump(data, file, indent=2)

#/‾‾‾ configParser-set-ini-defaults.ahk
myCmd = 'wine ' + home + '/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe "' + home + '/.config/autokey/data/Sample Scripts/configParser-set-ini-defaults.ahk" &'
# wine /home/m/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe "/home/m/.config/autokey/data/Sample Scripts/.config/autokey/data/Sample Scripts/configParser-set-ini-defaults.ahk" &
# works:
# wine /home/m/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe "/home/m/.config/autokey/data/Sample Scripts/configParser-set-ini-defaults.ahk" &
print(myCmd)
os.system(myCmd)
#\___ configParser-set-ini-defaults.ahk

# myCmd = 'autokey-qt'  # sleep 1s ;
# myCmd = 'autokey  > /dev/null &'  # sleep 1s ;
myCmd = 'autokey  > /dev/null &'  # sleep 1s ;
print(myCmd)
os.system(myCmd)
# cd ~/.wine/drive_c/Program\ Files/AutoHotkey/ ; wine AutoHotkey.exe ~/ahk/github/lintalist/lintalist.ahk -opengl > /dev/null

