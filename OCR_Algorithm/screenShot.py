import cv2
import time

# new Excel file making

# open camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
signal = cap.isOpened()
index = 1
n = 0

while signal:
    if n > 99:
        break
    ret, frame = cap.read()
    cv2.imshow("Current", frame)
    k = cv2.waitKey(1) & 0xFF

    cv2.imwrite("C:/Users/umbmz/PycharmProjects/project/HW/Section_I/" + "Test" + str(index) + ".jpg", frame)
    print("save" + str(index) + ".jpg successfully!")

    n = n + 1
    index = index + 1
    time.sleep(2)


cap.release()
cv2.destroyAllWindows()
