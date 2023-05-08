import os
import time
import psutil
import pyautogui


def makeComment(lineText, rpm, number):
    tList = lineText.split()
    com = " "
    for j in range(0, 4):
        tList.remove(tList[0])
    com = com + com.join(tList)
    lineFinal = lineText.replace(lineText,
                                 "  int rpm" + str(number + 1) + " = " + (rpm + ";") + " " * 20 + com + "\n")
    return lineFinal


class MotorControl:
    def __init__(self, dtime, rp1, rp2, rp3, rp4, filename):
        self.dtime = dtime
        self.rp1 = rp1
        self.rp2 = rp2
        self.rp3 = rp3
        self.rp4 = rp4
        self.filename = filename

    def startMotor(self):
        with open('L293D_Driver\\L293D_Driver.ino', 'r+') as f:
            rpmList = [self.rp1, self.rp2, self.rp3, self.rp4]
            text = f.readlines()
            n = 0
            a = ""
            for line in text:
                comment = " "
                if line.__contains__("  int delayTime = "):
                    line = line.replace(line, "  int delayTime = " + self.dtime + ";\n")

                if line.__contains__("  int rpm"):
                    line = makeComment(line, rpmList[n], n)
                    n = n + 1

                a = a + line
            f.close()
        with open('L293D_Driver\\' + self.filename, 'w') as f1:
            f1.seek(0)
            f1.write(a)
            f1.truncate()
            f1.close()

    def openFile(self):
        try:
            os.startfile('L293D_Driver\\' + self.filename)  # 'L293D_Driver\\L293D_Driver.ino'
        except Exception as e:
            print(e)
        time.sleep(1)
        if "javaw.exe" in (p.name() for p in psutil.process_iter()) != 0:
            pyautogui.click(900, 500)
            pyautogui.getWindowsWithTitle("L293D")[0].maximize()
        else:
            print("0")
