# whereis here: ~/Documents/github/PycharmProjects/Lintalist4Linux/configParser-set-defaults.py

from pathlib import Path
import json, os
home = str(Path.home())
path = home + "/.config/autokey/data/Sample Scripts/"
jsonFilePath = home + "/.config/autokey/data/Sample Scripts/.run-run-lintalistAHK-all.json"
file = open(jsonFilePath)
data = json.load(file)
for x in data['hotkey']:
    data['hotkey'][x] = '<f11>'
print(data)
with open(jsonFilePath, 'w') as file:
    json.dump(data, file, indent=2)

myCmd = 'wine ' + home + '/.wine/drive_c/Program\ Files/AutoHotkey/AutoHotkey.exe "' + home + '/.config/autokey/data/Sample Scripts/configParser-set-ini-defaults.ahk"'
os.system(myCmd)

# myCmd = 'autokey-run --script ifWineWin-sendEnter'
# os.system(myCmd)
