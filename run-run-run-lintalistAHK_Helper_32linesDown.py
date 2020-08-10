ok, text = dialog.input_dialog("Linwa down", "Choose number amount for curser down")

# keyboard.send_keys(str(text))

for i in range(0, int(text)):   
    keyboard.press_key('<down>')
    keyboard.release_key('<down>')
# 5



