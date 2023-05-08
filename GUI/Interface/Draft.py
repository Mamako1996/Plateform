import os
import time
import psutil
import pyautogui

dtime = "6000"
rp1 = "500"
rp2 = "600"
rp3 = "700"
rp4 = "800"

rpmList = [rp1, rp2, rp3, rp4]
newText = ""


def openFile():
    try:
        os.startfile('L293D_Driver/L293D_Driver.ino')
    except Exception as e:
        print(e)


def makeComment(lineText, rpm, number):
    tList = lineText.split()
    com = " "
    for j in range(0, 4):
        tList.remove(tList[0])
    com = com + com.join(tList)
    lineFinal = lineText.replace(lineText, "  int rpm" + str(number + 1) + " = " + (rpm + ";") + " " * 20 + com + "\n")
    return lineFinal


with open('L293D_Driver/L293D_Driver.ino', 'r+') as f:
    text = f.readlines()
    n = 0
    for line in text:
        comment = " "
        if line.__contains__("  int delayTime = "):
            line = line.replace(line, "  int delayTime = " + dtime + ";\n")

        if line.__contains__("  int rpm"):
            line = makeComment(line, rpmList[n], n)
            n = n + 1

        newText = newText + line

    f.seek(0)
    f.write(newText)
    f.truncate()
    print(newText)

openFile()
time.sleep(1)
if "javaw.exe" in (p.name() for p in psutil.process_iter()) != 0:
    pyautogui.click(900, 500)
    pyautogui.click(40, 55)
else:
    print("0")
