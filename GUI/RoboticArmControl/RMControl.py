import os
import time
import psutil
import pyautogui


class ServoControl:
    def __init__(self, bottles, glasses, bottles_filename, glasses_filename):
        self.bottles = bottles
        self.glasses = glasses
        self.bottles_filename = bottles_filename
        self.glasses_filename = glasses_filename

    def startRM(self):
        if self.bottles == 1 and self.glasses == 1:
            print("If there are mutiple arms, it can be consider")
        if self.bottles == 1 and self.glasses == 0:
            self.bottlesCapture()
        if self.bottles == 0 and self.glasses == 1:
            self.glassesCapture()

    def bottlesCapture(self):
        try:
            os.startfile("Robotic_Arm\\RM1.1.exe")  # 'L293D_Driver\\L293D_Driver.ino'
        except Exception as e:
            print(e)
        time.sleep(3)
        if "RM1.1.exe" in (p.name() for p in psutil.process_iter()) != 0:
            pyautogui.click(900, 500)
            pyautogui.getWindowsWithTitle("V1.1")[0].maximize()
            cur_path = os.path.abspath(os.path.dirname("RM1.1.exe"))

            # loading file
            pyautogui.click(1396, 727)
            # path typing
            pyautogui.click(622, 70)
            pyautogui.typewrite([cur_path, "\\Robotic_Arm\\"])
            pyautogui.press('enter')
            pyautogui.press('enter')
            # file typing
            pyautogui.click(377, 498)
            pyautogui.typewrite(self.bottles_filename)
            pyautogui.press('enter')
            # file open
            pyautogui.click(795, 527)

            # Set up (Need develop later)
            pyautogui.click(797, 726)

            # fixed COM number
            # pyautogui.click(x, y)

            # open port
            # pyautogui.click(775, 840)
            pyautogui.moveTo(775, 840)

            # start loop
            pyautogui.doubleClick(1040, 704)
            # pyautogui.click(1078, 766)
            pyautogui.moveTo(1066, 760)
        else:
            print("0")

    def glassesCapture(self):
        try:
            os.startfile("Robotic_Arm\\RM1.1.exe")  # 'L293D_Driver\\L293D_Driver.ino'
        except Exception as e:
            print(e)
        time.sleep(3)
        if "RM1.1.exe" in (p.name() for p in psutil.process_iter()) != 0:
            pyautogui.click(900, 500)
            pyautogui.getWindowsWithTitle("V1.1")[0].maximize()
            cur_path = os.path.abspath(os.path.dirname("RM1.1.exe"))

            # loading file
            pyautogui.click(1396, 727)
            # path typing
            pyautogui.click(622, 70)
            pyautogui.typewrite([cur_path, "\\Robotic_Arm\\"])
            pyautogui.press('enter')
            pyautogui.press('enter')
            # file typing
            pyautogui.click(377, 498)
            pyautogui.typewrite(self.glasses_filename)
            pyautogui.press('enter')
            # file open
            pyautogui.click(795, 527)

            # Set up (Need develop later)
            pyautogui.click(797, 726)

            # fixed COM number
            # pyautogui.click(x, y)

            # open port
            # pyautogui.click(775, 840)
            pyautogui.moveTo(775, 840)
            time.sleep(2)
            # start loop
            pyautogui.click(1040, 704)
            time.sleep(2)
            # pyautogui.click(1078, 766)
            pyautogui.moveTo(1066, 760)
            time.sleep(2)

        else:
            print("0")

    @staticmethod
    def stopMove():
        if "RM1.1.exe" in (p.name() for p in psutil.process_iter()) != 0:
            pyautogui.getWindowsWithTitle("V1.1")[0].maximize()
            # click center
            pyautogui.click(900, 500)

            # Stop
            # pyautogui.click(1716, 862)
            pyautogui.moveTo(1716, 862)

            # reset position
            pyautogui.click(17063, 846)
        # close Window
        for p in psutil.process_iter():
            if p.name() == "RM1.1.exe":
                p.kill()
