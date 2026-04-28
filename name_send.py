import pywhatkit as kit
import names as nm
import pyautogui as pg
import mouseinfo as ms

for i in range (100):
    kit.sendwhatmsg_instantly("+254119979706",nm.get_full_name(gender="male"),tab_close=True)
    # print(names.get_full_name (gender="male")
    