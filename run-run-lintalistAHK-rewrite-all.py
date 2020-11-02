# import os, time, datetime, pathlib, subprocess # TODO: one day install: http://omz-software.com/pythonista/docs/ios/clipboard.html
# from pathlib import Path
# home = str(Path.home())
# path = home + "/.config/autokey/data/Sample Scripts/"
# do_DisableUpdatingThe_all_file = False

# test

def writeAllFile_from_main_defs(path,rewriteAlways = False):
    global do_DisableUpdatingThe_all_file
    if do_DisableUpdatingThe_all_file:
        return
    path = home + "/.config/autokey/data/Sample Scripts/"
    # global data
    data = "# Attention: !!! don`t edit thi file. this file will be result from other files merged."

    if not rewriteAlways:
        getmtimeConfig = os.path.getmtime(path + 'run-run-lintalistAHK-config.py')
        getmtimeDefs = os.path.getmtime(path + 'run-run-lintalistAHK-defs.py')
        getmtimeMain = os.path.getmtime(path + 'run-run-lintalistAHK-main.py')
        getmtimeAll = os.path.getmtime(path + 'run-run-lintalistAHK-all.py')

    if rewriteAlways or (getmtimeAll < getmtimeDefs or getmtimeAll < getmtimeConfig or getmtimeAll < getmtimeMain):
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

writeAllFile_from_main_defs(path,True)