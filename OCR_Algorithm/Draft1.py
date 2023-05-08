import cv2
import pytesseract
import openpyxl
import re

# new Excel file making
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Testing Data'
sheet.append(['Number', 'UV Transmission', 'IR Transmission', 'VL Transmission'])

pytesseract.pytesseract.tesseract_cmd = pytesseract.pytesseract.tesseract_cmd = r"C:\Program " \
                                                                                r"Files\Tesseract-OCR" \
                                                                                r"\tesseract.exe "

# open camera
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
signal = cap.isOpened()
index = 1
while signal:
    ret, frame = cap.read()
    cv2.imshow("Current", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite("C:/Users/umbmz/PycharmProjects/project/HW/Section_I/" + "Test" + str(index) + ".jpg", frame)
        print("save" + str(index) + ".jpg successfully!")

        name = "Test" + str(index) + ".jpg"
        print(name)
        img = cv2.imread(name)
        # Resizing for scan
        img = cv2.resize(img, None, fx=0.5, fy=0.5)

        # threshold method for dividing the clearer color block
        ret, adaptive_threshold = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)

        # extract the text from image
        text = pytesseract.image_to_string(adaptive_threshold)

        # print it out for checking
        print(text + "\n")

        # make a cell to hold the data

        a = re.findall(r"\d+\.?\d*", text)
        a.insert(0, index)
        print(a)
        sheet.append(a)

        cv2.imshow('Result', img)
        cv2.imshow('Results', adaptive_threshold)
        cv2.waitKey(0)
        wb.save('Testing.xlsx')
        index += 1
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
