import os
import time

import psutil
import pyautogui as pag

for p in psutil.process_iter():
    print(p.name())

# from RMControl import ServoControl
#
# rmb = ServoControl(True, False, "Bottom", "Glasses")
# rmb.startRM()
# time.sleep(5)
# rmb.stopMove()
#
# rmg = ServoControl(False, True, "Bottom", "Glasses")
# rmg.startRM()
# time.sleep(5)
# rmg.stopMove()

# try:
#     while True:
#         print("Press Ctrl-C to end")
#         screenWidth, screenHeight = pag.size()
#         x, y = pag.position()
#         print("Screen size: (%s %s), Position: (%s, %s)\n" % (screenWidth, screenHeight, x, y))
#         time.sleep(5)
#         os.system('cls')
# except KeyboardInterrupt:
#     print("end")

# (115, 30) (147, 251) (512, 251)