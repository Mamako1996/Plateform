import pyautogui
import time


def bottle():
    pyautogui.click(576, 432)
    # port selection (115, 30) (147, 251) (512, 251)
    pyautogui.click(1181, 366)

    pyautogui.click(235, 886)

    time.sleep(105)
    pyautogui.click(576, 432)


def change(name):
    if name == "g":
        pyautogui.click(692, 404)
        time.sleep(1)
        pyautogui.doubleClick(262, 204)
        pyautogui.click(1188, 265)
        time.sleep(1)
        pyautogui.doubleClick(1215, 190)
    else:
        if name == "b":
            pyautogui.click(692, 404)
            time.sleep(1)
            pyautogui.doubleClick(269, 181)
            pyautogui.click(1187, 264)
            time.sleep(1)
            pyautogui.doubleClick(1229, 167)
            pyautogui.click(235, 787)
            time.sleep(1)
            pyautogui.doubleClick(408, 625)
        else:
            exit()


def glass():
    pyautogui.click(576, 432)
    # port selectgion (115, 30) (147, 251) (512, 251)

    pyautogui.click(1181, 366)

    time.sleep(124)
    pyautogui.click(576, 432)


while 1:
    c = input('请输入指令:g/b\n')
    change(c)
    if c == "g":
        glass()
    else:
        bottle()
