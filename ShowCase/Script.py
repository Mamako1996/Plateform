import os
import time
import psutil
import pyautogui


def openFile(self):
    try:
        os.startfile(self.filename + "\\" + self.filename + ".ino")
    except Exception as e:
        print(e)
    time.sleep(3)
    if "javaw.exe" in (p.name() for p in psutil.process_iter()) != 0:
        pyautogui.getWindowsWithTitle(self.filename)[0].maximize()
        pyautogui.click(900, 500)

        # port selection (115, 30) (147, 251) (512, 251)
        pyautogui.click(115, 30)

        pyautogui.click(147, 251)

        pyautogui.moveTo(512, 251)

        pyautogui.hotkey("ctrl", "u")
    else:
        print("0")
    time.sleep(30)
