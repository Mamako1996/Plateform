import os
import time
import pyperclip
import psutil
import pyautogui

# Point(x=35, y=147) ACT at Desk
while True:
    print(pyautogui.position())
    time.sleep(5)



# # Open software - Arduino
#
# def openFile():
#     try:
#         os.startfile('L293D_Driver/L293D_Driver.ino')
#     except Exception as e:
#         print(e)
#
#
# with open('L293D_Driver/L293D_Driver.ino') as f:
#     lines = f.read()
# print(lines)
#
# text = ''
# os.startfile('L293D_Driver/L293D_Driver.ino')
# time.sleep(1)
# if "javaw.exe" in (p.name() for p in psutil.process_iter()) != 0:
#     pyautogui.getWindowsWithTitle("L293D")[0].maximize()
# else:
#     print("0")
#     print(text)
