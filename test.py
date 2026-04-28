import pyautogui as pgui
with open('test.txt', 'r') as f:
    data = f.read()


pgui.moveTo(1536, 864)
pgui.click()
pgui.write(data, interval=0.05)


























